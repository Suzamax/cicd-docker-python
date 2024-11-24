from libraries.docker import DockerLib
import click

@click.command()
@click.argument('phase')
@click.argument('stage')
@click.option('-t', '--tag', type=click.STRING)
def flow(phase, stage, tag):
    match phase:
        case 'integration':
            match stage:
                case "build":
                    DockerLib().build(tag)
                case "prune":
                    DockerLib().prune()
                    

if __name__ == '__main__':
    flow()