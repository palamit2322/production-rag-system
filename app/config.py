import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

# 1️⃣ Load environment variables from .env file
load_dotenv()

# 2️⃣ Paths
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "configs"

# 3️⃣ Function to load any YAML file
def load_yaml(file_name: str) -> dict:
    file_path = CONFIG_DIR / file_name
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    
    return data

# 4️⃣ Load and merge settings
def load_settings() -> dict:
    # Determine environment (default = dev)
    env = os.getenv("APP_ENV", "dev").lower()
    
    # Load base config
    base_config = load_yaml("base.yaml")
    
    # Load environment-specific config
    env_config = load_yaml(f"{env}.yaml")
    
    # Merge configs (env overrides base)
    settings = {**base_config, **env_config}
    
    # Add secrets from environment variables
    settings["openai_api_key"] = os.getenv("OPENAI_API_KEY")
    
    return settings

# 5️⃣ Single settings object used throughout the app
settings = load_settings()
