salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
aa = 0
bb = 0
for x in range (1,11):
    if x == 1:
        money_capital = spend - salary
        aa += money_capital
    else :
        spend = increase*spend + spend
        money_capital = spend - salary
        bb += money_capital
summa = aa+bb


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f'{summa:.2f}')
