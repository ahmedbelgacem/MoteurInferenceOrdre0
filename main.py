import  re

#---Read lines from BF---
file_BFMETEO = r"BFMETEOROLOGIES.txt"
file_BRMETEO = r"BRMETEOROLOGIES.txt"
file_BFMALADIE = r"BFMALADIES.txt"
file_BRMALADIE = r"BRMALADIES.txt"
file_BFVILLE =  r"BFVILLES.txt"
file_BRVILLE = r"BRVILLES.txt"
def createBF(file):
    with open(file,"r") as x:
        data=x.readlines()
        units = [line[:-1] for line in data]
        bf = {}
        for element in units:
            l = re.split(" = ", element)
            try:
                int(l[1])
                bf[l[0]] = int(l[1])
            except:
                if l[1] == "Vrai":
                    bf[l[0]] = True
                elif l[1] == "Faux":
                    bf[l[0]] = False
                else:
                    bf[l[0]] = l[1][1:-1]
        return bf

def createBR(file):
    with open(file, "r") as x:
        data=x.readlines()
        rule = [line[:-1] for line in data]
        br_unsplited=[]
        br=[]
        for element in rule:
            l = re.split(" alors ",element)
            br_unsplited.append(l)
        # return br_unsplited
        for element in br_unsplited:
            premisse=element[0][3:]
            l = re.split(" & ",premisse)
            element[0]=l
            br.append(element)

        #________
        brFormatted = []
        for element in br:
            conditions = []
            for conditionUnsplitted in element[0]:
                conditionSplitted = conditionUnsplitted.split(" ", 2)
                if conditionSplitted[2] == 'Vrai':
                    conditionSplitted[2]=True
                conditions.append([conditionSplitted[0],(conditionSplitted[1], conditionSplitted[2])])
            brFormatted.append([conditions, element[1]])

        return brFormatted

def match(regle,baseFait):
    test = True
    for element in regle[0]:
        entite= element[0]
        value= element[1][1]
        operateur= element[1][0]
        if entite in baseFait.keys():
            currentvalue=baseFait[entite]
            if(operateur=='<'):
                test= test and (currentvalue < int(value))
            elif (operateur == '>'):
                test = test and (currentvalue > int(value))
            elif (operateur == '=='):
                test = test and (currentvalue == value)
            elif (operateur == '<='):
                test = test and (currentvalue <= int(value))
            elif (operateur == '>='):
                test = test and (currentvalue >= int(value))
        else :
            test = False
    return test


def satBF (baseFait, baseRegle):
    changement = True
    fichier = open("logs.txt", "a")
    fichier.write("\nTraceur")
    fichier.write("\n-------------------------------------\n")
    while changement:
        changement = False
        for regle in baseRegle:
            if match(regle,baseFait):
                l = re.split(" = ", regle[1])
                try:
                    int(l[1])
                    baseFait[l[0]] = int(l[1])
                except:
                    if l[1] == "Vrai":
                        baseFait[l[0]] = True
                    elif l[1] == "Faux":
                        baseFait[l[0]] = False
                    else:
                        baseFait[l[0]] = l[1][1:-1]
                fichier.write(str(regle))
                baseRegle.remove(regle)
                changement = True
    fichier.close()
    return baseFait,baseRegle






