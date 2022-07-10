import click

from pyfi.commander import run


def add_port_scanner(cli):
    @cli.command(name="port-knocking")
    @click.option(
        "--knocks",
        help="list of port to use for port knocking separated by `,`",
        type=str,
    )
    @click.option("--port", help="destination port", type=int)
    def port_knocking(knocks: str, port: int):
        knocks_list = knocks.split(",")
        run("iptables -F")
        run("iptables -X")
        run("iptables -Z")
        for i, knock in enumerate(knocks_list):
            run(f"iptables -N STATE{i}")
            if i:
                run(f"iptables -A STATE{i} -m recent --name KNOCK{i} --remove")
            run(
                f"iptables -A STATE{i} -p udp --dport {knock} -m recent --name KNOCK{i+1} --set -j DROP"
            )
            if i:
                run(f"iptables -A STATE{i} -j STATE0")
            else:
                run(f"iptables -A STATE{i} -j DROP")
        run(f"iptables -N STATE3")
        run(f"iptables -A STATE3 -m recent --name KNOCK3 --remove")
        run(f"iptables -A STATE3 -p tcp --dport {port} -j ACCEPT")
        run(f"iptables -A STATE3 -j STATE0")

        run(f"iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
        run(f"iptables -A INPUT -s 127.0.0.0/8 -j ACCEPT")
        run(f"iptables -A INPUT -p icmp -j ACCEPT")
        run(f"iptables -A INPUT -p tcp --dport {port} -j ACCEPT")
        for i in reversed(range(len(knocks_list))):
            run(f"iptables -A INPUT -m recent --name KNOCK{i+1} --rcheck -j STATE{i+1}")
        run("iptables -A INPUT -j STATE0")
