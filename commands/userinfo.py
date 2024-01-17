import nextcord
from nextcord.ext import commands

class UserInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="userinfo", description="C'est qui lui ??")
    async def userinfo(self, interaction, member: nextcord.User):
        try:
            accountage = (nextcord.utils.utcnow()) - (member.created_at)
            time = int(accountage.total_seconds())
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60

            roles = [role for role in member.roles[1:]]
            embed = nextcord.Embed(colour=member.color, timestamp=interaction.created_at)
            embed.set_author(name=f"{member.display_name}#{member.discriminator}", icon_url=member.avatar.url)
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="**Pseudo :**", value=f'{member.mention}')
            embed.add_field(name="A rejoint discord le :", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
            embed.add_field(name="A rejoint le serveur le  : ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
            embed.add_field(name=f"Rôles [{len(roles)}]:", value=" ".join([role.mention for role in roles]))
            embed.add_field(name="Top rôle:", value=member.top_role.mention, inline=False)
            embed.set_footer(text=f"ID: {member.id}", icon_url=interaction.user.avatar.url)

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed = nextcord.Embed(title="Une erreur est survenue !")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
            embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
            await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(UserInfoCog(bot))
