import boto3

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-south-1'
)

table = dynamodb.Table('ApplicationLogs')

table.put_item(
    Item={
        'LogID': '5001',
        'Severity': 'Critical',
        'Event': 'DiskFull'
    }
)

print("Log inserted successfully")
