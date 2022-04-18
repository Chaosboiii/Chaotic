from discord.ext import commands
import discord, random, time, subprocess, psutil

prefix = 'c!'
bot = commands.Bot(command_prefix=prefix, help_command=None)
blank = '\u200b '
embed = ''

@bot.event
async def on_ready():
	import time
	print(time.strftime(f'logged in as {bot.user} at %d. %B %Y %H:%M:%S', time.localtime(time.time())))
	await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="with the code"))
	global startTime
	startTime = time.time()

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.MissingPermissions):
		await ctx.reply(f'You need the permission `{error.missing_perms[0]}` to run this command!')
	elif isinstance(error, commands.errors.CommandNotFound):
		await ctx.reply(f'I don\'t recognize that command!')
	else:
		raise error

#Utility
@bot.command()
async def help(ctx, arg=None):
	if arg == None:
		embed = discord.Embed(title='Chaotic Commands', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 4}Utility', value=f'{blank * 8}`{prefix}help`{blank * 5}Sends this message\n{blank * 8}`{prefix}ping`{blank * 5}Sends ping and uptime\n{blank * 8}`{prefix}privacy`{blank * 5}Sends Chaotic\'s privacy policy\n{blank * 8}`{prefix}vote`{blank * 5}Sends voting link')
		embed.add_field(name=f'{blank * 4}Fun', value=f'{blank * 8}`{prefix}rng`{blank * 5}Generates a random number\n{blank * 8}`{prefix}coinflip`{blank * 5}Flips a coin\n{blank * 8}`{prefix}char`{blank * 5}Counts characters', inline=False)
		embed.add_field(name=f'{blank * 4}Time', value=f'{blank * 8}`{prefix}time`{blank * 5}Sends seconds since the Unix Epoch', inline=False)
		embed.add_field(name=f'{blank * 4}Numbers', value=f'{blank * 8}`{prefix}prime`{blank * 5}Check if a number is prime or not', inline=False)
		embed.set_footer(text=f'You can use {prefix}help (command) to get more information on a command')
		await ctx.reply(embed=embed)
	elif arg.lower() == 'help':
		embed = discord.Embed(title=f'Help | {prefix}help', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}If no command is given or given command is not valid, sends a list of commands.\n{blank * 8}If given command is valid, sends a description, usage and a usage example of the command, like this page.', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}help `(command)`\n{blank * 8}{prefix}help ping', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'ping':
		embed = discord.Embed(title=f'Help | {prefix}ping', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Sends the ping and uptime of the bot, takes no arguments', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}ping', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'privacy':
		embed = discord.Embed(title=f'Help | {prefix}privacy', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Sends Chaotic\'s privacy policy', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}privacy', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'vote':
		embed = discord.Embed(title=f'Help | {prefix}vote', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Sends voting link', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}vote', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'rng':
		embed = discord.Embed(title=f'Help | {prefix}rng', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Generates a random number, takes 2 arguments: minimum and maximum.', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}rng `minimum` `maximum`\n{blank * 8}{prefix}rng 0 10', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'coinflip':
		embed = discord.Embed(title=f'Help | {prefix}coinflip', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Sends Heads or Tails, takes no arguments.', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}coinflip', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'char':
		embed = discord.Embed(title=f'Help | {prefix}char', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Counts the amount of characters in the given argument.', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}char `argument`\n{blank * 8}{prefix}char The quick brown fox jumps over the lazy dog', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'prime':
		embed = discord.Embed(title=f'Help | {prefix}prime', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Checks if a number is a prime number', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}prime `number`\n{blank * 8}{prefix}prime 17', inline=False)
		await ctx.reply(embed=embed)
	elif arg.lower() == 'time':
		embed = discord.Embed(title=f'Help | {prefix}time', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}Sends seconds since the Unix Epoch', inline=False)
		embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}time', inline=False)
		await ctx.reply(embed=embed)
	else:
		embed = discord.Embed(title='Chaotic Commands', color=discord.Color.orange())
		embed.add_field(name=f'{blank * 4}Utility', value=f'{blank * 8}`{prefix}help`{blank * 5}Sends this message\n{blank * 8}`{prefix}ping`{blank * 5}Sends ping and uptime')
		embed.add_field(name=f'{blank * 4}Fun', value=f'{blank * 8}`{prefix}rng`{blank * 5}Generates a random number\n{blank * 8}`{prefix}coinflip`{blank * 5}Flips a coin\n{blank * 8}`{prefix}char`{blank * 5}Counts characters', inline=False)
		embed.add_field(name=f'{blank * 4}Time', value=f'{blank * 8}`{prefix}time`{blank * 5}Sends seconds since the Unix Epoch', inline=False)
		embed.add_field(name=f'{blank * 4}Numbers', value=f'{blank * 8}`{prefix}prime`{blank * 5}Check if a number is prime or not', inline=False)
		embed.set_footer(text=f'You can use {prefix}help (command) to get more information on a command')
		await ctx.reply(embed=embed)
@bot.command()
async def ping(ctx):
	import time
	embed = discord.Embed(color=discord.Color.orange())
	embed.add_field(name='Ping', value=f'{bot.latency * 1000:.1f} ms')
	seconds, minutes, hours, days = time.time() - startTime, (time.time() - startTime) // 60, (time.time() - startTime) // 60 // 60, (time.time() - startTime) // 60 // 60 // 24
	seconds -= minutes * 60
	minutes -= hours * 60
	hours -= days * 24
	if seconds != 1: sSuffix = 's'
	else: sSuffix = ''
	if minutes != 1: mSuffix = 's'
	else: mSuffix = ''
	if hours != 1: hSuffix = 's'
	else: hSuffix = ''
	if days != 1: dSuffix = 's'
	else: dSuffix = ''
	if int(days) != 0:
		embed.add_field(name='Bot Uptime', value=f'{int(days)} day{dSuffix}, {int(hours)} hour{hSuffix} and {int(minutes)} minute{mSuffix}', inline=False)
	elif int(hours) != 0:
		embed.add_field(name='Bot Uptime', value=f'{int(hours)} hour{hSuffix} and {int(minutes)} minute{mSuffix}', inline=False)
	elif int(minutes) != 0:
		embed.add_field(name='Bot Uptime', value=f'{int(minutes)} minute{mSuffix} and {int(seconds)} second{sSuffix}', inline=False)
	else:
		embed.add_field(name='Bot Uptime', value=f'{int(seconds)} second{sSuffix}', inline=False)
	embed.add_field(name='CPU temperature', value=str(int(psutil.sensors_temperatures()['cpu_thermal'][0].current)) + '\u00b0C', inline=False)
	embed.add_field(name='Memory', value=f'{int(psutil.virtual_memory().used / 1024**2)} MiB / {int(psutil.virtual_memory().total / 1024**2)}MiB', inline=False)
	embed.add_field(name='Server Uptime', value=subprocess.check_output('uptime -p', shell=True).decode('utf-8').replace('up ', ''), inline=False)
	await ctx.reply(embed=embed)

@bot.command()
async def privacy(ctx):
	embed = discord.Embed(color=discord.Color.orange())
	embed.add_field(name='Chaotic\'s privacy policy', value='Chaotic does not store any guild/user data')
	await ctx.reply(embed=embed)

@bot.command()
async def vote(ctx):
	embed = discord.Embed(title=f'Vote', description='You can vote at https://top.gg/bot/774735144837578802/vote', color=discord.Color.orange())
	await ctx.reply(embed=embed)

#Fun
@bot.command()
async def char(ctx, *, arg=None):
	if arg == None:
		await ctx.reply('No arguments given.')
	else:
		await ctx.reply(f'There are {len(arg)} character(s), and {len(arg.replace(" ", ""))} character(s) without spaces.')
@bot.command()
async def coinflip(ctx):
	await ctx.reply(f'You got {random.choice(["heads", "tails"])}.')

#Time
@bot.command()
async def time(ctx):
	import time
	await ctx.reply(f'There has been {int(time.time())} seconds since the Unix Epoch.')

#Numbers
@bot.command()
async def rng(ctx, min=None, max=None):
	if str(min).isdecimal() and str(max).isdecimal():
		await ctx.reply(f'Your random number is {random.randint(int(min), int(max))}.')
	else:
		await ctx.reply('Something was wrong with at least one of your arguments.')
@bot.command()
async def prime(ctx, number=None):
	if number != None and number.isdecimal():
		async with ctx.typing():
			number = int(number)
			if number > 10000000000000:
				await ctx.reply(f'{number} is too high, maximum is 10 trillion')
			else:
				def checkPrime(number):
					if number % 2 == 0 or number % 3 == 0:
						return False
					i = 5
					while i ** 2 <= number:
						if number % i == 0 or number % (i + 2) == 0:
							return False
						i += 6
					return True
				if checkPrime(number):
					await ctx.reply(f'{number} is a prime number')
				else:
					await ctx.reply(f'{number} is not a prime number')

	else:
		await ctx.reply('You need to send a number.')

bot.run(open('token', 'r').read())
