from pyquery import PyQuery

def get_exchange_table():
    # 資料來源網址
    url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
    # 輸出的字典
    table = {}
    # 爬取整份網頁
    html = PyQuery(url)
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
            table[name] = {
                "bid": bids[p],
                "offer": offers[p]
            }
            # 把p+1
            p += 1
    return table
