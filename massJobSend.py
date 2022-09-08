#Thomas Egg
#March 12, 2022
#This code will allow me to send any number of Gaussian jobs to palmetto nodes and will organize these jobs into folders

import os
import random
import numpy as np

#Function to create and run jobs
def create(name, frac, fi, D):
    with open(name+".com", "x") as w:
        w.write("%Mem=500MB")
        w.write("\n#p B3LYP/aug-cc-pVTZ OPT FREQ SCRF(PCM,Read)")
        w.write("\n\n"+name+"_"+str(frac))
        w.write("\n\n0 1\n")
        w.write(fi)
        w.write("\n")
        w.write(D)
        w.write("\n\n\n\n")
        w.close

    with open(name+".sub","x") as wSub:
        wSub.write("#PBS -q skystd")
        wSub.write("\n#PBS -l select=1:ncpus=1:mem=500mb,walltime=12:00:00")
        wSub.write("\n\ncd "+direcName)
        wSub.write("\n\nmodule load gaussian")
        wSub.write("\n\ng16 <"+name+".com"+" >"+name+".out")
        wSub.close()


#Reading in Cartesian coordinates and saving content into variables
waterG = open("WaterGeometry.txt")
methanolG = open("MethanolGeometry.txt")
ethanolG = open("EthanolGeometry.txt")

waterS = ""
methanolS = ""
ethanolS = ""

for line in waterG:
    waterS = waterS+line

waterG.close()

for line in methanolG:
    methanolS = methanolS+line

methanolG.close()

for line in ethanolG:
    ethanolS = ethanolS+line

ethanolG.close()

x = open('Concentrations.csv','r')
data = np.loadtxt(x,delimiter=',')
x.close()

#Saving in dielectric constants and taking user input for number of solvent models
epsWater = 78.3553
epsMethanol = 32.613
epsEthanol = 24.852

print('How many solvent models are necessary?')
num = input()

#This loop will execute three jobs per dielectric constant
for i in range(int(num)):
    molFracWater = data[i+800][0]
    molFracMethanol = data[i+800][1]
    molFracEthanol = data[i+800][2]
    finConst = (epsWater*molFracWater)+(epsMethanol*molFracMethanol)+(epsEthanol*molFracEthanol)

    toAdd = "Dielec_"+str(i+801)
    diC = "Eps="+str(finConst)

    direcName = "/home/thomasegg/AlcoholMixtureSpec/"+toAdd
    os.makedirs(toAdd)
    os.chdir(toAdd) 

    create("Water", molFracWater, waterS, diC)
    create("Methanol", molFracMethanol, methanolS, diC)
    create("Ethanol", molFracEthanol, ethanolS, diC)

    os.system("qsub Water.sub")
    os.system("qsub Methanol.sub")
    os.system("qsub Ethanol.sub")

    os.chdir("/home/thomasegg/AlcoholMixtureSpec/")

print("\nAll jobs have been submitted to Palmetto")
print(num+" jobs were created and run")
