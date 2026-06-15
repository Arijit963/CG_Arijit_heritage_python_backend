# HTTP response handler using tuple matching

def handle_response(status, message):

    match (status, message):

        case (200, msg):
            print(f"Success: {msg}")

        case (404, msg):
            print(f"Not Found: {msg}")

        case (500, msg):
            print(f"Server Error: {msg}")

        case (code, msg) if 400 <= code < 500:
            print(f"Client Error {code}: {msg}")

        case _:
            print("Unknown response")


handle_response(200, "Page loaded")
handle_response(404, "Page not found")
handle_response(403, "Access denied")