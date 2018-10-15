from random import *
from Mod_Funciones_ElGranGranjero import *


#PROGRAMA PRINCIPAL
def mainJuego():
            
    #VARIABLES INICIALES
    cultivosParcelas = []
    estadosParcelas = []
    crecimParcelas = []
    lluviaParcelas = []
    contMuerteParcelas = []
    condClima = []
    
    dinero = 0
    turno = 0
    
        
    #INICIALIZO | Estado = Limpio | Cultivos = Vacío | Crecimiento = 0 | Lluvia Acumulada = 0
    asignParcelas(estadosParcelas, "Limpio")
    asignParcelas(cultivosParcelas, "      ")
    asignParcelas(crecimParcelas, 0)
    asignParcelas(lluviaParcelas, 0)
    asignParcelas(contMuerteParcelas, 0)
    
    
    #TITULO
    print("************* E L    G R A N    G R A N J E R O *************\n")
    print("Convenciones:\nF.Fina = Frutas Finas\nA.Vera = Aloe Vera\nC.Cult = Con Cultivo")
      
    #DIBUJO
    dibujar(cultivosParcelas, estadosParcelas)
        
    #SEMBRADO INICIAL    
    sembrar(cultivosParcelas, estadosParcelas)
    
    #DIBUJO
    dibujar(cultivosParcelas, estadosParcelas)
    
    primeraVez = True
    #PREGUNTO SI HACE CAMBIO
    cambio = preguntar("Cambiar")
    while(cambio):
        #SET | Estado = Limpio
        estadosParcelas = []
        asignParcelas(estadosParcelas, "Limpio")
        
        dinero = modifParcela(cultivosParcelas, estadosParcelas, dinero, "Cambiar", primeraVez)
        cambio = preguntar("Cambiar")
        
        
    #SET | Estado = Con Cultivo
    estadosParcelas = []
    asignParcelas(estadosParcelas, "C.Cult")
    
    #INICIA EL JUEGO
    primeraVez = False
    dinero = 84
    turno += 1
    
    while(turno<=12):
        
        #MUESTRO TURNO Y DINERO
        print("\n********\nTURNO {0}\n********" .format(turno))
        print("Dinero: $ {:.2f}" .format(dinero))
        
        #DIBUJO
        dibujar(cultivosParcelas, estadosParcelas)
    
        #PIDO CLIMA: viento, lluvia y temperatura
        condClima = pedirClima()
        
        #ACUMULO CANTIDAD LLUVIA: se usa en el rendimiento
        acumularLluvia(lluviaParcelas, condClima[1], estadosParcelas)
        
        #PROBABILIDAD DE DESASTRE
        desastre = probDesastre()
        
        if(desastre):
            print("\n*ALERTA DE DESASTRE CLIMÁTICO* ¡Se perderá toda la cosecha!")
            
            estadosParcelas = []
            cultivosParcelas = []
            crecimParcelas = []
            lluviaParcelas = []
            contMuerteParcelas = []
            
            asignParcelas(estadosParcelas, "Limpio")
            asignParcelas(cultivosParcelas, "      ")
            asignParcelas(crecimParcelas, 0)
            asignParcelas(lluviaParcelas, 0)
            asignParcelas(contMuerteParcelas, 0)
            
        
        #CHEQUEO SI UN CULTIVO CRECE O MUERE
        checkCrecimiento(cultivosParcelas, estadosParcelas, crecimParcelas, lluviaParcelas, contMuerteParcelas, condClima)
        
        #CHEQUEO SI HAY ALGO POR COSECHAR
        dinero = checkCosechar(cultivosParcelas, estadosParcelas, crecimParcelas, lluviaParcelas, contMuerteParcelas, dinero)
        
        #DIBUJO
        dibujar(cultivosParcelas, estadosParcelas)
        
        
        #CHEQUEO SI SE PUEDE SEMBRAR
        puedeSembrar = checkParcelaVacia(estadosParcelas)
        while(puedeSembrar and dinero>=1):
            
            siembro = preguntar("Sembrar")
            if(siembro):
                dinero = modifParcela(cultivosParcelas, estadosParcelas, dinero, "Sembrar", primeraVez)

            puedeSembrar = checkParcelaVacia(estadosParcelas)
                            
            if(not siembro):
                puedeSembrar = False
        
        
        #CHEQUEO SI PUEDE SEGUIR COMPRANDO
        todoVacio = checkTodoVacio(estadosParcelas)
        if(dinero<1 and todoVacio):
            print("\n->Te has quedado sin dinero para sembrar un nuevo cultivo.\n")
            turno = 12
        
        
        turno+=1
        
    print("\n*************    F I N    D E L    J U E G O    *************\n")
    
    
mainJuego()
            



