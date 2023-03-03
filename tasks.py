from invoke import task
from invoke.context import Context
from invoke.exceptions import Exit, UnexpectedExit

from parser_sto.utils import print_error, print_success


@task
def run_parser(context: Context) -> None:
    """Run `main.py` file."""
    context.run("python3 -m parser_sto.main")


@task
def run_tests(context: Context) -> None:
    """Run tests against repo."""
    context.run("pytest tests")


@task
def run_linters(context: Context) -> None:
    """Run linters against repo."""
    linters = ("flake8", "isort", "mypy")
    ok = True

    for linter in linters:
        try:
            context.run(f"{linter} .")
            print_success(f"Linter {linter} passed")
        except UnexpectedExit:
            print_error(f"Linter {linter} failed")
            ok = False

    if not ok:
        print_error("Some errors occurred during checks")
        raise Exit(code=1)

    print_success("Everything OK")


@task
def compile_requirements(
    context: Context,
    dev: bool = True,
    install: bool = True,
) -> None:
    """Compile all requirements from `in` files to `txt` files."""
    compile_command = "pip-compile --resolver=backtracking"
    context.run(f"{compile_command} requirements/production.in")
    context.run(f"{compile_command} requirements/development.in")
    if install:
        install_requirements(context, dev=dev)


@task
def install_requirements(context: Context, dev: bool = True) -> None:
    """Sync requirements."""
    if not dev:
        context.run("pip-sync requirements/production.txt")
    else:
        context.run("pip-sync requirements/development.txt")
    install_init_requirements(context)


def install_init_requirements(context: Context) -> None:
    """Install init.txt requirements."""
    context.run("pip install -r requirements/init.txt")
