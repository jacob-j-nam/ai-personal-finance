import boto3
import logging
from typing import Any

logger = logging.getLogger()

def get_dynamodb_client() -> Any:
    """
    Get DynamoDB client with proper configuration
    """
    try:
        return boto3.client('dynamodb')
    except Exception as e:
        logger.error(f"Error creating DynamoDB client: {str(e)}")
        raise

def get_s3_client() -> Any:
    """
    Get S3 client for file operations
    """
    try:
        return boto3.client('s3')
    except Exception as e:
        logger.error(f"Error creating S3 client: {str(e)}")
        raise

def get_textract_client() -> Any:
    """
    Get Textract client for OCR operations
    """
    try:
        return boto3.client('textract')
    except Exception as e:
        logger.error(f"Error creating Textract client: {str(e)}")
        raise

def get_bedrock_client() -> Any:
    """
    Get Bedrock client for AI operations
    """
    try:
        return boto3.client('bedrock-runtime')
    except Exception as e:
        logger.error(f"Error creating Bedrock client: {str(e)}")
        raise

def get_ses_client() -> Any:
    """
    Get SES client for email operations
    """
    try:
        return boto3.client('ses')
    except Exception as e:
        logger.error(f"Error creating SES client: {str(e)}")
        raise 