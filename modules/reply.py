from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn
)

class Menu:
    def __init__(self):
        # https://github.com/line/line-bot-sdk-python
        # 請參考TemplateSendMessage - CarouselTemplate格式
        # 選單
        self.data = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://picsum.photos/id/1070/900/400',
                        title='標題1',
                        text='內文1',
                        actions=[
                            MessageAction(
                                label='按鈕1',
                                text='回傳內容1'
                            ),
                            MessageAction(
                                label='按鈕2',
                                text='回傳內容2'
                            ),
                            MessageAction(
                                label='按鈕3',
                                text='回傳內容3'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://picsum.photos/id/1071/900/400',
                        title='標題2',
                        text='內文2',
                        actions=[
                            MessageAction(
                                label='按鈕4',
                                text='回傳內容4'
                            ),
                            MessageAction(
                                label='按鈕5',
                                text='回傳內容5'
                            ),
                            MessageAction(
                                label='按鈕6',
                                text='回傳內容6'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://picsum.photos/id/1072/900/400',
                        title='標題3',
                        text='內文3',
                        actions=[
                            MessageAction(
                                label='按鈕7',
                                text='回傳內容7'
                            ),
                            MessageAction(
                                label='按鈕8',
                                text='回傳內容8'
                            ),
                            MessageAction(
                                label='按鈕9',
                                text='回傳內容9'
                            )
                        ]
                    )
                ]
            )
        )
    
    def get_menu(self):
        # 回傳選單
        return self.data