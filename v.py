from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Danh sách các URL mẫu
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

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Chào bạn! Gửi tôi lệnh /sent kèm theo các tham số theo thứ tự: <host> <time> <proxy>.")

def sent(update: Update, context: CallbackContext):
    # Kiểm tra xem người dùng có cung cấp đúng 3 tham số không
    if len(context.args) != 3:
        update.message.reply_text("Vui lòng gửi đúng 3 tham số: <host> <time> <proxy>")
        return
    
    # Lấy giá trị từ các tham số
    host = context.args[0]
    time = context.args[1]
    proxy = context.args[2]
    
    # Thay thế nhanh trong các URL
    new_urls = []
    for url in urls:
        url = url.replace("{host}", host)
        url = url.replace("{time}", time)
        url = url.replace("{proxy}", proxy)
        new_urls.append(url)
    
    # Trả lại các URL đã thay đổi
    response = "\n\n".join(new_urls)
    update.message.reply_text(response)

def main():
    # Tạo bot và updater
    updater = Updater("8193233706:AAEmFofZ4wtUaOe6ZoAEdu3CdiIPPVaBX-4", use_context=True)
    
    # Lấy dispatcher để thêm handler
    dispatcher = updater.dispatcher
    
    # Khởi tạo các handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("sent", sent))
    
    # Bắt đầu bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
