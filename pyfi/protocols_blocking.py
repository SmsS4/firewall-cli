import click

from pyfi.commander import run


def add_protocols_blocking(cli):
    @cli.command(name="block-ssh")
    @click.option("--user", help="user to restrict access", type=str)
    def block_addr(user: str):
        """
        Blocks user from accessing ssh to your computer
        """
        run(f'echo "DenyUsers {user}" >> /etc/ssh/sshd_config')
        run("systemctl restart ssh")
