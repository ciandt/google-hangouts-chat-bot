# A framework for Google Hangouts Chat Bot

[![Build Status](https://travis-ci.org/ciandt/google-hangouts-chat-bot.svg?branch=master)](https://travis-ci.org/ciandt/google-hangouts-chat-bot)
[![Current version at PyPI](https://img.shields.io/pypi/v/google-hangouts-chat-bot.svg)](https://pypi.python.org/pypi/google-hangouts-chat-bot)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/google-hangouts-chat-bot.svg)
![PyPI status](https://img.shields.io/pypi/status/google-hangouts-chat-bot.svg)
[![License: MIT](https://img.shields.io/pypi/l/google-hangouts-chat-bot.svg)](https://github.com/ciandt/google-hangouts-chat-bot/blob/master/LICENSE)

This is a framework you can use to build bots for Google Hangouts Chat.
It was made to be simple and extensible.

### What it does?

There are many ways to create a bot for Google Hangouts Chat. 
One of them is using HTTP endpoints and this framework here was built to facilitate it.

In a nutshell, the bot receives a JSON payload via a HTTP POST request and should respond it with another JSON, follow a defined message format.

The following diagram describes a typical interaction with a bot in a chat room:

![Flow diagram](https://developers.google.com/hangouts/chat/images/bot-room-seq.png)

#### How to use this framework?

1- Command _(our base class)_:

```python
class Command:
    # the keyword that will trigger it
    command = None 
    
    # some aliases, if needed
    command_aliases = []
    
    # description of expected arguments
    arguments = None
    
    # description of command
    description = None

    # if hidden, this command will not appear when listing commands
    hidden = False
    
    # main method
    def handle(self, arguments, **kwargs):
        raise NotImplementedError
```

Let's create a *Hello* command:
```python
class Hello(Command):
    command = "hello"
    command_aliases = ["hi", "hey"]
    arguments = "<name>"
    description = "Say hello"

    def handle(self, arguments, **kwargs):
        return create_text_response(f"Hello, {arguments[0]}!")
```

2- Commands:

```python
# List of available commands  
commands = Commands()
commands.add_command(Hello)

# if needed, you can add commands by module
commands.add_commands_from_module(some.module)
```

3- EventHandler:

```python
payload = {...}
response = EventHandler(payload, commands).process()
```

Sending a "hello" message:
```python
commands = Commands()
commands.add_command(Hello)

payload = {
    "type": "MESSAGE",
    "message": {"text": "hello Jane"},
    "space": "...",
    "user": "...",
}

# message will be parsed, returning:
#   command = "hello", 
#   arguments = ["Jane"]
# since we have a command triggered by "hello", an instance will be created and called:
#   return Hello().handle(arguments) 

response = EventHandler(payload, commands).process()

print(response) 
{"text": "Hello, Jane!"}
```

#### Built-in command: Help

It will list available commands (example):

```
Commands available:

hello <name>
Say hello

ciao <name>
Say ciao

help
List commands available

HINT: If you need to specify multiple words for a parameter, use quotes (").
```


_work in progress_


## Installing

You can install using [pip](https://pip.pypa.io/en/stable/):

```
$ pip install google_hangouts_chat_bot
```


## Authors

- [@jeanpimentel](https://github.com/jeanpimentel) (Jean Pimentel)


## Contributing

Contributions are always welcome and highly encouraged.
See [CONTRIBUTING](CONTRIBUTING.md) for more information on how to get started.


## License

MIT - See [the LICENSE](LICENSE) for more information.
