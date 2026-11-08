def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    return calculate_total(expenses) / len(expenses)


def most_expensive_day(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    totals = {}
    for expense in expenses:
        day = expense["day"]
        totals[day] = totals.get(day, 0) + expense["amount"]
    day = max(totals, key=totals.get)
    return day, totals[day]


def category_share(expenses, category):
    if not expenses:
        raise ValueError("список расходов пуст")
    found = 0
    seen = False
    for expense in expenses:
        if expense["category"] == category:
            seen = True
            found += expense["amount"]
    if not seen:
        raise ValueError("категории нет в данных")
    return found / calculate_total(expenses) * 100
