def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("30\textdegree C =", celsius_ke_fahrenheit(30), "\textdegree F")
print("86\textdegree F =", fahrenheit_ke_celsius(86), "\textdegree C")