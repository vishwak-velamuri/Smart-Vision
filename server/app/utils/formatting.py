def format_response(data):
    """Format data for API response."""
    return {
        "status": "success",
        "data": data
    }

def format_error(message):
    """Format error messages for API responses."""
    return {
        "status": "error",
        "message": message
    }