go = int(input())
for x in range(go):
    raj, she = map(str, input().split())
    if raj == she:
        print('empate')
    else:
        if raj == "tesoura" and she == 'papel':
            print('rajesh')
        else:
            if raj == "papel" and she == "pedra":
                print('rajesh')
            else:
                if raj == "pedra" and she == "lagarto":
                    print('rajesh')
                else:
                    if raj == "lagarto" and she == "spock":
                        print('rajesh')
                    else:
                        if raj == "spock" and she == "tesoura":
                            print('rajesh')
                        else:
                            if raj == "tesoura" and she == "lagarto":
                                print('rajesh')
                            else:
                                if raj == "lagarto" and she == "papel":
                                    print('rajesh')
                                else:
                                    if raj == "papel" and she == "spock":
                                        print('rajesh')
                                    else:
                                        if raj == "spock" and she == "pedra":
                                            print('rajesh')
                                        else:
                                            if raj == "pedra" and she == "tesoura":
                                                print('rajesh')
                                            else:
                                                print("sheldon")
#0.012 / 27.05.2021 / 1
