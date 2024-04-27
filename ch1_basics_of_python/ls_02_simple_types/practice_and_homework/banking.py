"""
Задача представляет собой написание программы для симуляции работы банкомата с определёнными правилами.

Шаги решения задачи:
Инициализация баланса: Начальный баланс установлен равным нулю.
Определение операций: Необходимо реализовать операции пополнения и снятия средств, а также выход из программы.
Проверка кратности суммы: Сумма пополнения и снятия должна быть кратна 50.
Комиссия за снятие: За каждое снятие средств взимается комиссия в размере 1.5%,
    но не менее 30 и не более 600 единиц.
Бонус за пополнение: После каждой третьей операции пополнения начисляется бонус в размере 3% от суммы пополнения.
Ограничение на снятие: Нельзя снять больше, чем есть на счете.
Налог на богатство: При балансе свыше 5 миллионов перед каждой операцией снимается налог в размере 10%.
"""


def apply_commission(amount):
    commission = max(30, min(600, amount * 0.015))
    return amount + commission


def apply_bonus(balance, amount, count_deposit):
    if count_deposit % 3 == 0:
        bonus = amount * 0.03
        balance += bonus
        print(f"Бонус в размере {bonus:.2f} был начислен на ваш счет.")
    return balance


def apply_wealth_tax(balance):
    if balance > 5000000:
        tax = balance * 0.1
        balance -= tax
        print(f"Налог на богатство в размере {tax:.2f} был снят.")
    return balance


balance = 0
operation_count = 0
count_deposit = 0

while True:
    print(f"Текущий баланс: {balance:.2f}")
    action = input("Выберите действие (пополнить, снять, выйти): ").lower()

    if action == 'выйти':
        break

    if action in ['пополнить', 'снять']:
        amount = int(input("Введите сумму (кратную 50): "))
        if amount % 50 != 0:
            print("Сумма должна быть кратной 50.")
            continue

        if action == 'пополнить':
            balance = apply_wealth_tax(balance)
            balance += amount
            balance = apply_bonus(balance, amount, count_deposit)
            count_deposit += 1
            operation_count += 1

        elif action == 'снять':
            balance = apply_wealth_tax(balance)
            if amount > balance:
                print("Невозможно снять больше, чем есть на счете.")
                continue
            commission = apply_commission(amount)
            balance -= commission
            operation_count += 1

        print(f"Операция успешно выполнена. Текущий баланс: {balance:.2f}")
    else:
        print("Неверная команда.")

print("Сеанс работы с банкоматом завершен.")
