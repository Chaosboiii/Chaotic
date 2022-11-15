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

from config import commandData


class Code(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.hybrid_command(description=commandData['code']['slash_desc'])
	async def code(self, ctx):
		embed = discord.Embed(title=f'Source Code', description='You can find Chaotic\'s source code at at https://github.com/Chaosboiii/Chaotic.', color=discord.Color.orange())
		await ctx.reply(embed=embed)

async def setup(bot):
	await bot.add_cog(Code(bot))
