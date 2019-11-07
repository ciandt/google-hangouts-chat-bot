# A framework for Google Hangouts Chat Bot

[![Build Status](https://travis-ci.org/ciandt/google-hangouts-chat-bot.svg?branch=master)](https://travis-ci.org/ciandt/google-hangouts-chat-bot)
[![Current version at PyPI](https://img.shields.io/pypi/v/google-hangouts-chat-bot.svg)](https://pypi.python.org/pypi/google-hangouts-chat-bot)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/google-hangouts-chat-bot.svg)
![PyPI status](https://img.shields.io/pypi/status/google-hangouts-chat-bot.svg)
[![License: MIT](https://img.shields.io/pypi/l/google-hangouts-chat-bot.svg)](https://github.com/ciandt/google-hangouts-chat-bot/blob/master/LICENSE)

This is a framework you can use to build bots for Google Hangouts Chat. (You can read more about Google Hangouts Chat below.)

It was made to be simple and extensible.

## What it does?

There are many ways to create a bot for Google Hangouts Chat and one of them is using HTTP endpoints.
In a nutshell, the bot receives a JSON payload via an HTTP POST request and should respond it with another JSON, following a defined message format.

This framework was built to facilitate the creation of _cli_-like bots. It parses the payload and verifies if there is some command associated with the message. If there is one, this command is called and the result is returned.  

The main pieces are:
- `Command`: our base command class
- `Commands`: a collection of commands
- `EventHandler`: the core, responsible to parse the message and call the associated command.
 
In addition to that, we have:
- response helpers: to create the responses with the right format.
	- `create_text_response()`
	- `create_cards_response()`
	- `create_card_header()`
	- `create_card_paragraph()`
	- `create_card_key_value()`
	- `create_card_image()`
	- `create_card()`
	
- security helpers:
    - `check_allowed_domain` - to verify if user can use the bot
    - `check_bot_authenticity` -  to verify if the request was made by a real bot
	
- built-in `Help` command:

When invoked, it will return a message with available commands (example):

```
Commands available:

hello <name>
Say hello

sum <n>...
Sum informed values

# Repeat for every non-hidden command
# [command] [arguments]
# [description]

help
List commands available

HINT: If you need to specify multiple words for a parameter, use quotes (").
```

### Atention

- This framework is not a web framework. You need to use it with one solution.

Example using _Flask_:
```python
@app.route("/", methods=["POST"])
def main():
    payload = request.get_json()
    response = EventHandler(payload, commands).process()
    return json.jsonify(response)
```

## How it works?

1 - `Command` _(our base class)_:

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

1.1 - Let's create a *Hello* command:
```python
class Hello(Command):
    command = "hello"
    command_aliases = ["hi", "hey"]
    arguments = "<name>"
    description = "Say hello"

    def handle(self, arguments, **kwargs):
        return create_text_response(f"Hello, {arguments[0]}!")
```

2 - `Commands`:

```python
# Creating a list of available commands  
commands = Commands()
commands.add_command(Hello)

# if needed, you can add commands by module
commands.add_commands_from_module(some.module)
```

3 - `EventHandler`:

```python
payload = {...}

# it receives the payload, commands list and more kwargs if needed
# then it processes the payload, returning a response
response = EventHandler(payload, commands).process()
```

4 - Sending a "hello" message:
```python
commands = Commands()
commands.add_command(Hello)

payload = {
    "type": "MESSAGE",
    "message": {"text": "hello Jane"}, # what the user has typed
    "space": "...",
    "user": "...",
}

# message will be parsed, identifying:
#   command = "hello" 
#   arguments = ["Jane"]
# 
# since we have a command triggered by "hello"
# 
# class Hello(Command):
#   command = "hello"
#   ...
# 
# an instance will be created and called:
#   return Hello().handle(arguments) 

response = EventHandler(payload, commands).process()

print(response) 
{"text": "Hello, Jane!"}
```

## Google Hangouts Chat

The following diagram describes a typical interaction with a bot in a chat room:

![Flow diagram](https://developers.google.com/hangouts/chat/images/bot-room-seq.png)

* [Design guidelines](https://developers.google.com/hangouts/chat/concepts/ux)
* [Creating new bots](https://developers.google.com/hangouts/chat/how-tos/bots-develop)
* [Publishing bots](https://developers.google.com/hangouts/chat/how-tos/bots-publish)
* [Hangouts Chat message formats](https://developers.google.com/hangouts/chat/reference/message-formats/)


## Installing

You can install using [pip](https://pip.pypa.io/en/stable/):

```
$ python -m pip install google_hangouts_chat_bot
```


## Authors

- [@jeanpimentel](https://github.com/jeanpimentel) (Jean Pimentel)


## Contributing

Contributions are always welcome and highly encouraged.
See [CONTRIBUTING](CONTRIBUTING.md) for more information on how to get started.


## License

MIT - See [the LICENSE](LICENSE) for more information.
