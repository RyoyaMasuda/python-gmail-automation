import smtplib  # SMTPサーバーとの通信を行うためのモジュール
from email.mime.text import MIMEText  # メール本文を作成するためのモジュール
import os
import sys
import yaml
from pprint import pprint
import pandas as pd

from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# コマンドライン引数に「読み込むyamlファイルのファイル名」を指定する。何も指定しない場合はsample.yamlが読み込まれる。 
if len(sys.argv) > 1:
    yaml_file_path = f'./{sys.argv[1]}'   
else:
    yaml_file_path = './sample.yaml'

with open(yaml_file_path, 'r') as f:
    setting_yaml = yaml.safe_load(f)

# メール送信を行うクラス
class Send():
    # クラスの初期化メソッド
    def __init__(self, AddressTo: str, subject: str, text: str, cc_list: list=None) -> None:
        self.password = os.getenv('GOOGLE_APP_PASSWORD')
        self.AddressFrom = os.getenv('GMAIL_ADDRESS')
        self.AddressTo = AddressTo  # 受信者のメールアドレス
        self.subject = subject  # メールの件名
        self.text = text  # メールの本文
        self.charset = "UTF-8"  # 文字エンコードの設定
        
        # cc_listにCCに入れるメールアドレスがlist形式で指定されている場合、
        if cc_list:
            self.cc_list = cc_list
        else:
            self.cc_list = []
        
    def send(self):
        # メールの本文を設定
        msg = MIMEText(self.text.encode(self.charset), 'plain', self.charset)
        msg['From'] = self.AddressFrom  # 送信者のメールアドレスを設定
        msg['To'] = self.AddressTo  # 受信者のメールアドレスを設定
        msg['Subject'] = self.subject  # メールの件名を設定

        # CCの設定
        msg['Cc'] = ', '.join(self.cc_list)

        # SMTPサーバーへの接続とメール送信の設定
        smtp = smtplib.SMTP('smtp.gmail.com', 587)  # GmailのSMTPサーバーに接続
        smtp.ehlo()  # サーバーにクライアントの情報を通知
        smtp.starttls()  # TLS暗号化を開始
        smtp.ehlo()  # TLSセッションで再度クライアントの情報を通知
        smtp.login(self.AddressFrom, self.password)  # Gmailアカウントにログイン
        smtp.send_message(msg)  # メールを送信
        smtp.close()  # SMTPセッションを終了

# メール本文を生成する関数
def MailText(last_name, first_name, company_name, position, mail_text_path):

    with open(mail_text_path, 'r') as f:
        content = f.read()  # テキストファイルからメールのテンプレートを読み込み

    text = content.format(last_name=last_name,
                          first_name=first_name,
                          company_name=company_name,
                          position=position)  # テンプレートに名前を挿入
    
    return text  # メール本文を返す

if __name__ == '__main__':

    # 設定ファイル(yaml)から必要情報を読み込む
    subject = setting_yaml['subject']  # メールの件名
    cc_list = setting_yaml['cc_list'] # CCのリスト
    address_list_path = setting_yaml['address_list_path']
    mail_text_path = setting_yaml['mail_text_path']

    # CSVファイルからデータを読み込む
    df = pd.read_csv(address_list_path)

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

        text = MailText(last_name, first_name, company_name, position, mail_text_path)
        
        mailer = Send(AddressTo, subject, text, cc_list)
        mailer.send()
