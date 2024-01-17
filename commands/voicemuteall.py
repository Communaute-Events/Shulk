import nextcord
from nextcord.ext import commands

class MuteAllview(nextcord.ui.View):
	def __init__(self, member: nextcord.Member):
		super().__init__()
		self.value = None
		self.member = member

	@nextcord.ui.button(
		label="Mettre en sourdine 🔉 ",
		style=nextcord.ButtonStyle.green,
		disabled=True,
	)
	async def confirm(
		self, button: nextcord.ui.Button, interaction: nextcord.Interaction
	):
		for member in voice_channel.members:
			
			await member.edit(mute=True)
			await interaction.channel.send("> **Succès !**")
		self.value = True
		self.stop()

	@nextcord.ui.button(label="Annuler ❌", style=nextcord.ButtonStyle.red)
	async def cancel(
		self, button: nextcord.ui.Button, interaction: nextcord.Interaction
	):
		await interaction.channel.send("> **Tout les utilisateurs ont était mis en sourdine**")

class MuteAllCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@nextcord.slash_command(description="Mute tout les membres dans le salon vocal.")
	async def vc_muteall(self, interaction):
		try:
			if interaction.user.voice:
				vc = interaction.user.voice.channel
				nombredegens = len(vc.membres)
				view = MuteAllview(member)
				await interaction.channel.send(f"> **Êtes-vous sûr de vouloir mettre en sourdine : {nombredegens} personnes ?", view=view)
									
			else:
				await interaction.channel.send(f"> **Vous n'êtes pas dans un salon vocal !")
		except Exception as e:
			embed = nextcord.Embed(title="Une erreur est survenue !")
			embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
			embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
			await interaction.response.send_message(embed=embed)

def setup(bot):
	bot.add_cog(MuteAllCog(bot))
