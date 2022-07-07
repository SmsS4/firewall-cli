import click

DEBUG = 1
OUTPUT = 2
COMMAND = 3
ERROR = 4

colors = {
    DEBUG: 'blue',
    OUTPUT: 'green',
    COMMAND: 'yellow',
    ERROR: 'red',
}


def log(text: str, level: int, *args):
    if not text:
        return
    click.echo(click.style(text % args, fg=colors[level]))


def debug(text: str, *args):
    log(text, DEBUG, *args)


def output(text: str, *args):
    log(text, OUTPUT, *args)


def command(text: str, *args):
    log(text, COMMAND, *args)


def error(text: str, *args):
    log(text, ERROR, *args)
