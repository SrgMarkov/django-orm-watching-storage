# Пульт охранника банка

Программа для отображения базы данных пропусков в хранилище банка. Так же отслеживаются все посещения и время нахождения сотрудника в хранилище.

## Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Подключение к базе данных в файле `settings.py`
```
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
```

### Основные файлы
- `models.py` модели данных и основные функции
- `datacenter\active_passcards_view.py` список активных пропусков
- `datacenter\passcard_info_view.py` список визитов по каждому сотруднику
- `datacenter\storage_information_view.py` список сотрудников, находящихся в хранилище в данный момент
