# Напишите функцию, которая принимает строку скобок и определяет, допустим ли порядок скобок.
# Функция должна возвращать true если строка действительная и false недействительна

# Наряду с открывающей ( и закрывающей ) круглыми скобками ввод может содержать любые допустимые ASCII символы

# Write a function that takes a string of parentheses and determines whether the order of the parentheses is valid.
# The function should return true if the string is valid and false is invalid

# '()' true
# ')(()))' false
# '(' false

def valid_parentheses(string):
    k = 0
    for i in string:
        if i == '(': k +=1
        if i == ')': k -= 1
        if k < 0: return False
    return k == 0

