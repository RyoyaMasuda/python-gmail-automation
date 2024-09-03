import smtplib
import csv
from email.mime.text import MIMEText
import os

from dotenv import load_dotenv

load_dotenv()

#メール送信のクラス
class Send():
    # 初期化
    def __init__(self, AddressTo, subject, text):
        self.password = os.getenv('GOOGLE_APP_PASSWORD')
        self.AddressFrom = os.getenv('GMAIL_ADDRESS')
        self.AddressTo = AddressTo
        self.subject = subject
        self.text = text
        self.charset = "UTF-8"

    def send(self):
        #メールの主要設定
        msg = MIMEText(self.text.encode(self.charset), 'plain', self.charset)
        msg['From'] = self.AddressFrom
        msg['To'] = self.AddressTo
        msg['Subject'] = self.subject

        #メールの詳細設定
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        # smtp.ehlo()でsmtp側にクライアント(このPythonソースコード)を認識させる。
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.AddressFrom, self.password)
        smtp.send_message(msg)
        smtp.close()

def MailText(Name):
    with open('mail.txt', 'r') as f:
        content = f.read()

    text = content.format(Name=Name)
    return text

if __name__ == '__main__':
    #データの読み込み
    file = 'sample.csv'  #パスを相対パスで指定
    with open(file, 'r') as f:
        date = csv.reader(f)
        header = next(date)  #ヘッダーの読み込み

        for row in date:
            # 名前、アドレスをCSVから取得
            Name = row[0]  #名前
            Email = row[1]  #メールアドレス

            # メール内容
            AddressTo = Email
            subject = "test送信"
            text = MailText(Name)
            mailer = Send(AddressTo, subject, text)
            mailer.send()