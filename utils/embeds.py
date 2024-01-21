import nextcord

def unmute(member):
    embed = nextcord.Embed(title="Modération - Unmute", color=0xeb01ef)
    embed.add_field(name="Action :", value=f"\n> {member.mention} a été unmute")
    embed.set_author(name="Shulk")
    return unmute

def mute(member):
    embed = nextcord.Embed(title="Modération - Mute", color=0xeb01ef)
    embed.add_field(name="Action :", value=f"\n> {member.mention} a été unmute")
    embed.set_author(name="Shulk")
    return mute

def error(e):
    embed = nextcord.Embed(title="Une erreur est survenue !", color=0xeb01ef)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1192441553269047346/1197213950610264197/a-red-flag-with-a-black-triangle-error-image-15.png?ex=65ba7360&is=65a7fe60&hm=28a825a05ab403d572256e97a365a5c41de9ead347301981cdd01c972a4366a7&=&format=webp&quality=lossless&width=442&height=442")
    embed.add_field(name="L'erreur en question : ", value=f"\n```{e}```")
    return error

