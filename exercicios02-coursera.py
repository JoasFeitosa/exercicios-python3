
# coding: utf-8

# In[1]:


def insertionSort(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i-1
        while j>=0 and x<A[j]:
            A[j+1] = A[j]
            j=j-1
        A[j+1] = x
    return A


# In[2]:


def dimensoes(array):
    tamanho = (len(array), len(array[0]))
    print(f'{tamanho[0]}X{tamanho[1]}')


# In[3]:


def dimensoes(m1,m2):
    linha = len(m1)
    coluna = len(m1[0])
    linha2 = len(m2)
    coluna2 = len(m2[0])
    if ( (linha == linha2) and (coluna == coluna2) ):
        return True
    else:
        return False


def soma_matrizes(m1,m2):
    if (dimensoes(m1,m2)):
        for a in range(len(m1)):
            for b in range(len(m1[0])):			
                m1[a][b] = m1[a][b] + m2[a][b]
        return m1
    else:
        return False


# In[4]:


def maiusculas(frase):
    p = 0
    result = ''
    while p <= (len(frase)-1):
        if ((ord(frase[p]) >= 65) and (ord(frase[p])) <= 90):
            result += frase[p]
        p+= 1
    return result


# In[5]:


def menor_nome(nomes):
    menor = ''
    cont = 0
    for l in nomes:
        if cont == 0:
            menor = l.strip()
        elif len(menor) > len(l.strip()):
            menor = l.strip()
        cont +=1
    return menor.capitalize()


# In[6]:


class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c


# In[7]:


class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if ((self.a == self.b) and (self.b == self.c) and (self.c == self.a)):
            return 'equilátero'
        elif ((self.a != self.b) and (self.b != self.c) and (self.c != self.a)):
            return 'escaleno'
        else:
            return 'isósceles'


# In[8]:


def ordenada(lista):
    fim = len(lista)
    for a in range (fim - 1):
        menor = a
        for b in range (a + 1, fim):
            if lista[b] < lista[menor]:
                return False
    return True


# In[9]:


def busca(lista, x):
    for l in range(len(lista)):
        if lista[l] == x:
            return l
    return False


# In[10]:


def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if lista[meio] == elemento:
             return meio
        elif elemento < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    return False


# In[11]:


def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
                print(lista)
    return lista


# In[12]:


def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + soma_lista(lista[1:])


# In[13]:


def encontra_impares(lista):
    if not lista:
        return []
    if lista[0] % 2 == 1:
        return [lista[0]] + encontra_impares(lista[1:])
    return encontra_impares(lista[1:])


# In[14]:


def incomodam(n):
    if n <= 0 or type(n) != int:
        return ''
    elif n == 1:
        return 'incomodam '
    else:
        return 'incomodam ' + incomodam(n - 1)

def elefantes(n, primeiro = True):
    if n < 1:
        return ''
    if n == 1:
        return 'Um elefante incomoda muita gente\n'

    if primeiro:
        return elefantes(n - 1, False)                + str(n) + ' elefantes ' + incomodam(n) + 'muito mais'
    else:
        return elefantes(n - 1, False)                + str(n) + ' elefantes ' + incomodam (n) + 'muito mais\n'                + str(n) + ' elefantes ' + incomodam (n) + 'muita gente\n'

