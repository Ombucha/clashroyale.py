import clashroyale as cr

client = cr.Client("token")

@client.on_battlelog_update("#URUGP8G0")
def on_battlelog_update(added_battles, removed_battles):
    print("Battlelog updated!")
    if added_battles:
        for battle in added_battles:
            print(f"{battle.battle_time} | {getattr(battle, 'trophy_change', 'N/A')} 🏆 (new battle)")
    if removed_battles:
        for battle in removed_battles:
            print(f"{battle.battle_time} removed from log.")

@client.on_member_join("#Q9LYC0YL")
def on_member_join(players):
    if players:
        for member in players:
            print(f"{member.name} ({member.trophies} 🏆) has joined!")

@client.on_member_leave("#Q9LYC0YL")
def on_member_leave(players):
    if players:
        for member in players:
            print(f"{member.name} ({member.trophies} 🏆) has left!")
