#!/usr/bin/env python
from pathlib import Path

from setuptools import setup, find_packages

from google_hangouts_chat_bot.version import __version__


def readme():
    return Path('README.md').read_text()


def requires():
    return Path('requirements.txt').read_text().splitlines()


if __name__ == "__main__":
    setup(
        name="google_hangouts_chat_bot",
        version=__version__,
        description="A framework for Google Hangouts Chat Bot",
        long_description=readme(),
        long_description_content_type="text/markdown",
        url="https://github.com/ciandt/google_hangouts_chat_bot",
        author="Jean Pimentel",
        author_email="contato@jeanpimentel.com.br",
        packages=find_packages(exclude=["tests"]),
        install_requires=requires(),
        python_requires=">=3.7",
        license="MIT",
        keywords="google hangouts chat chatbot",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Information Technology",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Topic :: Communications",
            "Topic :: Software Development :: Libraries",
        ],
    )
