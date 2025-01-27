# Telegram-бот для скачивания музыки из ВК

## Описание проекта

Этот проект представляет собой Telegram-бота, который позволяет пользователям загружать музыку из ВКонтакте. Бот предоставляет удобный способ найти и скачать треки, сохраняя их в высоком качестве.

### Возможности:

- Поиск музыки: пользователи могут искать треки по названию, исполнителю или альбому.

- Скачивание треков: загрузка музыки из ВКонтакте в формате MP3.

- Удобный интерфейс: интуитивно понятные команды и быстрый отклик.

### Установка и настройка:

- Склонируйте репозиторий:
```
git clone https://github.com/love-angelll/tg_music_chanell
cd tg_music_chanell
```

- Установите зависимости:
```
pip install -r requirements.txt
```

- Настройте переменные окружения в .env файле:
```
VK_API_TOKEN: токен для доступа к API ВКонтакте.

TELEGRAM_BOT_TOKEN: токен вашего Telegram-бота.
```


- Запустите бота:
```
python main.py
```


### Команды бота:
```
/start — начало работы с ботом.

/help — список доступных команд.

/search [название песни] — поиск трека.
```

## Примечания

⚠️ Важно: Убедитесь, что вы используете данный бот только для личных целей и соблюдаете правила использования ВКонтакте.

## Лицензия

Проект распространяется под лицензией MIT. Подробности в файле LICENSE.

