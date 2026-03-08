import json
import base64
import boto3

s3 = boto3.client('s3')

BUCKET_NAME = "nikhil-cloud-lab"   # make sure this is EXACT bucket name

def lambda_handler(event, context):

    try:
        body = json.loads(event["body"])

        file_name = body["file_name"]
        file_data = body["file_data"]

        decoded_file = base64.b64decode(file_data)

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=decoded_file
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "File uploaded successfully"})
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }