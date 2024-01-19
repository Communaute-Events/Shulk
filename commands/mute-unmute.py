import asyncio
import nextcord
from nextcord.ext import commands
from fonctions.roles import RolesUtils  

class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Réduire quelqu'un au silence.")
    async def mute(self, interaction, member: nextcord.Member):
        try:

            guild = interaction.guild
            self.roleutils = RolesUtils(guild)

            role_name = "Mute - Shulk"
            if not self.roleutils.role_exists(role_name):
                msgtoedit = await interaction.channel.send("> Le rôle `Mute` n'existe pas !")
                await asyncio.sleep(1)
                try:
                    await msgtoedit.edit("> Création du rôle...")
                    role = await self.roleutils.create_role(role_name, nextcord.Color.default())
                    await msgtoedit.edit(f"> Rôle créé **<@&{role.id}>** !")
                except Exception as e:
                    embed = nextcord.Embed(title="Une erreur est survenue !", color=0xeb01ef)
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
                    embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
                    await interaction.response.send_message(embed=embed)

            await self.roleutils.add_role(member, role_name)
            embed = nextcord.Embed(title="Modération - Mute", color=0xeb01ef)
            embed.add_field(name="Action :", value=f"\n> {member.mention} a été mute")
            embed.set_image(url="https://media.discordapp.net/attachments/1192441553269047346/1197972353959874630/image.png?ex=65bd35b2&is=65aac0b2&hm=94887f0df7eff9d2bc0590d9590e91d7b569eeaaad16a572b2ed3daa7bd102b4&=&format=webp&quality=lossless")
            embed.set_author(name="Shulk")
            await interaction.channel.send(embed=embed)

        except Exception as e:
            embed = nextcord.Embed(title="Une erreur est survenue !", color=0xeb01ef)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
            embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
            await interaction.response.send_message(embed=embed)


    @nextcord.slash_command(description="Retirer le silence à un utilisateur.")
    async def unmute(self, interaction, member: nextcord.Member):
        try:

            guild = interaction.guild
            self.roleutils = RolesUtils(guild)

            role_name = "Mute - Shulk"
            if not self.roleutils.role_exists(role_name):
                await interaction.channel.send("> Le rôle `Mute` n'existe pas !")
                return

            if await self.roleutils.remove_role(member, role_name):
                embed = nextcord.Embed(title="Modération - Unmute", color=0xeb01ef)
                embed.add_field(name="Action :", value=f"\n> {member.mention} a été unmute")
                embed.set_author(name="Shulk")
                await interaction.channel.send(embed=embed)
            else:
                await interaction.channel.send(f"> {member.mention} n'a pas le rôle Mute")

        except Exception as e:
            embed = nextcord.Embed(title="Une erreur est survenue !", color=0xeb01ef)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
            embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
            await interaction.response.send_message(embed=embed)



def setup(bot):
    bot.add_cog(MuteCog(bot))
