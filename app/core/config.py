

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DB_HOST: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+psycopg://"
            f"{self.DB_USERNAME}:"
            f"{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )
    
    @property
    def REDIS_URL(self):
        return(f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/")

    model_config = SettingsConfigDict(
        env_file=".env.example",
        env_file_encoding="utf-8"
    )


settings = Settings()
