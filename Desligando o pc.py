import os


desligar = input("vc quer desligar o computador: (sim/nao): ")

if desligar == "sim":
        os.system("shutdown /s /t 1")
else:
        exit()