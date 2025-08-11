from fastapi import HTTPException, status
from bson.errors import InvalidId

class InvalidObjectIdException(HTTPException):
    def __init__(self, detail: str = "Invalid ObjectId format"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)



from bson import ObjectId

def get_object_id(id_str: str) -> ObjectId:
    try:
        return ObjectId(id_str)
    except InvalidId:
        raise InvalidObjectIdException()

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Internal Server Error")
    

class OpenAIKeyError(Exception):
    pass

class OpenAIModelError(Exception):
    pass