import os
from dotenv import load_dotenv
import discord #import du module
from discord.ext import commands

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
# Récupérer le token Discord à partir des variables d'environnement
TOKEN = os.getenv("DISCORD_TOKEN_2")

#Intents
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True

# guilds = serveurs discords
intents.guilds = True
intents.members = True

# fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur
@bot.event
async def on_ready():
    print (f"{bot.user.name} s'est bien connecté !")

# Fonction "on_message" pour réagir aux messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "pong 🏓" in message.content:
        await message.channel.send("ping 🏓")
    if "Ça va être tout noir !" in message.content:
        await message.channel.send("TA GUEULE !!")
    # Laisser les autres fonctions on_message (comme les commandes) être exécutées
    await bot.process_commands(message)

# Connexion du bot au serveur avec le token
bot.run(TOKEN)