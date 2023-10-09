import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28645948"))
    API_HASH = os.environ.get("API_HASH", "0d1cca3a9f4f4beb7ae8508f05ec4fcd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6570587888:AAGtvjvPgrxjIma7UJ91kRoUGKPlBl46OSY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu6n4Xavu9UzGPfnzrpZcxwNxIPcOFJ6Yjo5shY-rcVoSnJHVGNNNxxOY7fXMrZ3Vv5xEUYuxd1O5Q_mQhdAmZiMVa7pSSKK6AnWbVmEAXrtiHnQsHvu0z82UnL2YNFSIlZ68I8WdEZBM3-YOD4J0x63sDamYQE2mYjJLJOl8zWnXTJUEzDovT0ct9LimJqgQJr6JDuVAfVY1ajzYg9Wiz-cs-1d5H5tW7ykaErF3XIsbPZ1SG1nQJjEvtuiRQ9Z1tA8Sp48LVhcHEzp50RIApUHAIy9DySyQoFbXKbszvLDgaH3H6kBdkxg_coaVUKuqoG9F5RwTziiBZsWkbMoVoXY=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "filter_file_robot")
    SUPPORT = os.environ.get("SUPPORT", "logchannel37") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Miraculous_brothers_hindi_dubbed") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6425682035") # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
