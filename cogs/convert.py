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

class Convert(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.hybrid_command(description=commandData['convert']['slash_desc'])
	async def convert(self, ctx, amount: float, unit: str, unit2: str):
		amount1 = amount
		unit1 = unit.lower()
		unit2 = unit2.lower()
		units = {'meters':'meter', 'grams':'gram', 'liters':'liter', 'seconds':'second'}
		prefixes = {
			'yocto':10**-24, 'zepto':10**-21, 'atto':10**-18, 'femto':10**-15, 'pico':10**-12, 'nano':10**-9, 'micro':10**-6, 'milli':0.001, 'centi':0.01, 'desi':0.1,
			'deca':10, 'hecto':100, 'kilo':1000, 'mega':10**6, 'giga':10**9, 'tera':10**12, 'peta':10**15, 'exa':10**18, 'zetta':10**21, 'yotta': 10**24
		}
		prefix1 = ''
		prefix2 = ''
		for prefix in prefixes:
			if prefix in unit1:
				unit1 = unit1.replace(prefix, '')
				prefix1 = prefix
				unit1multiplier = float(prefixes[prefix1])
			if prefix in unit2:
				unit2 = unit2.replace(prefix, '')
				prefix2 = prefix
				unit2multiplier = float(prefixes[prefix2])

			if prefix1 == '': unit1multiplier = 1
			if prefix2 == '': unit2multiplier = 1


		if unit1 in units or unit1 in units.values() or unit2 in units or unit2 in units.values():
			if unit1 in units: unit1 = units[unit1]
			if unit2 in units: unit2 = units[unit2]

			if amount1 == 0 or prefix1 == prefix2:
				await ctx.reply(f'*Really?*')
			elif unit1 != unit2:
				await ctx.reply(f'Did you really think you could convert `{unit1}` to `{unit2}`?')
			else:
				amount2 = amount1 * unit1multiplier / unit2multiplier
				if amount1.is_integer(): amount1 = int(amount1)
				if amount2.is_integer(): amount2 = int(amount2)
				if amount1 != 1:
					unit1 += 's'
				if amount2 != 1:
					unit2 += 's'
				await ctx.reply(f'{amount1} {prefix1}{unit1} is {amount2} {prefix2}{unit2}')
		else:
			await ctx.reply('Invalid unit(s).')

async def setup(bot):
	await bot.add_cog(Convert(bot))
