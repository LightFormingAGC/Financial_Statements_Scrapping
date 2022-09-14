import bs4
import pandas as pd
import requests as re
import numpy as np

class Screener:

    def __init__(self):
        self.sectors = ['Consumer Services', 'Distribution Services', 'Electronic Technology',
                        'Energy Minerals', 'Finance', 'Health Services', 'Health Technology',
                        'Industrial Services', 'Miscellaneous', 'Non-Energy Minerals',
                        'Process Industries', 'Producer Manufacturing', 'Retail Trade',
                        'Technology Services', 'Transportation', 'Utilities']

    @staticmethod
    def scrap(sector, N):
        text = sector.replace(' ', '-').lower()
        url = f"https://www.tradingview.com/markets/stocks-usa/sectorandindustry-sector/{text}/"
        info = re.get(url).text
        soup = bs4.BeautifulSoup(info, 'lxml')
        tickers = soup.find_all('a', class_='tv-screener__symbol')
        mkt_caps = soup.find_all('td', class_='tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big')
        tic_lst = []
        for ticker in tickers:
            tic_lst.append(ticker.get_text())
        mkt_caps_lst = []
        for i in np.arange(3, len(mkt_caps), 7):
            mkt_cap_str = mkt_caps[i].get_text()
            if mkt_cap_str.endswith('B'):
                mkt_caps_lst.append(float(mkt_cap_str[:-1]) * 1000000000)
            elif mkt_cap_str.endswith('M'):
                mkt_caps_lst.append(float(mkt_cap_str[:-1]) * 1000000)
        print(tic_lst, len(mkt_caps_lst))
        # df = pd.DataFrame(np.array(mkt_caps_lst), index=np.array(tic_lst))
        # print(df)


ttt = Screener
ttt.scrap('Consumer Services', 10)
