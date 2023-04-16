import discord
from discord.ext import tasks
import datetime

intents = discord.Intents.default()

channel_id = <ID> # channel id

times = []

for i in range(0,24):
    times.append(datetime.time(i,14)),
    times.append(datetime.time(i,29)),
    times.append(datetime.time(i,44)),
    times.append(datetime.time(i,59))

class MyClient(discord.Client):
    async def setup_hook(self):
        deletechat.start()
    async def on_ready(self):
        print(f'Logged in as {self.user}')

app = MyClient(intents=intents)

@tasks.loop(time=times)
async def deletechat():
        channel = app.get_channel(channel_id)
        await channel.purge(limit=100)
        print(f'Chat cleared')

app.run('<Bot_Token>') # Discord Bot Token