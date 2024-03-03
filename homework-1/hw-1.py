import click
import sys


@click.command()
@click.argument('file', type=click.File('r'), required=False)
def nl(file):
    if file is None:
        file = sys.stdin

    line_number = 1
    for line in file:
        click.echo(f"{line_number}\t{line}", nl=False)
        line_number += 1


if __name__ == '__main__':
    nl()
