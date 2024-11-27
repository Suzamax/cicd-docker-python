#!/usr/bin/env python3

import click
from library.docker import DockerLib

@click.group()
def integration():
    pass

@integration.command()
@click.argument('tag', type=click.STRING)
@click.option('-d', '--debug', type=click.BOOL)
def build(tag, debug):
    if debug:
        DockerLib("DEBUG").build(tag=tag)
    else:
        DockerLib("WARNING").build(tag=tag)

sources = [
    integration
]

cli = click.CommandCollection(sources=sources)

if __name__ == '__main__':
    cli()
