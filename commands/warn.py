import nextcord
from nextcord.ext import commands
import asyncio

class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def muterolemake(self, interaction):
        try:
            msgtoedit = await interaction.channel.send("> Le rôle `Warn - Shulk` n'existe pas !")
            await asyncio.sleep(1)
            msgtoedit2 = await msgtoedit.edit("> Création du rôle...")
            role = await interaction.guild.create_role(name="Warn - Shulk")
            await msgtoedit2.edit(f"> Rôle créé **<@&{role.id}>** !")
            return role
        except Exception as e:
            embed = nextcord.Embed(title="Une erreur est survenue lors de la création du rôle!")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
            embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
            await interaction.response.send_message(embed=embed)
            return None

    @nextcord.slash_command(description="Avertir un délinquant !")
    async def warn(self, interaction, member: nextcord.Member):
        role = nextcord.utils.get(interaction.guild.roles, name="Warn - Shulk")

        if role is None:
            role = await self.muterolemake(interaction)

        if role:
            try:
                if role in member.roles:
                    await member.add_roles(role)
                    await interaction.channel.send(f"> _**{member.mention}**_ a été mute pour avoir été averti deux fois.")
                else:
                    await member.add_roles(role)
                    await interaction.channel.send(f"> _**{member.mention}**_ a été averti.")
            except Exception as e:
                embed = nextcord.Embed(title="Une erreur est survenue lors de l'ajout du rôle!")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
                embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
                await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(WarnCog(bot))
