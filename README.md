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
3. ~~Pythonの環境を3.9.6に設定します。([Pyenv](https://github.com/pyenv/pyenv)等のバージョン管理ツールを使用することをお勧めします。)~~
4. ~~仮想環境の立ち上げ~~
   1. ~~```python -m venv .venv```で仮想環境を立ち上げます。~~
   2. ~~```source .venv/bin/activate```で仮想環境の有効化→ターミナルのプロンプトの横に`(.venv)`と表示されているか確認します。~~
   3. ~~```pip install -r requirements.txt```でライブラリをインストールします。~~
5. `.env.template`の名前を変更して`.env`にします。
6. `.env`ファイルの`GMAIL_ADDRESS=`に自分のGmailアドレス、`GOOGLE_APP_PASSWORD=`に先ほど設定したGoogleアプリパスワードを入力します。(クオテーションは不要)
7. `sample.csv.template`ファイル(名前やアドレスが記載されているファイル)の編集
   1. `sample.csv.template`のファイル名を変更し、`お好きな名前.csv`に変更してください。(一旦ここでは`test_address.csv`としておきます。)
   2. 1行目(カラム)に沿って2行目以降を入力してください。
8.  `sample.txt`ファイルの編集(メール本文が記載されているファイル)
    1. `sample.txt`の名前を編集し`お好きな名前.txt`に変更してください。(一旦ここでは`test_mail_text.txt`としておきます。)
    2. {変数名}は`test_address.csv`ファイルに記載された各カラムの情報が入力されるので{変数名}以外の部分を変更してください。
9.  `sample.yaml`ファイルの編集(設定ファイル)
    1.  `sample.yaml`の名前を編集し`お好きな名前.yaml`に変更してください。(一旦ここでは`test_setting.yaml`としておきます。)
    2.  `test_setting.yaml`を編集し、各valueを変更してください
        - `subject`はメールの本文です。(文字列で指定してください。)
        - `address_list_path`はアドレスリストのpathです。(`./test_address.csv`のように文字列で指定してください。)
        - `mail_text_path`はアドレスリストのpathです。(`./test_mail_text.txt`のように文字列で指定してください。)
        - `cc_list`はccに追加するメールアドレスです。(複数ある場合は`- `のあとに文字列で1つずつ文字列で記載してください。)
10. `sample.sh`の編集
    1.  `sample.sh`の名前を編集し`お好きな名前.sh`に変更してください。(一旦ここでは`test.sh`としておきます。)
    2.  `test.sh`内の`python main.py`の後に編集したyamlファイル名を指定してください。(例: `python main.py test_setting.yaml`)
        - 実行時はソース内で指定したコマンドライン引数(yamlファイル)を読み込みます。`test.yaml`を指定した場合は`test_setting.yaml`の情報が読み込まれ、その情報に沿って実行されます。
11. dockerコンテナの立ち上げd
    1.  `docker build -t gmail-automation .`でイメージをビルドしてください。
    2.  `docker run -it gmail-automation /bin/bash`でコンテナに入ってください。
    3.  コンテナ内のターミナルから```source test.sh```で実行してください。
12. メールが届いているか確認してください。
13. ~~使用後はターミナルで`deactivate`と入力し、`(.venv)`が消えたことを確認してください。~~
14. 使用後はコンテナ内のターミナルで`exit`を実行し、コンテナから抜けてください。
15. イメージを削除する場合
    1.  `docker image ls`でイメージ一覧を表示します。
    2.  削除したいイメージのIMAGE IDをコピーします。
    3.  `docker rmi <IMAGE ID>`の`<IMAGE ID>`の部分にペーストして実行してください。

# 補足
pyenvとvenvを使用した方法だとosよってはエラーがでる。(wsl2のubuntu20.04環境ではエラーが出ないがmacosだとエラーが出た。)<br>そのためdockerを使用することにした。