import os
from core.config.environments import ENVIRONMENTS

class Settings:
    def __init__(self, env: str):
        if env not in ENVIRONMENTS:
            raise ValueError(f"Unknown environment {env}")

        self.env = env
        self.base_url = ENVIRONMENTS[env]["base_url"]