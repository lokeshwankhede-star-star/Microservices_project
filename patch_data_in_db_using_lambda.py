import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('empolyee_id')

def lambda_handler(event, context):
        employee_id = event['queryStringParameters']['user_id']
        new_name = event['queryStringParameters']['name']
        print(event)
        response = table.update_item(
            Key={'user_id': employee_id},
            UpdateExpression='SET #n = :name',
            ExpressionAttributeNames={'#n': 'name'},
            ExpressionAttributeValues={':name': new_name},
            ReturnValues='ALL_NEW'
        )

        updated_item = response['Attributes']

        return {
            'statusCode': 200,
            'body': json.dumps("Hello from Lambda!")
        }

