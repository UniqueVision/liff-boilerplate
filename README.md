# liff-boilerplate
本リポジトリはLIFFアプリを素早く実装することを目的に作成されました。


# 実行方法

1. LIFF IDを設定

`./frontend/src/App.vue`の以下の部分にLIFF IDを設定する

```
// TODO:LIFF IDを設定する
const isInit = await liff.init('');
```

2. ログインチャネルのチャネルIDを設定

`./backend/app.py`の以下の部分に、ログインチャネルのチャネルIDを設定する

```
# TODO:ログインチャネルのチャネルIDを設定する
CLIENT_ID = ''
```

3. コンテナの起動

ポート番号は環境に応じて適宜修正する

```
docker-compose up -d
```

4. DynamoDBのテーブルを作成

サンプルでは`users`というテーブルの存在を期待します

```
aws --endpoint-url=http://localhost:8000 dynamodb create-table \
  --table-name users \
  --attribute-definitions AttributeName=name,AttributeType=S \
  --key-schema AttributeName=name,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
```

テーブル一覧を確認

```
aws --endpoint-url=http://localhost:8000 dynamodb list-tables
```

テーブルの内容を確認

```
aws --endpoint-url=http://localhost:8000 dynamodb scan --table-name users
```

4. ngrokの起動

フロントエンドのコンテナが動いているポート番号をフォワードする

```
ngrok http --host-header=rewrite 4001
```

5. ngrokのURLをLIFFアプリのエンドポイントURLに設定する
