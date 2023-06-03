import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'empolyee_id'  # Replace with your DynamoDB table name
def lambda_handler(event, context):
    # TODO implement
    print(event)
    item_data = {
        'user_id': event['queryStringParameters']['user_id'],
        'name': event['queryStringParameters']['name']
    }
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=item_data)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
