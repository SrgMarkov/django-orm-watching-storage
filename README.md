# Пульт охранника банка

Программа для отображения базы данных пропусков в хранилище банка. Так же отслеживаются все посещения и время нахождения сотрудника в хранилище.

## Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Подключение к базе данных 

в файле `.env` необходимо прописать данные для подключения, подставить данные вместо `USER`,`PASSWORD`,`HOST`,`PORT` и `NAME` в строке:
```
postgis://USER:PASSWORD@HOST:PORT/NAME
```
### Как запустить

Запускать запускать из командной строки 
```
python3 manage.py runserver 0.0.0.0:8000 
```
затем перейти по ссылке [0.0.0.0:8000](http://0.0.0.0:8000/)

### Режим отладки

Для получения детальной инфрмации на страницах с кодом ответа 404 можно включить режим отладки
Для этого в файле `.env` нужно указать 
```
DEBUG=True
```
по умолчанию `DEBUG=False`

### Основные файлы проекта
- `models.py` модели данных и основные функции
- `datacenter\active_passcards_view.py` список активных пропусков
- `datacenter\passcard_info_view.py` список визитов по каждому сотруднику
- `datacenter\storage_information_view.py` список сотрудников, находящихся в хранилище в данный момент

### Разрешенные хосты

для обслуживания сайта на домене, отличным от `localhost` необходимо в файле `.env` добавить имя домена в строку через запятую:
```
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
```