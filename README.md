# python-gmail-automation
PythonでGmailを1件1件一斉送信するスクリプト

# 事前準備
- Google 2段階認証の設定
- Googleアプリパスワードの設定

## Google2段階認証の設定
[2段階認証プロセスを有効にする](https://support.google.com/accounts/answer/185839?hl=ja&co=GENIE.Platform%3DDesktop&oco=0)を参照し、2段階認証を設定してください。

## Googleアプリパスワードの設定
[アプリ パスワードを作成、管理する](https://myaccount.google.com/apppasswords)を参照し、Googleアプリパスワードを作成してください。<br>
※16桁のパスワードは一度しか表示されないので注意してください。

# 使用方法
1. このリポジトリをクローンしてください。
2. Pythonの環境を3.9.6に設定します。([Pyenv](https://github.com/pyenv/pyenv)等のバージョン管理ツールを使用することをお勧めします。)
3. 仮想環境の立ち上げ
   1. ```python -m venv .venv```で仮想環境を立ち上げます。
   2. ```source .venv/bin/activate```で仮想環境の有効化→ターミナルのプロンプトの横に`(.venv)`と表示されているか確認します。
   3. ```pip install -r requirements.txt```でライブラリをインストールします。
4. `.env.template`の名前を変更して`.env`にします。
5. `.env`ファイルの`GMAIL_ADDRESS=`に自分のGmailアドレス、`GOOGLE_APP_PASSWORD=`に先ほど設定したGoogleアプリパスワードを入力します。(クオテーションは不要)
6. sample.csvファイルの編集
   1. 1行目(header)は`名前`と`メールアドレス`にします。
   2. 2行目以降名前とメールアドレスを記載してください。
7. mail.txtの編集
   1. {Name}はsample.csvファイルに記載された名前が入力されるので{Name}以外の部分を変更してください。
   2. `sample.csv`の名前を変更する場合は`main.py`の中にある`file = 'sample.csv'` (`if __name__ == '__main__'`のすぐ下)もファイル名に合わせて変更してください。(自分でエクセルファイルを作成してアップロードする場合を想定しています。) 
8. ターミナルから```python main.py```で実行してください。
9.  メールが届いているか確認してください。
10. 使用後はターミナルで`deactivate`と入力し、(.venv)が消えたことを確認してください。 