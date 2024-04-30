import random
import discord #import du module
from discord.ext import commands

#Intents
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True

# guilds = serveurs discords
intents.guilds = True
intents.members = True

# Liste de blagues
jokes = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "Qu'est-ce qu'une fourchette qui parle ? Une fourchette-telle !",
    "Pourquoi est-ce que les plongeurs plongent toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "Pourquoi Napoléon III a-t-il perdu la guerre ? Parce qu'il a misé sur l'État.",
    "Quel est le comble pour un électricien ? De péter les plombs !"
]

# Message de bienvenue
welcome_message = "Bienvenue sur notre serveur ! Nous sommes heureux de vous accueillir parmi nous."

# fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur
@bot.event
async def on_ready():
    print (f"{bot.user.name} s'est bien connecté !")

# Commande !ping
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Commande !touché
@bot.command()
async def touche(ctx):
    await ctx.send("coulé ! 💥")

# Commande !members
@bot.command()
async def members(ctx):
    guild = ctx.guild
    members_info = []
    for member in guild.members:
        roles = [role.name for role in member.roles if role.name != "@everyone"]
        roles_str = ", ".join(roles) if roles else "Aucun rôle"
        members_info.append(f"{member.display_name} - Rôles: {roles_str}")
    members_list = "\n".join(members_info)
    await ctx.send(f"Membres sur le serveur {guild.name}:\n{members_list}")


# Fonction "on_message" pour réagir aux messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Mot spécifique à détecter pour le bannissement
    mot_specifique = "negro"
    if mot_specifique in message.content.lower():
        # Bannir l'utilisateur qui a envoyé le message
        await message.author.ban(reason="Mot spécifique interdit.")
        await message.channel.send(f"L'utilisateur {message.author.mention} a été banni pour utilisation du mot spécifique.")
        return

    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")  # Réaction avec un emoji de salutation

    # N'oubliez pas de laisser les autres fonctions on_message (comme les commandes) être exécutées
    await bot.process_commands(message)

# Commande !joke
@bot.command()
async def joke(ctx):
    joke = random.choice(jokes)
    await ctx.send(joke)

# Commande !welcome
@bot.command()
async def welcome(ctx):
    await ctx.send(welcome_message)

# Fonction "on_member_join" pour envoyer le message de bienvenue lorsqu'un nouvel utilisateur rejoint le serveur
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(welcome_message)

# Commande !ping
@bot.command()
async def parle(ctx):
    await ctx.send("Ça va être tout noir !")


# Connexion du bot au serveur avec le token
bot.run("MTIzNDgzODU4MjczNzI0NDIwMg.GHIu9S.gBToPlPadH4pt1olNQE6kl60I3I1viQZIHfBlo")

