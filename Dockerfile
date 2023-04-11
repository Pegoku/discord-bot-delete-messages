FROM python

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN python3 -m pip install -U discord.py

# Copy the bot.py file to the /app directory
COPY bot.py /app/bot.py

# Run the bot.py file when the container launches
CMD ["python", "bot.py"]