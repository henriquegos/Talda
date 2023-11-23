# Imports
from math import sqrt
import pandas as pd
from scipy.interpolate import RegularGridInterpolator as RGI
import numpy as np
import matplotlib.pyplot as plt


class vpd:


    

    def __init__(self, Humidade, Temperatura, Fase):
        self.Humidade = Humidade
        self.Temperatura = Temperatura
        self.Fase = Fase




    def calcula_vpd(self):

        # Eixo X (Humidade)
        HumidadeDados = np.arange(35,96,5)

        # Data
        data = pd.read_excel("C:/Users/henriquegos/Desktop/VPDTABLEPASTA/VPDTABLE.xlsx")

        # Limpeza do DataFrame
        data = data.iloc[3:24,0:14]
        data.columns = ["Temperatura\Humidade","35%","40%","45%","50%","55%","60%","65%","70%","75%","80%","85%","90%","95%"]

        # Tranformando os valores de VPD em vetores
        VPD = data.iloc[1:21,1:14].to_numpy()

        # Preparação Eixo Y (Temperatura) e Eixo Z (VPD)
        TemperaturaDados = np.arange(15,36,1)

        diffs = 21
        i_temp = 0

        # Eixo Y (Temperatura) e Eixo Z (VPD)
        for i, temp in enumerate(TemperaturaDados):
                                
            
            diffscalc = sqrt((self.Temperatura-temp)**2)                  
            if diffscalc < diffs:
                diffs = diffscalc
                i_temp = i
                

        if i_temp-6<0:
            
            TemperaturaDados = TemperaturaDados[0:13]
            VPD = VPD[0:13]
            
        elif i_temp+6>19:
            
            TemperaturaDados = TemperaturaDados[8:21]
            VPD = VPD[7:20]
            
        else:
            
            TemperaturaDados = TemperaturaDados[i_temp-6:i_temp+7]
            VPD = VPD[i_temp-6:i_temp+7]

        

        #Realizando a interpolação e salvando em variável
        f = RGI((HumidadeDados, TemperaturaDados), VPD, method = "linear", fill_value = -1)

        valor_vpd_calculado = f((self.Humidade,self.Temperatura))

        return valor_vpd_calculado





    
    def print_vpd(self):

        if self.Fase == "vegetativo" or self.Fase == "vega":
    
            if self.calcula_vpd() < 0.6:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa. Há risco de haver fungo e doenças em sua planta =(".format(self.calcula_vpd()))
                
            elif self.calcula_vpd() < 1.1:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa.\nO que é saudável para sua planta! Ela está transpirando e crescendo bem nessa Vega!! =)".format(self.calcula_vpd()))
            
            elif self.calcula_vpd() < 1.8:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa.\nO que não é saudável para sua planta: ela está transpirando e crescendo mal nessa Vega!! =(".format(self.calcula_vpd()))
            
            else:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa.\nSua planta e está sobre alto stress e correndo perigo =(".format(self.calcula_vpd()))
                
        elif self.Fase == "floração" or self.Fase == "flora" or self.Fase == "floracao" or self.Fase == "floraçao" or self.Fase == "floracão":
            
            if self.calcula_vpd() < 0.6:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa.\nHá risco de haver fungo e doenças em sua planta =(".format(self.calcula_vpd()))
            
            elif self.calcula_vpd() < 1.1:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa.\nO que não é saudável para sua planta: ela está transpirando e crescendo mal nessa Flora!! =(".format(self.calcula_vpd()))
            
            elif self.calcula_vpd() < 1.8:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa.\nO que é saudável para sua planta: ela está transpirando e crescendo bem nessa Flora!! =)".format(self.calcula_vpd()))
        
            else:
                print("Valor de Déficit de pressão de vapor igual a {:.2f} kPa.\nSua planta e está sobre alto stress e correndo perigo =(".format(self.calcula_vpd()))

        else:

            print("Você não digitou uma fase válida para sua planta =(")






    def vizualizer_inter(self):

        # Eixo X (Humidade)
        HumidadeDados = np.arange(35,96,5)

        # Data
        data = pd.read_excel("C:/Users/henriquegos/Desktop/VPDTABLEPASTA/VPDTABLE.xlsx")

        # Limpeza do DataFrame
        data = data.iloc[3:24,0:14]
        data.columns = ["Temperatura\Humidade","35%","40%","45%","50%","55%","60%","65%","70%","75%","80%","85%","90%","95%"]

        # Tranformando os valores de VPD em vetores
        VPD = data.iloc[1:21,1:14].to_numpy()

        # Preparação Eixo Y (Temperatura) e Eixo Z (VPD)
        TemperaturaDados = np.arange(15,36,1)

        diffs = 21
        i_temp = 0


        # Eixo Y (Temperatura) e Eixo Z (VPD)
        for i, temp in enumerate(TemperaturaDados):
                                
            
            diffscalc = sqrt((self.Temperatura-temp)**2)                  
            if diffscalc < diffs:
                diffs = diffscalc
                i_temp = i
                

        if i_temp-6<0:
            
            TemperaturaDados = TemperaturaDados[0:13]
            VPD = VPD[0:13]
            
        elif i_temp+6>19:
            
            TemperaturaDados = TemperaturaDados[8:21]
            VPD = VPD[7:20]
            
        else:
            
            TemperaturaDados = TemperaturaDados[i_temp-6:i_temp+7]
            VPD = VPD[i_temp-6:i_temp+7]

        

        interpol = []
        #Realizando a interpolação e salvando em variável
        f = RGI((HumidadeDados, TemperaturaDados), VPD, method = "linear", fill_value = -1)

        for index, humid in enumerate(HumidadeDados):

            for index, humid in enumerate(HumidadeDados):
                interpol.append(f((HumidadeDados[index], TemperaturaDados)))

        #Transformando os valores de VPD de strings em float
        for index, vetor in enumerate(VPD):
            for index_vpd, vpd in enumerate(vetor):
                vetor[index_vpd] = float(vpd)

        #Iniciando figura
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")

        #Plotando os dados coletados
        ax.plot_wireframe(HumidadeDados, TemperaturaDados, VPD, rstride=5, cstride=1, color="k", label="Dados", alpha=1)

        #Plotando interpolação realizada
        ax.plot_wireframe(HumidadeDados,TemperaturaDados, np.array(interpol), color="pink", alpha=0.4, rstride=1, cstride=1, label="Interpolação")

        #Plotando VPD desejado
        ax.scatter(self.Humidade, self.Temperatura, self.calcula_vpd(), color="g", s=80, label="Ponto interpolado")

        #Configurando plot
        plt.style.use('seaborn-v0_8')
        plt.xlabel("Humidade [%]")
        plt.ylabel("Temperatura [°C]")
        ax.set_zlabel("Déficit de Pressão de Vapor [kPa]", labelpad=-14)
        ax.view_init(20,-50) #angulação da vista
        plt.legend(loc="best")
        plt.show()