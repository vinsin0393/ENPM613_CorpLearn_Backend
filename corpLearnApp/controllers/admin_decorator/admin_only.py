from rest_framework.response import Response
from rest_framework import status

def admin_only(controller_func):
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'role') and request.user.role.id == 1:
            return controller_func(request, *args, **kwargs)
        return Response({'error': 'You do not have permission to perform this action'}, status=status.HTTP_403_FORBIDDEN)
    wrapper.__name__ = controller_func.__name__
    return wrapper
