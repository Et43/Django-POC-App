from django.utils.deprecation import MiddlewareMixin

class LogRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Extract headers and redact cookies
        headers = {key: ("[redacted]" if key.lower() == "cookie" else value) for key, value in request.headers.items()}
        
        # Print the structured HTTP request details
        print("\n----- Raw HTTP Request -----")
        print(f"Method: {request.method}")
        print(f"Path: {request.get_full_path()}")
        print("\nHeaders:")
        for key, value in headers.items():
            print(f"{key}: {value}")
        
        # Print body only if it's not empty
        if request.body:
            print("\nBody:")
            print(request.body.decode('utf-8', errors='replace'))
        else:
            print("\nBody: [empty]")

        print("----------------------------\n")
