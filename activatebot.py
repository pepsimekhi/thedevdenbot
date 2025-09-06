import discord

# Bot token - REPLACE WITH YOUR NEW TOKEN
TOKEN = 'MTQxMzk1MzcxODU2MjMyODcyNg.GyRWmu.vj-tzyTWIEWiQjxj_J7eGEEK9CSzNdebdV8F-0'

# Set up bot with minimal intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """Event triggered when bot comes online"""
    print(f'{client.user} is now online!')
    print(f'Bot ID: {client.user.id}')
    print('Bot is running and will stay online...')

# Run the bot
if __name__ == "__main__":
    try:
        client.run(TOKEN)
    except discord.LoginFailure:
        print("Invalid token! Please check your bot token.")
    except Exception as e:
        print(f"An error occurred: {e}")
