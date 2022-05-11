from Candidato import Candidato

#  | Lembrando que esse e meu primeiro contato com o Python , fiz esse codigo com muita pesquisa e os estudos
#  | da pagina da faculdade e tambem com a ajuda de alguns amigos q ja manjam e ate mesmo amigos da faculdade.
#  | confesso que o codigo tem alguns erros , mais procurei deselvolver todos os topicos pedido no PDF que foi
#  | mandado ...     :)


# | Vou começar criando cada candidato para PREFEITO |

primeiroPrefeito = Candidato ('Junin do Grau', 10, 'Prefeito', 40, 'PL')
segundoPrefeito = Candidato ('Claytin do Bar', 11, 'Prefeito', 40, 'PT')
terceiroPrefeito = Candidato ('Fernanda da vila', 12, 'Prefeita',50, 'PSDB')

#  | Agora vou criar os candidatos para VEREADOR |

primeiroVereador = Candidato ('Ana do Bolo', 11111, 'Vereadora', 30, 'PL')
segundoVereador = Candidato ('Anderson Motos', 22222, 'Vereador', 30, 'PL')
terceiroVereador = Candidato ('Ze da farmacia', 33333, 'Vereador', 30, 'PL')
quartoVereador = Candidato ('Julia da saude', 44444, ' Vereadora', 50, 'PSDB')
quintoVereador = Candidato ('Antonio Preto', 55555, 'Vereador', 40, 'PSDB')
sextoVereador = Candidato ('Sandra Veiculos', 66666, 'Vereadora', 30, 'PT')
setimoVereador = Candidato ('Jo Cabelo', 77777, 'Vereador', 40, 'PT')
oitavoVereador = Candidato ('Jessica Tatto', 88888, 'Vereadora', 40, 'PT')
nonoVereador = Candidato ('Maria Tunes', 99999, 'Vereadora', 30, 'PSDB')
dezVereador = Candidato ('Ze da Eva', 00000, 'Vereador', 70, 'PSOL')

#  | Vou criar uma lista abaixo para Prefeito e Vereador |
#  | Para poder imprimir depois no final da votação ou ate mesmo na zeresima |

candidatosPrefeito = []                                        # Lista Prefeito
candidatosPrefeito.append(primeiroPrefeito)
candidatosPrefeito.append(segundoPrefeito)
candidatosPrefeito.append(terceiroPrefeito)

candidatosVereador = []                                         # Lista vereador
candidatosVereador.append(primeiroVereador)
candidatosVereador.append(segundoVereador)
candidatosVereador.append(terceiroVereador)
candidatosVereador.append(quartoVereador)
candidatosVereador.append(quintoVereador)
candidatosVereador.append(sextoVereador)
candidatosVereador.append(setimoVereador)
candidatosVereador.append(oitavoVereador)
candidatosVereador.append(nonoVereador)
candidatosVereador.append(dezVereador)

votoNulo = 0
boraUrna = True;

while boraUrna:                            # Vou iniciar um while para o MENU DO URNA

    print("--------------------------MENU DA URNA---------------------------------------")
    print("              IMPRIMIR ZERÉZIMA OU INICIAR VOTAÇÃO ?                         ")
    print("-----------------------------------------------------------------------------")
    EscolhaMenu = input("Digite v para iniciar votação, ou qualquer outra letra para sair e imprimir a zerésima: \n")

    if EscolhaMenu == 'v':
         inicioVotacao = True
         while inicioVotacao:

            print('======================= ESCOLHA SEU CANDIDATO =============================')
            voto = int(input("Digite um numero valido para seu candidato, 2 digitos para PREFEITO e 5 para VEREADOR: \n"))

            verificaExistencia = False
            lista = []
            if voto >= 99:
                lista = candidatosVereador
            else:
                lista = candidatosPrefeito

            for candidato in lista:

                if candidato.getNumero() == voto:
                    verificaExistencia = True
                    print("Você escolheu o candidato(a): "
                          + candidato.getNome()
                          + " para o cargo : "
                          + candidato.getCargo()
                          + ", numero : ", candidato.getNumero(), ", do partido : " + candidato.getPartido() + " \n")

                    print('================== CONFIRME AGORA SEU VOTO : =====================')
                    confirmar = input("Voce quer confirmar o seu voto ? Digite a letra s (SIM) para sim n (NAO) para não:  \n")

                    if confirmar == "s":
                        candidato.setVotos(candidato.getVotos() + 1)
                        print('========================= V O T O ===========================')
                        print("VOCE VOTOU : " + candidato.getNome() + " ELE TEM : ", candidato.getVotos(),", BOA SORTE... \n")

                        # AGORA AQUI E A CONTINUAÇÃO DA VOTAÇÃO ( SE DESEJA OU NAO CONTINUAR )
                        print('==================== QUER CONTINUAR A VOTAÇÃO ? ======================')
                        continua = input("CONTINUAR A VOTAÇÃO ? Digite s (SIM) para sim ou qualquer outra letra para não:  \n")

                        if continua == "s":
                            inicioVotacao = True
                        else:
                            print('>>>>>>>>>>>>>>>>> ENCERRANDO A VOTAÇÃO <<<<<<<<<<<<<<<<<<')
                            inicioVotacao = False
                            boraUrna = False

                    else:
                        print("ESCOLHA NOVAMENTE \n")

            if verificaExistencia == False:
                print('______________________________ VOTO NULO __________________________')
                confirmar = input('CANDIDATO NAO EXISTE, deseja votar em Nulo? Digite a letra s (SIM) ou qualquer outra para não:')
                if confirmar == "s":
                    votoNulo += 1
                    print('---------------------- VOTO NULO ESTA CONFIRMADO ---------------------')
                    print("Até agora ", votoNulo, " votaram Nulo.  \n")
                    print('------------------------- VOCE QUER CONTINUAR ? --------------------------')
                    continua = input("Deseja continuar ? Digite s (SIM) ou qualquer outra letra para não:  \n")
                    if confirmar == "s":
                        inicioVotacao = True
                    else:
                        print("_________________ ENCERRANDO A VOTAÇÃO __________________")
                        inicioVotacao = False
                        boraUrna = False

else:
        inicioVotacao = False

        print("---------------- IMPRIMINDO ZERESIMA -----------------")
        candidatosPrefeito.sort(key=lambda x: x.votos, reverse=True)
        candidatosVereador.sort(key=lambda x: x.votos, reverse=True)

        print("__________________ LISTA DE PREFETOS __________________")
        for candidato in candidatosPrefeito:
            candidato.toString()

        print()

        print("_____________PREFEITO ELEITO____________")
        if (candidatosPrefeito[0].votos == candidatosPrefeito[1].votos):
            print("Eleição para prefeito terá segundo turno, dois ou mais candidatos tiveram :",
                  candidatosPrefeito[0].votos,
                  " votos  \n")
        else:
            print("Prefeito é : " + candidatosPrefeito[0].nome + " com: ", candidatosPrefeito[0].votos, "\n")

        print("_________________LISTA VEREADORES_________________")
        for candidato in candidatosVereador:
            candidato.toString()

        print()

        print("--------------- VEREADORES ELEITOS -----------------")
        if candidatosVereador[0].votos > 0: print("PRIMEIRO : " + candidatosVereador[0].nome + " COM: ",
                                                  candidatosVereador[0].votos, " VOTOS")
        if candidatosVereador[1].votos > 0: print("SEGUNDO : " + candidatosVereador[1].nome + " COM: ",
                                                  candidatosVereador[1].votos, " VOTOS")
        if candidatosVereador[2].votos > 0: print("TERCEIRO : " + candidatosVereador[2].nome + " COM: ",
                                                               candidatosVereador[2].votos, " VOTOS")

        print()

        print("============ VOTOS NULOS ===============")
        print("VOTOS NULOS: ", votoNulo, "\n")

        print("============= VOTAÇÃO ENCERRADA  ==================")
        print(">>>>>>>>>>>>>>>> BOA SORTE... <<<<<<<<<<<<<<<<<<<")





















