import encontrastr
import urllib
import re

padrao = re.compile("title=")
dados = {}

class Filtro(object):

    def __init__(self):
        self.site = "https://www.globo.com"
        self.resultado = []


    def texto(self):
        # Pega o conteudo do site.
        conteudo = urllib.urlopen(self.site).read().split("><")
        conteiner = []
        
        for item in conteudo:
            # Busca um determinado padrao.
            if padrao.findall(item) != []:
                conteiner.append(item)

        for string in conteiner:
            # Encontra o comeco do texto.
            indice = encontrastr.buscar("title=", string)[1]
            parada = 0
            texto = ""

            while True:
                # Procura o texto separa e coloca as palavras em uma lista.
                if parada == 2:
                    if encontrastr.buscar("href=", texto):
                        pass

                    else:
                        encontrastr.colocaPalavra(texto.split(" "), 
                            self.resultado)
                    break

                if indice == len(string):
                    if encontrastr.buscar("href=", texto):
                        pass

                    else:
                        encontrastr.colocaPalavra(texto.split(" "),
                            self.resultado)
                    break

                elif string[indice] == '"':
                    parada += 1
                
                texto += string[indice]
                indice = indice + 1

        while True:
            # Contagem do numero de ocorrencia da palavra.
            for palavra in self.resultado:
                ocorrencia = self.resultado.count(palavra)
                girar = 0
                while girar < ocorrencia:
                    self.resultado.remove(palavra)
                    girar = girar + 1

                dados[palavra] = ocorrencia

            if len(self.resultado) == 0:
                return True


    def ordemOcorrencia(self):
        #Organiza em ordem de ocorrencia.
        copia = dados.copy()
        ordem = []

        while True:
            aux = 0
            ocoMax = {}
            for chave, valor in copia.items():
                for chaveDois, valorDois in dados.items():
                    if valor >= valorDois and valor > aux:
                        aux = valor
                        ocoMax = {}
                        ocoMax[chave] = valor

            ordem.append(ocoMax.items()[0])
            del copia[ocoMax.keys()[0]]
            exibir = ocoMax.items()
            print "Numero de ocorrencia da palavra/letra [{0}] = {1}".format(exibir[0][0], exibir[0][1])

            if len(copia) == 0:
                return True



if __name__ == "__main__":
    filtro = Filtro()
    filtro.texto()
    filtro.ordemOcorrencia()