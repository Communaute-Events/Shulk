import nextcord
from nextcord.ext import commands

class ClearCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@nextcord.slash_command(name='clear', description='Effacez quelque messages')
	async def clear(self, interaction, messages: int):
		try:
			if messages == 12938214210:
				await interaction.channel.purge(limit=10000000)
				await interaction.channel.send("> Tout les messages ont été supprimés !")
			else:
				await interaction.channel.purge(limit=messages)
				await interaction.channel.send(f"> Tu as supprimé [`{messages}`] messages \n > {interaction.user}")
				await asyncio.sleep(3)
				await interaction.channel.purge(limit=1)
		except Exception as e:
			embed = nextcord.Embed(title="Une erreur est survenue !")
			embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
			embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
			await interaction.response.send_message(embed=embed)

def setup(bot):
	bot.add_cog(ClearCog(bot))
