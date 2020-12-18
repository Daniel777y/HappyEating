def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'access': token,
        'id': user.id,
        'username': user.username,
    }