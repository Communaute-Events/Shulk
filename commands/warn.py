import nextcord
from nextcord.ext import commands

class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Avertir un délinquant !")
    async def warn(self, interaction, member: nextcord.Member):
        try:
            role = nextcord.utils.get(interaction.guild.roles, name="warn")
            if role in member.roles:
                mute_role = nextcord.utils.get(interaction.guild.roles, name="warn")
                await member.add_roles(mute_role)
                await interaction.channel.send(f"> _**{member.mention}**_ a été mute pour avoir été averti deux fois.")
            else:
                await member.add_roles(role)
                await interaction.channel.send(f"> _**{member.mention}**_ a été averti.")
        except Exception as e:
            embed = nextcord.Embed(title="Une erreur est survenue !")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
            embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
            await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(WarnCog(bot))
