def llenado(lista):
    x = 1800
    usuario = ["Victor Suxo","6150883","true",x,"Bs","6"]
    lista.append(usuario)
    x = 2800
    usuario = ["Rize Uchija","9182667","true",x,"Sus","10"]
    lista.append(usuario)
    x = 3500
    usuario = ["Naruto Uzumaki","7382648","true",x,"Bs","5"]
    lista.append(usuario)    

def registro(lista):
    #registra nuevo cliente
    nombre = input("Ingrese nombre completo : ")
    ci = input("Ingrese Ci : ")
    monto = input("Monto inicial : ")
    tipo = input("tipo de cambio : ")
    usuario = [nombre,ci,"true",monto,tipo,0]
    lista.append(usuario)

def mostrar(lista):
    
    print("-------------------------------------------------------------------------------------------------------------------------")
    for l in lista:
        print("Nombre : ",l[0],"| Ci :  ",l[1],"|   Ahorros : ",l[3],"| Cambio : ",l[4],"| Cant.Tiquets : ",l[5])
        print("-------------------------------------------------------------------------------------------------------------------------")


def retiro(lista,id):
    
    cliente = lista[id]
    print("Nombre del cliente : ",cliente[0])
    monto = int(input("Monto que va a retirar : "))
    
    ahrs = cliente[3]
    
    if(ahrs>monto):
        cliente[3] = cliente[3]-monto
        print("Ahorros : ",cliente[3])
    else:
        print("Ahorros insuficientes")    

def deposito(lista,id):
    cliente = lista[id]
    monto = int(input("Monto a depositar"))
    cliente[3] = cliente[3] + monto
    print("Monto total : ",cliente[3])

def habilitar(lista,id):
    cliente = lista[id]
    cliente[2] = "true"

def dHabilitar(lista,id):
    cliente = lista[id]
    cliente[2] = "false"

def mHablitados(lista):
    print("------------------------------------HABILITADOS-------------------------------------------------------------------------------------")
    for i in lista:
        if i[2]=="true":
            print("Nombre : ",i[0],"| Ci :  ",i[1],"|   Ahorros : ",i[3],"| Cambio : ",i[4],"| Cant.Tiquets : ",i[5])
            print("-------------------------------------------------------------------------------------------------------------------------")

def mdHablitados(lista):
    print("------------------------------------DESHABILITADOS-------------------------------------------------------------------------------------")
    for i in lista:
        if i[2]=="false":
            print("Nombre : ",i[0],"| Ci :  ",i[1],"|   Ahorros : ",i[3],"| Cambio : ",i[4],"| Cant.Tiquets : ",i[5])
            print("-------------------------------------------------------------------------------------------------------------------------")

def calcularMillas(lista,id):
    cliente = lista[id]
    if cliente[4]=="Sus":
        y = float(input("Igrese valor para calcular las millas"))
        if(y<1):
            mil = cliente[3]*y 
            print("===============================================")
            print("Las millas son : ", mil)
            print("===============================================")
    else:
        print("===============================================")
        print("El cliente no usa cambio en dolares")        
        print("===============================================")

def consulta(lista,id):
    cliente = lista[id]


def menu():
    banco = []
    llenado(banco)
    sw = 1 
    while(sw!=0):
        print("Registrar nuevo cliente    [1]")
        print("Mostrar clientes           [2]")
        print("Depositar                  [3]")
        print("Retirar                    [4]")
        print("Habilitar cliente          [5]")
        print("Deshabilitar cliente       [6]")
        print("Mos.clientes hablitados    [7]")
        print("Mos.clientes deshablitados [8]")
        print("calcular millas            [9]")
        print("Hacer una consulta         [10]")
        print("Salir                      [0]")
        sw = int(input())
        if(sw==1):
            registro(banco)
        if(sw==2):
            mostrar(banco)
        if(sw==3):
            id = int(input("Ingrese  id del cliente : "))
            if(id>=0):
                deposito(banco,id)        
        if(sw==4):
            id = int(input("Ingrese  id del cliente : "))
            if(id>=0):
                retiro(banco,id)
        if(sw==5):
            id = int(input("Ingrese  id del cliente : "))
            if(id>=0):
                habilitar(banco,id)            
        if(sw==6):
            id = int(input("Ingrese  id del cliente : "))
            if(id>=0):
                dHabilitar(banco,id) 
        if(sw==7):
            mHablitados(banco)
        if(sw==8):
            mdHablitados(banco)
        if(sw==9):
            id = int(input("Ingrese  id del cliente : "))
            if(id>=0):
                calcularMillas(banco,id) 
        if(sw==10):
            id = int(input("Ingrese  id del cliente : "))
            if(id>=0):
                consulta(banco,id)                        
        if(sw==0):
            break

menu()
