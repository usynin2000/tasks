from tasks import add

result = add.delay(4, 6)

print("Задача отправлена... Ждём результат.")
print("Готово?", result.ready())


print("Результат:", result.get(timeout=10))