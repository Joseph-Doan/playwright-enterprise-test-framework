import yaml
from pathlib import Path


CONFIG_FILE = Path("config/environments.yaml")


class Settings:
    def __init__(self, env="local"):
        with open(CONFIG_FILE, "r") as file:
            data = yaml.safe_load(file)

        if env not in data:
            raise ValueError(f"Unknown environment: {env}")

        self.base_url = data[env]["base_url"]