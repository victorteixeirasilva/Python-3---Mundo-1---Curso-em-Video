"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela
abaixo:

- Abaixo de 18.5: Abaixo do Peso.
- Entre 18.5 e 25: Peso Ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade Mórbida

"""
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Exemplo de uso
peso = float(input("Informe o seu peso: ")) # em kg
altura = float(input("Informe sua altura: "))  # em metros

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"Seu IMC é {imc:.2f}, o que indica: {classificacao}")