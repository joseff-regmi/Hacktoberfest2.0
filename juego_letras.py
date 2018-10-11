
from io import open
import random
import os


class juegoLetras():

    palabras_es = []
    palabras_en = []
    lista_palabras = []
    lista_palabras_2 = []
    listaFinalMezclada = []
    listaAcertadas = []

    def __init__(self):
        print("Bienvenido al juego de letras\n")
        self.cargar_palabras()
        self.select_language()
        self.mezclar_letras()
        self.mostrar_palabras()

    def select_language(self):
        opt = input("\n¿Quieres jugar con palabras en ingles o español? (i/e): ")
        if opt.upper() == "I":
            self.generar_palabras(opt)
        elif opt.upper() == "E":
            self.generar_palabras(opt)
        else:
            self.select_language()

    def cargar_palabras(self):
        fichero = open("palabras_es.txt", "r")
        fichero2 = open("palabras_en.txt", "r")
        #lineas = fichero.read().splitlines()
        #lineas2 = fichero2.read().splitlines()
        for line in fichero:
            self.palabras_es.append(line.rstrip())
        for line in fichero2:
            self.palabras_en.append(line.rstrip())
        fichero.close()
        fichero2.close()

    def generar_palabras(self, idioma):
        self.idioma = idioma
        if self.idioma.upper() == "I":
            self.lista_palabras = random.sample(self.palabras_en, 15)
            self.lista_palabras_2 = self.lista_palabras[:]
        else:
            self.lista_palabras = random.sample(self.palabras_es, 15)
            self.lista_palabras_2 = self.lista_palabras[:]

    def mezclar_letras(self):
        listaTmp = []
        for i in range(len(self.lista_palabras)):
            listaTmp.append(self.lista_palabras[i])

        for i in range(len(listaTmp)):
            self.listaFinalMezclada.append(('-'.join(sorted(listaTmp[i]))))


    def mostrar_palabras(self):
        if len(self.listaFinalMezclada) == 0:
            self.finalizarJuego()
        else:
            for i in self.listaFinalMezclada:
                print(i.upper())

        palabra = input("\nIntroduce una palabra: ")
        print("\nSi quieres rendirte escribe 'GG'\n")
        if palabra.upper() == "GG":
            self.finalizarJuego()
        else:
            self.comprobar_palabra(palabra)


    def comprobar_palabra(self, palabra):
        indexTmp = 0
        self.palabra = palabra
        if self.palabra in self.lista_palabras:
            if self.palabra in self.listaAcertadas:
                print("\nYa has introducido esta palabra\n")
                self.mostrar_palabras()
            else:
                print("\nLa palabra introducida está en la lista!\n")
                self.listaAcertadas.append(self.palabra)
                indexTmp = self.lista_palabras_2.index(self.palabra)
                del self.lista_palabras_2[indexTmp]
                del self.listaFinalMezclada[indexTmp]
                self.mostrar_palabras()
        else:
            print("\nLa palabra introducida no se encuentra en la lista\n")
            self.mostrar_palabras()

    def finalizarJuego(self):
        os.system('clear')
        if len(self.listaAcertadas) != 15:
            print("\nTe has rendido")
            print("\nHas acertado {} palabras".format(len(self.listaAcertadas)))
            print("\nLas palabras que no has adivinado son: ")
            for i in self.lista_palabras:
                if i not in self.listaAcertadas:
                    print(i)
            exit(0)
        else:
            print("\n¡Enhorabuena has acertado todas las palabras!\n")
            print("\nPalabras acertadas: \n")
            for i in self.listaAcertadas:
                print(i)
            exit(0)



juegoLetras()
