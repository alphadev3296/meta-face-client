from pathlib import Path


class Config:
    ROOT_DIR: Path = Path(__file__).parent.parent
    STATIC_DIR: Path = ROOT_DIR / "static"


config = Config()
