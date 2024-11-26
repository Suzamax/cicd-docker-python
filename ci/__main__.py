#!/usr/bin/env python3

from ci.library.kubernetes import K8sLib
from library.docker import DockerLib
import click


@click.group()
def integration():
    pass

@click.group()
def kubernetes_deploy():
    pass

@integration.command()
@click.argument('stage', type=click.STRING)
@click.option('-t', '--tag', type=click.STRING)
def ci(stage, tag):
    match stage:
        case "build":
            DockerLib("INFO").build(tag)
        case "prune":
            DockerLib().prune()

@kubernetes_deploy.command()
@click.argument('action')
@click.option("-k", "--kubeconfig", type=click.STRING)
@click.argument('yaml_file')
def k8s_cd(action, kubeconfig, yaml_file):
    match action:
        case "apply":
            K8sLib(kubeconfig).apply(yaml_path=yaml_file)


sources = [
    integration,
    kubernetes_deploy
]

cli = click.CommandCollection(sources=sources)

if __name__ == '__main__':
    cli()
