import logging
from json import loads, dumps
from src.utils import make_response, valid_body

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def example_get(event, context):
    return make_response(200, { "message": "Hello World" })

def scheduling(event, context):
    
    logger.info("[Message]: Hello World")
   
    return dumps({"message": "Hello World"})


def example_post(event, context):
    headers = event.get('headers')
    body = loads(event.get('body'))

    if not valid_body(body=body):
        return make_response(200, { "message": "Invalid Body" })

    return make_response(200, { "body": body, "headers": headers })
