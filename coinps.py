#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: Matheus Santana
# Grupo: [HAE]™Hazardous Hacking
import requests
import json
import os
import platform
import sys
def limp():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
limp()
def banner1():
    print("""\033[33;1m $$$$$$\            $$\           $$$$$$$\   $$$$$$\  
$$  __$$\           \__|          $$  __$$\ $$  __$$\ 
$$ /  \__| $$$$$$\  $$\ $$$$$$$\  $$ |  $$ |$$ /  \__|
$$ |      $$  __$$\ $$ |$$  __$$\ $$$$$$$  |\$$$$$$\  
$$ |      $$ /  $$ |$$ |$$ |  $$ |$$  ____/  \____$$\ 
$$ |  $$\ $$ |  $$ |$$ |$$ |  $$ |$$ |      $$\   $$ |
\$$$$$$  |\$$$$$$  |$$ |$$ |  $$ |$$ |      \$$$$$$  |
 \______/  \______/ \__|\__|  \__|\__|       \______/  \033[0;0m
\033[1mGrupo:\033[0;0m [HAE]™Hazardous Hacking                  \033[1mV.0.1\033[0;0m
\033[1mAutor:\033[0;0m Matheus Santana""")
banner1()
try:
    print("\033[1m"'+'+40*'='+'+')
    print("""\033[1m[0] Dólar     [2] Libra      [4] Bitcoin
[1] Euro      [3] Peso       \033[31m[5] Help\033[0;0m""")
    print("\033[1m"'+'+40*'='+'+')
    sel_options = int(input("\033[1mSelecione uma opção: \033[0;0m"))
    moedas = ['USD', 'EUR', 'GBP', 'ARS', 'BTC']
    number = []
    for x in range(len(moedas)):
        number.append(x)
    if sel_options in number: 
        moedas = moedas[sel_options]
    elif sel_options == 5:
        limp(), banner1()
        print("""\n\033[33;1m[INFO]\033[0;0m\n   O CoinPS é uma ferramenta para te manter informado sobre os preços atuais das selecionadas moedas.\n
\033[33;1m[HELP]\033[0;0m\n   O manejo da ferramenta é muito simples não há complexidade, basta apenas ter a versão 3x do Python instalada no seu sistema e executar o script. 
Ex:
    \033[1m$\033[0;0m python3 coinps.py\n
Caso esteja enfrentando algum problema técnico com a ferramenta, por favor, dirija-se a uma de nossas redes sociais e contate um administrador, links abaixo.\n
    [Facebook]
    > https://www.facebook.com/haehazardoushacking/
    [Telegram]
    > https://t.me/haehazardoushacking/
    
\033[1mAtt:\033[0;0m Matheus Santana""")
        sys.exit()
    elif sel_options != 5:
        print("\033[31mOps! Opção inválida!\033[0;0m")
        sys.exit()
    def banner2():
        print("\033[33;1m"'+'+20*'='+'+'"\033[0;0m")
        print("\033[33;1m|  COTAÇÃO DA MOEDA  |\033[0;0m")
        print("\033[33;1m"'+'+20*'='+'+'"\033[0;0m")

    def cotacao():
        banner2()
        rqts = requests.get("https://api.hgbrasil.com/finance/quotations?format=json&key=a8b7222f")
        if rqts.status_code == 200:
            dados = json.loads(rqts.content)
            lista = []
            for data in dados["results"]["currencies"][moedas]:
                lista.append(dados["results"]["currencies"][moedas][data])
                for i in range(len(lista)):
                    alt = lista[i]
            if alt > 0:
                print("""\033[37;1mMoeda:\033[0;0m {}
\033[37;1mValor:\033[0;0m {:.2f}
\033[37;1mVariação \033[44m[Alta]\033[0;0m: {}%""".format(lista[0], lista[1], lista[3]))
            else:
                print("""\033[37;1mMoeda:\033[0;0m {}
\033[37;1mValor:\033[0;0m {:.2f}
\033[37;1mVariação \033[41m[Queda]\033[0;0m: {}%""".format(lista[0], lista[1], lista[3]))
    cotacao()
except KeyboardInterrupt:
    print("\033[31mEncerrado!\033[0;0m")