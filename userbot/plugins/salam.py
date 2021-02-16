# Credit By @LiuAlvinas
# Master Userbot

import asyncio

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="p ?(.*)"))
@bot.on(sudo_cmd(pattern="p ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Assalammu'alaikum`")
      
@bot.on(admin_cmd(pattern="P ?(.*)"))
@bot.on(sudo_cmd(pattern="P ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Assalammu'alaikum`")

@bot.on(admin_cmd(pattern="l ?(.*)"))
@bot.on(sudo_cmd(pattern="l ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Wa'alaikumussalam`")

@bot.on(admin_cmd(pattern="L ?(.*)"))
@bot.on(sudo_cmd(pattern="L ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Wa'alaikumussalam`")



CmdHelp("salam").add_command(
  "p", None, "Untuk memberi salam"
).add_command(
  "l", None, "Untuk menjawab salam"
).add()
