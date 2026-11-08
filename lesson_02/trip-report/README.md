# Отчет по поездке

**Студент:** DARKle  
**Группа:**

Программа считает расходы поездки и печатает отчет таблицей.

Python 3.13.7

```
C:\Users\voerc\OneDrive\Desktop\backend-starter-template-main\lesson_02\trip-report\.venv\Scripts\python.exe
```

## Структура

- `app/main.py` - данные поездки, вызовы расчетов и печать.
- `app/services/calculator.py` - только расчеты, ничего не печатает.
- `app/utils/formatter.py` - только таблица Rich.
- `tests/test_calculator.py` - проверки расчетов.
- `requirements.txt` - список библиотек.
- `.gitignore` - что не класть в git.

## Команды (Windows, PowerShell)

Команды запускать из папки `lesson_02/trip-report`.

```
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
python -m unittest discover -s tests -v
```

`python app/main.py` падает с `ModuleNotFoundError`. Запуск только через `python -m app.main`.

## Ожидаемый результат

- записей: 10
- всего потрачено: 7900 руб
- средняя трата: 790.00 руб
- самый дорогой день: день 2, 2700 руб
- доля категории еда: 24.87 %
- доля категории жильё: 68.35 %

## Почему .venv не кладут в репозиторий

Папка `.venv` собрана на этом компьютере и хранит путь к местному Python. На другой машине она не запустится. Ее создают заново и ставят библиотеки из `requirements.txt`.

## Проверка на чистом месте

Папку скопировал без `.venv` в отдельный каталог. Там снова выполнил `py -m venv .venv` и `pip install -r requirements.txt`.

`python -m app.main` напечатал те же числа: 7900, 790.00, день 2 и 2700, еда 24.87 %, жильё 68.35 %. `python -m unittest discover -s tests -v` - 9 тестов, все прошли.

