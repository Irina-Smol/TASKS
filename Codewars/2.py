# Move the first letter of each word to the end of it, then add "ay" to the end of the ord

# Переместите первую букву каждого слова в конец, а затем добавьте "ау" в конец слова

# EXAMPLE: pig_it('Pig latin is cool')  ->  igPay atinlay siay oolcay
# EXAMPLE: pig_it('Hello world!')  ->  elloHay orldway!

def pig_it(text):
    return ' '.join([i[1:] + i[0] + 'ay' if i.isalpha() else i for i in text.split()])