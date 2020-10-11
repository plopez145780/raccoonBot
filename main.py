import discord
import json

from discord.ext import commands
from discord.utils import get

""" Recupération du token dans le conteneur keystore """
with open('keystore.json', 'r') as keystore:
    keys = json.load(keystore)
type(keys)
token=keys["discord"]["token"]

""" Déclaration du préfixe des commandes """
prefix="rcn_"
bot=commands.Bot(command_prefix=prefix)

# EVENEMENTS

@bot.event
async def on_ready():
    """
        Evènement au démarrage du bot.
        Affiche un message dans la console.
    """
    #await bot.change_presence(
    #    status=discord.Status.idle,
    #    activity=discord.("Je suis en ligne"))
    print("RaccoonBot a votre service")

@bot.event
async def on_raw_reaction_add(payload):
    """
        Evènement d'ajout de role au clique sur un emoji d'un message particulié dans le channel
    """
    print("Reaction ajoutée !")
    print(payload)

    emoji=payload.emoji.name
    canal=payload.channel_id
    message=payload.message_id
    #serveur=get(payload.guild_id.roles)
    VOTRE_NUM_DE_CANAL=123456789012345678
    VOTRE_NUM_DE_MESSAGE=123456789012345678

    if canal==VOTRE_NUM_DE_CANAL and message==VOTRE_NUM_DE_MESSAGE and emoji=="🧪":
        print("Grade OK")
        #user_id=payload.user_id
        #user=bot.get_user(user_id)

@bot.event
async def on_raw_reaction_remove(payload):
    """
        Evènement de suppression de role au clique sur un emoji d'un message particulié dans le channel
    """
    emoji=payload.emoji.name
    canal=payload.channel_id
    message=payload.message_id
    VOTRE_NUM_DE_CANAL=123456789012345678
    VOTRE_NUM_DE_MESSAGE=123456789012345678

    if canal==VOTRE_NUM_DE_CANAL and message==VOTRE_NUM_DE_MESSAGE and emoji=="🧪":
        print("Grade Supprimé")
        #user = payload.user_id


# COMMANDES

@bot.command()
async def salut(ctx): 
    """
        Commande: salut
        Affiche un message texte fixe de salut.
    """
    await ctx.send("Salut la meute")

@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    """
        Commande: bienvenue
        Affiche un message texte de bienvenue pour une personne dont le speudo est en paramètre.
        :param nouveau_membre: pseudo d'un membre discord
        :type nouveau_membre: discord.Member
    """
    pseudo=nouveau_membre.mention
    await ctx.send(f"Bienvenue {pseudo}")

@bienvenue.error
async def on_command_error(ctx, error):
    """
        Gestion d'erreur pour la commande 'bienvenue'
        Affiche un message avec la commande correcte.
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("La commande est : " + prefix + "bienvenue @speudo")


@bot.command()
async def regles(ctx): 
    """
        Commande: regles
        Affiche un message texte contenant les règles du serveur.
    """
    await ctx.send(
        "1 - Il est interdit de parler du Discord\n" +
        "2 - Il est interdit de parler du Discord,\n" +
        "3 - Si quelqu'un dit stop ou part, la conversation s'arrête,\n" +
        "4 - Pas de limite de participant par conversation,\n" +
        "5 - Une conversation à la fois,\n" +
        "6 - Pas d'insulte, pas de spam,\n" +
        "7 - La conversation dure aussi longtemps qu'elle doit durer,\n" +
        "8 - Si c'est votre premier soir au Discord, vous devez parler.")

""" Démarre le bot """
bot.run(token)

