import os

from src.exceptions import MissingEnvVar

DEBUG = os.getenv("DEBUG", True)

if DEBUG:
    from dotenv import load_dotenv

    load_dotenv()


def get_env_var_or_exc(var_name: str, default_value: str = None) -> str:
    result = os.getenv(var_name, default_value)
    if not result:
        raise MissingEnvVar(var_name)

    return result


DB_USER = get_env_var_or_exc("DB_USER")
DB_PASS = get_env_var_or_exc("DB_PASS")
DB_HOST = get_env_var_or_exc("DB_HOST")
DB_PORT = get_env_var_or_exc("DB_PORT")
DB_NAME = get_env_var_or_exc("DB_NAME")