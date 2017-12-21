def buscar(word, string):
    de = 0
    ate = 0

    for X in range(0, len(string)):
        de += 1
        if string[X:X + 2] == word[0:2]:
            if string[X + 2:X + 4] == word[2:4]:
                ate = (de - 1) + len(word)
                #print "Palavra encontrada [%i:%i]" %(de - 1, ate)
                return (de - 1, ate,)
            
            else:
                if string[X:X + 3] == word:
                    ate = (de - 1) + len(word)
                    #print "Palavra encontrada [{0}:{1}]".format(de - 1, ate)
                    return (de - 1, ate,)
        else:
            pass


def colocaPalavra(listaIn, listaOut, tipoPalavra = None):
    for palavra in listaIn:
        if tipoPalavra is "grande":
            listaOut.append(palavra.upper().replace('"', ""))

        elif tipoPalavra is "pequeno":
            listaOut.append(palavra.lower().replace('"', ""))

        else:
            listaOut.append(palavra.replace('"', ""))

    return True