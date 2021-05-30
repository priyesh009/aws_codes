import json
import boto3
from processor import Processor

lambda_client = boto3.client('lambda')

def get_items_to_process():
    return ['a', 'b', 'c','d']
    
    
def process_item(item):
    print('processing data from else block below:')
    print("################## Processing.......... the :   " + item + "   Data #################################")


def lambda_handler(event, context):
    print(event)
    processor = Processor(event)
    return processor.process(context, get_items_to_process(), process_item)