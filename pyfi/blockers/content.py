import click

from pyfi.commander import run


def add_content_blocking(cli):
    @cli.command(name="block-http")
    @click.option("--content", help="drop packets contains this word", type=str)
    @click.option("--port", help="use rules on this port", type=int)
    def http(content: str, port: int):
        """
        Blocks http if contains a specified content
        """
        run(
            f'iptables -I OUTPUT -p tcp --dport {port} -m string --string "{content}" --algo bm -j DROP'
        )

    @cli.command(name="block-header")
    @click.option("--key", help="header's key", type=str)
    @click.option("--value", help="header's value", type=str)
    @click.option("--port", help="use rules on this port", type=int)
    def headers(key: str, value: str, port: int):
        """
        Blocks http request if contains a header
        """
        run(
            f'iptables -I OUTPUT -p tcp --dport {port}  -m string --string "{key}: {value}" --algo bm -j DROP'
        )
