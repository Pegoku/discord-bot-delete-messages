import discord
import time

intents = discord.Intents.default()
intents.message_content = True

channel_id = <ID> # channel id

client = discord.Client(intents=intents)

# delete all the messages of a channel when the minutes are equal to 14, 29, 44 and 59
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    while True:
        minutes = time.strftime('%M')
        if minutes == '14' or minutes == '29' or minutes == '44' or minutes == '59':
            channel = client.get_channel(channel_id)
            async for message in channel.history(limit=None):
                await message.delete()




client.run('<Bot_Token>') # Discord Bot Token