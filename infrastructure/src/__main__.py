#!/usr/bin/env python3

import click

@click.group()
def infrastructure():
    pass

@infrastructure.command()
def tofu():
    pass

@infrastructure.command()
def ansible():
    pass

sources = [
    infrastructure
]

cli = click.CommandCollection(sources=sources)

if __name__ == '__main__':
    cli()
