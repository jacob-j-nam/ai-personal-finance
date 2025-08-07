# Main Lambda function handler for personal finance receipt processing 

import json
import boto3
import os
from typing import Dict, Any

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Main Lambda handler function
    """
    try:
        # Handle multiple records if they exist
        if 'Records' in event and event['Records']:
            for record in event['Records']:
                if record.get('eventSource') == 'aws:s3':
                    return handle_s3_upload(event, context)
        
        # Default response for other event types
        return {
            'statusCode': 200,
            'body': json.dumps('Event processed successfully')
        }
        
    except Exception as e:
        print(f"Error in lambda_handler: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def handle_s3_upload(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Handle S3 upload events
    Triggered when a file is uploaded to the S3 bucket
    """
    try:
        # Extract S3 event details
        record = event['Records'][0]
        s3_data = record['s3']
        
        # Get bucket and key information
        bucket_name = s3_data['bucket']['name']
        object_key = s3_data['object']['key']
        object_size = s3_data['object']['size']
        
        print(f"S3 Upload Event:")
        print(f"  Bucket: {bucket_name}")
        print(f"  Key: {object_key}")
        print(f"  Size: {object_size} bytes")
        
        # Get environment variables
        s3_bucket_name = os.environ.get('S3_BUCKET_NAME')
        dynamodb_table_name = os.environ.get('DYNAMODB_TABLE_NAME')
        
        print(f"Environment Variables:")
        print(f"  S3_BUCKET_NAME: {s3_bucket_name}")
        print(f"  DYNAMODB_TABLE_NAME: {dynamodb_table_name}")
        
        # TODO: Add your receipt processing logic here
        # This is where you would:
        # 1. Download the image from S3
        # 2. Process it with Textract
        # 3. Store results in DynamoDB
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'S3 upload processed successfully',
                'bucket': bucket_name,
                'key': object_key,
                'size': object_size
            })
        }
        
    except Exception as e:
        print(f"Error in handle_s3_upload: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing S3 upload: {str(e)}')
        } 