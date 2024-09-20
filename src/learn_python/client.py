import textwrap

import click
import requests

from . import __version__

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version=__version__)
def main():
    """The Learn Python project."""
    #click.echo("Hello, world!")
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()
    except Exception as err:
        click.secho("Oops, we hit a wall", fg="red")
        print("Error Log:", err)
        exit()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))

