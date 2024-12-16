import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the bot's responses
ABOUT_ME = """Привет! Я Catonis, веб-дизайнер и full-stack разработчик с более чем двухлетним опытом.
Я создаю минималистичные, удобные и функциональные решения. Моя работа охватывает дизайн, разработку веб-приложений, сайтов и ботов для автоматизации процессов.
Цель — превращать идеи клиентов в реальность."""

WHAT_I_DO = """• Создавать веб-сайты и приложения любой сложности
• Разрабатывать пользовательские интерфейсы (UI/UX)
• Создавать ботов для Telegram для автоматизации процессов и взаимодействия с пользователями
• Осуществлять полный цикл разработки: от идеи до финального продукта"""

SKILLS = """• React, Vue.js
• JavaScript, TypeScript
• Tailwind CSS
• Python, C++"""

EDUCATION = """НИШ, Казахстан — отличная база знаний и участие в IT-мероприятиях, что помогло развить навыки программирования и управления проектами."""

CONTACT = "https://t.me/Catonis_dev"

def get_keyboard():
    """Generate the inline keyboard markup."""
    keyboard = [
        [InlineKeyboardButton("📋 Обо мне", callback_data='about')],
        [InlineKeyboardButton("🛠️ Что я умею?", callback_data='what_i_do')],
        [InlineKeyboardButton("🎨 Навыки", callback_data='skills')],
        [InlineKeyboardButton("🎓 Образование", callback_data='education')],
        [InlineKeyboardButton("📞 Связаться со мной", url=CONTACT)]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    reply_markup = get_keyboard()
    await update.message.reply_text('Выберите интересующий вас раздел, чтобы узнать больше обо мне:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        new_text = f"📋 Обо мне:\n\n{ABOUT_ME}"
    elif query.data == 'what_i_do':
        new_text = f"🛠️ Что я умею?:\n\n{WHAT_I_DO}"
    elif query.data == 'skills':
        new_text = f"🎨 Навыки:\n\n{SKILLS}"
    elif query.data == 'education':
        new_text = f"🎓 Образование:\n\n{EDUCATION}"
    else:
        new_text = "Выберите интересующий вас раздел, чтобы узнать больше обо мне:"

    reply_markup = get_keyboard()
    await query.edit_message_text(text=new_text, reply_markup=reply_markup)

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7887735276:AAFpw2Z7CttDeBVhLGvZjvhqA2zXoeqAXQs").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()