from AkenoHimejimabot.sample_config import Config

class Development(Config):
    OWNER_ID = 1364874872  # your telegram ID
    OWNER_USERNAME = "no_phd"  # your telegram username
    API_KEY = "1422638635:AAEIFWpaB_IjG9cWSwmQ-0D8L9AWsXMcCMA"  # your api key, as provided by the @botfather
    JOIN_LOGGER = '-1001215912907' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    DRAGONS = [275257858, 1447345851]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
