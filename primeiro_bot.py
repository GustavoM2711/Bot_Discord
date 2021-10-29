import datetime

import discord
from discord.ext import commands, tasks

bot = commands.Bot("!")

@bot.event
async def on_ready():
    current_time.start()
    print(f"Estou pronto! Estou conectado como {bot.user}")
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "palavrao" in message.content:
        f"Por favor, {message.author.name}, nao ofenda os demias usuarios"
        await message.delete()
    
    await bot.process_commands(message)


@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    response = "Hello, " + name
    
    await ctx.send(response)
    
@bot.command(name = "calcular")
async def calculate_expression(ctx, *expression):
    expression = "".join(expression)
    print(expression) 
    response = eval(expression)
    await ctx.send("A resposta é: " + str(response))

@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now()
    
    now = now.strftime("%d/%m/%Y ás %H:%M:%S")
    
    channel = bot.get_channel(903417112180179004)
    await channel.send("Data atual: " + now)



bot.run("OTAzMzY5ODEwODk1ODMxMDYw.YXr-sg.5Q1M7QKcJ-gI8GQNwkJH__CwNXk")