def cria_conta():
    conta = { "numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta ["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))