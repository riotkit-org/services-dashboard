
from flask import config as AppConfig


class AdminLoginChecker:
    @staticmethod
    def is_admin_token_valid(config: AppConfig, token: str) -> bool:
        return str(config['APP_ADMIN_TOKEN']) == token
