from . import check_for_new_youtube_video
from nextcord.ext import tasks


@tasks.loop(minutes=15)
async def youtube_notify_task():
    await check_for_new_youtube_video()
