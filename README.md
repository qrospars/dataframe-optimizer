# Dataframe Optimizer

This package gives a helper function called `optimize_dataframe` that will process a int, float and object optimization on the dataframe. Changing column dtypes can help saving a lot of memory usage, and this package tries to automatically define the optimal dtype for each column of the given dataframe.

Please don't hesitate to contribute if you want to add more parameters or automatic optimization 🥰

## How to create new version

1. Increase version in `__init__.py` and `setup.py`
2. Run `python setup.py bdist_wheel` in terminal
3. Run `python -m twine upload dist/*` in terminal
4. Run `pip install dataframe-optimizer  --upgrade` in terminal