import click

from pyfi.commander import run


def add_block_addr(cli):
    @cli.command(name='block-addr')
    @click.option('--address', '-a', help='ip/url to block', type=str)
    @click.option('--output', is_flag=True, help='Blocks output')
    def block_addr(address: str, output: bool):
        """
        Blocks ip/url
        Args:
            address: dst/src ip/url
            output: blocks output traffic. default blocks input
        """
        cmd_args = ['sudo iptables']
        if output:
            cmd_args.append('-A OUTPUT')
            cmd_args.append(f'-d {address}')
        else:
            cmd_args.append('-A INPUT')
            cmd_args.append(f'-s {address}')
        cmd_args.append('-j DROP')
        cmd = ' '.join(cmd_args)
        run(cmd)
