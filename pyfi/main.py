import click

from pyfi.blockers.address import add_block_addr_and_port
from pyfi.blockers.content import add_content_blocking
from pyfi.blockers.dos import add_dos_blocking
from pyfi.blockers.port_scanner import add_port_scanner
from pyfi.blockers.protocols import add_protocols_blocking


@click.group()
def cli():
    ...


add_block_addr_and_port(cli)
add_protocols_blocking(cli)
add_content_blocking(cli)
add_dos_blocking(cli)
add_port_scanner(cli)

if __name__ == "__main__":
    cli()
