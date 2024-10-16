# Bot Discord for a Minecraft server control
This Bot Discord code will be capable with a discord server to :
  - Start the Minecraft server with `/start`
  - Stop the Minecraft server with `/stop`
  - Shutdown the hosting PC with `/shutdown`
  - Send a message with `/say {your_text}`
  - List all player on the server with `/list`

## Installation
1. Clone the repository

To clone this project run 
  - with HTTPS
```bash
  git clone https://github.com/Bertrand-DUCON/Minecraft-Server-Bot-Controller.git
  cd Minecraft-Server-Bot-Controller
```
  - with SSH 
```bash
  git clone git@github.com:Bertrand-DUCON/Minecraft-Server-Bot-Controller.git
  cd Minecraft-Server-Bot-Controller
```
2. Install requirement
```bash
 pip install requirment.txt
```
3. Modify code
After that you can replace in the code 
```bash
5  id_guild = "your server id"
6  id_channel = "your channel id"
7  password_mcrcon = "random password for MCRcon"
8  server_path = "the path of your Minecraft server"
```
And Place your discord token here 
```bash
74  bot.start("Your Discord token here")
```
If you don't have one you can create one with your Discord account when you follow [this link](https://discord.com/developers/applications/)
Here you can create your bot, and so, your token. 
To create it click on `New Application`, name your bot and click on `create`. 
When this done go to `Bot` section and click on `Reset token`. 
Now you have your token so place it in the code but your bot is not in your Discord server.
To insert it, go to `Installation` section and copy the install link. Enter it in your browser and select your server where you want it to be.
Now your Discord bot is install in your server.

## Use
Run the python program with 
```bash
  python bot_discord.py
```
After you can execute in your discord server
```bash
  /start
```
to start your Minecraft server and you are good to go !
