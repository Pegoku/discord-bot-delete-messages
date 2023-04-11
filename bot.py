import discord
import time

intents = discord.Intents.default()
intents.message_content = True

wait_time = <time> # seconds
channel_id = <ID> # channel id

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.channel.id == channel_id:
        time.sleep(wait_time)
        await message.delete()

client.run('<Bot_Token>') # Discord Bot Token