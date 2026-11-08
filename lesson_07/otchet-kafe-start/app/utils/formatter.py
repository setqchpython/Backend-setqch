"""Форматирование сумм и заголовков отчёта."""


def format_kopeks(kopeks: int) -> str:
    """Переводит сумму в копейках в строку вида «1 250,00 ₽»."""
    return f"{kopeks / 100:,.2f} ₽".replace(",", " ").replace(".", ",")


def format_title(text: str, width: int = 40) -> str:
    """Центрирует заголовок отчёта по заданной ширине."""
    return text.center(width, "=")
