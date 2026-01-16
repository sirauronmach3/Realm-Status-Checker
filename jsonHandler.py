import json

def handle_http_response(response:json) -> str:
    """
    Check HTTP response status and return response body as string.
    
    Args:
        response: HTTP response object
        
    Returns:
        str: Response body as string
        
    Raises:
        ValueError: If response status is not 200
    """
    if response.status_code != 200:
        raise ValueError(f"Expected status 200, got {response.status_code}")
    
    return response.JSONDecoder().decode(response.text)