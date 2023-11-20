import pandas as pd

def calc_tstats(event_cars):
    groups = event_cars.groupby('event_type')['car']
    print(groups.describe())

    car_bar = groups.mean()
    car_sem = groups.sem()
    car_t = car_bar/car_sem
    car_n = groups.count()
    res = pd.DataFrame({'car_bar':car_bar, 'car_t': car_t, 'n_obs': car_n})
    return res

