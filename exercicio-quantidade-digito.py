def inteiros(n):
    return len((str(n)))

n = str(input('Digite um número: ')).strip()
print(f'Esse número tem {inteiros(n)} dígitos')