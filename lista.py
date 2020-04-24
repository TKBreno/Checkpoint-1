vazamentos = []
a = 1
while True:
    consulta = input("Deseja consultar, adicionar ou sair (C/A/S)?").upper()
    if consulta == "C":
        search = input("Qual email deseja consultar?")
        if search in vazamentos:
            print("Email Vazado!!!")
        else:
            print("Email Seguro!")
        

    elif consulta == "A":
        if len(vazamentos) < 30:
            vazamentos.append(input("Digite um email vazado: "))
            print(vazamentos)
        else:
            print("A lista está cheia")

    elif consulta == "S":
        if a == 1:
            quit()

    else:
        print("VC digitou a reposta errada")
        
