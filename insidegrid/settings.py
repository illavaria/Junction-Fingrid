from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DBNAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_URL: str = ''  # noqa: value is set auto
    ROOT_FOLDER_ID: str
    TEMPLATES_DIRECTORY: str = 'templates'

    @model_validator(mode='after')
    def build_auto_values(self, data):
        # build POSTGRES_URL
        self.POSTGRES_URL = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST,
            self.POSTGRES_PORT,
            self.POSTGRES_DBNAME
        )


settings = Settings(_env_file=['../.env.local', '../.env'])
