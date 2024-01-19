import nextcord
from nextcord.ext import commands

class AvatarCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@nextcord.slash_command(description="Obtenir la photo de profil d'un utilisateur.")
	async def avatar(self, interaction: nextcord.Interaction, membre: nextcord.Member):
		try:
			embed = nextcord.Embed(title=f"Photo de profil ({membre.name}) ︲ 👤", color=0xeb01ef)
			embed.set_image(url=membre.avatar.url)

			await interaction.send(embed=embed)

		except Exception as e:
			embed = nextcord.Embed(title="Une erreur est survenue !", color=0xeb01ef)
			embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
			embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
			await interaction.response.send_message(embed=embed)

def setup(bot):
	bot.add_cog(AvatarCog(bot))