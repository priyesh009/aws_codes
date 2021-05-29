import json
import boto3

lambda_client = boto3.client('lambda')
tbl = ['a', 'b', 'c','d']


def lambda_handler(event, context):
    print(event,'printed event')
    #print(event.get('first_run'), event.get('table_name'))
    if event.get('first_run') is True:
        tbl_lst = tbl
        print(tbl_lst)
        for i in tbl_lst:
            payload = {
                "first_run": False,
                "table_name": i
            }
            print('invoking lambda with:',i, 'and payload is :',payload)
            lambda_client.invoke(FunctionName=context.function_name,
                                 InvocationType='Event',
                                 Payload=json.dumps(payload))
    else:
        print('processing data from else block below:')
        print("################## Processing.......... the :   " + str(event.get('table_name')) + "   Data #################################")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
