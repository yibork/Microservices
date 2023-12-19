import requests
from rest_framework import permissions
from rest_framework.exceptions import APIException

class IsAuthenticated(permissions.BasePermission):
    message = 'User is not authenticated.'

    def has_permission(self, request, view):
        # Extract the token from the incoming request
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return False

        # Prepare the header for the external API request
        headers = {'Authorization': auth_header}

        # URL of the external API that verifies the token
        verify_url = 'http://localhost:8000/api/v1/User/token/'

        try:
            # Make a request to the external API
            response = requests.get(verify_url, headers=headers)

            # If the external API verifies the token, return True
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.RequestException as e:
            # In case of a network error, raise an exception
            raise APIException(str(e))

        return False
