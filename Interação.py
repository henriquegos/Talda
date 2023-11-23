from vpd import vpd

#Inputs necessários
Humidade = float(input("Qual a humidade do seu grow? Digite um valor entre 35 e 95: "))
Temperatura = float(input("Qual a temperatura do seu grow? Digite um valor entre 15 e 35: "))
Fase = input("Qual o status do seu cultivo? Vegetativo ou Floração? ").lower()

instancia_vpd = vpd(Humidade, Temperatura, Fase)
# vpd_calc = instancia_vpd.calcula_vpd()

instancia_vpd.print_vpd()