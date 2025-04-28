
from setuptools import setup, find_packages

setup(
    name="sdtm-assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "sdtm-assistant=sdtm_assistant.cli:app",
        ],
    },
)
