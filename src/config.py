import os.path
import shutil
import toml

from pathlib import Path
from typing import TypedDict


# Types
class OpenAIConfig(TypedDict):
    base_url: str
    token: str


class ModelsConfig(TypedDict):
    planner: str
    scraper: str
    writer: str


class UpdatesConfig(TypedDict):
    enableCheck: bool


class Config(TypedDict):
    openai: OpenAIConfig
    models: ModelsConfig
    updates: UpdatesConfig


NUKITI_CONFIG_DIR = Path("./data")
CONFIG_DIR = Path.home() / ".config" / "GetMeA"


class ConfigManager:
    config: Config = None

    def getConfig(self):
        if self.config != None:
            return self.config

        config_file_path = CONFIG_DIR / "config.toml"

        # Check if custom config exists
        if not os.path.isfile(config_file_path):
            # Copy default config to config dir & load
            os.makedirs(CONFIG_DIR)
            shutil.copyfile(NUKITI_CONFIG_DIR / "config.default.toml", config_file_path)
            print(
                f"Copied default config to {CONFIG_DIR}. Please configure this file with your OpenAI API compatible base_url and token, and rerun this command."
            )
            exit(0)

        # Load custom config
        self.config = toml.load(config_file_path)

        return self.config


config = ConfigManager()
