vazamentos = []
a = ""
while True:
    consulta = input("Deseja consultar ou adicionar (C/A)?").upper()
    if consulta == "C":
        search = input("Qual email deseja consultar?")
        for i in range(len(vazamentos)):
            if vazamentos[i] == search.strip():
                print("Email vazado!!!")
                a = True
                                           
        if a != True:
            print("Email seguro!")

    elif consulta == "A":
        if len(vazamentos) < 30:
            vazamentos.append(input("Digite um email vazado: "))
            print(vazamentos)
        else:
            print("A lista está cheia")         
    else:
        print("VC digitou a reposta errada")
        
