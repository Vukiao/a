from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Danh sách URL mẫu
urls = [
    "https://cd0b-35-201-219-137.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://0847-35-236-136-249.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://37c4-35-234-37-91.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://9f33-35-234-37-91.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://efbd-35-194-184-158.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://b84a-35-234-37-91.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://40d3-35-234-37-240.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://4a48-35-221-235-140.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://99c6-35-221-250-153.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://7436-35-229-179-2.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://6673-35-234-37-240.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://ba32-35-221-235-140.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}",
    "https://bb2b-35-189-190-31.ngrok-free.app/api?host={host}&time={time}&proxy={proxy}"
]

async def sent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 3:
        await update.message.reply_text("Dùng: /sent <host> <time> <proxy>")
        return

    host, time, proxy = args
    result_urls = [
        url.replace("{host}", host).replace("{time}", time).replace("{proxy}", proxy)
        for url in urls
    ]
    await update.message.reply_text("\n\n".join(result_urls))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gửi lệnh: /sent <host> <time> <proxy>")

def main():
    app = ApplicationBuilder().token("8193233706:AAEmFofZ4wtUaOe6ZoAEdu3CdiIPPVaBX-4").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sent", sent))
    app.run_polling()

if __name__ == '__main__':
    main()
