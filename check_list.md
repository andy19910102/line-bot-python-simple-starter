# 第一次開始新專案

- [] 前往Line Developer建立一個Messaging API Channel
- [] 取得Channel Secret與Channel Access Token並放置於app.py中
- [] 取得ngrok軟體並放置於專案資料夾
- [] 設定ngrok authtoken
- [] 安裝必要的套件 `pip install -r requirements.txt`

# 開始本機端開發

- [] 啟動ngrok `./ngrok http 5001`
- [] 啟動應用程式點擊右上角播放鍵按鈕或是輸入指令 `python app.py`
- [] 將ngrok的網址貼到Line Developer的Webhook URL中
- [] 透過Line App掃描QR Code並開始對話