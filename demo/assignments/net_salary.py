# Net salary

salary = int(input("Enter salary :"))

if salary > 50000:
    hra = salary * 30 // 100
    da = salary * 20 // 100
else:
    hra = salary * 25 // 100
    da = salary * 15 // 100

gross_salary = salary + hra + da
tax = gross_salary * 10 // 100

net_salary = gross_salary - tax
print(net_salary)

