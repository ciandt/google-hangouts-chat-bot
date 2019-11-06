#!/usr/bin/env python
from pathlib import Path

from setuptools import setup

from google_hangouts_chat_bot.version import __version__


def readme():
    return Path("README.md").read_text()


def requires():
    return Path("requirements.txt").read_text().splitlines()


if __name__ == "__main__":
    setup(
        name="google-hangouts-chat-bot",
        version=__version__,
        description="A framework for Google Hangouts Chat Bot",
        long_description=readme(),
        long_description_content_type="text/markdown",
        url="https://github.com/ciandt/google-hangouts-chat-bot",
        author="Jean Pimentel",
        author_email="contato@jeanpimentel.com.br",
        packages=["google_hangouts_chat_bot"],
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
            "Programming Language :: Python :: 3.8",
            "Topic :: Communications",
            "Topic :: Software Development :: Libraries",
        ],
    )
