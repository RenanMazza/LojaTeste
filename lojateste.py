# ate 9 = 0%
# 10 a 99 = 5%
# 100 a 999 10%
# 1000 15%

def formatCurrency(valueUnformated) :
    thousands_separator = "."
    fractional_separator = ","
    strValue = str(valueUnformated) + ".00"

    if thousands_separator == ".":
        main_currency, fractional_currency = strValue.split(".")[0], \
                                             strValue.split(".")[1]
        new_main_currency = main_currency.replace(",", ".")
        currency = new_main_currency + fractional_separator + fractional_currency

    return "R$ " + currency


while True:

    print("------------------------------------------------")
    print("BEM VINDO A LOJA DO RENAN")
    print("------------------------------------------------")

    #Input valor do produto
    valorProduto = float(input("Qual o valor do produto? ").replace(",", "."))

    # Input Quantidade
    quantidadeProduto = int(input("Qual o quantidade comprada? "))

    # Verifica desconto de acordo com a quantidade
    desconto = 0
    if quantidadeProduto >= 10:
        if 10 <= quantidadeProduto < 100:
            desconto = 0.05
        elif 100 <= quantidadeProduto < 1000:
            desconto = 0.10
        else:
            desconto = 0.15

    # verifica valor sem desconto
    valorSemDesconto = int(valorProduto) * int(quantidadeProduto)

    # verifica valor com desconto
    valorComDesconto = valorSemDesconto - (valorSemDesconto * desconto)

    print("Valor total sem desconto: R$ {0:.2f}".format(valorSemDesconto))
    print("Valor total com desconto: R$ {0:.2f} (desconto {1:g}%)".format(valorComDesconto, desconto*100))

