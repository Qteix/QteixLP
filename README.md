# QteixLP
![Version](https://img.shields.io/badge/version-1.0-blue)
Позволяет вам использовать комманды прямо в чатах, администрировать,смотреть пинг,добавлять и удалять друзей прямо из чата.
## Установка
### Windows
Открываем cmd нажатием клавиш `Win+R` в поле ввода пишем cmd и нажимаем `enter`

Установим сам репозиторий
```shell script
    git clone  https://github.com/Qteix/QteixLP.git
```
Установим модуль vkquick для того чтобы наш юзербот запустился
```shell script
    python -m pip install --upgrade https://github.com/deknowny/vkquick/archive/1.0.zip --no-cache-dir
```
Дальше заполняем `config.py`
В поле `["$ACCESS_TOKEN"]` вводим свой токен от страницы вместо `$ACCESS_TOKEN`
И запускаем скрипт
```shell script
    py bot.py
```

