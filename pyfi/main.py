import click

from pyfi.address_blocking import add_block_addr_and_port


@click.group()
def cli():
    ...


add_block_addr_and_port(cli)

if __name__ == "__main__":
    cli()
