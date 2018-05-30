def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    msg = req
    if len(req) == 0:
    	return "Pass value to function"

    return str.format("Someone said: {}", msg)
