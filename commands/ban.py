import nextcord
from nextcord.ext import commands


class Banview(nextcord.ui.View):
	def __init__(self, member: nextcord.Member):
		super().__init__()
		self.value = None
		self.member = member

	@nextcord.ui.button(
		label="✅ L'utilisateur a bien été banni",
		style=nextcord.ButtonStyle.green,
		disabled=True,
	)
	async def confirm(
		self, button: nextcord.ui.Button, interaction: nextcord.Interaction
	):
		self.value = True
		self.stop()

	@nextcord.ui.button(label="👥 Unban l'utilisateur", style=nextcord.ButtonStyle.red)
	async def cancel(
		self, button: nextcord.ui.Button, interaction: nextcord.Interaction
	):
		await self.member.unban()
		embed = nextcord.Embed(title="Unbannisemment de l'utilisateur")
		embed.add_field(
			name=f"{self.member.name} a été débanni avec succès",
			value=f"par {interaction.user}",
		)
		await interaction.response.edit_message(embed=embed, view=None)


class BanCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

		@nextcord.slash_command(name='ban', description="Pars d'ici, et a plus jamais")
		async def ban(self, interaction: nextcord.Interaction, member: nextcord.Member, raison):
			try:
				"""Bannir les h@ck€rs"""

				await member.ban(reason=raison)

				embed = nextcord.Embed(title="🛡 Sécurité 🛡", color=0x00FF00)
				embed.add_field(name=f"__**{member}**__ a été banni avec succès !", value=f"```{raison}```", inline=False)
				embed.set_footer(text="Action effectuée par : " + ctx.author.name)
				view = Banview(member)
				await interaction.channel.send(embed=embed, view=view)

			except Exception as e:
				embed = nextcord.Embed(title="🛡 Sécurité 🛡", color=0xFF0000)
				embed.add_field(name="Erreur", value=str(e), inline=False)
				await interaction.channel.send(embed=embed)

def setup(bot):
	bot.add_cog(BanCog(bot))