from processor import Processor


def get_items_to_process():
    return ['a', 'b', 'c','d']
    
    
def process_item(item):
    print('processing data from else block below:')
    print("################## Processing.......... the :   " + item + "   Data #################################")


def lambda_handler(event, context):
    print(event)
    processor = Processor(event)
    return processor.process(context, get_items_to_process(), process_item)