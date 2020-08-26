from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

# 常見問答表
faq = {
    '貼圖': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
    '門市照片': ImageSendMessage(
        original_content_url='https://picsum.photos/id/395/900/400',
        preview_image_url='https://picsum.photos/id/395/900/400'
    ),
    '交通': TextSendMessage(text='請問您想使用何種方式前往？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="搭乘捷運", text="捷運")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="搭乘公車", text="公車")
                              )
                          ])
                          ),
    '捷運': TextSendMessage(
        text="搭乘捷運至木柵線科技大樓站步行5分鐘即可抵達。"
    ),
    '營業地址': LocationSendMessage(
        title='my location',
        address='Tokyo',
        latitude=35.65910807942215,
        longitude=139.70372892916203
    ),
    '查詢匯率': TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    thumbnail_image_url='https://picsum.photos/id/352/900/400',
                    title='匯率選單一',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢美金',
                            text='美金'
                        ),
                        MessageAction(
                            label='查詢港幣',
                            text='港幣'
                        ),
                        MessageAction(
                            label='查詢英鎊',
                            text='英鎊'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    thumbnail_image_url='https://picsum.photos/id/364/900/400',
                    title='匯率選單二',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢澳幣',
                            text='澳幣'
                        ),
                        MessageAction(
                            label='查詢加拿大幣',
                            text='加拿大幣'
                        ),
                        MessageAction(
                            label='查詢新加坡幣',
                            text='新加坡幣'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    thumbnail_image_url='https://picsum.photos/id/355/900/400',
                    title='匯率選單三',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢瑞士法郎',
                            text='瑞士法郎'
                        ),
                        MessageAction(
                            label='查詢日圓',
                            text='日圓'
                        ),
                        MessageAction(
                            label='查詢瑞典幣',
                            text='瑞典幣'
                        )
                    ]
                )
            ]
        )
    )
}

# 主選單
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # 卡片一圖片網址
                thumbnail_image_url='https://picsum.photos/id/296/900/400',
                title='主選單一',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='查詢匯率',
                        text='查詢匯率'
                    ),
                    MessageAction(
                        label='營業時間',
                        text='營業時間'
                    ),
                    MessageAction(
                        label='營業地址',
                        text='營業地址'
                    )
                ]
            ),
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url='https://picsum.photos/id/355/900/400',
                title='主選單二',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='交通資訊',
                        text='交通'
                    ),
                    MessageAction(
                        label='門市照片',
                        text='門市照片'
                    ),
                    URIAction(
                        label='官方網站',
                        uri='https://train.csie.ntu.edu.tw/train/'
                    )
                ]
            )
        ]
    )
)
