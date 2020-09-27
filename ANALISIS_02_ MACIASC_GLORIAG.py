#CODE_ANALISIS_02
import csv #Importacion de mi archivo csv
lista_general=[] #creo una lista vacia de mis datos en genral
with open('synergy_logistics_database.csv', 'r') as archivo_csv:  #Abriendo mi archivo csv en modo lectura
    reader= csv.reader(archivo_csv) #con reader estoy nombrando el lector por el que se leera el archivo csv
    
    for linea in reader: #lectura del archivo linea por linea
                lista_general.append(linea) #a la lista vacia le agrego los datos
                #print(linea) #impresion de la lista
#print(lista_general[0])
def bienvenida(mensaje='\nBienvenido a Synergy Logistics:\n'): #definiendo mi funcion de bienvenida en el menu
    print ('\nBienvenido a Synergy Logistics:\n') #impprimiendo lo que quiero que diga
bienvenida() #mandando llamar mi funcion
def menu_opciones():#definiendo el menu de opciones
    print('\nMENU DE OPCIONES:\n') #imprimiendo el menu de las opciones disponibles
menu_opciones() #llamando a la funcion de menu de opciones
opcion=int(input('\nELIGE UNA OPCION:\n''\n1.-Rutas de Exportacion:\n''\n2.-Rutas de Importacion:\n''\n3.-Medios de Transporte de Exports:\n''\n4.-Medios de Transporte de Importacion:\n'))
if opcion ==1: #if de la opcion 1
  dict_rexports={'South Korea', 'Vietnam', 497,'Netherlands', 'Belgium', 437,'USA', 'Netherlands', 436, 'China', 'Mexico', 330, 'Japan', 'Brazil', 306, 'Germany', 'France', 299, 'South Korea', 'Japan', 279,'Australia', 'Singapore', 273, 'Canada', 'Mexico', 261,'China', 'Spain', 250} #generando mi diccionario de exports
  print("Las Rutas de exportacion mas comercializadas son:",dict_rexports) #imprimiendo el diccionario de exportaciones
#El anterior diccionario fue generada apartir de la lista de referencia-conteo-rutas es la lista del conteo de exports
elif opcion ==2:#elif para la opcion 2
    dict_rimportaciones={'Singapore destino: Thailand','Germany destino: China', 'China destino: Japan', 
 'Japan destino:Mexico', 'China destino: Thailand', 'Malaysia destino: Thailand','Spain destino: Germany','Mexico destino: USA','China destino: United Arab Emirates','Brazil destino: China'} #generando mi diccionario de importaciones
    print("Las Rutas de importacion mas comercializadas son:\n", dict_rimportaciones) #mandando a imprimir mi diccionario
#El anterior diccionario fue generada apartir de la lista de referencia-"count_rImport" es la lista del conteo de las importaciones

def add_comentarios(): #definiendo mi funcion para agregar algun comentario o sugerencia por parte del ususario
    print('\nSi tienes alguna duda o sugerencia podrias solicitar asesoramiento al numero:000000:\n') #comentarle al usuario que tiene tambien la opcion 3 y4
add_comentarios() #llamando mi funcion de comentarios

if opcion==3: #condicional de opcion 3
    with open("Mediostr_export.txt","r") as archivo: #abriendo mi archivo txt
      Transporte_exports= archivo.read() #lectura de mi archivo txt
      print("Los 3 Medios de transporte mas usados para exportar son:\n",Transporte_exports)
elif opcion==4: #condicional de opcion 4
    with open("Mediost_imp.txt","r") as dict_transporte: #abriendo archivo txt de lista de transporte
        dict_txt= dict_transporte.read() #leyebdo el txt
        print('Los 3 medios de transporte mas utilizados para importar fueron:\n',dict_txt)
else: #si no sucede lo anterior entonces que imprima lo siguiente
    print('\nError de introduccion de opcion: vuelve a intentarlo, gracias:\n') #no hay mas opciones

#GENERACION DE RUTAS ESPORTS
direction ="exportaciones" #Definiendo la variable que me interesa analizar en este caso exp
contador = 0 #Contador uno=0
list_exports=[] #creando lista vacia donde iran las exportaciones en general
rutas_contadas=[] #Creando una lista vacia para contar las rutas en general
conteo_rutas=[]   #Lista vacia para el conteo de rutas totales de exportacion
# lista conteo rutas fue usada de referencia para crear mi lista de las 10 rutas de exports mas comercializadas
for valor in lista_general:  #valor  de mi lista con los  datos en general
    if valor [1]=='Exports': #if donde se indicara el valor  con el index 1 es exactamente igual a direccion
        list_exports.append(valor) #a mi lista vacia le agrego los valores 

for valor in list_exports: #for de la ruta y de mi lista con los  datos en general
    if [valor [2], valor[3]] not in rutas_contadas: #valores donde se encuentran las variables que me interesa analizar e indico donde se contaran las rutas
       rutas_contadas.append([valor [2], valor[3]]) #a mi lista vacia indico los valores que se le agregaran

for ruta in rutas_contadas: #for de rutas y conteo
    contador=0 #contador 2
    for export in list_exports: #for de exportaciones
        if export [2]==ruta[0] and export [3]==ruta[1]: #valor de exports
            contador +=1 #contador 2
    conteo_rutas.append([ruta[0], ruta[1], contador]) #conteo de las rutas exports
conteo_rutas.sort(reverse=True, key= lambda x:x[2]) #ordenando de mayor a menor mi lista con sort.reverse ylamda 

#print ('\nLISTA DE RUTAS DE EXPORTACION MAS UTILIZADAS\n:')
#print(conteo_rutas[0:10]) #Imprimiendo las 10 rutas mas comercializadas para exportar

#GENERACION DE LA LISTA DE RUTAS A IMPORTAR 
direction ="importac" #Definiendo imports
importaciones=[] #creando lista vacia de importaciones
rutas_countimp=[] #Creando una lista vacia para contar las rutas de importacion
count_rImport=[]   #Lista vacia para el conteo de rutas totales
#esta lista de conunt_rImport fue usada como referencia para crear mi lista de las rutas mas comercializadas en importaciones

for valor in lista_general:  #valor  de mi lista con los  datos en general
    if valor [1]=='Imports': #se indica el index 1 es exactamente igual a direccion
       importaciones.append(valor) #a mi lista vacia le agrego los valores 

for valor in importaciones: #for de la ruta y de mi lista con imports generales
    if [valor [2], valor[3]] not in rutas_countimp: #se indico donde se contaran las rutas
       rutas_countimp.append([valor [2], valor[3]]) #a mi lista vacia indico los valores que se le agregaran

for ruta in rutas_countimp: #for de rutas y conteo de importaciones
    contador=0 #contador
    for imports in importaciones: #for de imports
        if imports [2]==ruta[0] and imports [3]==ruta[1]: #valor de imports
            contador +=1 #contador
    
    count_rImport.append([ruta[0], ruta[1], contador]) #conteo de las rutas de imports total
count_rImport.sort(reverse=True, key= lambda x:x[2]) #ordenando de mayor a menor mi lista con sort.reverse ylamda 

#print ('\nLISTA DE RUTAS DE IMPORTACION MAS UTILIZADAS\n:')
#print(count_rImport[0:10]) #Imprimiendo las 10 rutas mas comercalizadas en importaciones


#CONSIGNA 2
 #Medio de transporte utilizado. 
# los datos del archivo csv que ocupe en este caso y genere apartir de mi lista de exports
# incluye:id, register_id,direction,transport_mode,total_value en exports general
## 
transport_Sea=[] #mim lista vacia de transporte por mar
transporte1=["Sea"]#creando lista transporte por mar
transport_Air=[] #lista vacia transport air
transporte2=["Air"] #creando la lista donde estara el total de tranp por air
transport_Rail=[] #creando mi lista vacia de tranp por carretera
transporte3=["Rail"] #lista de datos para transp carriles
transport_Road=[] #lista vacia para tranporte por camino
transporte4=["Road"] 
contador=0 #cantodor uno=0

#TRANSPORTE POR MAR EN EXPORTS
import csv #Importacion de mi archivo csv
lista_exptransp=[] #lista vacia de mi nuevo archivo csv que contiene lsita de exportaciones y sus transportes
 
with open('list_exp.csv', 'r') as archivo: #Abriendo mi archivo csv en modo lectura
   reader= csv.reader(archivo) #con reader estoy nombrando el lector por el que se leera el archivo csv
   
   lista_exptransp.append(linea) #a la lista vacia antes generada especifico los datos agregar 
   for transport in transporte1: #se incluiran datos a la lista transp 1
       for linea in reader: #lectura del archivo por medio de sus fila
           if linea[2]==transport:  #especifico el indice donde se encuentra el tipo de transporte
               contador+=1 #contador que ira sumando y recorriendo la iteracion
               
   transport_Sea.append([transport,contador])  #agregando datos a la lista con el tipo de tranporte que me interesa
   contador=0   #contador =0
#print(transport_Sea) #impresion de mi lista con los transportes por mar en exportaciones
#total_Sea=len(transport_Sea)
#print(total_Sea) #total de veces que se utilizo el transporte por mar en exportaciones

#TRANSPORTE AIR EN EXPORTACIONES
#EN ESTA LISTA BASICAMENTE REPETIRE LOS MISMOS PASOS 
#ANTERIORES PERO AHORA PARA OTRO TIPO DE TRANSPORTE
with open('list_exp.csv','r') as archivo:  #Abriendo mi archivo csv en modo lectura
   reader= csv.reader(archivo) #con reader estoy nombrando el lector por el que se leera el archivo csv
   lista_exptransp.append(linea)
   for transport in transporte2:#Aqui hago la direfencia que ahora me referire al transpote nombrado como 2
       for linea in reader: #lectura del archivo por medio de sus fila
           if linea[2]==transport:  
               contador+=1 #contador 
               
transport_Air.append([transport,contador])#agregando datos a la lista con el tipo de tranporte que me interesa
contador=0 
#print(transport_Air) #imprimiendo mi lista de tranporte por aire en exports

#TRANSPORTE RAIL EN EXPORTACIONES
#EN ESTA LISTA BASICAMENTE REPETIRE LOS MISMOS PASOS ANTERIORES 
#PERO AHORA PARA EL TRANSPORTE POR AIRE
with open('list_exp.csv', 'r') as archivo:  #Abriendo mi archivo csv en modo lectura
   reader= csv.reader(archivo) #con reader estoy nombrando el lector por el que se leera el archivo csv
   lista_exptransp.append(linea) #lista  donde se incluiran los datos
   for transport in transporte3: #se especifica el transport a analizar
       for linea in reader: #lectura del archivo por medio de sus fila
           if linea[2]==transport:  
               contador+=1 #contador de sumatoria
transport_Rail.append([transport,contador])  ##agregando datos a la lista con el tipo de tranporte que me interesa
contador=0 #contador 
#print(transport_Rail) #imprimiendo mi lista de transporte 

#TRANSPORTE ROAD IN EXPORTS
#SIGO REPITIENDO LOS PASOS ANTERIORES
with open('list_exp.csv', 'r') as archivo:  #Abriendo mi archivo csv en modo lectura
   reader= csv.reader(archivo) #con reader estoy nombrando el lector por el que se leera el archivo csv
   lista_exptransp.append(linea) #lista principal creada al principio de estos datos
   for transport in transporte4: #se especifica el transport road
       for linea in reader: #lectura del archivo por medio de sus fila
           if linea[2]==transport:  
               contador+=1 #contador 
transport_Road.append([transport,contador])  #agregando la lista anterio
contador=0
#print(transport_Road) #imprimiendo mi lista de transp road en exports

#TRANSPORTE SEA IN IMPORTS
# EN ESTE CASO HARE MIS LISTAS AHORA PARA LOS TRANSPORTES EN IMPORTACION
# LAS LISTAS LAS CREARE CON UN NUEVO ARCHIVO CSV PERO DE IMPORTS
# EL ARCHIVO CSV EN ESTE CASO INCLUYE: id, register_id,direction,transport_mode,total_value
# todos los datos son por importaciones en general 
 
#Medio de transporte utilizado. 
lista_import=[] #LISTA VACIA QUE CONTENDRA MIS DATOS DE IMPORTS POR TRANPS
Transport_Sea=[] #mim lista vacia de transporte por mar
Transp_sea=["Sea"]#creando lista transporte por mar
Transport_Air=[] #lista vacia transport air
Transp_air=["Air"] #creando la lista donde estara el total de tranp por air
Transport_Rail=[] #creando mi lista vacia de tranp por carretera
Transp_Rail=["Rail"] #lista de datos para transp carriles
Transport_Road=[] #lista vacia para tranporte por camino
Transp_Road=["Road"] 
contador=0 #contador

#TRANSPORTE SEA IN IMPORTS
#SEGUIRE REPIENDO LOS MISMOS PASOS QUE EN LAS EXPORTS
#EN ESTE CASO SE ANALIZARA POR TRANSPORTE EN IMPORTS
import csv #IMPORTANDO MI ARCHIVO CSV DE LAS IMPORTS
with open('list_imp.csv', 'r') as imports:  #Abriendo mi archivo csv en modo lectura
    reader=csv.reader(imports) #con reader estoy nombrando el lector por el que se leera el archivo csv
    
    lista_import.append(linea) #Se agregaran los datos a mi lista vacia creada anterior
    for transporte in Transp_sea: #especificando el transporte por mar
        for linea in reader: #se leera linea por linea 
            if linea[2]==transporte:  #en este indice se encuentra el medio de transporte utilizado 
                    contador+=1 #contador 1
                    
        Transport_Sea.append([transporte,contador])  #agregando la lista anterio
        contador=0 #contador 2
#        print(Transport_Sea) #imprimiendo mim lista de transporte por mar pero en imports

#TRANSPORTE AIR IN IMPORTS
with open('list_imp.csv', 'r') as imports:  #Abriendo mi archivo csv en modo lectura
    reader=csv.reader(imports) #con reader estoy nombrando el lector por el que se leera el archivo csv
    
    lista_import.append(linea) #se agregaran datos a mi lista vacia
    for transporte in Transp_air: #especificando el tranporte que me interesa
        for linea in reader: #lectura linea por linea
            if linea[2]==transporte:  #linea donde estan mis tranportes en list imports
                    contador+=1
                    
        Transport_Air.append([transporte,contador])  #agregando datos a mi lista vacia de transp tot
        contador=0 #regresando el contador
#        print(Transport_Air) #imprimiendo mi lista de transporte

#TRANSPORTE RAIL IN IMPORTS
with open('list_imp.csv', 'r') as imports:  #Abriendo mi archivo csv en modo lectura
    reader=csv.reader(imports) #con reader estoy nombrando el lector por el que se leera el archivo csv
    
    lista_import.append(linea)
    for transporte in Transp_Rail: #ahora se iterara en el transp rail
        for linea in reader:
            if linea[2]==transporte:  #especificando el indice de la lista transporte
                    contador+=1
                    
        Transport_Rail.append([transporte,contador])  #agregando y contando los datos
        contador=0
#        print(Transport_Rail) #imprimiendo lista con el total 

#TRANSPORTE ROAD IN IMPORTS
with open('list_imp.csv', 'r') as imports:  #Abriendo mi archivo csv en modo lectura
    reader=csv.reader(imports) #con reader estoy nombrando el lector por el que se leera el archivo csv
    
    lista_import.append(linea) #vuelvo a referenciar a mi lista vacia 
    for transporte in Transp_Road: #especifico el transp analizar
        for linea in reader: #recorriendo linea por linea el archivo csv
            if linea[2]==transporte:  #indice donde se encuentra lista mode trsp
                    contador+=1 #contador 
                    
        Transport_Road.append([transporte,contador])  #agregando la lista anterio
        contador=0
#        print(Transport_Road) #imprimiendo mi lista de t_road en imports

#valores de mi lista en general principal 
lista_general.pop(0)#Con opor elimino el primer elemento de mi lista de datos
valores=[] #creo uan lilsta vacia para los valores
for ruta in lista_general: #con for especifico la lista de referencia
    valores.append(int(ruta[9])) #incluyo el indice donde se encuentran los datos
#    print(sum(valores)) #sumo los valores
    
#CONSIGNA 3
#GENERACION DE VALORES EN EXPORTS
Origen="Exportacion" #Definiendo la variable que me interesa analizar en este caso exp
contador = 0 #Contador uno=0
paises=[] #Creando una lista vacia para contar los paises en general
conteo_paises=[]   #Lista vacia para el conteo de paises totales de exportacion
pais_actual=[] #lista para indicar en que pais se encuentra al ult dev al iterar

for valor in list_exports:  #valor  de mi lista con los  datos en general
    if valor[2]not in paises: #indice donde se encuentra paises de origen en lista_exports
        paises.append(valor[2]) #a mi lista vacia le agrego los valores 

for valor in list_exports: #vuelvo a iterar sobre la lista de exportaciones
    if [valor[2],valor[9]] not in pais_actual:#indico los indices a iterar en list
       pais_actual.append([valor[2],valor[9]]) #incluyo en mi lista pais_ac los valores

for pais in pais_actual: #for de paiese y conteo
    contador=0 #contador 
    for v_exp in list_exports: #for de exportaciones
        if v_exp [2]==pais[0] and v_exp[9]==pais[1]: #valor de exports por pais de origen y vlaor total
            contador +=1 #contador 
            
    conteo_paises.append([pais[0], pais[1], contador]) #conteo de los paises exports y su valor
conteo_paises.sort(reverse=True, key= lambda x:x[2]) #ordenando la lista de los valores de exp que contiene paises de origen

#def gnral_paises(): #definiendo mi funcion para que mostrara la lista del conteo paises
#    print(conteo_paises) #LISTA DE REFERENCIA PARA LOS PASOS SIGUIENTES
#gnral_paises() llamando  lafuncion

#GENERACION DE LISTA APARTIR DE LISTA CONTEO_PAISES CONTEMPLANDO LOS PAISES 
#CON VALOR DE SUS EXPORTACIONES TOTALES Y NO. DE VECES QUE SE REPETIA DICHO VALOR
#primero abrire un nuevo txt donde cree una lista pero paises con mayor valor de acuerdo al conteo 
#En este caso de exports se toman en cuenta paises de origen
with open("Exp_valuepaises.txt","r") as archivo: #abriendo mi archivo de txt donde se encuentra la lista con los paises con mayor valor sacada de la lista conteo_paises
     expt_p= archivo.read() #leyendo mi archivo txt 
     #print("\nLista del valor total en exportaciones datos apartir  de lista de referencia conteo_paises \n:", expt_p)#mandando a imprimir el txt
# LISTA DE VALOR TOTAL DE EXP APARTIR DE CONTEO PAISES 
#NOTA LA LISTA DE REFERENCIA DE ESTA LIST INCLUYE LA FILTRACION Y CONTEO DE PAISES QUE GENERAN EL 80% DE MAS VALOR

def infExp_Synergy(): #definiendo mi funcion de la informacion que mumestra Synergy en general en cuento a exportaciones
    print('\nSe te mostrara la lista de los paises con mayor valor total en exportaciones\n:')
infExp_Synergy() #llamando a la funcion para que esta sea ejecutada

def dicc_valorexp(): #definiendo mi funcion de diccionario donde iran los valores 
    print('\n Lista de paises que generan el 80% del valor total en las exportaciones, siendo informacion por default de la empresa:\n') #imprimiendo el diccionario de mi lista de paises y sus valores de las exports
dicc_valorexp() #llamando a mi funcion diccionario

dict_naciones={'Australia', 'United Kingdom', 'USA','China', 'United Kingdom', 
 'Germany', 'Italy', 'Japan', 'India', 'Austria','United Kingdom', 'Netherlands',
 'Canada','South Korea'} #diccionario

print(dict_naciones) #imprimiendo el diccionario

#IMPORTACIONES CON MAYOR VALOR

#AHORA SE VERAN LOS PAISES QUE TIENEN MAYOR REPRESENTACION EN IMPORTACIONES
#En esta lista tome en cuenta los paises de destino y de ahi hice mi conteo en una nueva lista 
#LA LISTA DE CONTEO ES TOTAL_vLiMP
contador=0 #contador
listaimp_paises=[] #creando una lista vacia para losvalores de paises de imports
actual_paisim=[] #creando otra lista vacia
total_vpImp=[] #lista vacia que contendra valores finales 

for valor in importaciones:  #valor  de mi lista con los  datos en general
    if valor[3]not in listaimp_paises: #en el indice indico que iterar sobre  paises destino 
        listaimp_paises.append(valor[3]) #a mi lista vacia le agrego los valores 

for valor in importaciones: #iteracion en mi lista de referencia de imports
    if [valor[3],valor[9]] not in actual_paisim:  #de nuevo indico los index para iterar
       actual_paisim.append([valor[3],valor[9]]) #agrego los valores ant a la lista vacia

for pais in actual_paisim: #for de pais en lista paisa importacion y conteo
    contador=0 #contador 2
    for nacion in importaciones: #for de importaciones
        if nacion[3]==pais[0] and nacion[9]==pais[1]: #valor de paises de destino
            contador +=1 #contador 
            
    total_vpImp.append([pais[0], pais[1], contador]) #conteo de las paises y su valor en imports
    total_vpImp.sort(reverse=True, key= lambda x:x[2]) #ordenando la lista
#print(total_vpImp) #alista de referencia
#generando lista de importaciones de acuerdo a sus valores totales 
#se toman en cuenta los valores de mi lista llamada total_vpImp
with open("Import_value.txt","r") as archivo: #abriendo mi archivo de txt donde se encuentra la lista con los paises con mayor valor sacada de la lista conteo_paises
     imp_val= archivo.read() #leyendo mi archivo txt 
#LISTAS GENERADAS DE LA INFORMACION INCLUIDA EN LISTAS DE REFERENCIA 
#print("\nLista del valor total en importaciones-datos apartir de lista de referencia total_vpImp\n:", imp_val)#mandando a imprimir el txt
 
#NOTA LA LISTA DE REFERENCIA EN ESTE CASO IGUAL ESTA FILTRADA YA POR VALORES MAYORES Y EL CONTEO DEL TOTAL DE REPETICIONES
# LA LISTA DE REFERENCIA SE CREO ANTERIORMENTE Y ES LA LISTA TOTAL_VPIMP
#GENERACION DE PAISES CON MAYOR VALOR EN IMPRTACIONES 
#NOTA LA LISTA DE REFERENCIA EN ESTE CASO ES total_vpImp de la cual saque los valores de mayor valor y los exporte a una lista txt
#EN ESTA LISTA ES INCLUYE EL PAIS DE DESTINO, VALOR TOTAL Y N-VECES DE REPET

def valor_Importaciones(): #definiendo valor de las importaciones
    print('\n Lista de paises que generan el 80% del valor total en las importaciones, esta es informacion por default de la empresa:\n')  
valor_Importaciones() #llamando la funcion para que se ejecute

#creando un diccionario para imprimir los paises que generan el 80% de valor a Synergy
dict={'Thailand','China','Japan','Canada','Germany','Mexico','Poland','United Arab Emirates'}
print(dict) #imprimiendo el diccionario

def salida_synergy(): #definiendo mi funcion de salida 
    print('\nFue un gusto atenderte!: Vuelve Pronto:\n') #mensaje que se mostrara al salir
salida_synergy() #llamando a mi funcion salida para que se ejecute