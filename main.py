list = ["CadenaCaracteres","second"]
word = list[0]
word= word[1:]
word2 = word[0:len(word)-1]
list[0] = word
print(word2)


"""
#-----------------------------------Modulo comparación de palabras y combinaciones posibles
list = ['abc','aba','acc','aca','bbc','bba','bcc','bca']
list_word = ['abc','bca','dac','dbc','cba']

count = 0
for x in list:
    if x in list_word:
        count += 1
print(count)
#fin Modulo comparación de palabras y combinaciones posibles
"""


#----------------------------------------------
"""def recursivo(lista,ini,cant,text):

    index = 0
    print("Lista Ini: " + lista[ini])
    while(index < len(lista[ini])):
        text = text + lista[ini][index]
        ini += 1
        if(ini == len(lista)):
            list_comp.append(text)
        recursivo((lista,ini,cant,text))
        text = ""
        index += 1
#----------------Modulo de prueba para separación de caracteres
txt = "xz(ab)c(de)fg"
txt2= ""
aux_ini = 0
aux_fin=0

for x in range(len(txt)):
    if(txt[x] == ")"):
        aux_fin = x
    if(txt[x] == "("):
        aux_ini = x
    if(aux_fin < aux_ini):
        while (aux_fin < aux_ini ):
            txt2 = txt2 + txt[aux_fin] + " "
            aux_fin += 1
    else:
        while(aux_ini < aux_fin):
            txt2 = txt2 + txt[aux_ini]
            aux_ini += 1
        txt2 = txt2 + " "

if(txt[len(txt)-1] != ")"):
    while(aux_fin < len(txt)):
        txt2 = txt2 + txt[aux_fin] + " "
        aux_fin += 1
txt2 = txt2.replace("(","")
txt2 = txt2.replace(")","")
word_list = txt2.split(" ")
word_list = [item for item in word_list if item]
#------------------------Fin Modulo de prueba Separación de caracteres

print(word_list)
print("--------------------")
text = ""
global list_comp
#------------------------------------------------------------------------------
recursivo(word_list,0,len(word_list),text)
"""