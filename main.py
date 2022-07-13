lista_candidatos = []

def main():
    quantidadeCandidados = int(input("Quantos candidados deseja cadastra: "))

    for i in range(quantidadeCandidados):
        adicionarCandidatos()

        quantidadeCandidados = quantidadeCandidados -1

    arquivo = ('candidatos.txt', 'w')
    for x in lista_candidatos:
        arquivo.write(x)
    arquivo.close()
    print("Salvo em TXT")

def adicionarCandidatos():
    teste_analita = ['PowerBI', 'SQL', 'Boa comunicaçao']
    teste_cientista = ['Machine Learning','Resolução De Problemas', 'Estatística']
    
    candidato = {'Nome': '', "Resumo":'', 'Vaga': '0'}
    
    candidato['Nome'] = input("Nome do candidato: ")
    candidato['Resumo']= input("Resumo do candidato: ")

    for x in teste_analita:
        if(candidato["Resumo"].lower().find(x.lower()) != -1):
            candidato['Vaga'] = "Análista de dados"
    for x in teste_cientista:
        if(candidato['Resumo'].lower().find(x.lower()) != -1):
            candidato['Vaga'] = "Cientista de dados"
    if(candidato['Vaga'] == 0):
        candidato['Vaga'] = 'Não se qualificou pra nem uma vaga!'

    print(candidato)

main()