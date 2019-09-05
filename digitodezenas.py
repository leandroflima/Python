inteirostr = input("Digite um número inteiro: ")

inteiro = int(inteirostr)

inteiroDivididoPorDez = inteiro // 10

inteiroDivididoPorCemVezesCem = (inteiro // 100)

inteiroDivididoPorCemVezesCem = inteiroDivididoPorCemVezesCem * 10

digitodezenas = inteiroDivididoPorDez - inteiroDivididoPorCemVezesCem

print("O dígito das dezenas é", digitodezenas)
