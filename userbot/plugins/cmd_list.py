import asyncio
import io

from hellbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import bot as hellbot
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Master"
hell_logo = "./MasterUserbot/masterlogo.jpg"

@hellbot.on(admin_cmd(pattern=r"cmds"))
@hellbot.on(sudo_cmd(pattern=r"cmds", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    cmd = "ls userbot/plugins"
    thumb = hell_logo
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**Daftar Plugin Master:** \n\n{o}\n\n<><><><><><><><><><><><><><><><><><><><><><><><>\nBantuan: Jika Anda mau mencari tahu informasi Plugin,  Ketik .plinfo <nama plugin> tanpa < >. \nJoin https://t.me/lorduserbot_group untuk bantuan."
    if len(OUTPUT) > 69:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "cmd_list.text"
            hell_file = await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                thumb=thumb,
                reply_to=reply_to_id,
            )
            await edit_or_reply(hell_file, f"Output Terlalu Besar, Ini adalah file untuk daftar Plugin di Master.\n\n**☛ Master:** `{DEFAULTUSER}`")
            await event.delete()
