# Contributor's Guide

Thank you for considering contributing to `google-hangouts-chat-bot`!

This document lays out guidelines and advice for contributing to this project.
If you're thinking of contributing, start by reading this thoroughly and getting a feel for how contributing to the project works. 
If you've still got questions after reading this, you should go ahead and contact the maintainers: he'll be happy to help.


*Get Early Feedback*

If you are contributing, do not feel the need to sit on your contribution until it is perfectly polished and complete. 
It helps everyone involved for you to seek feedback as early as you possibly can. 
Submitting an early, unfinished version of your contribution for feedback in no way prejudices your chances of getting that contribution accepted, and can save you from putting a lot of work into a contribution that is not suitable for the project.


## Bug Reports

Bug reports are hugely important! 
Before you raise one, though, please check through the GitHub issues, both open and closed, to confirm that the bug hasn't been reported before. 
Duplicate bug reports are a huge drain on the time of other contributors, and should be avoided as much as possible.

- Describe what you expected to happen.
- If possible, include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) to help us identify the issue.
- Describe what actually happened. Include the full traceback if there was an exception.


## Feature Requests

Feature requests are always welcome, but please note that all the general guidelines for contribution apply.
Also note that the importance of a feature request without an associated Pull Request is always lower than the importance of one with an associated Pull Request: code is more valuable than ideas.


## Code Contributions

- Use [Black](https://github.com/psf/black) to autoformat your code. You can use the command `make format`.

- This project has a suite of tests, both unit tests and integration tests, and tries to achieve 100% code coverage. Whenever you contribute, you must write tests that exercise your contributed code, and you must not regress the code coverage. 

- *New Contributors* - If you are new or relatively new to Open Source, welcome! If you're concerned about how best to contribute, please consider contacting the maintainers, asking for help and they will be very happy to help you.


### First time setup

- Download and install the latest version of [git](https://git-scm.com/downloads).
- Configure git with your [username](https://help.github.com/en/articles/setting-your-username-in-git) and [email](https://help.github.com/en/articles/setting-your-commit-email-address-in-git):

```bash
git config --global user.name 'your name'
git config --global user.email 'your email'
```

- Make sure you have a [GitHub account](https://github.com/join).
- Fork this repository to your GitHub account by clicking the [Fork](https://github.com/ciandt/google-hangouts-chat-bot/fork) button.
- [Clone](https://help.github.com/en/articles/fork-a-repo#step-2-create-a-local-clone-of-your-fork) your GitHub fork locally: 

```bash
git clone https://github.com/{username}/google-hangouts-chat-bot
cd google-hangouts-chat-bot
```

- Add the main repository as a remote to update later:

```bash
git remote add ciandt https://github.com/ciandt/google-hangouts-chat-bot
git fetch ciandt
```

- Create a virtualenv:

```bash
python3 -m venv env
. env/bin/activate
# or "env\Scripts\activate" on Windows
```

- Install dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

### Start coding

-   Create a branch to identify the issue you would like to work on. 
```bash
git checkout -b your-branch-name origin/master
```

- Using your favorite editor, make your changes, [committing as you go](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes).

- Include tests that cover any code changes you make.
Make sure the test fails without your patch. [Run the tests](#Running-the-tests).

- Push your commits to GitHub and [create a pull request](https://help.github.com/en/articles/creating-a-pull-request) by using:
```bash
git push --set-upstream origin your-branch-name
```

- Celebrate 🎉


### Running the tests

#### Run the basic test suite with:
```bash
make tests
```

#### Running test coverage:

Generating a report of lines that do not have test coverage can indicate
where to start contributing. Run `pytest` using `coverage` and generate a
report on the terminal and as an interactive HTML document:

```bash
make coverage
# then open htmlcov/index.html
```

Read more about [coverage](https://coverage.readthedocs.io).
