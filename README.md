# RescueTime-notifications
Интеграция нативных уведомлений Windows 10 и утилиты для повышения продуктивности RescueTime.
Скрипт присылает уведомление, когда время, проведенное в определенной категории (например, видеоигры) превышает определенную отметку (например, 1 час). Частота показа уведомления, его продолжительность и отображаемый текст могут быть настроены.

## Технологии
- Python 3
- python requests
- Библиотека Win10toast https://github.com/jithurjacob/Windows-10-Toast-Notifications

## Установка и запуск
Вы должны быть зарегистрированы в RescueTime:
https://www.rescuetime.com/get_rescuetime

Установить необходимые зависимости: `pip install -r requirements.txt`

Заполнить конфигурационный файл `config.ini`

Запустить скрипт: `python -m main.py`
