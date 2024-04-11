def leitura_notas(notas_aluno):
    for i in range(4):
        nota = int(input(f"Informe a nota do {i + 1}º Bimestre:")) 
        notas_aluno.append(nota)
    return notas_aluno

def calc_media(notas_aluno):
        media = sum(notas_aluno)
        media = media/4
        print(f"A média final do aluno é: {media}!")
        print(verificar_aprovacao(media))
        return media

def verificar_aprovacao(media):
    if media >= 7:
        print("O aluno está aprovado!")
    else:
        print("O aluno foi reprovado!") 
    return ""

notas_aluno = []
aluno_notas = leitura_notas(notas_aluno)
media = calc_media(notas_aluno)


    
    

