import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.message_delete = True
intents.message_edit = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # Contoh filter kata-kata yang tidak diinginkan
    banned_words = ["kata1", "kata2", "kata3"]
    if any(word in message.content.lower() for word in banned_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, tolong hindari menggunakan kata-kata tidak sopan.")

    await bot.process_commands(message)

@bot.command(name='kick')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.display_name} telah dikick. Alasan: {reason}')

@bot.command(name='ban')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.display_name} telah dibanned. Alasan: {reason}')

@bot.command(name='clear')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} pesan telah dihapus.')

bot.run('MTE5Nzg5MDY2OTIyMjU3NjI1OQ.GVXb2_.HplkVvCgZbG_xkKS4LLT2fkXV9TQbd7u2_IXUY')
