# Discord Bot: Message deleter
A bot that deletes messages automatically.

# Running
### On linux
1. Install the dependencies:
```bash
# Debian-based:
sudo apt install wget git python3
# Red Hat-based:
sudo dnf install wget git python3
# Arch-based:
sudo pacman -S wget git python3
```
2. Install python dependencies
``` python3 -m pip install -U discord.py ```
3.  Download the file
``` wget https://raw.githubusercontent.com/Pegoku/discord-bot-delete-messages/main/bot.py ```
4. Edit the file
5. Run the file
``` python3 bot.py ```

### Using docker
1. Install [docker](https://docs.docker.com/engine/install/)
2. Install [git](https://git-scm.com/downloads)
3. Clone the repository
``` git clone https://github.com/Pegoku/discord-bot-delete-messages.git ```
4. Edit **bot.py**
5. Build the docker image
``` docker build <image_name> . ```
6. Run the image
``` docker run <image_name> ```