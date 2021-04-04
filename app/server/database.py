import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config
import os
import sys
# MONGO_DETAILS = "mongodb://localhost:27017/"

mongo_password= os.environ.get("MONGO_PASSWORD", None)
if not mongo_password:
    sys.exit(1)

MONGO_DETAILS = f"mongodb+srv://root:{mongo_password}@cluster0.vgoq0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.myFirstDatabase

collection = database.get_collection("audio")


# helpers


def song_helper(song) -> dict:
    return {
        "id": str(song["_id"]),
        "audioFileType": song["audioFileType"],
          "audioFileMetaData": {
          "uploaded_time": song["audioFileMetaData"]["uploaded_time"],
          "duration_time": song["audioFileMetaData"]["duration_time"],
          "name": song["audioFileMetaData"]["name"] if "name" in song["audioFileMetaData"] else "NA"
        }
    }

def podcast_helper(podcast) -> dict:
    return {
        "id": str(podcast["_id"]),
        "audioFileType": podcast["audioFileType"],
          "audioFileMetaData": {
          "uploaded_time": podcast["audioFileMetaData"]["uploaded_time"],
          "duration_time": podcast["audioFileMetaData"]["duration_time"],
          "name": podcast["audioFileMetaData"]["name"],
          "host": podcast["audioFileMetaData"]["host"],
          "participents": podcast["audioFileMetaData"]["participents"]
        }
    }

def audiobook_helper(audiobook) -> dict:
    return {
        "id": str(audiobook["_id"]),
        "audioFileType": audiobook["audioFileType"],
          "audioFileMetaData": {
          "uploaded_time": audiobook["audioFileMetaData"]["uploaded_time"],
          "duration_time": audiobook["audioFileMetaData"]["duration_time"],
          "title": audiobook["audioFileMetaData"]["title"],
          "author": audiobook["audioFileMetaData"]["author"],
          "narrator": audiobook["audioFileMetaData"]["narrator"]
        }
    }  
# crud operations

# Retrieve all audios present in the database based on type
async def retrieve_audios(audio_type: str):
    audios = []
    async for audio in collection.find({"audioFileType": audio_type}):
        if audio_type == 'song':
            audios.append(song_helper(audio))
        elif audio_type == 'podcast':
            audios.append(podcast_helper(audio))
        elif audio_type == 'audiobook':
            audios.append(audiobook_helper(audio))
    return audios


# Add a new audio into to the database
async def add_audio_data(type: str, song_data: dict) -> dict:
    song = await collection.insert_one(song_data)
    new_song = await collection.find_one({"_id": song.inserted_id})
    if type == 'song':
        return song_helper(new_song)
    elif type == 'podcast':
        return podcast_helper(new_song)
    elif type == 'audiobook':
        return audiobook_helper(new_song)


# Retrieve a audio with a matching ID
async def retrieve_audio(audio_type: str, id: str) -> dict:
    audio = await collection.find_one({"_id": ObjectId(id)})
    if audio:
        if audio_type == 'song':
            return song_helper(audio)
        elif audio_type == 'podcast':
            return podcast_helper(audio)
        elif audio_type == 'audiobook':
            return audiobook_helper(audio)


# Update a audio with a matching ID
async def update_audio_db(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    audio = await collection.find_one({"_id": ObjectId(id)})
    if audio:
        updated_audio = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_audio:
            return True
        return False


# Delete a audio from the database
async def delete_audio_db(id: str):
    audio = await collection.find_one({"_id": ObjectId(id)})
    if audio:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
