from typing import Optional, Dict
import datetime
from pydantic import BaseModel, EmailStr, Field

class SongsMetaData(BaseModel):
    uploaded_time: str
    duration_time: int
    name: Optional[str]
    host: Optional[str]
    participents: Optional[list]
    title: Optional[str]
    author: Optional[str]
    narrator: Optional[str]

class AudioSchema(BaseModel):
    audioFileType: str = Field(...)
    audioFileMetaData: Optional[dict] = {}

    class Config:
        schema_extra = {
            "example": {
                    "audioFileType": "audiobook",
                    "audioFileMetaData": {
                        "uploaded_time": "2021-03-13 16:20:20",
                        "duration_time": 120,
                        "title": "happy happy",
                        "author": "azhar",
                        "narrator": "mr white"
                }
                }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(message, error="Bad Request", code=400):
    return {"error": error, "code": code, "message": message}
