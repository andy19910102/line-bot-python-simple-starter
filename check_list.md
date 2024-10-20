# 開發流程相關

## 第一次開始新專案

- [] 前往Line Developer建立一個Messaging API Channel
- [] 取得Channel Secret與Channel Access Token並放置於app.py中
- [] 取得ngrok軟體並放置於專案資料夾
- [] 設定ngrok authtoken
- [] 安裝必要的套件 `pip install -r requirements.txt`

## 開始本機端開發

- [] 啟動ngrok `./ngrok http 5001`
- [] 啟動應用程式點擊右上角播放鍵按鈕或是輸入指令 `python app.py`
- [] 將ngrok的網址貼到Line Developer的Webhook URL中
- [] 透過Line App掃描QR Code並開始對話

----

# 部署相關

## 第一次使用 Git

- [] 設定 user name 與 email

## 專案第一次上傳 Github

- [] 建立一個新的Github Repository
- [] 專案git初始化 `git init`
- [] 將專案目前所有須記錄的變更暫存 `git add .`
- [] 將暫存的檔案記錄到本地端 `git commit -m "first commit"`
- [] 變更使用main當作預設分支 `git branch -M main`
- [] 與Github Repository建立連結，請參考各自的 Repository 文件
- [] 將本地端的專案上傳到Github `git push -u origin main`

## 專案更新上傳 Github

- [] 將專案目前所有須記錄的變更暫存 `git add .`
- [] 將暫存的檔案記錄到本地端 `git commit -m "first commit"`
- [] 將本地端的專案上傳到Github `git push -u origin main`