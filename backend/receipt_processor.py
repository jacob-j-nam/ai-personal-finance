# Receipt processing module for text extraction using AWS Textract 

import json
from typing import Dict, Any
from utils.aws_helpers import get_textract_client

def process_receipt_with_textract(bucket_name: str, object_key: str) -> Dict[str, Any]:
    """
    Process a receipt image stored in S3 using AWS Textract
    
    Args:
        bucket_name (str): Name of the S3 bucket containing the image
        object_key (str): S3 object key (file path) of the image
        
    Returns:
        Dict[str, Any]: Raw Textract response containing extracted text and metadata
        
    Raises:
        Exception: If Textract processing fails
    """
    try:
        # Get Textract client
        textract_client = get_textract_client()
        
        # Call Textract with S3 object reference
        response = textract_client.analyze_document(
            Document={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': object_key
                }
            },
            FeatureTypes=['FORMS', 'TABLES', 'LINES']  # Extract forms, tables, and individual text lines
        )
        
        print(f"Textract processing completed for {bucket_name}/{object_key}")
        print(f"Extracted {len(response.get('Blocks', []))} blocks")
        print(response)
        
        return response
        
    except Exception as e:
        print(f"Error processing receipt with Textract: {str(e)}")
        raise 