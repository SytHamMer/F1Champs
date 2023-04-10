import numpy as np
import json
import matplotlib.pyplot as plt
def birth_date(file):
    res=[]
    with open(file,'r') as json_file:
        data = json.load(json_file)  
    for i in data:
        res.append(i['birthdate'])
    return res

def month_list(tab):
    res =[]
    for i in tab:
        res.append(int(i[5:-3]))
    month, frequency = np.unique(res,return_counts=True)
    return (month,frequency) 
     

def year_list(tab):
    res =[]
    for i in tab:
        res.append(int(i[:4]))
    year, frequency = np.unique(res,return_counts=True)
    return (year,frequency)   

def day_list(tab):
    res =[]
    for i in tab:
        res.append(int(i[-2:]))
    day, frequency = np.unique(res,return_counts=True)
    return (day,frequency) 



def show_hist2d(y,m,d):
    plt.figure()
    plt.subplot(1,3,1)
    plt.hist2d(y[0],y[1],cmap='Blues',bins=73)
    plt.xlabel("Année de naissance")
    plt.ylabel("Nombre de champions")
    plt.colorbar()
    plt.subplot(1,3,2)
    plt.hist2d(m[0],m[1],cmap='Reds',bins=12)
    plt.xlabel("Mois de naissance")
    plt.ylabel("Nombre de champions")
    plt.colorbar()
    plt.subplot(1,3,3)
    plt.hist2d(d[0],d[1],cmap='Greens',bins=31)
    plt.xlabel("Jours de naissance")
    plt.ylabel("Nombre de champions")
    plt.colorbar()
    plt.show()
    

if __name__ == "__main__":
    year = year_list(birth_date('spiders//data_clean.json'))
    month =month_list(birth_date('spiders//data_clean.json'))
    day = day_list(birth_date('spiders//data_clean.json'))
    show_hist2d(year,month,day)
