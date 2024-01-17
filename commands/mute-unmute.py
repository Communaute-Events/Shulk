import asyncio
import nextcord
from nextcord.ext import commands

class MuteCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@nextcord.slash_command(description="Reduire quelqu'un aux silence.")
	async def mute(self, interaction, member: nextcord.Member):
		try:
			role = nextcord.utils.get(interaction.guild.roles, name="Mute - Shulk")
			if role is None:
				msgtoedit = await interaction.channel.send("> Le rôle `Mute` n'existe pas !")
				await asyncio.sleep(1)
				try:
					msgtoedit2 = await msgtoedit.edit("> Création du rôle...")
					role = await interaction.guild.create_role(name="Mute - Shulk")
					await msgtoedit2.edit(f"> Rôle crée **<@&{role.id}>** !")
				except Exception as e:
					embed = nextcord.Embed(title="Une erreur est survenue !")
					embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
					embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
					await interaction.response.send_message(embed=embed)

			await member.add_roles(role)
			await interaction.channel.send(f"{member.mention} a été mute")

		except Exception as e:
			embed = nextcord.Embed(title="Une erreur est survenue <:vhrisk60:1106293888039272541>")
			embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
			embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
			await interaction.response.send_message(embed=embed)
			
	@nextcord.slash_command(description="Retirer le silence a un utilisateur.")
	async def unmute(self, interaction, member: nextcord.Member):
		try:
			role = nextcord.utils.get(interaction.guild.roles, name="Mute - Shulk")
			if role in member.roles:
				await member.remove_roles(role)
				await interaction.channel.send(f"> {member.mention} a été unmute")
			else:
				await interaction.channel.send(f"> {member.mention} n'a pas le rôle Mute")
		except Exception as e:
			embed = nextcord.Embed(title="Une erreur est survenue <:vhrisk60:1106293888039272541>")
			embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
			embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
			await interaction.response.send_message(embed=embed)


def setup(bot):
	bot.add_cog(MuteCog(bot))
