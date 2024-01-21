import nextcord

class RolesUtils:
    def __init__(self, guild):
        self.guild = guild
        self.roles = guild.roles

    def create_role(self, role_name: str, color: nextcord.Color = nextcord.Color.default()):
        return self.guild.create_role(name=role_name, color=color)

    def role_exists(self, role_name: str) -> bool:
        return any(role.name == role_name for role in self.guild.roles)

    def delete_role(self, role_name: str):
        role = nextcord.utils.get(self.guild.roles, name=role_name)
        if role:
            return role.delete()

    async def add_role(self, member: nextcord.Member, role_name: str):
        role = nextcord.utils.get(self.guild.roles, name=role_name)
        if role:
            await member.add_roles(role, reason="Mute")
            print("added role")

    async def remove_role(self, member: nextcord.Member, role_name: str):
        role = nextcord.utils.get(self.guild.roles, name=role_name)
        if role:
            await member.remove_roles(role)
            print("removed role")
