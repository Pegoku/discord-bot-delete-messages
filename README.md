# Python Discord Bots
Simple discord bots made by Pegoku
# Running
### On linux
1. Install the dependencies:
```bash
# Debian-based:
sudo apt install wget python3 python3-pip
# Red Hat-based:
sudo dnf install wget python3 python3-pip
# Arch-based:
sudo pacman -S wget python3 python3-pip
```
2. Install python dependencies
``` python3 -m pip install -U discord.py ```
3.  Download the file
``` wget https://raw.githubusercontent.com/Pegoku/python-discord-bots/main/<BotNumber>/bot.py ```
4. Edit **bot.py**
5. Run the file
``` python3 bot.py ```

### Using docker
1. Install [docker](https://docs.docker.com/engine/install/)
2. Install [git](https://git-scm.com/downloads)
3. Clone the repository
``` git clone https://github.com/Pegoku/python-discord-bots.git ```
4. Edit **\<BotNumber>/bot.py**
5. Edit **Dockerfile**
6. Build the docker image
``` docker build -t <image_name> . ```
7. Run the image
``` docker run <image_name> ```