import click

from pyfi.address_blocking import add_block_addr


@click.group()
def cli():
    ...


add_block_addr(cli)

if __name__ == '__main__':
    cli()
