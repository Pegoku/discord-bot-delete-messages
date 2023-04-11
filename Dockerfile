FROM python

# Set the working directory to /bot
WORKDIR /bot

# Install dependencies
RUN python3 -m pip install -U discord.py

# Copy the bot.py file to the /bot directory
COPY bot.py /bot

# Add the discord bot token to bot.py
ARG token
RUN echo "client.run('$token')" >> bot.py
