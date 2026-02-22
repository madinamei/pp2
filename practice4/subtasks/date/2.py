from datetime import datetime, timedelta

today = datetime.now().date() 
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера:", yesterday)
print("Сегодня:", today)
print("Завтра:", tomorrow)