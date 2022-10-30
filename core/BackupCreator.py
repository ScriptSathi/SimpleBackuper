from os import path as os_path
from pathlib import Path

from core.Context import Context
from core.CommandUtils import CommandUtils
from core.Logger import logger

class BackupCreator:

    context: Context
    utils: CommandUtils

    def __init__(self, context: Context) -> None:
        self.context = context
        self.utils = CommandUtils(context)

    def start_backuping(self) -> None:
        self._create_folder_if_not_exist(self.context.save_dir_path)
        for dir_name in self.context.directories_to_backup:
            backup_path = os_path.join(self.context.backup_dir_path, dir_name)
            logger.info(backup_path)
            self._backup_dir(backup_path)

    def _backup_dir(self, dir_name: str) -> None:
        self.utils.scp(dir_name)

    def _create_folder_if_not_exist(self, path_to_test: str):
        path = Path(path_to_test)
        if not path.is_dir(): 
            logger.info(f"Creating directory {path_to_test}")
            path.mkdir(parents=True, exist_ok=True)
