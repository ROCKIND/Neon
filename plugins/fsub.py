# (c) @Sanchit0102 & ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️ # Dont Remove Credit

# ===================== [ importing Requirements ] ===================== #

from pyrogram import enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import DS_AUTH_CHANNEL, DS_BOT_USERNAME

# ===================== [ Force Sub Def ] ===================== #


async def checkSub(bot, message):
    userid = message.from_user.id
    try:
        user =await bot.get_chat_member(DS_AUTH_CHANNEL, userid)
        if user.status == enums.ChatMemberStatus.BANNED:
            await message.reply_text("**Sorry, You're Banned. Contact my [Developer](https://t.me/Developer_DM_Bot) to get unbanned.**", disable_web_page_preview=True)
            return False
        return True
    except UserNotParticipant:
        invite_link = await bot.export_chat_invite_link(DS_AUTH_CHANNEL)
        join_button = InlineKeyboardMarkup([
            [
            InlineKeyboardButton('🤖 Join Channel 🤖', url=invite_link)
            ],[
            InlineKeyboardButton('🔃 Refresh 🔃', url=f'https://t.me/{DS_BOT_USERNAME}?start=True')
            ]
        ])
        await message.reply_text("**Please Join My Updates Channel to use this Bot!**\n\n**Due to Overload, Only Channel Subscribers can use this Bot!**", reply_markup=join_button)
        return False
    except Exception as e:
        print(e)
        await message.reply_text("Something went wrong. Contact my [Developer](https://t.me/Developer_DM_Bot).")
        return False
    

# ===================== [🔺 End Of Force Sub 🔺] ===================== #
