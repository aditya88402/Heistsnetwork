from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VILLAIN import app
from config import BOT_USERNAME
from VILLAIN.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**Cʟᴏɴɪғʏ** - Tʜᴇ Uʟᴛɪᴍᴀᴛᴇ Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ Sᴏʟᴜᴛɪᴏɴ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇs.

┏━━━━━━━━━━━━━━━━━⧫
┠ ◆ **sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:** [Click Here](https://github.com/aditya88402/Heistsnetwork)  
┠ ◆ **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [༐DEV](https://t.me/I_VAMPIRE_KING)
┠ ◆ **ʀᴇʟᴇᴀsᴇᴅ ʙʏ:** [@I_VAMPIRE_KING](https://t.me/I_VAMPIRE_KING)
┗━━━━━━━━━━━━━━━━━⧫

__Fᴏʀᴋ ɪᴛ, ᴄᴜsᴛᴏᴍɪᴢᴇ ɪᴛ, ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ʏᴏᴜʀ ᴏᴡɴ!__
"""





@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
                InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/+o7_uPKxtL5hkY2Q1"),
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘", url="https://t.me/TG_HEIST")
        ],
        [ 
          InlineKeyboardButton("𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘", url=f"https://github.com/aditya88402/Heistsnetwork")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://i.ibb.co/gFm6VW52/source-code.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/aditya88402/Heistsnetwork/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/I_VAMPIRE_KING) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/+o7_uPKxtL5hkY2Q1)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
