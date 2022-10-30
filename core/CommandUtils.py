from subprocess import Popen, PIPE

from core.Logger import logger
from core.Context import Context

class CommandUtils:
    def spawn(cmd: str) -> None:
        process = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
        _stdout, _stderr = process.communicate()
        stdout, stderr = _stdout.decode("utf-8").strip(), _stderr.decode("utf-8").strip()

        if stderr != "":
            return (stderr, -1)
        return (stdout, 0)
    
    context: Context

    def __init__(self, context: Context) -> None:
        self.context = context

    def scp(self, remote_dir: str) -> None:
        logger.info(f"Copying directory {remote_dir} from {self.context.ip_addr} to {self.context.parent_save_dir_path}")
        output, status_code = CommandUtils.spawn(
            f"scp -i {self.context.ssh_key_path} -P {self.context.port} -r " +
            f"{self.context.remote_user}@{self.context.ip_addr}:{remote_dir} " +
            f"{self.context.save_dir_path}")
        if status_code < 0:
            logger.error(f"An error occured during the process - {output}")
