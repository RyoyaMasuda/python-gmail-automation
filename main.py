import smtplib  # SMTPサーバーとの通信を行うためのモジュール
import csv  
from email.mime.text import MIMEText  # メール本文を作成するためのモジュール
import os
import pandas as pd
from IPython.display import display

from dotenv import load_dotenv

load_dotenv()

# メール送信を行うクラス
class Send():
    # クラスの初期化メソッド
    def __init__(self, AddressTo, subject, text):
        self.password = os.getenv('GOOGLE_APP_PASSWORD')
        self.AddressFrom = os.getenv('GMAIL_ADDRESS')
        self.AddressTo = AddressTo  # 受信者のメールアドレス
        self.subject = subject  # メールの件名
        self.text = text  # メールの本文
        self.charset = "UTF-8"  # 文字エンコードの設定

    def send(self):
        # メールの本文を設定
        msg = MIMEText(self.text.encode(self.charset), 'plain', self.charset)
        msg['From'] = self.AddressFrom  # 送信者のメールアドレスを設定
        msg['To'] = self.AddressTo  # 受信者のメールアドレスを設定
        msg['Subject'] = self.subject  # メールの件名を設定

        # SMTPサーバーへの接続とメール送信の設定
        smtp = smtplib.SMTP('smtp.gmail.com', 587)  # GmailのSMTPサーバーに接続
        smtp.ehlo()  # サーバーにクライアントの情報を通知
        smtp.starttls()  # TLS暗号化を開始
        smtp.ehlo()  # TLSセッションで再度クライアントの情報を通知
        smtp.login(self.AddressFrom, self.password)  # Gmailアカウントにログイン
        smtp.send_message(msg)  # メールを送信
        smtp.close()  # SMTPセッションを終了

# メール本文を生成する関数
def MailText(last_name, first_name, company_name, position):
    with open('mail.txt', 'r') as f:
        content = f.read()  # テキストファイルからメールのテンプレートを読み込み

    text = content.format(last_name=last_name,
                          first_name=first_name,
                          company_name=company_name,
                          position=position)  # テンプレートに名前を挿入
    
    return text  # メール本文を返す

if __name__ == '__main__':
    # CSVファイルからデータを読み込む
    file = 'sample.csv'  # 読み込むCSVファイルのパス
    # with open(file, 'r') as f:
    #     date = csv.reader(f)  # CSVファイルを読み込む
    #     header = next(date)  # CSVファイルのヘッダーを読み飛ばす
    df = pd.read_csv(file)


    for _idx, row in df.iterrows():
        # CSVの各行から名前とメールアドレスを取得
        # Name = row[0]  # 名前
        Email = row['メールアドレス']  # メールアドレス
        company_name = row['会社・組織名']
        first_name = row['氏名（名）']
        last_name = row['氏名（姓）']
        position = row['役職']

        # メール送信の設定
        AddressTo = Email  # 受信者のメールアドレス
        subject = "test送信"  # メールの件名
        text = MailText(last_name, first_name, company_name, position)
        mailer = Send(AddressTo, subject, text)
        mailer.send()
