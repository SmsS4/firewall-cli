import click

from pyfi.address_blocking import add_block_addr_and_port
from pyfi.protocols_blocking import add_protocols_blocking


@click.group()
def cli():
    ...


add_block_addr_and_port(cli)
add_protocols_blocking(cli)
if __name__ == "__main__":
    cli()
