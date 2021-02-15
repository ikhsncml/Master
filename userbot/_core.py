import asyncio
import os
from datetime import datetime
from pathlib import Path
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from hellbot.utils import *
from userbot import *
from userbot import bot as hellbot

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Master"
hell_logo = "./MasterUserbot/masterlogo.jpg"
kraken = hellbot.uid
hell = f"[{DEFAULTUSER}](tg://user?id={kraken})"

@hellbot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@hellbot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = hell_logo
    input_str = event.pattern_match.group(1)
    omk = f"**⍟ Nama Plugin ≈** `{input_str}`\n**⍟ Diunggah Oleh ≈** {hell}\n\n🔱 **[Master](t.me/LordUserbot_Group)** 🔱"
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "`File Tidak Ditemukan`")

@hellbot.on(admin_cmd(pattern="install$", outgoing=True))
@hellbot.on(sudo_cmd(pattern="install$", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    a = "__Installing.__"
    b = 1
    await event.edit(a)
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "./userbot/plugins/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**Commands found in** `{}` (sudo included)\n".format((os.path.basename(downloaded_file_name)))
                    for i in CMD_LIST[shortname]:
                        string += "  •  `" + i 
                        string += "`\n"
                        if b == 1:
                            a = "__Installing..__"
                            b = 2
                        else:
                            a = "__Installing...__"
                            b = 1
                        await event.edit(a)
                    return await event.edit(f"✅ **Modul Yang Terpasang** :- `{shortname}` \n➥ **Dari:**- {hell}\n\n{string}\n\n        🔱 **[Master](t.me/Lorduserbot_Group)** 🔱", link_preview=False)
                return await event.edit(f"Installed module `{os.path.basename(downloaded_file_name)}`")
            else:
                os.remove(downloaded_file_name)
                return await event.edit(f"**Gagal Memasang** \n`Kesalahan`\nModules Sudah Dipasang Atau Format Tidak Diketahui")
        except Exception as e: 
            await event.edit(f"**Gagal Memasang** \n`Kesalahan`\n{str(e)}")
            return os.remove(downloaded_file_name)
    
@hellbot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@hellbot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def uninstall(kraken):
    if kraken.fwd_from:
        return
    shortname = kraken.pattern_match["shortname"]
    dir_path =f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await kraken.edit(f"Uninstall `{shortname}` Berhasil Dilakukan")
    except OSError as e:
        await kraken.edit("Kesalahan: %s : %s" % (dir_path, e.strerror))

@hellbot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@hellbot.on(sudo_cmd(pattern=r"upload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Berhasil Unloaded `{shortname}`")
    except Exception as e:
        await event.edit(
            "Berhasil Unloaded `{shortname}`\n{}".format(
                shortname, str(e)
            )
        )


@hellbot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@hellbot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Berhasil Loaded `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Maaf, Tidak Bisa Memuat {shortname} Karna Kesalahan Berikut.\n{str(e)}"
        )

CmdHelp("core").add_command(
  "install", "<balas ke .py file>", "Instal file python yang dibalas jika sesuai dengan kode userbot. (SEMENTARA DINONAKTIFKAN SEBAGAI HACKER MEMBUAT ANDA INSTAL BEBERAPA PLUGIN DAN DAPATKAN DATA ANDA)"
).add_command(
  "uninstall", "<nama plugin>", "Uninstal plugin yang diberikan dari userbot. Untuk mendapatkannya lagi, lakukan .restart", "uninstall alive"
).add_command(
  "load", "<nama plugin>", "Memuat plugin yang telah dibongkar ke userbot Anda", "load alive"
).add_command(
  "unload", "<nama plugin>", "Unload plugin dari userbot anda", "unload alive"
).add_command(
  "send", "<nama file>", "Mengirim file yang diberikan dari server userbot Anda, jika ada.", "send alive"
).add_command(
  "cmds", None, "Memberikan daftar modul di Master."
).add()
