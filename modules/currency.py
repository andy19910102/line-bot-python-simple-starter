from pyquery import PyQuery
# 貨幣


class Currency:
    # 定義貨幣屬性: 名稱name、銀行買入價bid、銀行賣出價offer
    def __init__(self, name, bid, offer):
        # 貨幣名稱
        self.name = name
        # 買價
        self.bid = bid
        # 賣價
        self.offer = offer

    def show_info(self):
        '''
            show_info()
            輸出str:回傳此貨幣報告
        '''
        return f'{self.name},買價:{self.bid}賣價:{self.offer}'

# 貨幣爬蟲


class CurrencyCrawler:
    # 貨幣爬蟲屬性: 目標網址url(https://rate.bot.com.tw/xrt?Lang=zh-TW)、爬取的資料data
    # 貨幣爬蟲函數:
    # fetch_data(): 爬取資料,
    # get_report(幣別名稱): 查詢幣別資訊
    def __init__(self):
        self.url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
        self.data = {}
        print('[爬蟲實例已被建立，準備第一次爬取資料]')
        self.fetch_data()

    def fetch_data(self):
        '''
            fetch_data()
            爬取台灣銀行牌告匯率網站資訊，並建立貨幣買賣價查詢表
        '''
        # 爬取整份網頁
        html = PyQuery(self.url)
        # 所有貨幣名稱
        names = html('div.hidden-phone.print_show').text().split()
        # 所有現金買價
        bids = html(
            'td.rate-content-cash.text-right.print_hide[data-table="本行現金買入"]').text().split()
        # 所有現金賣價
        offers = html(
            'td.rate-content-cash.text-right.print_hide[data-table="本行現金賣出"]').text().split()
        # 價格計數器
        p = 0
        for n_idx, name in enumerate(names):
            if n_idx % 2 == 0:
                # 建立一個貨幣表
                # Currency(貨幣名稱, 買價, 賣價)
                self.data[name] = Currency(name, bids[p], offers[p])
                # 把p+1
                p += 1

    def get_report(self, currency_name):
        '''
            get_report(currency_name)
            輸入currency_name(str):貨幣名稱，如：美金、港幣
            輸出str:回傳此貨幣報告
            EX: 美金 => 美金,買價:29.83 賣價:30.5
            EX: 日圓 => 日圓,買價:0.2667 賣價:0.2795
        '''
        if currency_name in self.data:
            currency = self.data[currency_name]
            return currency.show_info()
        else:
            return f'查無此貨幣資訊'
