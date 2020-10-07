# Vlad Is Bot

Simple Twitch Bot created for fun.

## Requirements
- Python 3.7
- PiPy (pip) 20.0.2
- Pipenv:latest

### Pipenv
- The environment is managed using `pipenv`, a python package that helps with environment variables and creates a file witha purpose similar to npm's `package.json`. 
- Install `pipenv` with: ```pip install pipenv```
- after install the rest of the packages with the command: ```pipenv install``` it'll read pipfile and install all packages contained there.
- please install new packages with `pipenv`.

## Environment
- environment variables are added on the `.env` file, for security it is private and you should make your own in the following format:

```js
TMI_TOKEN=Twitch oauth token
CLIENT_ID=twitch client ID
BOT_NICK=bot nickename
BOT_PREFIX=!
CHANNEL=main channel name for the bot to join
```

- `TMI_TOKEN` and `CLIENT_ID` are variables generated at the [Twitch developer thingy](https://dev.twitch.tv/console/apps/create)


## misc

Special thanks to [NinjaBunny9000](https://github.com/NinjaBunny9000) for the wonderful [tutorial](https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8)
