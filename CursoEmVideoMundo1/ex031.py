"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
Km para viagens até 200Km e R$0,45 para viagens mais longas.

"""
distância = float(input("Informe a distância da viagem: "))
if distância <= 200:
    print("Para viagens até 200km é cobrado R$0,50 por KM"
          "Nese caso você vai precisar percorrer {}Km, então a passagem vai custar R${:.2f}".format(distância, distância*0.5))
else:
    print("Para viagens acima 200km é cobrado R$0,45 por KM"
          "Nese caso você vai precisar percorrer {}Km, então a passagem vai custar R${:.2f}".format(distância, distância*0.45))
