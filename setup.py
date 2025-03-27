from setuptools import setup

setup(
    name="todolist",
    version="0.1",
    py_modules=["todolist"],
    entry_points={
        "console_scripts": ["todolist=todolist:main"],
    },
)
