## 概要

lambda でローカル開発環境のテンプレート
  - with Selenium
    - with 日本語化


* python3
* docker-lambda
* selenium
* lambda

## ディレクトリ構成

```
.
├── Dockerfile ・・・deployパッケージファイル作成用のDockerfile
├── README.md
├── lambda_function.py ・・・実行ファイル
├── layers
│   └── python3-selenium-headless ・・・headress 用のドライバ
│             └── headless
│               └── python
│                    └── bin
│                        ├── chromedriver
│                        ├── headless-chromium
│                        └── locales
└── requirements.txt ・・・依存ファイル
```

## 開発環境

docker-lambda を利用して、lambda と同等の環境で実行します。

```shell script
$ docker run -v "$PWD":/var/task -e WANT_ENVIRONMENT="" lambci/lambda:python3.7 lambda_function.lambda_handler
```

## デプロイ

```shell script
$ docker build -t your-image-name .
$ docker run -v "$PWD":/var/task your-image-name:latest
# デプロイ用のファイルが作成できたことを確認
$ ls -al deploy_package.zip

$ aws s3 cp deploy_package.zip s3://your-s3-bucket

$ aws lambda update-function-code --function-name your-lambda-function --profile default --region ap-northeast-1 --s3-bucket your-s3-bucket --s3-key deploy_package.zip
```
