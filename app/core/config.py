

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

    model_config = SettingsConfigDict(
        env_file=".env.example",
        env_file_encoding="utf-8"
    )


settings = Settings()
