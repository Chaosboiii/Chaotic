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
import subprocess

import psutil

import discord
from discord.ext import commands

from config import commandData


class Ping(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.hybrid_command(description=commandData['ping']['slash_desc'])
	async def ping(self, ctx):
		seconds = int(time.time() - self.bot.startTime)
		minutes = int(seconds / 60)
		hours = int(minutes / 60)
		days = int(hours / 24)

		seconds -= minutes * 60
		minutes -= hours * 60
		hours -= days * 24


		m, h, d = '', '', ''
		s = f'{seconds} second'
		if seconds != 1: s += 's'

		if minutes != 0:
			m = f'{minutes} minute'
			if minutes != 1: m += 's'
			m += ','
		if hours != 0:
			h = f'{hours} hour'
			if hours != 1: h += 's'
			h += ','
		if days != 0:
			d = f'{days} day'
			if days != 1: d += 's'
			d+= ','

		embed = discord.Embed(color=discord.Color.orange())
		embed.add_field(name='Latency', value=f'{self.bot.latency * 1000:.1f} ms')
		embed.add_field(name='Bot Uptime', value=f'{d} {h} {m} {s}', inline=False)
		embed.add_field(name='CPU temperature', value=str(int(psutil.sensors_temperatures()['cpu_thermal'][0].current)) + '\u00b0C', inline=False)
		embed.add_field(name='Memory', value=f'{int(psutil.virtual_memory().used / 1024**2)} MiB / {int(psutil.virtual_memory().total / 1024**2)}MiB', inline=False)
		embed.add_field(name='Server Uptime', value=subprocess.check_output('uptime -p', shell=True).decode('utf-8').replace('up ', ''), inline=False)
		await ctx.reply(embed=embed)

async def setup(bot):
	await bot.add_cog(Ping(bot))
