import logging
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

def exception_log_handler(service_func):
    def wrapper(*args, **kwargs):
        try:
            return service_func(*args, **kwargs)
        except ObjectDoesNotExist as e:
            logger.error(f'Object not found: {e}')
            raise
        except Exception as e:
            logger.error(f'Error in service layer: {e}')
            raise
    return wrapper
