lista_candidatos = []

def adicionarCandidatos(Nome, Resumo):
    teste_analita = ['Python', 'PowerBI', 'Banco de dados', 'SQL', 'Boa comunicaçao']
    tests_cientista = [ 'Python', 'Banco de dados', 'Machine Learning','Resolução De Problemas', 'Estatística']
    
    candidato = {'Nome': '', "Resumo":'', 'Vaga': ''}
    
    for i in candidato.keys():
        if(i == 'Nome'):
            candidato['Nome'].append(Nome)
        elif(i == 'Resumo'):
            candidato['Resumo'].append(Resumo)
        elif(i == 'Vaga'):
            if(Resumo.find(teste_analita[1]) != -1) or lista_candidatos = []