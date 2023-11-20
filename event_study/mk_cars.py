import numpy as np
import pandas as pd
import event_study.config as cfg


def mk_cars_df(ret_df, event_df):
    cars = event_df.apply(calc_car, axis=1, ret_df=ret_df)
    event_df.loc[:, 'car'] = cars
    return event_df


def expand_dates(ser, window=2):
    row_lst = [ser] * (2*window+1)
    df = pd.concat(row_lst, axis=1).transpose()

    df.loc[:, 'event_date'] = pd.to_datetime(df.loc[:, 'event_date'])
    df.loc[:, 'event_time'] = [i for i in range(-window, window+1)]


    df.loc[:, 'ret_date'] = df.event_date + pd.to_timedelta(df.event_time, unit='day')

    cols = ['firm', 'event_date', 'event_time', 'ret_date']
    df = df.loc[:, cols]

    df.index.name = 'event_id'
    return df


def calc_car(ser, ret_df, window=2):
    dates = expand_dates(ser, window=window)
    dates.set_index('ret_date', inplace=True)
    df = dates.join(ret_df, how='inner')
    df.loc[:, 'aret'] = df.loc[:, 'ret'] - df.loc[:, 'mkt']
    if len(df) == 0:
        return np.nan
    else:
        return df['aret'].sum()


def _test_mk_cars_df(sample_only=False):
    from event_study import mk_rets, mk_events

    def _mk_example_event_df(event_df):
        cond = (event_df.event_date == '2020-09-23') & (event_df.firm == 'DEUTSCHE BANK')
        event_df = event_df.loc[cond]
        event_df.index = [1]
        event_df.index.name = 'event_id'
        return event_df

    tic = 'TSLA'
    ret_df = mk_rets.mk_ret_df(tic)
    event_df = mk_events.mk_event_df(tic)

    if sample_only is True:
        event_df = _mk_example_event_df(event_df)
        ret_df = ret_df.loc['2020-09-21':'2020-09-25']

    print('-----------------------------')
    print(' event_df:')
    print('-----------------------------')
    print(event_df)
    print('')

    print('-----------------------------')
    print(' ret_df:')
    print('-----------------------------')
    print(ret_df)
    print('')

    # Create the CAR df
    cars_df = mk_cars_df(ret_df=ret_df, event_df=event_df)

    print('-----------------------------')
    print(' cars_df:')
    print('-----------------------------')
    print(cars_df)


if __name__ == "__main__":
    sample_only = True
    _test_mk_cars_df(sample_only)

