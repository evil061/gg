import discord
from discord.ext import commands
import youtube_dl
import os

bot = commands.Bot(command_prefix="?", case_insensitive=True)
bot.remove_command("help")

@bot.command()
async def dow(ctx,video_url):
  await ctx.message.delete() #use ??dow youtube url to downlad the song
  if video_url == None:
    await ctx.send("{} Please enter a url")
  else:
    
    msg = await ctx.send("Download in process")
  #video_url = input("please enter youtube video url:")
    video_info = youtube_dl.YoutubeDL().extract_info(
    url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
  
    with youtube_dl.YoutubeDL(options) as ydl:
      ydl.download([video_info['webpage_url']])

      print("Download complete... {}".format(filename))
      await msg.delete(msg)
      await ctx.send("<@{}> Your song has been downloaded\n{}".format(ctx.author.id, filename))
      await ctx.send(file=discord.File(r'{}'.format(filename)))
      os.remove('{}'.format(filename))


bot.run('.G2Pvvp.dTJd4qFB9QYCkWJySIc5A7svSrqObxSM3RLa3U')
