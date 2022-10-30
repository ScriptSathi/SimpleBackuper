from datetime import datetime
from typing import List
from os import listdir, path
from shutil import rmtree

from core.Context import Context
from core.Logger import logger

class BackupRotator:

    context: Context

    def __init__(self, context: Context) -> None:
        self.context = context
    
    def rotate(self) -> None:
        backup_folders = [folder for folder in listdir(self.context.parent_save_dir_path)]
        backup_sorted_list = sorted(
            backup_folders,
            key=lambda datesList: (datesList.split('-')[0], datesList.split('-')[1], datesList.split('-')[2]))
        there_is_too_many_backups = self.context.number_of_backup_to_keep < len(backup_sorted_list)
        if there_is_too_many_backups:
            self._delete_oldest_backup(backup_sorted_list)

    def _delete_oldest_backup(self, backup_sorted_list: List[str]) -> None:
        backup_to_del = backup_sorted_list[0]
        logger.info(f"Deleting oldest backup from {backup_to_del}")
        rmtree(path.join(self.context.parent_save_dir_path, backup_to_del))
