from fuzzywuzzy import process
    
def pre_tratamento(text):
    saida = []
    for element in text.split(' '):

        if element.isalpha():
            saida.append(element)

        else:
            # Verificando quanto da palavra é simbolo especial
            tamanho = [token.isalpha() for token in element]

            if tamanho.count(True)/len(tamanho)>0.6 and len(tamanho)>1:
                saida.append(element)


    return ' '.join(saida)


def refino(text):

    categorias = list(set(text))
    print(categorias[0])
    print()
    melhor_match = process.extractOne(categorias[0], filter(lambda x: x !=categorias[0] ,categorias))
    print(melhor_match)
    pass


if __name__ == '__main__':
    print(pre_tratamento('03 4/8 Areia argilosa, Pouco compacta(o), Marrom'))