import click

from pyfi.commander import run

CHAIN_NAME = "udp-flood"


def add_dos_blocking(cli):
    @cli.command(name="dos-dns-flood")
    @click.option(
        "--rate-limit", help="number of allowed requests per second", type=int
    )
    def udp_flood(rate_limit: int):
        """
        Ratelimit on dns requests to prevent dns-flood attack
        """
        run(f"iptables -F {CHAIN_NAME}")
        run(
            f"iptables -A {CHAIN_NAME} -m limit --limit {rate_limit}/second --limit-burst {rate_limit} -j RETURN"
        )
        run(f"iptables -A {CHAIN_NAME} -j DROP")
        run(f"iptables -A INPUT -p udp -j {CHAIN_NAME}")
        run(f"iptables -A INPUT -f -j DROP")

    @cli.command(name="dos-slowloris")
    @click.option("--port", help="port to limit number of connections", type=int)
    @click.option("--connections-limit", help="number of allowed connections", type=int)
    @click.option(
        "--protocol",
        help="protocol of connection. defaults to tcp",
        type=str,
        default="tcp",
    )
    def slowloris(port: int, connections_limit: int, protocol: str):
        run(
            f"iptables -I INPUT -p {protocol} --dport {port} -m connlimit --connlimit-above {connections_limit} --connlimit-mask {connections_limit * 2} -j DROP"
        )

    @cli.command(name="dos-syn-flood")
    @click.option("--port", help="port to limit number of connections", type=int)
    @click.option("--rate-limit", help="number of allowed connections", type=int)
    @click.option(
        "--protocol",
        help="protocol of connection. defaults to tcp",
        type=str,
        default="tcp",
    )
    def syn_flood(port: int, rate_limit: int, protocol: str):
        run(
            f"iptables -A INPUT -p {protocol} --syn -m limit --limit {rate_limit}/s --limit-burst {rate_limit*3} -j RETURN"
        )
