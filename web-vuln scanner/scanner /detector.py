def is_vulnerable(response, payload):
    if payload in response.text:
        return True
    return False
