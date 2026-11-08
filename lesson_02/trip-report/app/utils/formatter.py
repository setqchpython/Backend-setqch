from rich.console import Console
from rich.table import Table


def print_report(expenses, total, average, day, day_sum, food_share, housing_share):
    console = Console()
    table = Table(title="Отчет по поездке")
    table.add_column("День")
    table.add_column("Категория")
    table.add_column("Сумма", justify="right")
    for expense in expenses:
        table.add_row(str(expense["day"]), expense["category"], str(expense["amount"]))
    console.print(table)

    summary = Table(title="Итог")
    summary.add_column("Показатель")
    summary.add_column("Значение")
    summary.add_row("Записей", str(len(expenses)))
    summary.add_row("Всего потрачено", f"{total} руб")
    summary.add_row("Средняя трата", f"{average:.2f} руб")
    summary.add_row("Самый дорогой день", f"день {day}, {day_sum} руб")
    summary.add_row("Доля категории еда", f"{food_share:.2f} %")
    summary.add_row("Доля категории жильё", f"{housing_share:.2f} %")
    console.print(summary)
