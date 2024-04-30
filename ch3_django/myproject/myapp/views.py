import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page accessed.")
    return HttpResponse("Hello, world. You're at the myapp index.")


def about(request):
    try:
        # raise Exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error: {e}', exc_info=e)
        return HttpResponse("Error in myapp: " + str(e))
    else:
        logger.debug('About page accessed.')
        return HttpResponse("Hello, world. You're at the myapp about.")
