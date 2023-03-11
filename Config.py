import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25656584"))
    API_HASH = os.environ.get("API_HASH", "df0659031ea6af4d4e8f905ad0c09750")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6085468201:AAHUneVmxENO1qmA5fsMfbkVaLPQJ3YYHZw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGYBuzt-22pvzm_wZ5Vv7v7EQehnhdH2BilMk49KNLVXBgIxGbs6Fmnn9BWGOWq01aEHAbdxYy7KcyIaLHEjQJi4K4XOMJ97iW5Hf-UO3A0LWJ6MzsGsbmBm531L06EvcrEqR8bpWGB6bADShPCXoJGJjsiRmjK2Ffm6h1lFVdI_TkIV8RfSnVS9nY11fWmrfpBkCGH2vF6u7ed3Z2l-yHtzS4En_Em1XK03Erd-2D1Vk9iypiaYhzQRBHSqYj-KgHmzPnvsVFgQFZVQUPGp7npELaKPAqydOjuw5Y3-WDXinoaNdq3Teoq4ivkAzZBG9n_dzNVSpOdYUdb6nc1jnrZOg84=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ShelbysMusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6052457588")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
