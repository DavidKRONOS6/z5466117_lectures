import pandas as pd

import event_study.config as cfg

def mk_event_df(tic):
    pth = cfg.csv_locs(tic)['rec_csv']
    df = pd.read_csv(pth, index_col='Date', parse_dates=['Date'])

    cols = ['firm', 'action']
    df = cfg.standardise_colnames(df)[cols]

    df.loc[:, 'firm'] = df.loc[:, 'firm'].str.upper()

    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')

    df.sort_index(inplace=True)
    groups = df.groupby(['event_date', 'firm'])

    df = groups.last().reset_index()


    cond = df.loc[:, 'action'].str.contains('up|down')
    df = df.loc[cond]

    def _mk_et(value):
        """ Converts the string `value` as follows:
            - "down" --> "downgrade"
            - "up" --> "upgrade"
        and raise an exception if value is not "up" or "down"
        """
        if value == 'down':
            return 'downgrade'
        elif value == 'up':
            return 'upgrade'
        else:
            raise Exception(f'Unknown value for column `action`: {value}')
    df.loc[:, 'event_type'] = df['action'].apply(_mk_et)

    df.reset_index(inplace=True)
    df.index = df.index + 1
    df.index.name = 'event_id'

    cols = ['firm', 'event_date', 'event_type']
    df = df[cols]


    return df


if __name__ == "__main__":
    tic = 'TSLA'
    df = mk_event_df(tic)
    print(df)
    df.info()

