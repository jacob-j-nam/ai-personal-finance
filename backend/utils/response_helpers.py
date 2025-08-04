import json
import logging
from typing import Dict, Any, Callable
from functools import wraps

logger = logging.getLogger()

def create_api_response(status_code: int, body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a properly formatted API Gateway response
    
    Args:
        status_code: HTTP status code
        body: Response body as dictionary
        
    Returns:
        API Gateway response format
    """
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  # CORS header
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'
        },
        'body': json.dumps(body, default=str)
    }

def handle_errors(func: Callable) -> Callable:
    """
    Decorator for handling errors in Lambda functions
    
    Args:
        func: Function to wrap with error handling
        
    Returns:
        Wrapped function with error handling
    """
    @wraps(func)
    def wrapper(event, context):
        try:
            return func(event, context)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            return create_api_response(500, {
                'error': 'Internal server error',
                'message': str(e)
            })
    return wrapper

def validate_required_fields(data: Dict[str, Any], required_fields: list) -> bool:
    """
    Validate that required fields are present in request data
    
    Args:
        data: Request data dictionary
        required_fields: List of required field names
        
    Returns:
        True if all required fields are present, False otherwise
    """
    for field in required_fields:
        if field not in data or data[field] is None or data[field] == '':
            return False
    return True

def create_error_response(error_code: int, error_message: str) -> Dict[str, Any]:
    """
    Create a standardized error response
    
    Args:
        error_code: HTTP error code
        error_message: Error message
        
    Returns:
        Error response
    """
    return create_api_response(error_code, {
        'error': True,
        'message': error_message
    })

def create_success_response(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a standardized success response
    
    Args:
        data: Response data
        
    Returns:
        Success response
    """
    return create_api_response(200, {
        'success': True,
        'data': data
    }) 