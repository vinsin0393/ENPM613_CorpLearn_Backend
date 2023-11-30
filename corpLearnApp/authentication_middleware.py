from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken

UNAUTHENTICATED_PATHS = ['/corpLearn/users/create', '/corpLearn/login', '/swagger/']  # Paths to bypass authentication


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if any(request.path.startswith(path) for path in UNAUTHENTICATED_PATHS):
            return None

        jwt_authenticator = JWTAuthentication()
        try:
            user_auth = jwt_authenticator.authenticate(request)
            if user_auth is not None:
                request.user, request.auth = user_auth

                if request.method in ["PUT", "DELETE"] and not request.user.role.allow_edit():
                    raise AuthenticationFailed('User does not have permission for this action')


            else:
                raise AuthenticationFailed('Authentication failed')

        except InvalidToken as e:
            raise AuthenticationFailed(f'Invalid token: {e}')
        except AuthenticationFailed as e:
            raise

