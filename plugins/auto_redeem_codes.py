# (c) ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️ # Dont Remove Credit

import random
import string
from datetime import datetime, timedelta
import pytz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import AUTO_REDEEM_CODE, DURATION_OF_PREMIUM, POST_DELETE_TIME, DS_AUTH_CHANNEL, DS_BOT_USERNAME, DS_LOG_CHANNEL, VALID_REDEEM_CODES
# from scheduler import scheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import generate_code

scheduler = AsyncIOScheduler()

REDEEM_MESSAGE_ID = None
REDEEM_MESSAGE_DATE = None
REDEEM_CODES_TRACKER = {}

async def post_daily_redeem_codes(bot):
    global REDEEM_MESSAGE_ID, REDEEM_CODES_TRACKER, REDEEM_MESSAGE_DATE
    codes = []
    VALID_REDEEM_CODES.clear()
    REDEEM_CODES_TRACKER.clear()

    for _ in range(AUTO_REDEEM_CODE):
        code = generate_code()
        VALID_REDEEM_CODES[code] = DURATION_OF_PREMIUM
        REDEEM_CODES_TRACKER[code] = {"used": False, "user_id": None}
        codes.append(code)

    today_str = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y")
    codes_text = '\n'.join(f"➤ <code>/redeem {c}</code>" for c in codes)

    text = f"""<b>Redeem Codes Generated For Today ({today_str})!

🎟️ Total Codes: {AUTO_REDEEM_CODE}
⏳ Duration: {DURATION_OF_PREMIUM}</b>

{codes_text}

🔰<u>𝗥𝗲𝗱𝗲𝗲𝗺 𝗜𝗻𝘀𝘁𝗿𝘂𝗰𝘁𝗶𝗼𝗻</u>🔰
<b>Just click the above code to copy and then send that code to the Bot, that's it 🔥</b>"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Redeem Here ✓", url=f"https://t.me/{DS_BOT_USERNAME}")],
        [InlineKeyboardButton("Any Query ❔", url="https://t.me/Developer_DM_Bot")]
    ])

    msg = await bot.send_message(DS_AUTH_CHANNEL, text, reply_markup=keyboard)
    REDEEM_MESSAGE_ID = msg.message_id
    REDEEM_MESSAGE_DATE = datetime.utcnow()

    delete_time = datetime.now() + timedelta(days=POST_DELETE_TIME)
    scheduler.add_job(delete_redeem_post, 'date', run_date=delete_time, args=[bot])


async def update_redeem_post(bot):
    global REDEEM_MESSAGE_ID
    if REDEEM_MESSAGE_ID:
        today_str = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y")
        lines = []
        for code, data in REDEEM_CODES_TRACKER.items():
            if data["used"]:
                lines.append(f"➤ <s><code>/redeem {code}</code></s>")
            else:
                lines.append(f"➤ <code>/redeem {code}</code>")

        codes_text = "\n".join(lines)
        text = f"""<b>Redeem Codes Generated For Today ({today_str})!

🎟️ Total Codes: {AUTO_REDEEM_CODE}
⏳ Duration: {DURATION_OF_PREMIUM}</b>

{codes_text}

🔰<u>𝗥𝗲𝗱𝗲𝗲𝗺 𝗜𝗻𝘀𝘁𝗿𝘂𝗰𝘁𝗶𝗼𝗻</u>🔰
<b>Just click the above code to copy and then send that code to the Bot, that's it 🔥</b>"""

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Redeem Here ✓", url=f"https://t.me/{DS_BOT_USERNAME}")],
            [InlineKeyboardButton("Any Query ❔", url="https://t.me/Developer_DM_Bot")]
        ])

        await bot.edit_message_text(
            chat_id=DS_AUTH_CHANNEL,
            message_id=REDEEM_MESSAGE_ID,
            text=text,
            reply_markup=keyboard
        )


async def delete_redeem_post(bot):
    global REDEEM_MESSAGE_ID
    if REDEEM_MESSAGE_ID:
        try:
            await bot.delete_messages(chat_id=DS_AUTH_CHANNEL, message_ids=[REDEEM_MESSAGE_ID])
            REDEEM_MESSAGE_ID = None
        except Exception:
            pass
