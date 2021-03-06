# filed-audio-server

A Audio file server developed with python's new and ultra light framework `FastAPI` which helps in developing APIs in less time and with best practices.

- Heroku link - https://filed-audio-server.herokuapp.com/docs
- API endpoints are mentioned below screenshots

## RUN SERVER
1. Create virtual env with `python` (Python should be greater than 3.7 version)
2. Activate env (/venv/scripts/activate for windows) (/venv/bin/activate for linux/mac)
3. Install all dependencies witb `pip install -r requirements.txt`
4. Go to app directory
5. run `python3 main.py`

## Screenshots (Swagger doc)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/one.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/two.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/one.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/three.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/four.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/five.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/six.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/seven.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/eight.png)
![image](https://github.com/Azharsayyed5/filed-audio-server/blob/main/screenshot/nine.png)

# API END POINTS

## 1. Create record
    url = /v1/filed
    method = Post
    content-type=application/json
    
   - structures:
        - song 
                
             Request body
                
               {
                "audioFileType":"song",
                "audioFileMetadata":{
                    "duration_time":<time duration in seconds>,
                    "name":"<song name>"
                    }
                }
        - podcast
            
            - request body
                   
                   {
                        "audioFileType":"podcast",
                        "audioFileMetadata":{
                                "duration_time":<time duration in seconds>,
                                "name":"<podcast name>",
                                "host":"<host name>",
                                "participents":["<participents name>","<participents name>"]
                        }
                     }      
        - audiobook
        
            - request body
            
                    {
                        "audioFileType":"audiobook",
                        "audioFileMetadata":{
                                "duration_time":<time duration in seconds>,
                                "title":"<title>",
                                "author":"<author name>",
                                "narrator":"<narrator name>"
                        }
                    }
                    
## 2. UPDATE

    url = /v1/filed/<audioFileType>/<audioFileID> 
    method = PUT
    content-type=application/json
    - song

        - url : `/v1/filed/song/1`
        - request body :

                {
                    "audioFileType":"song",
                    "audioFileMetadata":{
                            "duration_time":<time duration in seconds>,
                            "name":"<song name>"    
                    }
                }



    - podcast

        - url : `/v1/filed/podcast/1`
        - request body : 

                {
                    "audioFileType":"podcast",
                    "audioFileMetadata":{
                        "duration_time":<time duration in seconds>,
                        "name":"<podcast name>",
                        "host":"<host name>",
                        "participents":["<participents name>", "<participents name>"]    
                     }    
            }


    - audiobook

        - url : `/v1/filed/audiobook/1`       
        - request body:

                {
                "audioFileType":"audiobook",
                "audioFileMetadata":{
                        "duration_time":<time duration in seconds>,
                        "title":"<title>",
                        "author":"<author name>",
                        "narrator":"<narrator name>"  
                }
            }
## 3. delete
  
    url = /v1/filed/<audioFileType>/<audioFileID>
    method = DELETE
    content-type = application/json
    
    - Delete song record
        - url: `/v1/filed/song/1` 
    - Delete podcast record
        - url: `/v1/filed/podcast/1`
    - Delete audiobook record
        - url : `/v1/filed/audiobook/1`

## 4. Get records

   1. - URL:  `/v1/filed/<audioFileType>`
      - description: `Get all the data present for type <audioFileType>`
    
   2. - URL:  `/v1/filed/<audioFileType>/<audioFileID>`
      - description: `Get data present for type <audioFileType> and id <audioFileID>`    
