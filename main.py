from core.BackupCreator import BackupCreator
from core.BackupRotator import BackupRotator
from core.ConfigLoad import ConfigLoader
from core.Logger import logger

def main():
    context = ConfigLoader.load()
    backup_creator = BackupCreator(context)
    backup_creator.start_backuping()
    logger.info("Backup done successfully")
    backup_rotator = BackupRotator(context)
    backup_rotator.rotate()

if __name__ == "__main__":
    main()