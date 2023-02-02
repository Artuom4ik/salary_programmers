# salary_programmers
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

___
#### Это программа которая показывает таблицу вакансий программистов в Москве за последние 30 дней. 
___
### Содержание:
* [Требования](https://github.com/Artuom4ik/salary_programmers#%D0%B4%D0%BB%D1%8F-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F)
* [Как запустить программу](https://github.com/Artuom4ik/salary_programmers#%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D1%82%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%83)
* [Пример работы программы](https://github.com/Artuom4ik/salary_programmers#%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B)
* [Что делать если вы хотите найти вакансии в своём городе](https://github.com/Artuom4ik/salary_programmers#%D0%B5%D1%81%D0%BB%D0%B8-%D0%B2%D1%8B-%D1%85%D0%BE%D1%82%D0%B8%D1%82%D0%B5-%D0%BD%D0%B0%D0%B9%D1%82%D0%B8-%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B8-%D0%B2-%D1%81%D0%B2%D0%BE%D0%B5%D0%BC-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B5)
___
>### Для запуска программы требуется:
 * Скачать [Python](https://www.python.org/) версии 3.1 или выше.
 * Операционная система macOS, linux, windows 7 или выше.
 * Установить все нужные библиотеки Python командой:
```
pip install -r requirements.txt
```
___
>### Как запустить программу:
* Чтобы запустить программу требуется напечатать в кансоль команду:
```
python table_vacancy.py
```
* После этого требуется подождать 2 - 5 минут (в зависамости от компьютера или ноутбука).
* Дальше в кансоле будет напечатана таблица вакансий программиста по разным языкам программирования.
___
>### Пример работы программы:
![Описание](/images/scrin.png)
___
>### Если вы хотите найти вакансии в своем городе:
* Открываем скрипт ```get_vacancy.py```.
* Ищем кусочек кода который представлен ниже на фотографии.
* | Параметр  | Описание |
  | ------------- | ------------- |
  | area  | Город, область |
* В ```area``` нужно записать ```id``` вашего города.
* Список [городов](https://api.hh.ru/areas) и их ```id```.
![Описание](/images/code.png)
___
>### Цель проекта:
* Код написан в образовательных целях  
