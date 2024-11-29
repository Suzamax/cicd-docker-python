#!/usr/bin/env python3

import click
from library.opentofu import OpentofuLib


@click.group()
def infrastructure():
    pass

@infrastructure.command()
@click.argument('arg', type=click.STRING)
def terraform(arg):
    match arg:
        case 'plan':
            OpentofuLib.opentofu_plan()

@infrastructure.command()
def ansible():
    pass

if __name__ == '__main__':
    infrastructure()
