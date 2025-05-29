# Get random xkcd comics to your Telegram channel #

A minimal script that fetches a random XKCD comic and posts it to your Telegram channel.

## Requirements ##

- **Python**: 3.7–3.10  
- **Telegram bot token**: create one via [BotFather](https://telegram.me/BotFather)  
- **Bot permissions**: add your bot as an administrator in the target channel  
- **Environment variables**: `TG_TOKEN` and `CHAT_ID`

## Installation ##

Clone the repo, then create and activate a virtual environment (it should be Python 3.7–3.10):

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Then install dependencies:

```shell
pip install -r requirements.txt
```

Then, create an .env file in the root project directory and add the keys from .env.example file. There are two environment variables: `TG_TOKEN` (token for Telegram bot which is necessary for auto publishing) and `CHAT_ID` (name of your Telegram channel where you are going to post comics).

Generate your Telegram bot token via using [BotFather](https://telegram.me/BotFather), following simple instructions. Be sure that you added this bot as an administrator to channel where you are going to post comics. `CHAT_ID` is the name of your Telegram channel (e.g. @telegram_channel).

## Usage ##

Run the script to post a random comic:s

```shell
python path/to/random_xkcd_poster.py
```

## Project Purpose ##

This project was created for educational purposes as part of the web development course at [dvmn.org](https://dvmn.org).