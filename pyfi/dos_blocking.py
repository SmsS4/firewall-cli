import click

from pyfi import logger
from pyfi.commander import run

CHAIN_NAME = "udp-flood"
PREFIX = "$dos-ips$"


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
    @click.option("--rate-limit", help="number of allowed connections", type=int)
    @click.option(
        "--protocol",
        help="protocol of connection. defaults to tcp",
        type=str,
        default="tcp",
    )
    def syn_flood(rate_limit: int, protocol: str):
        run(
            f"iptables -A INPUT -p {protocol} --syn -m limit --limit {rate_limit}/s --limit-burst {rate_limit * 3} -j RETURN"
        )

    @cli.command(name="dos-add-logger")
    def add():
        """
        Run tihs command once to add logger to INPUT chain
        """
        run(f"iptables -A INPUT -j LOG --log-prefix '{PREFIX}'")

    @cli.command(name="dos-export")
    def export():
        """
        Exports ips history
        """
        history = {}
        with open("/var/log/kern.log") as f:
            for line in f:
                if PREFIX in line:
                    data = line[line.find(PREFIX) + len(PREFIX) :].split()
                    for d in data:
                        if d.startswith("SRC="):
                            ip = d[4:]
                        if d.startswith("LEN="):
                            packets = int(d[4:])
                    if ip not in history:
                        history[ip] = (0, 0)
                    history[ip] = (history[ip][0] + 1, history[ip][1] + packets)
        logger.output(
            f"{'IP'.ljust(20)} {'NUMBER OF PACKETS'.ljust(20)} LENGTH OF PACKETS"
        )
        for ip in history:
            logger.output(
                "%s %s %d", ip.ljust(20), str(history[ip][0]).ljust(20), history[ip][1]
            )
