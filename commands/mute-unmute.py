import asyncio
import nextcord
from nextcord.ext import commands
from functions.roles import RolesUtils  
from utils.embeds import unmute, mute, error

role_name = "Mute - Shulk"

class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Réduire quelqu'un au silence.")
    async def mute(self, interaction, member: nextcord.Member):
        try:
            guild = interaction.guild
            self.roleutils = RolesUtils(guild)

            if not self.roleutils.role_exists(role_name):
                notexistingrole = await interaction.channel.send("> Le rôle `Mute` n'existe pas !")
                try:
                    await notexistingrole.edit("> Création du rôle...")
                    role = await self.roleutils.create_role(role_name, nextcord.Color.default())
                    await notexistingrole.edit(f"> Rôle créé **<@&{role.id}>** !")
                except Exception as e:
                    error_embed = error(e)()
                    await interaction.response.send_message(embed=error_embed)

            embed = mute(member)
            await self.roleutils.add_role(member, role_name)
            await interaction.channel.send(embed=embed)

        except Exception as e:
            embed = error(e)
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

            if self.roleutils.role_exists(role_name) and await self.roleutils.remove_role(member, role_name):
                embed = unmute(member)()
                await interaction.channel.send(embed=embed)
            else:
                await interaction.channel.send(f"> {member.mention} n'a pas le rôle Mute")

        except Exception as e:
            embed = error(e)
            await interaction.response.send_message(embed=embed)



def setup(bot):
    bot.add_cog(MuteCog(bot))
