from yaml import safe_load
from os import path
from datetime import datetime

from core.Context import Context
from core.Constants import Constants

class ConfigLoader:
    def load() -> Context:
        with open(Constants.config_file_path, 'r') as yaml_file:
            config_data = safe_load(yaml_file)
            save_dir_path = path.join(config_data['pathWhereToSaveBackup'],
                            ConfigLoader._generate_dateTime_dir_name())
            return Context(config_data['remoteUser'], config_data['remoteIP'], 
                           config_data['remotePort'], config_data['sshKeyPath'],
                           config_data['pathToBackupDir'], save_dir_path, 
                           config_data['pathWhereToSaveBackup'], config_data['directoryNameToBackup'],
                           config_data['numberOfBackupToKeep'])

    def _generate_dateTime_dir_name() -> str:
        return datetime.now().strftime("%Y-%m-%d")
