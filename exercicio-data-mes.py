#coding: utf-8

#Data com mês por extenso. Construa uma função que receba uma data no formato
#DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
#Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def extenso_mes(mes):
	lista_de_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	mes_ex = lista_de_mes[mes-1]
	return mes_ex

def extenso_dia(dia):

	lista_de_dia = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorzer", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte", "Vinte e Um", "Vinte e Dois", "Vinte e Três", "Vinte e Quatro", "Vinte e Cinco", "Vinte e Seis", "Vinte e Sete", "Vinte e Oito", "Vinte e Nove", "Trinta", "Trinta e Um"]
	dia_ex = lista_de_dia[dia-1]
	return dia_ex


print"O valor por extenso é " + extenso_dia(dia) + " de " + extenso_mes(mes) + " de %i "%ano