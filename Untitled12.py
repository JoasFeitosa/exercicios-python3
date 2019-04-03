
# coding: utf-8

# In[3]:


from random import randint
n = int(randint(1, 10))
p = 0
t = 0

while p != n:
    p = int(input("Seu Palpite: "))
    t += 1
    if p == n:
        print("ACERTOOU! Placar %i" % t)
    elif p < n:
        print("Chute um valor maior")
    else:
        print("Chute um valor menor")
print("Fim do Jogo!")

