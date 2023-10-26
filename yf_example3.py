
import os
from yf_example1 import yf_prc_to_csv


def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    start = f"{year}-01-01"
    end = f"{year}-12-31"
    datadir = '/Users/kronos/PycharmProjects/Toolkit/data'
    pth = os.path.join(datadir, f'qan_prc_{year}.csv')
    df=yf_prc_to_csv(tic=tic, pth=pth, start=start, end=end)


if __name__ == "__main__":
    year=2020
    qan_prc_to_csv(year)
