import os
from core.config.environments import ENVIRONMENTS

ENV = os.getenv("ENV", "dev")
BASE_URL = ENVIRONMENTS[ENV]