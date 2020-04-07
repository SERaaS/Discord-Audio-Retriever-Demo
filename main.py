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

""" Class to handle Discord events for the bot """

class DiscordClient(discord.Client):
  async def on_ready(self):
    print("Logged on as {0}!".format(self.user))

  async def on_message(self, message):
    print("Message from {0.author}: {0.content}".format(message))
    if len(message.attachments) == 0:
      return
    
    # Contains attachments, check if any audio files
    audioFiles = [message for message in message.attachments if message.filename[-3:] == "wav"]
    if len(audioFiles) == 0:
      print("No audio files found..")
      return
    print("Audio files found..")

    # TODO: Save audio files and send to SERaaS API
    channel = message.channel
    for message in audioFiles:
      await message.save("files/")
      await channel.send("Saving file `{0.filename}`..".format(message))

    # TODO: Remove saved audio files

""" Initializing the bot connection using the bot token """
client = DiscordClient()
client.run(discordBotToken.botToken)