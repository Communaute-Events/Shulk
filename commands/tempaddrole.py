import nextcord
from nextcord.ext import commands
import asyncio

class TempRoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="temp-addrole",
        description="Ajoute un rôle temporaire à un utilisateur"
    )
    async def temp_addrole(
            self,
            interaction,
            member: nextcord.Member,
            role: nextcord.Role,
            duration: int
    ):
        try:
            await member.add_roles(role)
            embed = nextcord.Embed(
                title=f"Rôle temporaire ⏰",
                colour=nextcord.Colour.green(),
                timestamp=interaction.created_at
            )
            embed.add_field(name="Rôle :", value=f"`{role.name}`", inline=False)
            embed.add_field(name="Durée :", value=f"`{duration}` secondes", inline=True)
            embed.add_field(name="Ajouté a :", value=f"`{member.name}`", inline=False)
            embed.set_footer(text=f"Ajouté par : {interaction.user}")
            message = await interaction.channel.send(embed=embed)


            await asyncio.sleep(duration)
            await member.remove_roles(role)
            await message.edit(embed=nextcord.Embed(
                title=f"Rôle temporaire ⏰",
                description=f"Le rôle temporaire a été retiré à : {member.display_name}",
                colour=nextcord.Colour.red(),
                timestamp=interaction.created_at
            ))

        except Exception as e:
            embed = nextcord.Embed(title="Une erreur est survenue !")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
            embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
            await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(TempRoleCog(bot))
