import click

from pyfi.commander import run


def add_block_addr_and_port(cli):
    @cli.command(name="block-regex")
    @click.option("--address", "-a", help="ip/url to block", type=str)
    @click.option("--output", is_flag=True, help="Blocks output")
    def block_regex(address: str, output: str):
        run(
            f'iptables -I {"OUTPUT" if output else "INPUT"} -p tcp --dport 80 -m string --string "/\/ .+Host: {address}" --algo regex -j DROP'
        )

    @cli.command(name="block-addr")
    @click.option("--address", "-a", help="ip/url to block", type=str)
    @click.option("--output", is_flag=True, help="Blocks output")
    def block_addr(address: str, output: bool):
        """
        Blocks ip/url
        """
        cmd_args = ["sudo iptables"]
        if output:
            cmd_args.append("-A OUTPUT")
            cmd_args.append(f"-d {address}")
        else:
            cmd_args.append("-A INPUT")
            cmd_args.append(f"-s {address}")
        cmd_args.append("-j DROP")
        cmd = " ".join(cmd_args)
        run(cmd)
        # save_iptables()

    @cli.command(name="block-port")
    @click.option("--port", help="port to block", type=int)
    @click.option("--protocol", help="protocol to block. tcp/udp", type=str)
    @click.option("--output", is_flag=True, help="Blocks output")
    def block_port(port: int, protocol: str, output: bool):
        """
        Blocks port with given protocol
        """
        cmd_args = ["sudo iptables"]
        if output:

            cmd_args.extend(
                [
                    "-A",
                    "OUTPUT",
                ]
            )
        else:
            cmd_args.extend(
                [
                    "-A",
                    "INPUT",
                ]
            )
        cmd_args.extend(["-p", protocol, "--dport", str(port)])
        cmd_args.append("-j DROP")
        cmd = " ".join(cmd_args)
        run(cmd)
        # save_iptables()
