import logging
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def exception_log_handler(controller_func):
    def wrapper(*args, **kwargs):
        request = args[0]
        try:
            return controller_func(*args, **kwargs)
        except ValidationError as e:
            logger.error(f'Validation error in {request.path}: {e}')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            logger.error(f'Object not found in {request.path}')
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f'Unexpected error in {request.path}: {e}')
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    wrapper.__name__ = controller_func.__name__
    return wrapper
