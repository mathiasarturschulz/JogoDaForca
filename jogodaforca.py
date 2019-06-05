import random


# CLASSE RESPONSÁVEL POR ARMAZENAR O ARRAY COM O DESENHO DA FORÇA
# BUSCAR O TXT COM A LISTA DE PALAVRAS E REALIZAR O SORTEIO
# DE UMA PALAVRA
class Auxilio():
    # ARRAY COM A EVOLUÇÃO DA FORCA DE ACORDO COM OS ERROS
    aDesenhoForca = ['''

     +---+
     |   |
         |
         |
         |
         |
    ==========''', '''

     +---+
     |   |
     O   |
         |
         |
         |
    ==========''', '''

     +---+
     |   |
     O   |
     |   |
         |
         |
    ==========''', '''

     +---+
     |   |
     O   |
    /|   |
         |
         |
    ==========''', '''

     +---+
     |   |
     O   |
    /|\  |
         |
         |
    ==========''', '''

     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    ==========''', '''

     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ==========''']

    # METODO QUE REALIZA A LEITURA DE UM ARQUIVO TXT COM AS PALAVRAS E TRANFORMA 
    # O TXT EM UM ARRAY DE PALAVRAS
    def carregarPalavras(self):
        file = open('listaDePalavras.txt', 'r')
        # REALIZO A LEITURA DO ARQUIVO
        aPalavras = file.read()
        # QUEBRO O ARQUIVO EM ARRAY A CADA ESPAÇO ENCONTRADO NO ARQUIVO
        aPalavras = aPalavras.split(' ')
        
        return aPalavras

    # METODO QUE RETORNA A PALAVRA ALEATÓRIA ESCOLHIDA PARA A FORCA
    def sortearPalavra(self):
        aPalavras = self.carregarPalavras()
        # METODO QUE SELECIONA UMA ELEMENTO ALEATÓRIO DA LISTA DE PALAVRAS
        sPalavraAleatoria = random.choice(aPalavras)
        # COLOCAR A PALAVRA PARA LETRAS MAIUSCULAS
        sPalavraAleatoria = sPalavraAleatoria.upper()

        return sPalavraAleatoria


# CLASSE RESPONSÁVEL POR VALIDAR A ENTRADA DO USUÁRIO, VERIFICAR A LETRA INFORMADA 
# E REALIZAR A CONSTRUÇÃO DO JOGO DA FORCA DE ACORDO COM OS MÉTODOS ABAIXO
class JogoDaForca():
    sPalavra = ''
    aPalavra = []
    aLetrasEncontradas = []
    aLetrasTestadas = []
    aLetrasErradas = []
    iQtdChances = 0
    iQtdErros = 0
    iPosicaoDesenho = 0
    
    # CONSTRUTOR DA CLASSE
    def __init__(self):
        # INICIO AS VARIAVEIS COM UM VALOR PADRAO
        self.sPalavra = ''
        self.aPalavra = [] 
        self.aLetrasEncontradas = []
        self.aLetrasTestadas = []
        self.aLetrasErradas = []
        self.iQtdChances = 0
        self.iQtdErros = 0
        self.iPosicaoDesenho = 0

        # INSTANCIAR A CLASSSE AUXILIO E É REALIZADO O SORTEIO DE UMA PALAVRA
        self.oAuxilio = Auxilio()
        self.sPalavra = self.oAuxilio.sortearPalavra()
        
        # iQtdChances RECEBE -1 POIS A PRIMEIRA POSIÇÃO DA FORCA NÃO CONTA COMO UMA CHANCE
        self.iQtdChances = len(self.oAuxilio.aDesenhoForca) - 1
        
        # TRANSFORMO A PALAVRA EM UM ARRAY DE LETRAS
        self.aPalavra = list(self.sPalavra)

        # PERCORRO CADA POSICAO DO ARRAY aPalavra E ADICIONO _ (LETRA NAO ENCONTRADA) 
        # PARA CADA POSICAO DO ARRAY aLetrasEncontradas
        for i in range(len(self.aPalavra)):
            self.aLetrasEncontradas.append('_')
    
    # MÉTODO QUE RECEBE A LETRA INFORMADA E VERIFICA SE A LETRA FAZ PARTE DA PALAVRA ALEATÓRIA
    def tentarASorte(self, sLetra):
        # NÃO PERMITE LETRA VAZIA
        if sLetra == '':
            return 0

        # CASO sLetra SEJA UMA STRING COM VÁRIAS POSIÇÕES ME CERTIFICO DE PEGAR APENAS A PRIMEIRA LETRA
        sLetra = list(sLetra)[0]

        # COLOCO A LETRA PARA MAIUSCULA
        sLetra = sLetra.upper()

        # CASO A LETRA INFORMADA PELO USUÁRIO SEJA IGUAL A ALGUMA LETRA DA PALAVRA ALEATORIA
        # ESSA LETRA É ADICIONADA NO ARRAY DE LETRAS ENCONTRADAS NA MESMA POSIÇÃO QUE FOI ENCONTRADA
        # NA PALAVRA ALEATÓRIA
        iQtdLetras = 0
        for i in range(len(self.aPalavra)):
            if sLetra == self.aPalavra[i]:
                iQtdLetras += 1
                self.aLetrasEncontradas[i] = self.aPalavra[i]
        
        # ADICIONO A LETRA INFORMADA COMO UMA LETRA JÁ TESTADA
        self.aLetrasTestadas.append(sLetra)

        # CASO iQtdLetras SEJA IGUAL A 0, SIGNIFICA QUE NÃO FOI ENCONTRADO NENHUMA LETRA IGUAL
        # NA PALAVRA ALEATÓRIA, COM ISSO ADICIONO A LETRA NO ARRAY aLetrasErradas
        if iQtdLetras == 0:
            self.aLetrasErradas.append(sLetra)
            self.iQtdErros += 1
            self.iPosicaoDesenho +=1
        
        # RETORNA 0 CASO NAO ENCONTRE NENHUMA LETRA IGUAL NA PALAVRA OU sLetra SEJA VAZIO
        return iQtdLetras
    
    # METODO QUE VERIFICA SE AINDA POSSUI CHANCES
    # VERIFICA SE A QUANTIDADE DE ERROS É MENOR QUE A QUANTIDADE DE CHANCES QUE O USUÁRIO POSSUI
    def possuiNovasChances(self):
        if self.iQtdErros < self.iQtdChances:
            return True
        else:
            return False

    # METODO QUE VERIFICA SE ENCONTROU A PALAVRA
    # CASO aLetrasEncontradas NÃO POSSUA NENHUM _ (UNDERLINE) SIGNIFICA
    # QUE TODAS AS LETRAS JÁ FORAM COLOCADAS NO ARRAY aLetrasEncontradas
    # E QUE A PALAVRA FOI ENCONTRADA
    def verificaAchouPalavra(self):
        achouPalavra = True
        for letra in self.aLetrasEncontradas:
            if letra == '_':
                achouPalavra = False
                break
        return achouPalavra

    # METODO PRINCIPAL DO JOGO DA FORCA
    def jogarUmaVez(self):
        sLetra = ''
        bContinuar = True
        bPrimeiraExecucao = True
        
        # REALIZA O LOOP ENQUANTO A PALAVRA AINDA NÃO FOI ENCONTRADA E AINDA EXISTEM CHANCES
        # PARA DESCOBRIR A PALAVRA
        # E TAMBEM REALIZA O LOOP ENQUANTO O USUÁRIO NÃO INFORMAR 0
        while(bContinuar):
            print('\n' * 30)
            print('#' * 79)

            # SE FOR A PRIMEIRA EXECUÇÃO APRESENTO Jogo da Forca
            if bPrimeiraExecucao:
                bPrimeiraExecucao = False
                print(('#' * 31), ' Jogo da Forca ', ('#' * 31))
                print('--> Sair = 0')
            
            # VERIFICO SE A LETRA INFORMADA AINDA JÁ FOI TESTADA
            elif sLetra in self.aLetrasTestadas:
                print('Você já informou a letra \'', sLetra, '\'.')
                print('Tente novamente!\n')
            # SE NÃO, VERIFICO A LETRA INFORMADA
            else:
                self.tentarASorte(sLetra)

            # VERIFICO SE ACHOU TODAS AS LETRAS DA PALAVRA
            if self.verificaAchouPalavra():
                print('Parabéns!')
                print('Palavra encontrada: ', self.sPalavra)
                bContinuar = False

            # SE NÃO, SE AINDA NÃO ACHOU A PALAVRA, VERIFICO SE PERDEU
            elif not self.possuiNovasChances():
                bContinuar = False
                print('Você perdeu! Esgotaram suas chances... ')
                print('A palavra era: ', self.sPalavra)

            # SE NÃO ACHOU A PALAVRA E POSSUI CHANCES, CONTINUA O JOGO
            else:
                # APRESENTO AS PALAVRAS JÁ ENCONTRADAS
                print("\n--> Palavra: ", ' '.join(self.aLetrasEncontradas))
                # APRESENTO A FORCA
                print(self.oAuxilio.aDesenhoForca[self.iPosicaoDesenho])
                # APRESENTO A LISTA DE LETRAS ERRADAS JÁ TESTADAS
                print("Letras erradas: [", ' '.join(self.aLetrasErradas) , '] ')

                # RECEBO A LETRA COMO ENTRADA E JÁ CONVERTO PARA MAIUSCULA COM O COMANDO UPPER
                sLetra = input('\nAdivinhe alguma letra: ').upper()
                # SE A LETRA FOR 0 O LOOP É PARADO
                if sLetra == '0':
                    bContinuar = False


# CLASSE RESPONSÁVEL POR PERMITIR QUE O USUÁRIO JOGUE O JOGO DA FORÇA COM
# QUANTAS PALAVRAS ELE QUISER
class Jogar():

    # MÉTODO PRINCIPAL DA CLASSE
    def jogar(self):
        bJogo = True
        # WHILE QUE PERMITE JOGAR VÁRIAS VEZES E IRÁ SAIR QUANDO bJogo FOR FALSE
        while(bJogo):
            jogoDaForca = None
            jogoDaForca = JogoDaForca()
            jogoDaForca.jogarUmaVez()

            # VERIFICO DE DESEJA JOGAR COM UMA NOVA PALAVRA OU SAIR DO JOGO
            # VALIDA iOpcao PARA PERMITIR APENAS 0 OU 1
            iOpcao = -1
            while (iOpcao != '0' and iOpcao != '1'):
                iOpcao = input("\nDeseja jogar novamente? (1 - Sim | 0 - Não)\n")
            
            if iOpcao == '0':
                bJogo = False

        print('Fim de Execução!!! ')


# JOGO DA FORCA
jogar = Jogar()
jogar.jogar()


