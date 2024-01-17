import nextcord
from nextcord.ext import commands

class KickCog(commands.Cog):
	def init(self, bot):
		self.bot = bot


		@nextcord.slash_command(name='kick', description='Expulser les h@ck€rs')
		async def kick(self, interaction, membre: nextcord.User, raison):
			"""Expulser les h@ck€rs"""
			try:
				await membre.kick()
				embed = nextcord.Embed(title="🛡 Sécurité 🛡", color=0x00ff00)
				embed.add_field(name=f"__**{membre}**__ a été expulsé avec succès !", value=f"```{raison}```", inline=False)
				embed.set_footer(text="Action effectuée par : " + interaction.user.name)
				await interaction.channel.send(embed=embed)

			except Exception as e:
				embed = nextcord.Embed(title="🛡 Sécurité 🛡", color=0xff0000)
				embed.add_field(name=f"__**{membre}**__ n'a pas pu être expulsé !", value=f"```{e}```", inline=False)
				embed.set_footer(text="Action effectuée par : " + interaction.user.name)
				await interaction.channel.send(embed=embed)	

def setup(bot):
	bot.add_cog(KickCog(bot))