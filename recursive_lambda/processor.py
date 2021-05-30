import boto3
import json

class Processor:
    def __init__(self, event):
        self.event = event


    def process(self, context, items, function):
        if self.event.get('detail-type') == "Scheduled Event":
            for item in items:
                payload = {
                "table_name": item
                }
                self._make_recursive_call(context,payload)

        else:
            tab_nm=self.event.get('table_name')
            function(tab_nm)
        return


    def _make_recursive_call(self, context,payload):
        lambda_client = boto3.client('lambda')
        lambda_client.invoke(FunctionName=context.function_name,
                             InvocationType='Event',
                             Payload=json.dumps(payload))
        return