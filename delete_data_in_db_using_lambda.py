import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'student-details'  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    # TODO implement
    print(event)
    try:
        rollno = event['queryStringParameters']['rollno']
    except KeyError:
        return {
            'statusCode': 400,
            'body': 'Missing item ID'
        }
        
    table = dynamodb.Table(table_name)
    response = table.delete_item(
        Key={'rollno': rollno}
    )


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
