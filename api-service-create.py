import json
import boto3
import random

def lambda_handler(event, context):
  
  member_name = ['Ama', 'Jone', 'Zon', 'Penny', 'Jessie']
  member_status = ['Happy', 'Sad', 'Serious', 'Satisfied', 'Free']

  dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb.ap-northeast-2.amazonaws.com')
  member_table = dynamodb.Table('hello-member')

  name = member_name[random.randint(0, 4)]
  status = member_status[random.randint(0, 4)]

  member_table.put_item(
    Item = {
      'name': name,
      'status': status,
    }
  )

  documents = {'name': name, 'status': status}

  print(documents)

  return {
    'statusCode': 200,
    'headers': {'Access-Control-Allow-Origin': '*'},
    'body': json.dumps(documents)
  }