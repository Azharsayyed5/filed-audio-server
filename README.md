# filed-audio-server


# API END POINTS

@ 1. Create record /n
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
                    
- 2. UPDATE

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

- 3. delete
  
    url = /v1/filed/<audioFileType>/<audioFileID>
    method = DELETE
    content-type = application/json
    
    - Delete song record
        - url: `/v1/filed/song/1` 
    - Delete podcast record
        - url: `/v1/filed/podcast/1`
    - Delete audiobook record
        - url : `/v1/filed/audiobook/1`

- 4. Get records

   1. - URL:  `/v1/filed/<audioFileType>`
      - description: `Get all the data present for type <audioFileType>`
    
   2. - URL:  `/v1/filed/<audioFileType>/<audioFileID>`
      - description: `Get data present for type <audioFileType> and id <audioFileID>`    
