calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower()) #tuple
    return string

def is_contains(string, list_to_search):
    count_calls()
    list_to_search_upper = []
    for j in list_to_search:
        list_to_search_upper.append(j.upper())
    for i in list_to_search:
        if string.upper() in list_to_search_upper:
            return True
        else:
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)