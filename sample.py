import typer

app = typer.Typer()


@app.command()
def hello():
    print("hello, world!")

@app.command()
def bye():
    print("Until next time")


if __name__ == "__main__":
    app()

# TODO: https://docs.python-guide.org/writing/structure/
