n = input('Type something, int, str...')
methods_to_check = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper', 'isspace', 'istitle']

for method in methods_to_check:
    print(f'{method}: {getattr(n, method)()}')