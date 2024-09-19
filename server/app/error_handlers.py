from flask import jsonify

def handle_validation_error(error):
    """Handle validation errors."""
    response = {
        "status": "error",
        "message": "Validation Error",
        "details": error.messages  # Assuming error.messages contains the details
    }
    return jsonify(response), 400

def handle_not_found_error(error):
    """Handle not found errors."""
    response = {
        "status": "error",
        "message": "Resource Not Found"
    }
    return jsonify(response), 404

def handle_internal_server_error(error):
    """Handle internal server errors."""
    response = {
        "status": "error",
        "message": "Internal Server Error"
    }
    return jsonify(response), 500