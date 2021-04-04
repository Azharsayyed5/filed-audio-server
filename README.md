# filed-audio-server


- Test create song :

  curl -X 'POST' \
    'https://filed-audio-server.herokuapp.com/v1/filed/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "audioFileType": "song",
    "audioFileMetaData": {
      "uploaded_time": "2021-03-13 16:20:20",
      "duration_time": 120,
      "name": "New 2021"
    }
  }'
