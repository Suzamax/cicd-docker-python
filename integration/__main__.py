#!/usr/bin/env python3

import click
from library.docker import DockerLib

@click.group()
@click.option('-d', '--debug', type=click.BOOL)
@click.pass_context
def integration(ctx, debug):
    ctx.obj['DEBUGLVL'] = "DEBUG" if debug else "WARNING"

@integration.command()
@click.argument('tag', type=click.STRING)
@click.pass_context
def build(ctx, tag):
    DockerLib(ctx.obj['DEBUGLVL']).build(tag=tag)

@integration.command()
@click.argument('tag', type=click.STRING)
@click.argument('repo', type=click.STRING)
@click.pass_context
def push(ctx, tag, repo):
    DockerLib(ctx.obj['DEBUGLVL']).push(tag=tag, repo=repo)


if __name__ == '__main__':
    integration()
