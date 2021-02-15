from userbot import *
from hellbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/2d4bff46a2fcc62e67fda.jpg"
pm_caption = "__**♛ Master Userbot ♛**__\n\n"


pm_caption += f"**❃ Master**\n   ➥ [{DEFAULTUSER}](tg://user?id={kraken})\n"

pm_caption += f"**❃ Bot**\n   ➥ `Versi {hellversion}`\n"

pm_caption += f"**❃ Telethon\n   ➥ `Versi {version.__version__}`\n"

pm_caption += f"**❃ Status Sudo**\n   ➥ `{sudou}`\n"

pm_caption += "**❃ Grup Userbot**\n   ➥ [Grup Userbot](https://t.me/LordUserbot_Group)\n"

pm_caption += "**❃ Owner Repo**\n   ➥ [Alvin](https://t.me/liualvinas)\n\n"

pm_caption += "**❃ Repo**\n   ➥ [Repo Master](https://github.com/hellboy-op/hellbot)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Untuk Check Bot Mu Hidup Atau Tidak'
).add_command(
  'master', None, 'Untuk Check Bot Mu Hidup Atau Tidak. Menggunakan Kustom Gambar Alive Dan Pesan Alive'
).add()
