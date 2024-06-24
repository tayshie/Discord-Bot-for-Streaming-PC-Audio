import discord
from discord.ext import commands
from .audio_handler import AudioHandler

def setup_bot(config):
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)
    audio_handler = AudioHandler(config)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    @bot.command()
    async def join(ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f"Joined {channel}")
        else:
            await ctx.send("You need to be in a voice channel to use this command.")

    @bot.command()
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Disconnected from voice channel")
        else:
            await ctx.send("I'm not in a voice channel.")

    @bot.command()
    async def stream(ctx, duration: int = 5):
        if not ctx.voice_client:
            await ctx.send("I'm not in a voice channel. Use !join first.")
            return

        await ctx.send(f"Starting audio capture for {duration} seconds...")
        frames = await audio_handler.capture_audio(duration)
        
        await ctx.send("Streaming captured audio...")
        await audio_handler.stream_audio(ctx.voice_client, frames)
        
        await ctx.send("Streaming finished.")

    return bot
