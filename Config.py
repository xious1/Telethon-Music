import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25656584"))
    API_HASH = os.environ.get("API_HASH", "df0659031ea6af4d4e8f905ad0c09750")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6085468201:AAHUneVmxENO1qmA5fsMfbkVaLPQJ3YYHZw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGYBu0yGADpbhhxAyS8_MZnadCXXrcoBEWxyMU66FyAkwsH5tI4A7SL8sT9o6-_NBh3EY2_E7L5dH30HQJ6JcApjg5bGsPPFXTvLxq1zV1cyHh5jKtDK5HnlEOgNlgkwwku3W2OeuxmfF704liE2whbns3eljMxf1dJlVsbfERkyH2tFc9aIaicn2jydJo3nDVOi37eJCzVkvsLgdbQcf7kBCxBENV8UJUTudN5T074uMYzCPvelFg2qU48bl6TKQ3P7If2L574TNvTP0zx4m55G1L89oy_bI5Upk8RNnC90eWAJHE8Y3DSrc1HR0TIv4eWVFxjdIXhfyIdfloU_2K8kL6E= ")
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
