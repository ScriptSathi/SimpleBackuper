from os import path
from pathlib import Path

class Constants:
    project_path = Path(path.dirname(__file__)).parent.absolute()
    config_file_path = path.join(project_path, "config.yml")