# Example of project that uses evc library

This is a simple example of a project that uses the evc library to manage the
versions of Machine Learning projects.

## Installation of requirements

Start a new virtual environment and install the requirements:

TODO: move `auto` branch to `master` in `evc` repo.

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install  git+https://github.com/verri/evc@auto
$ pip install -r requirements.txt
```

## Updating evc library

Since evc is still under heavy development, you may need to update the library
frequently.  To update the evc library, you can use the following command:

```bash
$ pip install --force-reinstall --no-deps git+https://github.com/verri/evc@auto
```

## Usage

After modifying the code of the model (inside `model/__init__.py`), you must
update the meta data before committing the changes.

```bash
$ python -m evc update
```

This will update the metadata in `.meta/*.json` files with the new version of
the model.
