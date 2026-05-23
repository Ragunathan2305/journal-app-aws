this is broken code !!!
# v2 deployment test

import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JournalEntries')

def lambda_handler(event, context):
    
    http_method = event['httpMethod']
    
    # SAVE a new journal entry
    if http_method == 'POST':
        body = json.loads(event['body'])
        entry_text = body['entryText']
        
        table.put_item(Item={
            'UserID': 'user_001',
            'EntryTimestamp': datetime.now().isoformat(),
            'EntryText': entry_text
        })
        
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps('Entry saved successfully!')
        }
    
    # GET all journal entries
    elif http_method == 'GET':
        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('UserID').eq('user_001')
        )
        
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(response['Items'])
        }