from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("Сейчас:", now)
print("Без микросекунд:", without_microseconds)