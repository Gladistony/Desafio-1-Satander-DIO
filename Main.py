BancoDeHerois = []

def AdicionarHeroi():
    nome = input("Digite o nome do Heroi:")
    xp = int(input("Digite a quantidade de XP do Heroi:"))
    BancoDeHerois.append({"Nome": nome, "XP": xp})

def rankXP(valor):
    if valor <= 1000:
        return "Ferro"
    elif valor <= 2000:
        return "Bronze"
    elif valor <= 5000:
        return "Prata"
    elif valor <= 7000:
        return "Ouro"
    elif valor <= 8000:
        return "Platina"
    elif valor <= 9000:
        return "Ascendente"
    elif valor <= 10000:
        return "Imortal"
    else:
        return "Radiante"

def InformacaoHerois():
    if len(BancoDeHerois) == 0:
        print("Não há Herois cadastrados")
        return
    id = 1
    for heroi in BancoDeHerois:
        print(f"ID: {id} - Nome: {heroi['Nome']} ")
        id += 1
    idler = int(input("Digite o ID do Heroi para ver a quantidade de XP:"))
    if idler > len(BancoDeHerois):
        print("ID inválido")
        return
    print(f"O Heroi {BancoDeHerois[idler-1]['Nome']} é do rank {rankXP(BancoDeHerois[idler-1]['XP'])} e tem {BancoDeHerois[idler-1]['XP']} de XP")

def atualizarXP():
    if len(BancoDeHerois) == 0:
        print("Não há Herois cadastrados")
    id = 1
    for heroi in BancoDeHerois:
        print(f"ID: {id} - Nome: {heroi['Nome']} ")
        id += 1
    idler = int(input("Digite o ID do Heroi para atualizar a quantidade de XP:"))
    if idler > len(BancoDeHerois):
        print("ID inválido")
    BancoDeHerois[idler-1]['XP'] = int(input("Digite a nova quantidade de XP do Heroi:"))

def main():
    while True:
        print("1 - Adicionar Heroi")
        print("2 - Informação dos Herois")
        print("3 - Atualizar XP")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada:"))
        if opcao == 1:
            AdicionarHeroi()
        elif opcao == 2:
            InformacaoHerois()
        elif opcao == 3:
            atualizarXP()
        elif opcao == 4:
            break
        else:
            print("Opção inválida")

main()