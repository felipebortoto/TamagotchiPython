class TamagotchiPython:
    def __init__(self,nome):
        """
        Inicializando um novo objeto Tamagotchi. Definindo atributos iniciais
        :param nome: O nome do Tamagotchi.
        :type nome: str
        """
        self.nome = nome
        self.fome = 20
        self.saude = 100
        self.idade = 1
    def TrocarNome(self, novoNome):
        """
        Troca o nome do Tamagochi
        :param novoNome: Novo nome para o Tamagochi.
        :type novoNome: str
        """
        self.nome = novoNome
    def AlterarFome(self, valorFome):
        """
        Modifica a fome, mantendo um intervalo de 0 a 100
        :param valorFome: Valor a ser somado(+) ou subtraído(-)
        :type valorFome: int
        """
        self.fome += valorFome
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def AlteraSaude(self, valorSaude):
        """
        Modifica a saude, mantendo intervalo de 0 a 100
        :param valorSaude: Valor a ser somado(+) ou subtraído(-)
        :type valorSaude: int
        """
        self.saude += valorSaude
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0
    def AlterarIdade(self):
        self.idade += 1
    """
    Retornando todos os valores atuais ao Tamagochi
    :return: Nome do Tamagotchi
    :rtype: str
    :return: Valor da fome
    :rtype: int
    :return: Valor da saúde
    :rtype: int
    :return: Valor da idade
    :rtype: int
    :return: Valor do humor
    :rtype: int
    """
    def RetornarNome(self):
        return self.nome
    def RetornarFome(self):
        return self.fome
    def RetornarSaude(self):
        return self.saude
    def RetornarIdade(self):
        return self.idade
    def RetornarHumor(self):
        humor = self.saude - self.fome 
        return humor
    
# Início do Jogo

nomeT = input('Qual o nome do seu Tamagotchi? ')
t = TamagotchiPython(nome = nomeT)
while (t.saude > 0) and (t.fome < 100):
    t.AlterarFome(+2)
    t.AlteraSaude(-2)
    t.AlterarIdade()
    resposta = input(f"""\n------------------------------------------\n 
 __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOlá meu nome é {t.nome}. O que você deseja fazer comigo agora? 
     \n1- Alimentar (-10 de fome)
     \n2- Dormir (+10 de saúde)
     \n3- Alterar nome
     \n4- Visualizar humor
     \n5- Visualizar idade
     \n6- Visualizar fome
     \n7- Visualizar saúde
     \nResposta: """)
    print('\n')
    match resposta:
        case '1':
            t.AlterarFome(-10) 
            print("-10 de fome! Obrigado!")
        case '2':
            t.AlterarSaude(10)
            print("Se sentindo melhor! +10 de saúde!")
        case '3':
            novo_nome = input('Qual nome deseja colocar? ')
            t.TrocarNome(novo_nome)
            print("Nome alterado com sucesso!")
        case '4':
            print("Humor atual:", t.RetornarHumor())
            if t.RetornarHumor() > 50:
                print("""\n------------------------------------------\n
 __         __
/  \.-" "-./  \.
\    ^   ^    /
 |   o   o   |
 \ \.^'''^./ /
  '-\__Y__/-'
     `---`
Feliz! =)
""")
            elif t.RetornarHumor() >= 25 and t.RetornarHumor() <=50:
                print("""\n------------------------------------------\n
 __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
Normal! =|
""")
            elif t.RetornarHumor() < 25:
                print("""\n------------------------------------------\n
 __         __
/  \.-" "-./  \.
\    -   -    /
 |   U   U   |
 \ .´ ''' `. /
  '-/__Y__\-'
     `---`
Triste! =C
""")
        case '5':
            print("Idade atual: ", t.RetornarIdade())
        case '6':
            print("Fome atual: ", t.RetornarFome())
        case '7':
            print("Saúde atual: ", t.RetornarSaude())
        case _:  # Caso padrão para qualquer outra entrada
            print('Opção inválida! Tente novamente.')

print("\n--- FIM DE JOGO ---")
if t.RetornarSaude() <= 0:
    print("""\n------------------------------------------\n 
 __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê me deixou morrer!\n
""")
    print("Oh não! {} ficou muito doente e não resistiu. :(".format(t.RetornarNome()))
elif t.RetornarFome() >= 100:
    print("""\n------------------------------------------\n 
 __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê me deixou morrer!\n
""")
    print("Oh não! {} morreu de fome. :(".format(t.RetornarNome()))