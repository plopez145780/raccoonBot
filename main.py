import discord
import json

from discord.ext import commands


# Recupération des token dans le conteneur keystore
with open('keystore.json', 'r') as keystore:
    keys = json.load(keystore)
type(keys)


prefix="rcn_"
bot=commands.Bot(command_prefix=prefix)

token=keys["discord"]["token"]

@bot.event
async def on_ready():
    #await bot.change_presence(
    #    status=discord.Status.idle,
    #    activity=discord.("Je suis en ligne"))
    print("RaccoonBot a votre service")


# COMMANDES

@bot.command()
async def salut(ctx): 
    await ctx.send("Salut la meute")

@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    #pseudo=nouveau_membre.display_name
    pseudo=nouveau_membre.mention
    await ctx.send(f"Bienvenue {pseudo}")

@bienvenue.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("La commande est : " + prefix + "bienvenue @speudo")

@bot.command()
async def regles(ctx): 
    await ctx.send(
        "1 - Il est interdit de parler du Discord\n" +
        "2 - Il est interdit de parler du Discord,\n" +
        "3 - Si quelqu'un dit stop ou part, la conversation s'arrête,\n" +
        "4 - Pas de limite de participant par conversation,\n" +
        "5 - Une conversation à la fois,\n" +
        "6 - Pas d'insulte, pas de spam,\n" +
        "7 - La conversation dure aussi longtemps qu'elle doit durer,\n" +
        "8 - Si c'est votre premier soir au Discord, vous devez parler.")


bot.run(token)

