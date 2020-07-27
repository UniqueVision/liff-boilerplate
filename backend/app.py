import os
from chalice import Chalice
import requests
import boto3

# TODO:ログインチャネルのチャネルIDを設定する
CLIENT_ID = ''

app = Chalice(app_name='backend')

def get_dynamodb_resource():
    dynamo_endpoint = os.getenv('ENDPOINT_URL')
    if dynamo_endpoint:
        return boto3.resource('dynamodb', endpoint_url=dynamo_endpoint, region_name='us-east-1')
    else:
        return boto3.resource('dynamodb')

@app.route('/', cors=True, methods=['POST'])
def index():
    # IDトークンを検証する
    # https://developers.line.biz/ja/reference/social-api/#verify-id-token
    request = app.current_request
    r = requests.post('https://api.line.me/oauth2/v2.1/verify', data={
        'id_token': request.json_body['idToken'],
        'client_id': CLIENT_ID
    })

    # DynamoDBにデータを保存
    dynamodb = get_dynamodb_resource()
    table = dynamodb.Table(os.getenv('TABLE_NAME'))
    table.put_item(Item=r.json())

    # レスポンスを作成
    # NOTE: 以下のレスポンスはサンプルです
    return {'message': 'こんにちは、{0}さん。'.format(data['name'])}
