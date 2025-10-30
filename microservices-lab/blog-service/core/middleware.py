import logging

logger = logging.getLogger(__name__)

class LogAuthorizationHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            # Solo loguea, no valida
            logger.info(f"Authorization header found: {auth_header[:15]}...") # Loguea solo el inicio
        else:
            logger.info("No Bearer token found in Authorization header.")

        response = self.get_response(request)
        return response