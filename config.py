import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8342795792:AAHI-jRCbcyKdatQQS-20eEMc92k4K-e1yQ")
    
    API_ID = int(os.environ.get("API_ID", "22448724"))
    
    API_HASH = os.environ.get("API_HASH", "4dcc0e5b700ad50b1f878e6f1e44c172")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "7276272743"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://akalishyadav869:2cj16JGdoPv3Ssxq@cluster0.xg73wax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    MAX_RESULTS = "50"
