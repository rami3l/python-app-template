# python-app-template

A simple Python app template configured with [`pdm`].

Several shortcuts have been set in [`pyproject.toml`](pyproject.toml):

- `pdm run main` to launch the app.
- `pdm run test` to launch tests.
- `pdm run fmt` to format all Python source files.

## Quick Start

Replace all occurrences of `bonjour` to your project name both in the files and file/folder names (eg. `./src/bonjour`).

You might also have to perform [this hack][hack] for the moment, especially when `Jupyter`, `VSCode` debugging, etc. complain about `PYTHONPATH`:

> > Add a file called `.env` inside of your project directory and set your paths there, like so:
> >
> > ```txt
> > PYTHONPATH=/<your-workspace-path>/__pypackages__/<major>.<minor>/lib:/<your-workspace-path>/src
> > ```
>
> ... where `/<your-workspace-path>` is the **absolute** path of the project directory (e.g. `/Users/rami3l/bonjour`),
>
> ... and `<major>.<minor>` is your Python version (e.g. `3.9`).

[`pdm`]: https://github.com/pdm-project/pdm
[hack]: https://github.com/pdm-project/pdm/issues/848#issuecomment-1032696178
