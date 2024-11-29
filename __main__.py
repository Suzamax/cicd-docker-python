#!/usr/bin/env python3

import click
from library.docker import DockerLib
from library.opentofu import OpentofuLib
from library.kubernetes import K8sLib

"""
Groups for Click CLI
"""
@click.group()
@click.option('-d', '--debug', type=click.BOOL)
@click.pass_context
def deployment(ctx, debug):
    ctx.obj['DEBUGLVL'] = "DEBUG" if debug else "WARNING"

@click.group()
@click.option('-d', '--debug', type=click.BOOL)
@click.pass_context
def infrastructure(ctx, debug):
    ctx.obj['DEBUGLVL'] = "DEBUG" if debug else "WARNING"

@click.group()
@click.option('-d', '--debug', type=click.BOOL)
@click.pass_context
def integration(ctx, debug):
    ctx.obj['DEBUGLVL'] = "DEBUG" if debug else "WARNING"


"""
Commands for Deployment Group
"""
@deployment.command()
@click.argument('file', type=click.STRING)
@click.option('-n', '--namespace', type=click.STRING)
@click.option('-k', '--kubeconfig', type=click.STRING)
def apply(file, namespace, kubeconfig):
    """
    :param str file: The file to apply.
    :param str namespace: The namespace where to apply the file. Defaults to default.
    :param str kubeconfig: The kubeconfig to use. Defaults to /app/.kube/config arbitrarily.
    """
    if not namespace:
        namespace = 'default'
    if not kubeconfig:
        kubeconfig = '/app/.kube/config'
    K8sLib(kubeconfig).apply(file)

"""
Commands for Infrastructure Group
"""
@infrastructure.command()
@click.argument('arg', type=click.STRING)
def terraform(arg):
    match arg:
        case 'plan':
            OpentofuLib.opentofu_plan()

@infrastructure.command()
def ansible():
    pass

"""
Commands for Integration Group"""
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


cli = click.CommandCollection(sources=[
    integration,
    infrastructure,
    deployment
])

if __name__ == '__main__':
    cli()
