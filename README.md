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
2. 以下のコマンドでプロジェクトディレクトリに移動してください。
```bash
cd python-gmail-automation
```
3. Pythonの環境を3.9.6に設定します。([Pyenv](https://github.com/pyenv/pyenv)等のバージョン管理ツールを使用することをお勧めします。)
4. 仮想環境の立ち上げ
   1. ```python -m venv .venv```で仮想環境を立ち上げます。
   2. ```source .venv/bin/activate```で仮想環境の有効化→ターミナルのプロンプトの横に`(.venv)`と表示されているか確認します。
   3. ```pip install -r requirements.txt```でライブラリをインストールします。
5. `.env.template`の名前を変更して`.env`にします。
6. `.env`ファイルの`GMAIL_ADDRESS=`に自分のGmailアドレス、`GOOGLE_APP_PASSWORD=`に先ほど設定したGoogleアプリパスワードを入力します。(クオテーションは不要)
7. sample.csv.templateファイルの編集
   1. `sample.csv.template`のファイル名を変更し、`お好きな名前.csv`に変更してください。(一旦ここでは`test.csv`としておきます。)
   2. 1行目(カラム)に沿って2行目以降を入力してください。
8.  `sample.txt`の編集
    1. `sample.txt`の名前を編集し`お好きな名前.txt`に変更してください。(一旦ここでは`test.txt`としておきます。)
    2. {変数名}は`test.csv`ファイルに記載された各カラムの情報が入力されるので{変数名}以外の部分を変更してください。
9.  `sample.yaml`の編集
    1.  `sample.yaml`の名前を編集し`お好きな名前.yaml`に変更してください。(一旦ここでは`test.yaml`としておきます。)
    2.  `test.yaml`を編集し、各valueを変更してください
        - `subject`はメールの本文です。(文字列で指定してください。)
        - `address_list_path`はアドレスリストのpathです。(`./test.csv`のように文字列で指定してください。)
        - `mail_text_path`はアドレスリストのpathです。(`./test.txt`のように文字列で指定してください。)
        - `cc_list`はccに追加するメールアドレスです。(複数ある場合は`- `のあとに文字列で1つずつ文字列で記載してください。)
10. `sample.sh`の編集
    1.  `sample.sh`の名前を編集し`お好きな名前.sh`に変更してください。(一旦ここでは`test.sh`としておきます。)
11.  ターミナルから```source test.sh```で実行してください。
12.  メールが届いているか確認してください。
13.  使用後はターミナルで`deactivate`と入力し、`(.venv)`が消えたことを確認してください。 