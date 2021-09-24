"""
Prueba Técnica para Consorcio
Autor: Felipe Cárdenas
Condición del programa: No finalizado. Separado por modulos validados en archivo "main.py"
"""

def recursivo(lista,ini,cant,text): #Metodo recursivo para obtener las posibles combinaciones.

    index = 0
    while(index < len(lista[ini])): #recorre cada uno de los caracteres de los elementos de la lista
        text = text + lista[ini][index]
        ini += 1
        if(ini == len(lista)): #condición que termina la recursividad, al llegar al final de la lista
            list_comp.append(text)  #Se encuentra declarada una lista global, que almacena las posibles combinaciones para cada patrón dado.
        else:
            recursivo((lista,ini,cant,text)) #Llamada recursiva, Se utilizan ini para obtener cada palabra segun el indice hasta llegar al final.
        text = text[0:len(text)-1] #antes de cambiar de indice para continuar con la siguiente posibilidad, se elimina el caracter usado, para que no figure en el siguiente caso.
        index += 1
"""
Acerca del Modulo anterior:
El modulo presenta problemas de ejecución, por lo que no se ha probado correctamente para validar su lógica.
En este caso, es el que mayor complejidad ha presentado.

Para el ejemplo (ab)c(de)(fg)
posibles combianciones:
acdf  [0,0,0,0]
acdg  [0,0,0,1]
acef  [0,0,1,0]
aceg  [0,0,1,1]
bcdf  [1,0,0,0]
bcdg  [1,0,0,1]
bcef  [1,0,1,0]
bceg  [1,0,1,1]

"""


def extract_split(txt): #Modulo que, desde un patrón entregado, separa los caracteres según formato. Obteniendo de resultado una lista ordenada.
    #Esta lista ordenada, será utilizada en el metodo recursivo.
    txt2 = ""
    aux_ini = 0
    aux_fin = 0
    #variables que se utilizan para demarcar donde se encuentran las separaciones por "(" y ")". Ayudarán según el caso a determinar el tratamiento.
    for x in range(len(txt)): #indice que recorre todos los caracteres del patron recibido.
        if (txt[x] == ")"):
            aux_fin = x
        if (txt[x] == "("):
            aux_ini = x
        if (aux_fin < aux_ini):#condición para recorrer las palabras que mantendrán su lugar (ab)ce(fg)   en este caso, ce
            while (aux_fin < aux_ini):
                txt2 = txt2 + txt[aux_fin] + " "
                aux_fin += 1
        else:
            while (aux_ini < aux_fin):
                txt2 = txt2 + txt[aux_ini]
                aux_ini += 1
            txt2 = txt2 + " "

    if (txt[len(txt) - 1] != ")"):
        while (aux_fin < len(txt)):
            txt2 = txt2 + txt[aux_fin] + " "
            aux_fin += 1
    txt2 = txt2.replace("(", "")
    txt2 = txt2.replace(")", "")
    word_list = txt2.split(" ")
    word_list = [item for item in word_list if item]
    return word_list
    #para ab(cd)e(fg)hi   retorna   [a,b,cd,e,fg,hi]


def menu():
    print("1.- Ingresar Configuración")
    print("2.- Ingresar Palabras")
    print("3.- Ingresar patrones")
    print("4.- Ejecutar programa")
    print("5.- Salir") #por tiempo, no se logró implementar. Posteriormente se enviará una versión con menu implementado, de ser necesario.


print("Buenos Días")


while(True): #Validador de formato, solo saldra al presentar un formato correspondiente para el caso. Solo permitira 3 numeros y separados por espacios
    print("Valores de Entrada:")
    entry = input()
    entry_split = entry.split()
    bol = True
    for x in range(len(entry_split)):
        try:
            int(entry_split[x])
        except ValueError:
            bol=False
    if (len(entry_split)==3 and bol == True):
        break
    else:
        print("Debe ingresar 3 números separados por un espacio")

list_words = []

for x in range(int(entry_split[1])):
    while(True):#validador de formato, solo dejará seguir en caso que las palabras ingresadas sean del mismo largo que el presentado en los primero valores correspodnientes
        print("Ingresar palabra " + str(x + 1) + ":")

        words = input()
        if(len(words) != int(entry_split[0])):
            print("Debe Ingresar una palabra de largo: " + entry_split[0])
        else:
            list_words.append(words)
            print("Ingresado Correctamente: "+list_words[x])
            break

list_pattern = []
print("---------------------------------------------")
for x in range(int(entry_split[2])): #for que permite ingresar los patrones solicitados
    print("Ingresar patrón " + str(x+1) + ":")
    list_pattern.append(input())
    print("Ingresado Correctamente: "+list_pattern[x])

print("---------------------------------------------")
for x in range(int(entry_split[2])): #for que permite recorrer todos los patrones ingresados

    wp_split = extract_split(list_pattern[x])
    print(wp_split)
    global list_comp
    list_comp = []
    text = ""
    recursivo(wp_split, 0, len(wp_split), text) #llamado al metodo recursivo, para obtener las posibles combinaciones. Metodo no terminado.

    #Supuesto: Al terminar el metodo recursivo, la lista list_comp debería de contener todas las posibles combinaciones para cada caso, y se resetearía antes de
    #volver a llenarse

    count = 0
    for y in list: #Modulo para comparar los registros obtenidos de las combinatorias posibles del patron, con respecto a las palabras ingresadas.
        if y in list_comp:
            count += 1
    print("Case #" + x +":" + str(count))









