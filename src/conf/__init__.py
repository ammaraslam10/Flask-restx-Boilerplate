import json
from pathlib import Path
from typing import Any


class Settings:
    settings, locked = None, False

    def __getattr__(cls, key: str):
        if key in cls.settings:
            return cls.settings[key]
        raise AttributeError(f"'{key}' is not present in settings")

    def __delattr__(self, key: str) -> None:
        if self.locked:
            raise AttributeError(f"Can not modify settings")
        super().__delattr__(key)

    def __setattr__(self, key: str, value: Any) -> None:
        if self.locked:
            raise AttributeError(f"Can not modify settings")
        super().__setattr__(key, value)

settings = None
if not settings:
    settings = Settings()
    project_root = str(Path(__file__).resolve().parent.parent.parent)
    with open(f"{project_root}/etc/settings.json", "r") as file:
        configs = json.load(file)
        settings.settings = configs
    settings.locked = True