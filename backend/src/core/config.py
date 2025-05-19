import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DATABASE", env_file=".env")
    database_host: str
    database_port: int
    database_username: str
    database_password: str
    database_name: str
    redis_host: str
    redis_port: int


class AuthJWT(BaseSettings):
    """
    base config for jwt information
    """

    public_key_path: str
    private_key_path: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    token_type_field: str


class AuthConfig(BaseSettings):
    verification_code_time_expiration: int
    jwt: AuthJWT


def load_config() -> AuthConfig:
    """
    return config in modules that requires settings
    :return: config with all parameters
    """
    return AuthConfig(
        verification_code_time_expiration=60 * 5,
        jwt=AuthJWT(
            public_key_path=Path(
                os.path.join(BASE_DIR.parent, "certs", "jwt-public.pem")
            ).read_text(),
            private_key_path=Path(
                os.path.join(BASE_DIR.parent, "certs", "jwt-private.pem")
            ).read_text(),
            algorithm="RS256",
            access_token_expire_minutes=5,
            refresh_token_expire_days=10,
            token_type_field="token_type",
        ),
    )


auth_config: AuthConfig = load_config()
db_config = DBConfig()
