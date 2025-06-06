import discord
import clashroyale as cr

client = cr.Client("token")

intents = discord.Intents.default()
bot = discord.ext.commands.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()
    print("Slash commands synced.")

@bot.tree.command(name="profile", description="Fetches a Clash Royale player's profile.")
async def profile(interaction: discord.Interaction, tag: str):
    player = client.get_player(tag)
    embed = discord.Embed(
        title=f"{player.name} ({player.tag})",
        description=(
            f"Trophies: 🏆 {player.trophies}\n"
            f"Level: {player.exp_level}\n"
            f"Clan: {getattr(player, 'clan', {}).get('name', 'None')}\n"
            f"Total Donations: {getattr(player, 'total_donations', 'N/A')}"
        ),
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

bot.run("token")
