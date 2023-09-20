import asyncio
from pathlib import Path
token = "6679592783:AAFViS5wpuUN2sqN86Z5fa4MUXauJBv8qrg"
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# python_course_bot_1921
# @botfather -> /newbot


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("hello")
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(f'Nice to see you here')


async def sleep(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        sleep_time = int(update.message.text.split(' ')[1])
        await asyncio.sleep(sleep_time)
        await update.message.reply_text(f"Good Morning!")
    except (ValueError, IndexError):
        await update.message.reply_text(f"Usage: /sleep <time>")


async def read(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        filename = update.message.text.split(' ')[1]
        text = Path(filename).read_text('utf8')
        await update.message.reply_text(text)
    except (ValueError, IndexError):
        await update.message.reply_text(f"Usage: /read <filename>")

app = ApplicationBuilder().token(token).concurrent_updates(True).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sleep", sleep))
app.add_handler(CommandHandler("read", read))

app.run_polling()
