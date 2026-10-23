*This project has been created as part of the 42 curriculum by mchauvin.*

# Python Module

## Description

A collection of Python exercises from the 42 curriculum, organized in ten progressive modules. It starts with the basics of the language and moves up to object-oriented design, packages, data validation and functional programming. Each module is a folder (`python00` to `python10`) split into numbered exercises (`ex0`, `ex1`, ...), each with its own script.

| Module | Topic |
|---|---|
| `python00` | Language basics: functions, loops, iterative vs. recursive approaches |
| `python01` | Object-oriented programming: classes and objects |
| `python02` | Exceptions: handling, custom errors, `finally`, raising errors |
| `python03` | Command-line arguments, data structures and generators |
| `python04` | File handling and data streams |
| `python05` | Abstract classes and polymorphism (`ABC`, `abstractmethod`) |
| `python06` | Packages and modules: package layout, imports, `__init__.py` |
| `python07` | Abstract classes, factories and the strategy pattern |
| `python08` | Environments and dependencies: virtual environments, `pyproject.toml`, `requirements.txt`, `.env` files |
| `python09` | Data validation with Pydantic |
| `python10` | Functional programming: lambdas, higher-order functions, scope, `functools`, decorators |

## Instructions

### Requirements

- Python 3.11 or higher (some exercises use `typing.Self`)
- Third-party packages for specific modules:

```sh
pip install pydantic python-dotenv
```

`pydantic` is used in `python09`, and `python-dotenv` in `python08/ex2`.

### Running an exercise

Run a script from its folder:

```sh
cd python02/ex0
python3 ft_first_exception.py
```

For modules organized as packages (such as `python06` and `python07`), run the scripts from the module's root folder so that imports resolve correctly.

## Resources

- [Python documentation](https://docs.python.org/3/)
- [PEP 8, the Python style guide](https://peps.python.org/pep-0008/)
- [Pydantic documentation](https://docs.pydantic.dev/)
