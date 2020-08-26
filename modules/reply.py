from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn
)

# 官方文件
# https://github.com/line/line-bot-sdk-python


faq = {
    '貼圖': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
    '照片': ImageSendMessage(
        original_content_url='https://picsum.photos/id/1040/900/400',
        preview_image_url='https://picsum.photos/id/1040/900/400'
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
                    # 卡片一圖片網址
                    thumbnail_image_url='https://picsum.photos/id/1070/900/400',
                    title='卡片一標題',
                    text='內文一',
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
                    # 卡片二圖片網址
                    thumbnail_image_url='https://picsum.photos/id/1071/900/400',
                    title='卡片二標題',
                    text='內文二',
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
                    # 卡片三圖片網址
                    thumbnail_image_url='https://picsum.photos/id/1072/900/400',
                    title='卡片三標題',
                    text='內文三',
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
                thumbnail_image_url='https://picsum.photos/id/1070/900/400',
                title='主選單',
                text='主選單敘述',
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
            )
        ]
    )
)
