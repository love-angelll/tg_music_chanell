# Telegram-бот для скачивания музыки из ВК

## Описание проекта

Этот проект представляет собой Telegram-бота, который позволяет пользователям загружать музыку из ВКонтакте. Бот предоставляет удобный способ найти и скачать треки, сохраняя их в высоком качестве.

Алгоритмически это очень простой бот — это тот самый момент, когда интерфейс бота занимает больше строк кода, чем его функциональная часть. Но тут уж извините — все вопросы к Телеге с ее кнопками. Тем не менее со своей задачей он справляется, а большего нам и не надо. з VK и передавать юзеру в Telegram. Попутно предлагая ему подписаться на нужные вам каналы.

Впрочем, так как бот одной ногой в Telegram, а второй в ВК — у совсем далеких от темы людей могут возникнуть трудности. Но на деле все очень просто и сводится к следующему:

- Бот авторизуется в ВК и Telegram.
- Затем он прослушивает эфир, ожидая запросов от пользователя
- Как только юзер присылает сообщение, которое не является сервисным (/start, /help и т. д.), бот пересылает его в ВК, в «строку поиска по музыке».
На самом деле он делает не это, но те, кто в теме, — и так в теме. В любом случае так будет проще представить принцип работы бота.
- Итак, сообщение от юзера «введено в поиск по музыке», на что ВК выдает соответствующие треки. Ну или не выдает, если нет совпадений — это бот тоже учитывает.
- Ответ от ВК «нарезается» на фрагменты по 10 треков (для удобства), и первые 10 присылаются юзеру в Телеге.
- Далее он либо указывает номер искомой песни, либо жмет «Вперед»/«Назад» — для перехода к следующей/предыдущей пачке песен, соответствующих его запросу.
- При вводе номера трека бот его считывает и проверяет, подписан ли пользователь на рекламируемый канал. Если нет — предлагает подписаться.
- Если юзер подписан, бот скачивает трек из ВК и загружает его в Телегу. После завершения загрузки в Telegram бот удаляет трек со своего сервера для экономии места.

### Установка и настройка:

#### Для получения токена для бота от Телеги пишем в ЛС к [BotFather](https://t.me/BotFather), выполняем его инструкции и сохраняем присвоенный токен.

#### Для получения токена от ВК переходим на vkhost и следуем инструкции. Обратите внимание: токен дает полный доступ к вашей странице — так что не используйте личный аккаунт! 

#### Затем создаем файл main.py и вставляем туда код из этого же файла репощитория. А так же можем скачать репозиторий.
После этого останется только ввести в код API-ключи в нужные переменные.


- Склонируйте репозиторий (через CMD):
```
git clone https://github.com/love-angelll/tg_music_chanell
cd tg_music_chanell
```

- Установите зависимости:
```
pip install -r requirements.txt
```

- Настройте переменные окружения в файле:
```
vk_token = 'ВК ТОКЕН' : Токен ВК. (Kate Mobile)
tg_token = 'ТГ ТОКЕН' : Токен бота Вк.
```

- Создаем файл:
```
ads.txt
```
И добавляем в него нужные нам каналы в формате @channel.
Если не создавать файл — бот проигнорирует проверку подписки.
**НЕ РЕКОМЕНДУЕМ ВНОСИТЬ БОЛЕЕ 3 КАНАЛОВ — ЭТО СУЩЕСТВЕННО СНИЗИТ КОНВЕРСИЮ!**

- Пример файла «ads.txt»
```
@channel1
@channel2
-1001234567890
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

⚠️ Важно: Убедитесь, что вы используете данный бот только для личных целей и соблюдаете правила использования ВКонтакте и Телеграмм.

## Лицензия

Проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## Содействие

Не стесняйтесь отправлять проблемы или запросы на исправление, если у вас есть какие-либо вопросы то пишите в соц. сетях.

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/iv_frunza)
[![VK Основной](https://img.shields.io/badge/VK%20Основной-4A76A8?style=for-the-badge&logo=vk&logoColor=white)](https://vk.com/iv.frunza)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/iv.frunza)


