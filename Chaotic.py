# MIT License
#
# Copyright (c) 2022 Chaosboiii
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time

import discord
from discord.ext import commands

import cogs
from config import extensions, prefix


bot = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.default())
bot.startTime = 0

@bot.event
async def on_ready():
	for extension in extensions:
		await bot.load_extension(extension)
	await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="with the code"))
	await bot.tree.sync()
	bot.startTime = time.time()
	print(time.strftime(f'logged in as {bot.user} at %d. %B %Y %H:%M:%S', time.localtime(time.time())))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CommandNotFound):
		await ctx.reply(f'I don\'t recognize that command!')
	elif isinstance(error, commands.errors.BadArgument):
		await ctx.reply(f'There was something wrong with one or more of your arguments.')
	elif isinstance(error, commands.errors.CommandOnCooldown):
		await ctx.reply(f'You must wait {error.retry_after:.1f} seconds before using that command again..')
	elif isinstance(error, commands.errors.MissingPermissions):
		await ctx.reply(f'You need the permission `{error.missing_perms[0]}` to run this command!')
	else:
		await ctx.reply(f'Something went wrong.')
		raise(error)

bot.run(open('token', 'r').read())
