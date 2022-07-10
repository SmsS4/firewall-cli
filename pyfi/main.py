import click

from pyfi.address_blocking import add_block_addr_and_port
from pyfi.content_blocking import add_content_blocking
from pyfi.dos_blocking import add_dos_blocking
from pyfi.protocols_blocking import add_protocols_blocking


@click.group()
def cli():
    ...


add_block_addr_and_port(cli)
add_protocols_blocking(cli)
add_content_blocking(cli)
add_dos_blocking(cli)
if __name__ == "__main__":
    cli()
