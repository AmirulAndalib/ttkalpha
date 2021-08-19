try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # Set true if its VPS
        IS_VPS = False
        
        API_HASH = "7eed50ece24855c65ed1d7540a27e723"
        API_ID = 3248813
        BOT_TOKEN = "1714814585:AAHEhvhH6mDbKaL9r9q0n2KoJhabRd7B7YU"
        BASE_URL_OF_BOT = "https://torx23z.herokuapp.com"

        # Edit the server port if you want to keep it default though.
        SERVPORT = 80

        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [1706086286, 1709149684, -1001174980463, -1001421497337]
        OWNER_ID = 0
        
        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = False

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 60

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 2147483648

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = True

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DB_URI = "postgres://vkpskerczrjmxa:0af60f9edd4c4293b920be0e7824d0c656c83874e6bbd27c6a6d190bee30c7bb@ec2-54-236-137-173.compute-1.amazonaws.com:5432/dep829eme0u3iq"
        
        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        #DB_URI = "dbname=tortk user=postgres password=your-pass host=db port=5432"

        # Use the central update (everything will be updated in one msg)
        CENTRAL_UPDATE = True

        # MEGA CONFIG
        MEGA_ENABLE = True
        MEGA_API = "fW4zTYDJ"
        MEGA_UNAME = "ritikaa.singh.26+01@gmail.com"
        MEGA_PASS = "/pfVr7n))~RZ;GPh"
        ALLOW_MEGA_FOLDER = True
        ALLOW_MEGA_FILES = True
        MAX_MEGA_LIMIT = 100

        # qBittorrent Config
        # TODO add port, retry to ints
        QBIT_HOST = "localhost"
        QBIT_PORT = 8090
        QBIT_UNAME = "admin"
        QBIT_PASS = "adminadmin"
        QBIT_MAX_RETRIES = 2

        # Gdrive Config
        GDRIVE_BASE_DIR = "/"

        # Onedrive Config
        ONEDRIVE_BASE_DIR = "/"
        ONEDRIVE_BASE_FOLDER_URL = ""
        ONEDRIVE_INDEX_URL = ""

        # The base direcory to which the files will be upload if using RCLONE for other engine than GDRIVE/ONEDRIVE
        RCLONE_BASE_DIR = "/"
        
        # Set this value to show all the remotes while leeching
        SHOW_REMOTE_LIST = False
        
        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # If set then you can view the downloaded files which are currently on the server
        ENABLE_WEB_FILES_VIEW = False

        # Try beta ytdl download if errored turn this off
        ENABLE_BETA_YOUTUBE_DL = True

        # Max size direct link
        MAX_DL_LINK_SIZE = 100

        # SA Account Enable/Disable. Read the readme.md before using this feature.
        ENABLE_SA_SUPPORT_FOR_GDRIVE = False
        SA_FOLDER_ID = ""
        SA_TD_ID = ""
        SA_ACCOUNTS_FOLDER = ""

        SA_ACCOUNT_NUMBER = 0

        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 50
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 100

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = "@ondiveeranxbot" 

        # Time out for the status Delete.
        STATUS_DEL_TOUT = 120

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = False

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 180

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True
        
