# Discord Audio Retriever Demo

This is a demo implementing a playground use case for Speech Emotion Recognition. The demo is a Python script that loads a Discord bot to accept audio files from Discord message attachments and send API requests to SERaaS which then outputs emotions back if an audio file is retrieved.

SERaaS is a Final Year Project for [Waterford Institute of Technology](https://www.wit.ie/) developed by [Wei Kit Wong](https://github.com/andyAndyA), which aims to provide a Speech Emotion Recognition as a Web API service. This is achieved by Machine Learning to build the SER classification model; the [User Management Service](https://github.com/SERaaS/SERaaS-User-Management-Service) to provide authentication features, and the [API Service](https://github.com/SERaaS/SERaaS-API-Service) to deploy it all as a service.

## General

## Technologies Used

* *discord.py* - Discord API for handling connections and message interactions

## Usage

You can use the following commands in the terminal to run the demo;

1) `git clone https://github.com/SERaaS/Discord-Audio-Retriever-Demo.git` - Download the repository to your computer.

2) `cd discord-audio-retriever-demo` - Move to the demo folder.

3) `pip install -r requirements.txt` - Ensure you have all necessary dependencies installed (requires Python).

4) Create the missing files as defined below.

5) `python main.py` - Run the program.

Once running, perform the following on Discord;

6) Invite your Discord bot to your server by following this [tutorial](https://discordpy.readthedocs.io/en/latest/discord.html) and give him the sufficient permissions.

7) TODO

### Missing Files

`./seraasURLHandler.py` and `discordBotToken.py` files are missing from the repo that you must create before running the program.

`./seraasURLHandler.py`
```python
# This is your own SERaaS API endpoint URL
endpoint = "http://????/analyse/????"
```

`./discordBotToken.py`
```python
# This is your own Discord Bot Token
# To figure out how to retrieve one, go here; https://discordpy.readthedocs.io/en/latest/discord.html
botToken = "??????????????.??????.???????????????"
```