from dataclasses import dataclass
from typing import List

@dataclass()
class Context:
    remote_user: str
    ip_addr: str
    port: int
    ssh_key_path: int
    backup_dir_path: str
    save_dir_path: str
    parent_save_dir_path: str
    directories_to_backup: List[str]
    number_of_backup_to_keep: int