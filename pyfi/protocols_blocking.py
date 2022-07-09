import click

from pyfi.commander import run


def add_protocols_blocking(cli):
    @cli.command(name="block-ssh")
    @click.option("--user", help="user to restrict access", type=str)
    def ssh(user: str):
        """
        Blocks user from accessing ssh to your computer
        """
        run(f'echo "DenyUsers {user}" >> /etc/ssh/sshd_config')
        run("systemctl restart ssh")

    @cli.command(name="block-dns")
    @click.option("--addr", help="address to block", type=str)
    def dns(addr: str):
        """
        Blocks address for dns resolve
        """
        run(
            f"iptables -A OUTPUT -p udp --dport 53 -m string --algo bm --string {addr} -j DROP"
        )
        run(
            f"iptables -A INPUT -p udp --dport 53 -m string --algo bm --string {addr} -j DROP"
        )
        run(
            f"iptables -A FORWARD -p udp --dport 53 -m string --algo bm --string {addr} -j DROP"
        )

    @cli.command(name="block-dhcp")
    @click.option("--addr", help="mac-address to block", type=str)
    def dhcp(addr: str):
        """
        Blocks dhcp protocol for specified mac address
        """
        run(f"iptables -A FORWARD -p udp -m mac --mac-source {addr} --dport 67 -j DROP")
