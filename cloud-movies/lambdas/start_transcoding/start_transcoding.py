import os
import json
import boto3
import time


def handler(event, context):
    state_machine_arn = os.environ['TRANSCODING_STATE_MACHINE']
    sfn_client = boto3.client('stepfunctions')
    
    object_key = event['Records'][0]['s3']['object']['key']
    timestamp = str(round(time.time()))
    print(timestamp)
    sfn_client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps({
            'objectKey': object_key,
            'timestamp': timestamp
        })
    )
