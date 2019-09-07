def ret(l, a):
    if l > 20:
        l = 20
    if a > 20:
        a = 20
    print('-+-'*l)
    c =0
    while c < a:
        z = '|'
        print(f'{z}{z:>{(l*3 - 1)}}')
        c += 1
    print('-+-' * l)


l = int(input('Digite a largura: '))
a = int(input('Digite a altura: '))
ret(l, a)