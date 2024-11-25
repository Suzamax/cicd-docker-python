#!/usr/bin/env python3

from library.docker import DockerLib
import click


@click.group()
def integration():
    pass

@integration.command()
@click.argument('stage', type=click.STRING)
@click.option('-t', '--tag', type=click.STRING)
def ci(stage, tag):
    match stage:
        case "build":
            DockerLib().build(tag)
        case "prune":
            DockerLib().prune()

sources = [
    integration
]

cli = click.CommandCollection(sources=sources)

if __name__ == '__main__':
    cli()