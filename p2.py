from random import randint
from datetime import datetime

import psycopg2
#poso1 crear conección


conn = psycopg2.connect(
    host='localhost',
    database='tienda_boletos',
    user ='postgres',
    password = '1234'
    )

print('conección creada')
cursor=conn.cursor()
cur = conn.cursor()
#cursor.execute('select * from lugar\n')
#consulta=cursor.fetchall()
#cursor.execute('select * from lugar where (id_lugar = 3)')
#consulta=cursor.fetchone()
#print(consulta)

def Compra():
    validación1 = True
    validación2 = True
    validación3 = True
    validación4 = True
    respuesta = True
    respuesta2 = True
    boleto = 0

    print("\n------------------------------***¡Bienvenido!***----------------------------------- \n\tPara continuar con tu compra necesitaremos verificar algunos datos:")

    #Validar ID del cliente
    while validación1 == True:
        ID_Cliente = input("\nProporciona tu ID del registro:")
        cur.execute('select id_cliente from cliente where id_cliente ='+ID_Cliente)
        consulta1 = cur.fetchone()
        if(consulta1 == None):
            print("El ID no existe, vuelve a intentarlo")
        else:
            print("ID identificado puede continuar")
            validación1 = False

    print("\nLos conciertos disponibles son:")
    print("Id___________artista_______________fecha______________________dirección___")
    cursor.execute('select id_concierto,artista,fecha,direccion from concierto B,lugar V where B.id_lugar = V.id_lugar')
    consulta=cursor.fetchall()
    for fila in consulta:
        print(fila)
    #Seleccionar el ID del concierto
    while(validación2 == True):
        ID_Concierto = int(input("\nSelecciona el concierto al que deseas asistir según su número(ID):"))
        if((ID_Concierto>7) or (ID_Concierto<1)):
            print("\n\tOpción no válida intenta de nuevo\n")
        else:
            #Asignando monto y artista en cada ID
            if(ID_Concierto==1):            
                Monto=1620
                cur.execute('select capacidad from lugar where id_lugar='+str(ID_Concierto))
                capacidad = cur.fetchone()
                cur.execute('select artista from concierto where id_concierto='+str(ID_Concierto))
                artista = cur.fetchone()
            elif(ID_Concierto==2):
                Monto=1100
                cur.execute('select capacidad from lugar where id_lugar='+str(ID_Concierto))
                capacidad = cur.fetchone()
                cur.execute('select artista from concierto where id_concierto='+str(ID_Concierto))
                artista = cur.fetchone()
            elif(ID_Concierto==3):
                Monto=2100
                cur.execute('select capacidad from lugar where id_lugar='+str(1))
                capacidad = cur.fetchone()
                cur.execute('select artista from concierto where id_concierto='+str(ID_Concierto))
                artista = cur.fetchone()
            elif(ID_Concierto==4):
                Monto=500
                cur.execute('select capacidad from lugar where id_lugar='+str(ID_Concierto-1))
                capacidad = cur.fetchone()
                cur.execute('select artista from concierto where id_concierto='+str(ID_Concierto))
                artista = cur.fetchone()
            elif(ID_Concierto==5):
                Monto=2500
                cur.execute('select capacidad from lugar where id_lugar='+str(ID_Concierto-1))
                capacidad = cur.fetchone()
                cur.execute('select artista from concierto where id_concierto='+str(ID_Concierto))
                artista = cur.fetchone()
            elif(ID_Concierto==6):
                Monto=500
                cur.execute('select capacidad from lugar where id_lugar='+str(ID_Concierto-1))
                capacidad = cur.fetchone()
                cur.execute('select artista from concierto where id_concierto='+str(ID_Concierto))
                artista = cur.fetchone()
            else:
                Monto=250
                cur.execute('select capacidad from lugar where id_lugar='+str(ID_Concierto-1))
                capacidad = cur.fetchone()
                cur.execute('select artista from concierto where id_concierto='+str(ID_Concierto))
                artista = cur.fetchone()
            
            validación2 = False

    #Generar el número de asiento
    print("\nHay un total de", capacidad,"asientos.")
    cur.execute('select asiento from boleto where id_concierto='+str(ID_Concierto))
    asientos_oc = cur.fetchall()
    cantidad = len(asientos_oc)
    if (cantidad == 0):
        print("Todos los asientos están disponibles")
    else:
        print("\nLos asientos no disponibles son:")
        print(asientos_oc)
    #Comprobar asientos ocupados
    while(validación3 == True):
        asientos = int(input("\nSelecciona el número de asiento:"))
        res = int(''.join(map(str, capacidad)))
        if((asientos>res) or (asientos<1)):
            print("\tOpción no válida intenta de nuevo")
        else:
            for i in range (0,cantidad):
                res2 = int(''.join(map(str, asientos_oc[i])))
                if(asientos == res2):
                    respuesta = False
            
            if respuesta == False:        
                print("Asiento ocupado intenta de nuevo")
                respuesta = True
            elif respuesta == True:
                print("Has registrado tu asiento de manera exitosa")
                validación3 = False

    #Generar el número de boleto
    cur.execute('select no_boleto from boleto where id_concierto='+str(ID_Concierto))
    boletos_com = cur.fetchall()
    cantidad2 = len(boletos_com)

    #Comprobar boletos ocupados
    while(validación4 == True):
        for j in range (0,cantidad2):
            res2 = int(''.join(map(str, boletos_com[j])))
            if(boleto == res2):
                respuesta2 = False

        if respuesta2 == False:
            respuesta2 = True
            boleto = boleto + 1
        elif respuesta2 == True:
            boleto = boleto + 1
            validación4 = False


    #Generar el número de su ticket
    id_ticket = randint(1000,9999)

    #Generar la fecha de la compra
    fecha = datetime.now().strftime('%Y-%m-%d')


    print("\nLos datos de tu boleto son:\n")
    print("\t\t|ID ticket\t\t|",id_ticket)
    print("\t\t--------------------------------------------------------")
    print("\n\t\t|Monto\t\t\t|", Monto)
    print("\t\t--------------------------------------------------------")
    print("\n\t\t|Fecha\t\t\t|", fecha)
    print("\t\t--------------------------------------------------------")
    print("\n\t\t|N° de boleto\t\t|",boleto)
    print("\t\t--------------------------------------------------------")
    print("\n\t\t|Asiento\t\t|",asientos)
    print("\t\t--------------------------------------------------------")
    print("\n\t\t|Artista\t\t|",artista)
    print("\t\t--------------------------------------------------------")
    print("\n\t\t|ID_Cliente\t\t|", ID_Cliente)
    print("\t\t--------------------------------------------------------")
    print("\n\t\t|ID_Concierto\t\t|", ID_Concierto)
    print("\t\t--------------------------------------------------------")

    validación1 = True
    validación2 = True
    validación3 = True
    validación4 = True
    respuesta = True
    respuesta2 = True

    compra=input("\n¿Desea finalizar su registro?(1 = SI o 2 = NO):")
    if(compra == '1'):
        sql="INSERT INTO boleto (id_tiket, monto, fecha, no_boleto, asiento, artista, id_cliente, id_concierto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val2=(id_ticket, Monto, fecha, boleto, asientos, artista, ID_Cliente, ID_Concierto)
        cur.execute(sql, val2)
        conn.commit()
        boleto = 0
    else:
        boleto = 0
        print("\nSi desea regresar al menú principal presiona 1")
        print("Si desea salir del sistema presiona cualquier tecla")
        final=input("Respuesta:")

        if(final == '1'):
            print('-------------------------------')
            print('Opción 1:Registrarse' )
            print('Opción 2:Consiltar (Boleto,conciertos,usuarios)')
            print('Opción 3:Comprar (solo si ya estas registrado)')
            print('Opción 4:Cerrar')
            seleccion=int( input('Selecciona con numero la opción que deseas: '))
            menu(seleccion)
        else:
            exit()

    print("\n¡Gracias por tu compra!\n")
    
def registro1():
    ID=[]
    tiempos=[]
    decision = True
    transaccion = True
    validación1 = False
    validación2 = False
    validación3 = False
    validación4 = False
    validación5 = False

    while transaccion == True:
        print("\n¡Bienvenido! Para llevar a cabo tu registro es necesario que proporciones algunos datos. Comenzemos.")
        id_transaction = randint(1000,9999)
        while validación1 == False:
            nombre = input("\nIngresa tu nombre completo:")
            if(any(chr.isdigit() for chr in nombre) == True):
                print("Nombre inválido, intente de nuevo.")
            else:
                validación1 = True

        while validación2 == False:
            tarjeta = int(input("\nIngresa el número de tu tarjeta:"))
            if(len(str(tarjeta))!=16):
                print("Número de tarjeta inválido, intente de nuevo. Debe ser de 16 dígitos")
            else:
                validación2 = True

        dirección = input("\nIngresa la dirección de tu domicilio:")
        
        while validación3 == False:
            edad = int(input("\nIngresa tu edad:"))
            if ((edad<18) or (edad>99)):
                print("Eres menor de edad o tu edad está fuera del rango. Vuelve a intentarlo")
            else:
                validación3 = True

        while validación4 == False:
            sexo = input("\nIngresa tu sexo (ATENCIÓN: Sólo coloca F o M):")
            if((len(sexo)>1) or (any(chr.isdigit() for chr in sexo) == True) or (any((cr == 'F' or cr == 'M') for cr in sexo) == False)):
                print("Respuesta no válida, sigue las indicaciones.")
            else:
                validación4 = True

        while validación5 == False:
            correo = input("\nIngresa tu correo electrónico:")
            if(any(c == '@' for c in correo)==False):
                print("Correo no válido.") 
            else:
                validación5 = True                
        

        time_transaction = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("El ID de tu registro es: ",id_transaction)
        ID.append(id_transaction)
        tiempos.append(time_transaction)
        print("Los datos que has proporcionado son:\n")
        print("\t\t|ID\t\t|",id_transaction)
        print("\t\t--------------------------------------------------------")
        print("\n\t\t|Nombre\t\t|", nombre)
        print("\t\t--------------------------------------------------------")
        print("\n\t\t|Tarjeta\t|", tarjeta)
        print("\t\t--------------------------------------------------------")
        print("\n\t\t|Dirección\t|",dirección)
        print("\t\t--------------------------------------------------------")
        print("\n\t\t|Edad\t\t|",edad)
        print("\t\t--------------------------------------------------------")
        print("\n\t\t|Sexo\t\t|",sexo)
        print("\t\t--------------------------------------------------------")
        print("\n\t\t|Correo\t\t|", correo)
        print("\t\t--------------------------------------------------------")
        
        validación1 = False
        validación2 = False
        validación3 = False
        validación4 = False
        validación5 = False
        registro=input("\n¿Desea finalizar su registro?(1 = SI o 2 = NO):")
        if(registro == '1'):
            sql="INSERT INTO CLIENTE (id_cliente, nombre, tarjeta, direccion, edad, sexo, correo) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val=(id_transaction, nombre, tarjeta, dirección, edad, sexo, correo)
            cur.execute(sql, val)
            conn.commit()

        while decision == True:
            print("\n¿Quieres Volver al menu principal?:\n\t1:SI\t2:NO")
            answer = int(input("\nRespuesta:"))
            if(answer == 2):
                decision = False
                transaccion = False
            elif(answer == 1):
                print('Opción 1:Registrarse' )
                print('Opción 2:Consiltar (Boleto,conciertos,usuarios)')
                print('Opción 3:Comprar (solo si a estas registrado)')
                print('Opción 4:Cerrar')
                seleccion=int( input('Selecciona con numero la opción que deseas: '))
                menu(seleccion)
            else:
                print("\nOpción invalida. Try again")
    print("\nLos registros realizados fueron:\n")
    print ("{:<8} {:<7} {:<1}".format('Order','ID','Date'))
    for indice in range(0, len(ID)):
        print(indice, "|\t", ID[indice], "|\t", tiempos[indice])
        print("----------------------------------------")
    print("\n¡Gracias por tu registro!\n")
    
def con_usuario():
    usuario= input('Proporciona id del cliente: ')
    cursor.execute('select id_cliente from cliente where id_cliente ='+usuario)
    consulta=cursor.fetchone()
    print('id cliente:',consulta)
    cursor.execute('select nombre from cliente where id_cliente ='+usuario)
    consulta=cursor.fetchone()
    print('nombre:',consulta)
    cursor.execute('select tarjeta from cliente where id_cliente ='+usuario)
    consulta=cursor.fetchone()
    print('tarjeta:',consulta)
    cursor.execute('select direccion from cliente where id_cliente ='+usuario)
    consulta=cursor.fetchone()
    print('direccion:',consulta)
    cursor.execute('select edad from cliente where id_cliente ='+usuario)
    consulta=cursor.fetchone()
    print('edad:',consulta)
    cursor.execute('select sexo from cliente where id_cliente ='+usuario)
    consulta=cursor.fetchone()
    print('sexo:',consulta)
    cursor.execute('select correo from cliente where id_cliente ='+usuario)
    consulta=cursor.fetchone()
    print('correo:',consulta)
    sel=int( input('Deseas volver al menu principal 1:SI 2:No'))
    if sel==1:
        print('-------------------------------')
        print('Opción 1:Registrarse' )
        print('Opción 2:Consiltar (Boleto,conciertos,usuarios)')
        print('Opción 3:Comprar (solo si ya estas registrado)')
        print('Opción 4:Cerrar')
        seleccion=int( input('Selecciona con numero la opción que deseas: '))
        menu(seleccion)
    return

def con_boleto():
    tiket= input('Proporciona id del tiket: ')
    cursor.execute('select id_tiket from boleto where id_tiket ='+tiket)
    consulta=cursor.fetchone()
    print('id:',consulta)
    cursor.execute('select monto from boleto where id_tiket ='+tiket)
    consulta=cursor.fetchone()
    print('monto:',consulta)
    cursor.execute('select asiento from boleto where id_tiket ='+tiket)
    consulta=cursor.fetchone()
    print('asiento:',consulta)
    cursor.execute('select artista from boleto where id_tiket ='+tiket)
    consulta=cursor.fetchone()
    print('artista:',consulta)
    cursor.execute('select id_concierto from boleto where id_tiket ='+tiket)
    consulta=cursor.fetchone()
    print('Id concierto:',consulta)
    sel=int( input('Deseas volver al menu principal 1:SI 2:No'))
    if sel==1:
        print('-------------------------------')
        print('Opción 1:Registrarse' )
        print('Opción 2:Consiltar (Boleto,conciertos,usuarios)')
        print('Opción 3:Comprar (solo si ya estas registrado)')
        print('Opción 4:Cerrar')
        seleccion=int( input('Selecciona con numero la opción que deseas: '))
        menu(seleccion)
        
    if sel==2:
        exit()
    return()

def con_concierto():
    print("Id___________artista_______________fecha______________________dirección___")
    cursor.execute('select id_concierto,artista,fecha,direccion from concierto B,lugar V where B.id_lugar = V.id_lugar')
    consulta=cursor.fetchall()
    for fila in consulta:
        print(fila)
    sel=int( input('Deseas volver al menu principal 1:SI 2:No'))
    if sel==1:
        print('-------------------------------')
        print('Opción 1:Registrarse' )
        print('Opción 2:Consiltar (Boleto,conciertos,usuarios)')
        print('Opción 3:Comprar (solo si ya estas registrado)')
        print('Opción 4:Cerrar')
        seleccion=int( input('Selecciona con numero la opción que deseas: '))
        menu(seleccion)

def menu_consulta():
    print("Opción 1:Boleto")
    print("Opción 2:Conciertos Disponibles")
    print("Opción 3:Datos del usuario")
    print("Opción 4:Volver al menu anterior")
    sel=int( input('Selecciona con numero la opción que deseas: '))
    if sel==1:
        con_boleto()
    if sel==2:
        print('opción2')
        con_concierto()
    if sel==3:
        print('opción2')
        con_usuario()
    if sel==4:
        print('-------------------------------')
        print('Opción 1:Registrarse' )
        print('Opción 2:Consiltar (Boleto,conciertos,usuarios)')
        print('Opción 3:Comprar (solo si ya estas registrado)')
        print('Opción 4:Cerrar')
        seleccion=int( input('Selecciona con numero la opción que deseas: '))
        menu(seleccion)
    return()

def menu(a):
    if a==1:
        print('opción1')
        registro1()
    elif a==2:
        print('opcion2')
        menu_consulta()
    elif a==3:
        print('opción3')
        Compra()
    elif a==4:
        print('opción4')
        exit()
    else:
        print('opción invalida')
    return(a)


#Creación menu
print('HOLA BIEMVENIDO A BOLETILANDIA')
print('Opciones de la pagina')
print('Opción 1:Registrarse' )
print('Opción 2:Consiltar (Boleto,conciertos,usuarios)')
print('Opción 3:Comprar (solo si ya estas registrado)')
print('Opción 4:Cerrar')
seleccion=int( input('Selecciona con numero la opción que deseas: '))
menu(seleccion)



#paso3 final
conn.close()