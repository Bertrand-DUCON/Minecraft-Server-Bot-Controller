import os
from interactions import Client, Intents, listen, slash_command, SlashContext, SlashCommandOption
from mcrcon import MCRcon as r

id_guild = "your server id"
id_channel = "your channel id"
password_mcrcon = "random password for MCRcon"
server_path = "the path of your Minecraft server"

bot = Client(
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
    sync_interactions=True,
)

@listen()
async def on_ready():
    print("Ready")
    await bot.get_channel(id_channel).send("Bot start !")

@slash_command(name="shutdown", description="Shutdown the hosting PC", scopes=[id_guild])
async def poweroff_pc_command_function(ctx: SlashContext):
    os.system('shutdown -s -t 5')
    await ctx.send("Shutdown the PC in next 5 secondes...")

@slash_command(name="stop", description="Stop the server", scopes=[id_guild])
async def stop_server_command_function(ctx: SlashContext):
    await ctx.send("Server stoping")
    try:
        with r('localhost', 'password_mcrcon') as mcr:
            mcr.command('/stop')
    except Exception as e:
        await ctx.send(f"Error while stoping the server : {e}")

@slash_command(
    name="say",
    description="Send a message on the Minecraft serveur with your Discord nickname",
    scopes=[id_guild],
    options=[
        SlashCommandOption(
            name="text",
            description="The message to send on the minecraft server",
            type=3,  # Utilise '3' pour spécifier une chaîne de caractères (str)
            required=True
        )
    ]
)
async def say_command_function(ctx: SlashContext, text: str):
    try:
        with r('localhost', 'password_mcrcon') as mcr:
            mcr.command(f'/say {ctx.author.username}: {text}')
        await ctx.send(f"{text}")
    except Exception as e:
        await ctx.send(f"Error while sending the message : {e}")

@slash_command(name="start", description="Start the server", scopes=[id_guild])
async def start_server_command_function(ctx: SlashContext):
    await ctx.send("Server starting...")
    os.chdir(server_path)
    os.startfile(fr"{server_path}/run.bat")

@slash_command(name="list", description="List of all player on the server", scopes=[id_guild])
async def list_players_command_function(ctx: SlashContext):
    try:
        with r('localhost', 'password_mcrcon') as mcr:
            player_list = mcr.command('/list')
            
        if "players online:" in player_list:
            player_list = player_list.split("players online: ")[1]

        await ctx.send(f"Players online : {player_list}")
    except Exception as e:
        await ctx.send(f"Error while listing players : {e}")

bot.start("Your Discord token here")
