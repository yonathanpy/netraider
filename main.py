import click
from core.scanner import scan_host
from core.sniffer import start_sniffer


@click.group()
def cli():
    pass


@cli.command()
@click.argument("target")
def scan(target):
    scan_host(target)


@cli.command()
@click.argument("interface")
def sniff(interface):
    start_sniffer(interface)


if __name__ == "__main__":
    cli()
