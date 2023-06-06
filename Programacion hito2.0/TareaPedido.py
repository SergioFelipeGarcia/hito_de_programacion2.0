class Producto: ##creo la clase producto y le defino los atributos a esta clase
  def __init__ (self, referencia, nombre_P,precio, existencias): 
        self.referencia = referencia#aqui lo que estoy haciendo es igualar los valores que estamos recibiendo a los atributos de nuestro objeto producto
        self.nombre_P = nombre_P
        self.precio = precio
        self.existencias = existencias

class Cliente:
  def __init__ (self, nombrecli, direccioncli, nifcli, telfcli, mailcli, tasascli ):
    self.nombrecli = nombrecli
    self.direccioncli = direccioncli
    self.nifcli = nifcli
    self.telfcli = telfcli
    self.mailcli= mailcli
    self.tasascli = tasascli
    
class Pedido(Producto):
    def __init__(self, referencia, nombre_P, precio, existencias):
      super().__init__(referencia, nombre_P, precio, existencias)







# Para poder enviar la factura por email
# hay que configurar en phyton el servicio de mail SMTP 
# importar esta libreria (info desde video https://www.youtube.com/watch?v=7ZcFcTdCa7o)
#import smtplib
#from decouple import config
#message='Hola desde python'
#server = smtplib.SMTP("smtp.gmail.com", 587)
#server.starttls()
#server.login('sergio.felipeg2004@gmail.com',config('MAIL_PASSWORD'))
#password = ""
#server.login("sergio.felipeg2004@gmail.com", password)

i=0
Lista_productos=[] #todavía no se utilizar ficheros o una BBDD en py, entonces guardo los productos en una lista.
def consultar_catalogo():   # 
    k = 0
    while k < len(Lista_productos):
        print (Lista_productos[k].referencia, " ", Lista_productos[k].nombre_P, " ", "El precio unidad es:", Lista_productos[k].precio, "€", "disponibles:", Lista_productos[k].existencias)
        k+=1

Lista_clientes=[] 
def mostrar_cliente():
  j = 0
  while j < len(Lista_clientes):
    print ("Bienvenido" , Lista_clientes[j].nombrecli, " ",Lista_clientes[j].mailcli)
    j+=1

Lista_pedidos=[]
def consultar_pedido():
  x=0
  while x < len(Lista_pedidos):
    print(Lista_pedidos[x].nombre_P," ","El precio unidad es:", Lista_pedidos[x].precio, "€", "Cantidad deseada:", Lista_pedidos[x].existencias)

    x+=1




while i==0: #utilizo un bucle para  hacer repeticiones de mi menu y que mientras i sea ==0 se muestren las opciones a elegir
  print("---- ***** Menu de mi Aplicación ***----")
  print("1.- Registrar un Cliente")
  print("2.- Registrar un Producto")
  print("3.- Consultar Catálogo Productos")
  print("4.- Seleccionar producto y Comprar")
  print("5- Registrar el pedido")
  print("6.- Consultar los pedidos")
  print("7.- Salir")
  opcion = int(input()) # defino la variable opcion y solicito mediante un input el valor para elegir las opciones 
  if opcion==1: #mediante un condicional verifico la opcion ingresada
    print ("--- Registrar un Cliente ---")
    nom = input("introduzca su nombre de Cliente:")#defino varias variables y solicito con un input los datos
    dir = input("introduce su direccion de Cliente:")
    nif = input("introduce su NIF:")
    telf = input("escriba el telefono móvil:")
    mail = input("introduce la dirección de correo electronico:")
    tax = input("por favor indique el porcentaje que debemos aplicar a sus facturas (iva o igic):")
    cli = Cliente(nom, dir, nif, telf, mail, tax) #creo el objeto tipo cliente  y dentro pongo la clase y entre parentesis los atributos para crear ese objeto
    Lista_clientes.append(cli) #luego ese objeto sera añadido a la lista de clientes
    print ("\n\n El Cliente se ha registrado en la Aplicación con éxito \n\n")
    mostrar_cliente()
  elif opcion==2:
    print ("--- Registrar un Producto ---")
    ref = input("introduce la referencia del producto:")
    nom = input("introduce el nombre del producto:")
    pre = input("introduce el precio del producto:")
    stock = input("introduce la cantidad de existencias del producto:")
    articulo = Producto(ref, nom, pre, stock)
    Lista_productos.append(articulo)
    print ("\n\n El Producto se ha guardado en el catálogo correctamente \n\n")
  elif opcion==3:
    print ("Consultar Catálogo Productos")
    consultar_catalogo() 
  elif opcion==4:
    print("\n\n -- Seleccionar productos del catalogo y comprar --\n\n") 
    print("Los productos disponibles en el catalogo son:\n") 
    consultar_catalogo()
   # Aquí empezaríamos a llenar el carro. Habria que hacer un bucle
   # preguntando al cliente si desea comprar mas articulos hasta que este diga que no
   # ¿Desea seguir comprando? S/N
    seguir = 'si'        # utilizo un while para que te siga preguntando hasta que tu hayas comprado 3 productos luego te pregunta si quieres continuar o no  si le das a no te muestra el precio de los productos
    while seguir == 'si':
        print("indica el nombre del primer producto que desea comprar:")  
        p1 = input()    # pongo  las variable p1  con input para que introduzcas el producto del catálogo  con su precio y la cantidad que quieras
        print("indica la cantidad a comprar de:", p1)
        p1_cant= int(input())
        print("indica el precio de catalogo del producto de:" , p1)
        p1_pre= float(input())
        seguir=input('quiere seguir comprando(si - no): ')
        print("indica el nombre del segundo producto que desea:")
        p2 = input()
        print("indica la cantidad a comprar de:", p2)
        p2_cant = int(input())
        print("indica el precio de catalogo del producto de:", p2)
        p2_pre = float(input())
        seguir=input('quiere seguir comprando(si - no): ')
        print("indica el nombre del tercer producto:")
        p3= input()
        print("indica la cantidad a comprar de:", p3)
        p3_cant= int(input())
        print("indica el precio de catalogo del producto de:", p3)
        p3_pre= float(input())
        seguir=input('quiere seguir comprando(si - no): ')
    
    
  # Calculo de los subtotales del pedido     
    p1_subt = p1_cant * p1_pre
    p2_subt = p2_cant * p2_pre
    p3_subt = p3_cant * p3_pre
    subtot = p1_subt + p2_subt + p3_subt
  # Calculo el IVA y el IGIG (mas adelante daré opción a elegir cual corresponde)
    IVA = subtot * 0.21
    IGIG = subtot * 0.06
    TotalIva = subtot + IVA 
    TotalIgic= subtot + IGIG
  # Factura  
    print("el total a pagar por", p1 , "es:", p1_subt)     #muestra el precio total del producto 
    print("el total a pagar por", p2 , "es:", p2_subt)
    print("el total a pagar por", p3 , "es:", p3_subt)
    print("El precio de su pedido antes de impuestos es: ", subtot,"€" )
    print("El importe del IVA es de: ", IVA, "€")      #muestra lo que se le añade de IVA al precio
    print("El importe del IGIG es de: ", IGIG, "€")     #muestra lo que se le añade de IGIG al precio
    print("El precio de su pedido con IVA es: ", TotalIva,"€" )  # muestra el total del precio con el IVA

    print("Para enviar la factura por correo :")
    print('se envia un SMS a tu teléfono')

  
  elif opcion==5:
    print('--- Registrar el pedido---')
    ref = input("introduce la referencia del producto:")
    nom = input("introduce el nombre del producto:")
    pre = input("introduce el precio del producto:")
    stock = input("introduce la cantidad de existencias desea comprar :")
    elpedido=Pedido(ref,nom,pre,stock)
    Lista_pedidos.append(elpedido)
    print ("\n\n El Pedido se ha guardado correctamente \n\n")
  elif opcion==6:
    print ("Consultar los pedidos")
    consultar_pedido() 

  elif opcion==7:
    print ("Salir de la Aplicación")
    exit()
  else:
    print ("Opcion invalida") 

