# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# By: Wei Kit Wong
# 
# This demo program loads a Discord bot that accepts audio files
# from message attachments. The audio files are then sent to the
# SERaaS API to output the emotions shown in the file.
# 
# Codebase Inspiration:
# https://discordpy.readthedocs.io/en/latest/intro.html
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import discord
import discordBotToken
import requests
import seraasURLHandler

""" Location to store temporary audio files at """

TEMPORARY_AUDIO_FILENAME = "tempfile.wav"

""" Function to handle making an API call to SERaaS """

async def seraasCall(audioFile):
  # Code generated using Postman, such a good tool !
  apiEndpointURL = seraasURLHandler.endpoint

  if apiEndpointURL is not None:
    print("Making API request to SERaaS at '%s'.." % apiEndpointURL)

    response = requests.request(
      "POST",
      apiEndpointURL,
      headers = { "Content-Type": "application/x-www-form-urlencoded" },
      data = {},
      files = [ ("file", open(audioFile, "rb")) ]
    )

    print("Got response from SERaaS:")
    print(response.text.encode('utf8'))
    print("fin. API request operation.")
  else:
    print("A seraasURLHandler.py file is required for making the API request. Please read README.md for more information.")

""" Class to handle Discord events for the bot """

class DiscordClient(discord.Client):
  async def on_ready(self):
    print("Logged on as {0}!".format(self.user))

  async def on_message(self, message):
    print("Message from {0.author}: {0.content}".format(message))
    if len(message.attachments) == 0:
      return
    
    # Contains attachments, check if any audio files
    audioFiles = [message for message in message.attachments if message.filename[-3:] == "wav"] # List comprehension
    if len(audioFiles) == 0:
      print("No audio files found..")
      return
    print("Audio files found..")

    channel = message.channel
    message = audioFiles[0] # Users can only send one attachment at once
    print(message)

    # Save audio file and send to SERaaS API
    await message.save(TEMPORARY_AUDIO_FILENAME)
    await channel.send("Saving file %s to %s.." % (message.filename, TEMPORARY_AUDIO_FILENAME))
    await seraasCall(TEMPORARY_AUDIO_FILENAME)

    # TODO: Remove saved audio files

""" Initializing the bot connection using the bot token """
client = DiscordClient()
client.run(discordBotToken.botToken)