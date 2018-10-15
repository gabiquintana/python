from random import *

#CREO EL TERRENO 4X4 DE LAS PARCELAS
def asignParcelas(lista, parametro):
    
    listaFilas = []
    for i in range(4):
        for j in range(4):
            listaFilas.append(parametro)
        
        lista.append(listaFilas)
        listaFilas = []
    
    return


#ELEGIR CULTIVO
def selecCultivo():
    
    cultivoElegido = "      "
    
    print("¿Qué desea sembrar?")
    print("1. Frutas Finas\n2. Aloe Vera\n3. Hongos\n")
            
    opcion = int(input("Ingrese una opción: "))
    while(opcion<1 or opcion>3):
        opcion = int(input("Ingrese una opción válida: "))
                
    if(opcion==1):
        cultivoElegido = "F.Fina"
    elif(opcion==2):
        cultivoElegido = "A.Vera"
    elif(opcion==3):
        cultivoElegido = "Hongos"
    
    return cultivoElegido


#SEMBRADO INICIAL
def sembrar(cultPar, estPar):
    
    print("INGRESE EL CULTIVO A SEMBRAR EN LAS PARCELAS.")
    
    contador = 0
    for i in range(4):
        for j in range(4):
            print("\nParcela {0}:" .format(contador))
            
            #Elección de cultivo          
            cultPar[i][j] = selecCultivo()
            estPar[i][j] = "C.Cult"
            contador += 1
    
    return


#MODIFICAR UNA PARCELA
def modifParcela(cultPar, estPar, plata, accion, primeraVez):
    
    editFila = 0
    editCol = 0
    
    if(accion == "Cambiar"):
        numParcela = int(input("\nIngrese el número de Parcela que desea cambiar: "))
        
    if(accion == "Sembrar"):
        print("\nDinero: $ {:.2f}" .format(plata))
        numParcela = int(input("Ingrese el número de Parcela en donde desea sembrar: "))
    
    while(numParcela<0 or numParcela>15):
        numParcela = int(input("Ingrese un número de Parcela válido: "))
        
    contador = 0
    for i in range(4):
        for j in range(4):
            if(contador==numParcela):
                editFila = i
                editCol = j
            
            contador+=1
            
    if(primeraVez):
        print("\nParcela {0}:" .format(numParcela))
        nuevoCultivo = selecCultivo()
        cultPar[editFila][editCol] = nuevoCultivo
        estPar[editFila][editCol] = "C.Cult"
        
    else:
            
        #Si la parcela está limpia
        if(estPar[editFila][editCol] == "Limpio"):
            print("\nParcela {0}:" .format(numParcela))
            nuevoCultivo = selecCultivo()
                
            if(nuevoCultivo == "F.Fina" and plata>=10):
                cultPar[editFila][editCol] = nuevoCultivo
                estPar[editFila][editCol] = "C.Cult"
                plata = plata - 10
                
            elif(nuevoCultivo == "A.Vera" and plata>=1):
                cultPar[editFila][editCol] = nuevoCultivo
                estPar[editFila][editCol] = "C.Cult"
                plata = plata - 1
                
            elif(nuevoCultivo == "Hongos" and plata>=5):
                cultPar[editFila][editCol] = nuevoCultivo
                estPar[editFila][editCol] = "C.Cult"
                plata = plata - 5
                
            else:
                print("\n-> Dinero insuficiente para sembrar {0}." .format(nuevoCultivo))
                
        #Si la parcela está con cultivo
        elif(estPar[editFila][editCol] == "C.Cult"):
            print("\n-> La Parcela {0} tiene cultivo activo. No se puede sembrar ahí." .format(numParcela))
    
    
    return plata


#DECISIÓN DE CAMBIO
def preguntar(accion):
    
    decision = False
    
    if(accion == "Cambiar"):
        print("\n¿Desea realizar algún cambio?")
        
    if(accion == "Sembrar"):
        print("\n¿Desea sembrar un nuevo cultivo?")
        
    print("1. Sí.")
    print("2. No. (Avanzar)")
    
    opcion = int(input("Ingrese una opción: "))
    while(opcion<1 or opcion>2):
        opcion = int(input("Ingrese una opción válida: "))
    
    if(opcion==1):
        decision = True
        
    elif(opcion==2):
        decision = False
        
    return decision


#PROBABILIDAD DE DESASTRE
def probDesastre():
    
    hayDesastre = False
    
    numero = randint(1,1000)
    if(numero>=10 and numero<=40):
        hayDesastre = True
        
    return hayDesastre


#PEDIR DATOS DEL CLIMA AL JUGADOR
def pedirClima():
    
    lista = []
    
    print("\nINGRESE VALORES CLIMÁTICOS: \n")
    viento = int(input("Ingrese velocidad del viento (km/h): "))
    while(viento<0):
        viento = int(input("Ingrese un valor válido para la velocidad del viento (Km/h): "))
    
    lluvia = int(input("Ingrese precipitación de lluvia (mL): "))
    while(lluvia<0):
        lluvia = int(input("Ingrese un valor válido para la precipitación de lluvia (mL): "))
        
    temperatura = int(input("Ingrese temperatura (°C): "))
    
    lista.append(viento)
    lista.append(lluvia)
    lista.append(temperatura)
    
    return lista


#TURNOS DE CRECIMIENTO O MUERTE DEL CULTIVO
def checkCrecimiento(cultPar, estPar, crecPar, lluviaPar, contMuertePar, clima):
    
    for i in range(4):
        for j in range(4):
            
            contador = 0
            if(estPar[i][j]=="C.Cult"):
                
                #Si tengo Frutas Finas
                if(cultPar[i][j]=="F.Fina"):
                    if(clima[0]<=30):
                        contador += 1
                    if(clima[1]>=34 and clima[1]<=112):
                        contador += 1
                    if(clima[2]>=9 and clima[2]<=25):
                        contador += 1
                    
                #Si tengo Aloe Vera
                if(cultPar[i][j]=="A.Vera"):
                    contador =2 
                    if(clima[0]<=100):
                        contador += 1
                        
                #Si tengo Hongos
                if(cultPar[i][j]=="Hongos"):
                    if(clima[0]<=80):
                        contador += 1
                    if(clima[1]>=34 and clima[1]<=200):
                        contador += 1
                    if(clima[2]>=6 and clima[2]<=30):
                        contador += 1
                        
                #Hay crecimiento
                if(contador==3):
                    crecPar[i][j] += 1
                else:
                    contMuertePar[i][j] += 1
                
                #Se muere el cultivo
                if(contMuertePar[i][j] == 3):
                    estPar[i][j] = "Limpio"
                    cultPar[i][j] = "      "
                    crecPar[i][j] = 0
                    lluviaPar[i][j] = 0
                    contMuertePar[i][j] = 0
                    
                    print("\n-> Se murió el cultivo en la Parcela {0}." .format(i*4+j))
 
    return
                
                
#ACUMULAR LLUVIA
def acumularLluvia(lluviaPar, valorLluvia, estPar):
    
    for i in range(4):
        for j in range(4):
            if(estPar[i][j]=="C.Cult"):
                lluviaPar[i][j]+=valorLluvia
            
    return


#COSECHAR
def checkCosechar(cultPar, estPar, crecPar, lluviaPar, contMuertePar, plata):
    
    for i in range(4):
        for j in range(4):
            
            rendimiento = 0
            ganancia = 0
            precio = 0
            blanqueo = False
            
            #Si tengo Frutas Finas
            if(cultPar[i][j]=="F.Fina"):
                if(crecPar[i][j]==9):
                    
                    blanqueo = True
                    precio = 10
                    
                    if(lluviaPar[i][j]>=300 and lluviaPar[i][j]<600):
                        rendimiento = 50
                    if(lluviaPar[i][j]>=600 and lluviaPar[i][j]<800):
                        rendimiento = 80
                    if(lluviaPar[i][j]>=800 and lluviaPar[i][j]<=1000):
                        rendimiento = 100
                    
                    
            #Si tengo Aloe Vera
            if(cultPar[i][j]=="A.Vera"):
                if(crecPar[i][j]==1):
                    
                    blanqueo = True
                    precio = 1
                    
                    if(lluviaPar[i][j]<100):
                        rendimiento = 50
                    if(lluviaPar[i][j]>=100 and lluviaPar[i][j]<=300):
                        rendimiento = 80
                    if(lluviaPar[i][j]>300):
                        rendimiento = 100
                        
                        
            #Si tengo Hongos
            if(cultPar[i][j]=="Hongos"):
                if(crecPar[i][j]==5):
                    
                    blanqueo = True
                    precio = 5
            
                    if(lluviaPar[i][j]>=100 and lluviaPar[i][j]<400):
                        rendimiento = 50
                    if(lluviaPar[i][j]>=400 and lluviaPar[i][j]<500):
                        rendimiento = 80
                    if(lluviaPar[i][j]>=500 and lluviaPar[i][j]<=600):
                        rendimiento = 100
                        
            if(blanqueo):
                
                #Blanqueo los turnos de crecimiento, pongo estado limpio y el cultivo
                estPar[i][j] = "Limpio"
                cultPar[i][j] = "      "
                crecPar[i][j] = 0
                lluviaPar[i][j] = 0
                contMuertePar[i][j] = 0
                
                
                #Calculos
                ganancia = precio + (precio * rendimiento/100)
                plata = plata + ganancia
                    
                #Parcela cosechada
                print("\n-> Se cosechó la Parcela {0}." .format(i*4 + j))
                print("-> Ganancia recibida: + $ {0}." .format(ganancia))
                print("-> Dinero: $ {:.2f}" .format(plata))
    
    return plata


#CHECK PARCELA VACIA
def checkParcelaVacia(estPar):
    
    disponible = False
    
    for i in range(4):
        for j in range(4):
            if(estPar[i][j]=="Limpio"):
                disponible = True 
    
    return disponible


#CHECK TODO VACIO
def checkTodoVacio(estPar):
    
    todoVacio = False
    
    contador = 0
    for i in range(4):
        for j in range(4):
            if(estPar[i][j]=="Limpio"):
                contador += 1
                
    if(contador==16):
        todoVacio = True
    else:
        todoVacio = False
    
    return todoVacio


#DIBUJO EL TERRENO 4X4
def dibujar(cultPar, estPar):
    
    par = [["PAR. 0", "PAR. 1", "PAR. 2", "PAR. 3"], ["PAR. 4", "PAR. 5", "PAR. 6", "PAR. 7"], ["PAR. 8", "PAR. 9", "PAR.10", "PAR.11"], ["PAR.12", "PAR.13", "PAR.14", "PAR.15"]]
    vacio = "      "
    
    print("\n\n")
    for i in range(31):
        print("*", end=" ")
        
    for i in range(4):
        
        print()
        print("*    {0}    *    {1}    *    {2}    *    {3}    *" .format(par[i][0], par[i][1], par[i][2], par[i][3]))
        print("*    {0}    *    {1}    *    {2}    *    {3}    *" .format(cultPar[i][0], cultPar[i][1], cultPar[i][2], cultPar[i][3]))
        print("*    {0}    *    {1}    *    {2}    *    {3}    *" .format(estPar[i][0], estPar[i][1], estPar[i][2], estPar[i][3]))
        
        for j in range(31):
            print("*", end=" ")   
    print("\n\n")
    
    return

