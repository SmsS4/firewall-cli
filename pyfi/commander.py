import subprocess

from pyfi import logger


def run(command: str) -> int:
    """
    Runs a command
    """
    logger.command("Command: %s", command)
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return_code = result.wait()
    text = result.communicate()[0]
    logger.output("Exit code: %d", return_code)
    logger.output(text.decode())
    if return_code:
        logger.error("Failed")
    return return_code
