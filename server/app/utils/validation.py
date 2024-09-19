def validate_user_data(user_data):
    """Validate user data before processing."""
    if not isinstance(user_data.get("email"), str) or "@" not in user_data["email"]:
        raise ValueError("Invalid email address.")
    if not isinstance(user_data.get("name"), str) or len(user_data["name"]) < 1:
        raise ValueError("Name must be a non-empty string.")
    return True