count = 0
def count_calls():
    global count
    count +=1

def string_info(slovo):
    count_calls()
    cort = ()
    a = len(slovo)
    b = slovo.lower()
    c = slovo.upper()
    cort_sl = list(cort)
    cort_sl.append(a)
    cort_sl.append(b)
    cort_sl.append(c)
    cort = tuple(cort_sl)
    return cort

def is_contains(stroka, spisok):
    count_calls()
    return stroka.upper() in [x.upper() for x in spisok]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('привет', ['ban', 'BaNaN', 'Привет'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(count)