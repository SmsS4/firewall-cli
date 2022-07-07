import subprocess

from pyfi import logger


def run(command: str, log: bool = True) -> int:
    """
    Runs a command
    """
    if log:
        logger.command("Command: %s", command)
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return_code = result.wait()
    text = result.communicate()[0]
    if log:
        logger.output("Exit code: %d", return_code)
        logger.output(text.decode())
    if return_code:
        logger.error("Failed")
    return return_code


#
# def save_iptables():
#     """
#     Saves iptable
#     """
#     run('sudo iptables save', log=False)
