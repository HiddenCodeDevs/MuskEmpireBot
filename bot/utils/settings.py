from pydantic_settings import BaseSettings, SettingsConfigDict
from bot.utils.logger import log

logo = """

███    ███ ██    ██ ███████ ██   ██     ███████ ███    ███ ██████  ██ ██████  ███████ 
████  ████ ██    ██ ██      ██  ██      ██      ████  ████ ██   ██ ██ ██   ██ ██      
██ ████ ██ ██    ██ ███████ █████       █████   ██ ████ ██ ██████  ██ ██████  █████   
██  ██  ██ ██    ██      ██ ██  ██      ██      ██  ██  ██ ██      ██ ██   ██ ██      
██      ██  ██████  ███████ ██   ██     ███████ ██      ██ ██      ██ ██   ██ ███████ 
                                                                                      
"""


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_ID: str = 'hero737844465'

    TAPS_ENABLED: bool = True
    TAPS_PER_SECOND: list[int] = [20, 30]  # tested with 4 fingers
    PVP_ENABLED: bool = False
    PVP_LEAGUE: str = 'bronze'
    PVP_STRATEGY: str = 'random'
    PVP_COUNT: int = 10

    SLEEP_BETWEEN_START: list[int] = [20, 360]
    ERRORS_BEFORE_STOP: int = 3
    USE_PROXY_FROM_FILE: bool = False


try:
    config = Settings()
except Exception as error:
    log.error(error)
    config = False
