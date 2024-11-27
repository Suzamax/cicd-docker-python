#!/usr/bin/env python3

from library.kubernetes import K8sLib
import click

@click.group()
def deployment():
    pass

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

    
cli = click.CommandCollection(sources=[deployment])

if __name__ == '__main__':
    cli()