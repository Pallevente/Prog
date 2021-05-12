import sys
import matplotlib.pyplot as plt
import numpy as np
def szamba(asd):
    newasd=[]
    for i in asd:
        newasd.append(int(i))
    return newasd

try:
    bekert=input("Adjon meg egy évszámot(2005 és 2015 között) és egy számot(20-ig) szóközzel elválasztva:")
    bekertdarabol=bekert.split(" ")
    if bekertdarabol[0].isdigit()==False or bekertdarabol[1].isdigit()==False:
        print("Csak számokat tartalmazhat.")
    else:
        ev=int(bekertdarabol[0])
        m = int(bekertdarabol[1])
        if ev<2005 or ev>2015:
            print("Csak 2005 és 2015 között adjon meg évszámot.")
        elif m>20:
            print("Csak 20 megye van.")
        else:
            f=open(sys.argv[1],"r")
            elsosor = f.readline()
            print(elsosor)
            d_elsosor=elsosor.split(",")
            oszlopszam=len(d_elsosor)

            sorokszama=0

            for i in f:
                i_d=i.split(",")
                ev_d=i_d[0].split("/")
                if int(ev_d[2])==ev:
                    sorokszama+=1
            sorokszama+=1
            print(sorokszama)

            f.seek(0)
            matrix=np.empty((sorokszama,oszlopszam), dtype=object)

            elsosor2 = f.readline()
            print(elsosor2)
            d_elsosor2 = elsosor2.split(",")
            oszlopszam2 = len(d_elsosor2)

            x=0
            for i in range(oszlopszam2):
                matrix[x,i]=d_elsosor2[i]

            print(ev)
            print(f)

            x=1
            for i in f:
                i=i.strip()
                i_d=i.split(",")
                ev_d=i_d[0].split("/")
                if int(ev_d[2])==ev:
                    for j in range(len(i_d)):
                        matrix[x,j]=i_d[j]
                    x+=1

            print(matrix)

            atlag=[]
            for i in range(oszlopszam):
                sum=0
                for j in range(sorokszama):
                    if i>0 and j>0:
                        sum+= int(matrix[j,i])
                atlag2=sum/(sorokszama-1)
                if i>0:
                    atlag.append((matrix[0,i],atlag2))

            atlag.sort(key=lambda k:k[1], reverse=True)
            atlag=atlag[:m]
            print()
            print(atlag)

            dict={}
            for i in range(m):
                dict["d"+str(i)]=[]
            print(dict)
            for i in range(m):
                for oszlop in range(oszlopszam):
                    for sorok in range(sorokszama):
                        if oszlop>0 and sorok>0:
                            if matrix[0,oszlop]==atlag[i][0]:
                                dict["d"+str(i)].append(matrix[sorok,oszlop])

            print()
            print(dict)
            print()

            matrix2=[]
            for i in range(len(dict["d0"])):
                matrix2.append(i)
            szin=["b","g","r","c","m","y","k","magenta","orchid","darkgreen","lime","bisque","papayawhip","darkkhaki","khaki","olivedrab","pink","chocolate","sandybrown","peru"]
            for i in range(m):
                plt.plot(matrix2,szamba(dict["d"+str(i)]),color=szin[i],label=atlag[i][0])
                plt.legend()
            plt.show()
            f.close()


except FileNotFoundError:
    print("A fájl nem található.")
except IndexError:
    print("Csak 2005 és 2015 között adjon meg évet és maximum 20 megyét.")