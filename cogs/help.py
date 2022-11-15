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

import discord
from discord.ext import commands

from config import commandData, prefix

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.hybrid_command(description=commandData['help']['slash_desc'])
	async def help(self, ctx, command=str()):
		blank = '\u200b '

		if command.lower().replace(prefix, '') in commandData:
			embed = discord.Embed(title=f'Help | {prefix}{command}', color=discord.Color.orange())
			embed.add_field(name=f'{blank * 5}Description', value=f'{blank * 8}{commandData[command]["description"]}'.replace('\n', f'\n{blank * 8}'), inline=False)
			embed.add_field(name=f'{blank * 5}Usage', value=f'{blank * 8}{prefix}{command} {commandData[command]["arguments"]}\n{blank * 8}{prefix}{command} {commandData[command]["example"]}', inline=False)
			await ctx.reply(embed=embed)

		else:
			embed = discord.Embed(title='Chaotic Commands', color=discord.Color.orange())

			embed.add_field(name=f'{blank * 4}Utility', value=f'''{blank * 8}`{prefix}help`{blank * 5}{commandData["help"]["short_desc"]}
			{blank * 8}`{prefix}ping`{blank * 5}{commandData["ping"]["short_desc"]}\n{blank * 8}`{prefix}privacy`{blank * 5}{commandData["privacy"]["short_desc"]}
			{blank * 8}`{prefix}vote`{blank * 5}{commandData["vote"]["short_desc"]}\n{blank * 8}`{prefix}code`{blank * 5}{commandData["code"]["short_desc"]}''')

			embed.add_field(name=f'{blank * 4}Time', value=f'{blank * 8}`{prefix}time`{blank * 5}{commandData["time"]["short_desc"]}', inline=False)

			embed.add_field(name=f'{blank * 4}Numbers', value=f'''{blank * 8}`{prefix}prime`{blank * 5}{commandData["prime"]["short_desc"]}
			{blank * 8}`{prefix}convert`{blank * 5}{commandData["convert"]["short_desc"]}\n{blank * 8}`{prefix}rng`{blank * 5}{commandData["rng"]["short_desc"]}''', inline=False)

			embed.add_field(name=f'{blank * 4}Misc.', value=f'''{blank * 8}`{prefix}coinflip`{blank * 5}{commandData["coinflip"]["short_desc"]}
			{blank * 8}`{prefix}char`{blank * 5}{commandData["char"]["short_desc"]}''', inline=False)

			embed.set_footer(text=f'You can use {prefix}help (command) to get more information on a command.')
			await ctx.reply(embed=embed)

async def setup(bot):
	await bot.add_cog(Help(bot))
