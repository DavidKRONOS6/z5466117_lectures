import yfinance as yf
import config as cfg


def yf_rec_to_csv(tic, pth,
                  start=None,
                  end=None):

    c = yf.Ticker(tic)
    c.history(start=start, end=end)
    # Make sure we only relevant dates
    if start is not None and end is not None:
        df = c.recommendations.loc[start:end]
    elif start is not None:
        df = c.recommendations.loc[start:]
    elif end is not None:
        df = c.recommendations.loc[:end]
    else:
        df = c.recommendations
    df.to_csv(pth)


def get_data(tic):
    locs = cfg.csv_locs(tic)

    print(f'Downloading prices for {tic}...')
    df = yf.download(tic,
            start=cfg.START,
            end=cfg.END)
    pth = locs['prc_csv']
    df.to_csv(pth)
    print('Done')

    print(f'Downloading recs for {tic}...')
    yf_rec_to_csv(tic, 
            pth=locs['rec_csv'], 
            start=cfg.START,
            end=cfg.END)
    print('Done')


if __name__ == "__main__":
    get_data('tsla')

