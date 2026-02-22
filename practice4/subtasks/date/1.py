from datetime import datetime, timedelta

today = datetime.now()

five_days_ago = today - timedelta(days=5)

print("Сегодня:", today)
print("Пять дней назад:", five_days_ago)