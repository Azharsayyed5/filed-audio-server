from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
import datetime
from ..models.filed import (
    ErrorResponseModel,
    ResponseModel,
    AudioSchema
)

from ..database import (
    add_audio_data,
    delete_audio_db,
    retrieve_audio,
    retrieve_audios,
    update_audio_db,
)


router = APIRouter()

def validate_participents(body):
    if 'participents' in body.audioFileMetaData:
        participents = body.audioFileMetaData['participents']
        if len(participents) > 10 or any(i for i in participents if len(i) > 100):
            return True

def validate_body(body):
    keys = body.audioFileMetaData.keys()
    if body.audioFileType == "song":
        if 'name' in keys:
            return True
    elif body.audioFileType == "podcast":
        if 'name' in keys and 'host' in keys:
            return True
    elif body.audioFileType == "audiobook":
        if 'title' in keys and 'author' in keys and 'narrator' in keys:
            return True


@router.post("/", response_description="Add audio to the database")
async def add_audio(request: Request, data: AudioSchema):
    # Get raw json request body
    body = await request.body()
    json_body = await request.json()
    # Get audio type and Check if audio type is valid
    audio_type = json_body['audioFileType']
    if audio_type in ('song', 'podcast', 'audiobook'):
        # validate request body and store json encoded output
        if validate_body(data):
            # Validate participents limit
            if audio_type == 'podcast':
                if validate_participents(data):
                    return ErrorResponseModel("Number of participents should be below or equal to 10 and participents character limit should ne less than 100.")
            # Add current upload datetime
            data.audioFileMetaData['uploaded_time'] = datetime.datetime.utcnow()
            # Encode data
            create_data = jsonable_encoder(data) 
            if create_data["audioFileMetaData"]["duration_time"] <= 0:
                    return ErrorResponseModel("Please check audio duration, it should be greater than 1 second.")
            new_data = await add_audio_data(audio_type, create_data)
            return ResponseModel(new_data, "file added successfully.")
        else:
            return ErrorResponseModel("please check missing fields in the request body.")
    return ErrorResponseModel("please check audio file type, only following file types are allowed e.g song, podcast, audiobook.")


@router.put("/{audioFileType}/{audioFileID}", response_description="Audio update")
async def update_audio(audioFileType: str, audioFileID: str, data: AudioSchema):
    # Check if audio type is valid
    if audioFileType in ('song', 'podcast', 'audiobook'):
        # validate request body and update the record
        if validate_body(data):
            # Validate participents limit
            if audio_type == 'podcast':
                if validate_participents(data):
                    return ErrorResponseModel("Number of participents should be below or equal to 10 and participents character limit should ne less than 100.")
            audios = await update_audio_db(audioFileID, data)
            if audios: return ResponseModel({}, "Audio data updated successfully")
            return ErrorResponseModel("Something went wrong.")
        else:
            return ErrorResponseModel("please check missing fields in the request body.")
    else:
        return ErrorResponseModel("please check audio file type, only following file types are allowed e.g song, podcast, audiobook.")


@router.get("/{audioFileType}", response_description="Audio retrieved")
@router.get("/{audioFileType}/{audioFileID}", response_description="Audio data retrieved")
async def get_audios(audioFileType: str, audioFileID: str = None):
    # Check if audio type is valid
    if audioFileType in ('song', 'podcast', 'audiobook'):
        # If audio ID is not in path, return all the record of particular type
        if not audioFileID:
            # fetch record for ID
            audios = await retrieve_audios(audioFileType)
            if not audios:
                return ResponseModel(audios, "Empty list returned")
        else:
            # fetch all the record of particular type
            audios = await retrieve_audio(audioFileType, audioFileID)
            if not audios:
                return ErrorResponseModel("Audio doesn't exist.")
        return ResponseModel(audios, "Audio data retrieved successfully")
    else:
        return ErrorResponseModel("please check audio file type, only following file types are allowed e.g song, podcast, audiobook.")


@router.delete("/{audioFileType}/{audioFileID}", response_description="Audio delete")
async def delete_audio(audioFileType: str, audioFileID: str):
    # Check if audio type is valid
    if audioFileType in ('song', 'podcast', 'audiobook'):
        # Delete record from database
        audios = await delete_audio_db(audioFileID)
        if audios: return ResponseModel([], "Audio data deleted successfully")
        return ErrorResponseModel("Audio doesn't exist.")
    else:
        return ErrorResponseModel("please check audio file type, only following file types are allowed e.g song, podcast, audiobook.")
