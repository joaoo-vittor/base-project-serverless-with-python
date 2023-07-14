from json import dumps

# Consulte a documetação do Cerberus em: https://docs.python-cerberus.org/en/stable/
from cerberus import Validator

def make_response(status: int, body: dict) -> dict:
    return {
        "statusCode": status, 
        "body": dumps(body)
    } 

def valid_body(body: dict) -> bool:
    if body is None:
        return False
    
    schema = {
        "name": {
            "type": "string", 
            "required": True
        },
        "age": {
            "type": "integer", 
            "required": True
        }
    }


    validator = Validator(schema)
    return validator.validate(body)
