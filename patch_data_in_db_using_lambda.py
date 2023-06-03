import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student-database')

def lambda_handler(event, context):
        rollno = event['queryStringParameters']['rollno']
        new_name = event['queryStringParameters']['name']
        print(event)
        response = table.update_item(
            Key={'rollno': rollno},
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

