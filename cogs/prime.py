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

class Prime(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	def checkPrime(self, number):
		if number % 2 == 0 or number % 3 == 0:
			return False
		i = 5
		while i ** 2 <= number:
			if number % i == 0 or number % (i + 2) == 0:
				return False
			i += 6
		return True

	@commands.hybrid_command(description=commandData['prime']['slash_desc'])
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def prime(self, ctx, number: int):
		async with ctx.typing():
			if number <= 9999999999999:
				if self.checkPrime(number):
					await ctx.reply(f'{number} is a prime number.')
				else:
					await ctx.reply(f'{number} is not a prime number.')
			else:
				await ctx.reply(f'yeah right, as if i can calculate that before the end of the universe, that number is wayyy too high')

async def setup(bot):
	await bot.add_cog(Prime(bot))
