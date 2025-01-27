import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, CallbackQueryHandler, MessageHandler, filters


class VKBot:
    def __init__(self, token):
        self.token = token
        self.api_version = '5.131'

    def search_audio(self, query, offset=0, count=10):
        params = {
            'access_token': self.token,
            'v': self.api_version,
            'q': query,
            'count': count,
            'offset': offset
        }
        response = requests.get('https://api.vk.com/method/audio.search', params=params)
        if response.status_code == 200:
            return response.json().get('response', {}).get('items', [])
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")
            return []

    def get_audio_url(self, owner_id, audio_id):
        params = {
            'access_token': self.token,
            'v': self.api_version,
            'audios': f"{owner_id}_{audio_id}"
        }
        response = requests.get('https://api.vk.com/method/audio.getById', params=params)
        if response.status_code == 200:
            audio_url = response.json().get('response')[0].get('url')
            return audio_url
        else:
            print(f"Ошибка при получении URL аудиозаписи: {response.status_code}")
            return None

    def download_audio(self, audio_url, save_path):
        try:
            response = requests.get(audio_url, stream=True)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        f.write(chunk)
                print(f"Аудиозапись успешно сохранена как '{save_path}'")
                return save_path
            else:
                print(f"Ошибка при скачивании аудиозаписи: {response.status_code}")
                return None
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            return None


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Введите название трека для поиска:')


async def handle_message(update: Update, context: CallbackContext) -> None:
    query = update.message.text
    context.user_data['query'] = query
    context.user_data['offset'] = 0
    await show_results(update, context)


async def show_results(update: Update, context: CallbackContext) -> None:
    query = context.user_data.get('query')
    offset = context.user_data.get('offset', 0)
    results = bot.search_audio(query, offset=offset, count=10)

    if results:
        keyboard = [
            [InlineKeyboardButton(f"{track['artist']} - {track['title']}", callback_data=f"track_{idx}")]
            for idx, track in enumerate(results)
        ]
        keyboard.append([
            InlineKeyboardButton('Предыдущая страница', callback_data='prev'),
            InlineKeyboardButton('Следующая страница', callback_data='next')
        ])
        keyboard.append([InlineKeyboardButton('Выйти', callback_data='quit')])
        reply_markup = InlineKeyboardMarkup(keyboard)

        if update.message:
            await update.message.reply_text(
                f"Результаты {offset + 1} - {offset + len(results)}:", reply_markup=reply_markup
            )
        else:
            await update.callback_query.edit_message_text(
                f"Результаты {offset + 1} - {offset + len(results)}:", reply_markup=reply_markup
            )
    else:
        await update.message.reply_text("Результаты не найдены.")


async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'next':
        context.user_data['offset'] += 10
        await show_results(query, context)
    elif data == 'prev':
        if context.user_data['offset'] >= 10:
            context.user_data['offset'] -= 10
            await show_results(query, context)
    elif data == 'quit':
        await query.message.delete()
    elif data.startswith('track_'):
        idx = int(data.split('_')[1])
        results = bot.search_audio(context.user_data['query'], offset=context.user_data['offset'], count=10)
        audio = results[idx]
        audio_url = bot.get_audio_url(audio['owner_id'], audio['id'])
        if audio_url:
            save_path = f"{audio['artist']} - {audio['title']}.mp3"
            file_path = bot.download_audio(audio_url, save_path)
            if file_path:
                with open(file_path, 'rb') as f:
                    await query.message.reply_audio(audio=f, title=audio['title'], performer=audio['artist'])
                os.remove(file_path)
            else:
                await query.message.reply_text("Не удалось скачать аудиозапись.")
        else:
            await query.message.reply_text("Не удалось получить URL аудиозаписи.")


if __name__ == '__main__':
    vk_token = 'ВК ТОКЕН'
    bot = VKBot(vk_token)
    tg_token = 'ТГ ТОКЕН'

    application = ApplicationBuilder().token(tg_token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()