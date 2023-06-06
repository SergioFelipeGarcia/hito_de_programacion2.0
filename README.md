# hito_de_programacion2.0

El proyecto es una aplicación que permite gestionar clientes, productos y pedidos
Clase "Producto": Esta clase representa un producto y tiene los siguientes atributos:

referencia: la referencia del producto.
nombre_P: el nombre del producto.
precio: el precio del producto.
existencias: la cantidad de existencias disponibles del producto.
Clase "Cliente": Esta clase representa un cliente y tiene los siguientes atributos:

nombrecli: el nombre del cliente.
direccioncli: la dirección del cliente.
nifcli: el NIF (Número de Identificación Fiscal) del cliente.
telfcli: el número de teléfono del cliente.
mailcli: la dirección de correo electrónico del cliente.
tasascli: el porcentaje de tasas que se aplican a las facturas del cliente (IVA o IGIC).
Clase "Pedido": Esta clase hereda de la clase "Producto" y representa un pedido realizado por un cliente. Tiene los mismos atributos que la clase "Producto".

Funciones y listas:

"consultar_catalogo()": Muestra el catálogo de productos disponibles.
"mostrar_cliente()": Muestra la lista de clientes registrados.
"consultar_pedido()": Muestra la lista de pedidos registrados.
"Lista_productos": Lista que almacena los productos registrados.
"Lista_clientes": Lista que almacena los clientes registrados.
"Lista_pedidos": Lista que almacena los pedidos registrados.
Menú de la aplicación: El programa utiliza un bucle while para mostrar un menú de opciones al usuario:

Registrar un cliente.
Registrar un producto.
Consultar el catálogo de productos.
Seleccionar productos y comprar.
Registrar un pedido.
Consultar los pedidos.
Salir de la aplicación.
El programa permite registrar clientes, productos y pedidos, mostrar la información de los clientes y productos, realizar compras de productos y generar facturas con impuestos. Además, cuenta con la funcionalidad básica de envío de facturas por correo electrónico y SMS (aunque el código necesario para esto se encuentra comentado y no funcional).

Cabe mencionar que el proyecto muestra algunas deficiencias y áreas de mejora, como la falta de validación de datos ingresados por el usuario, la ausencia de persistencia de datos (utiliza listas en memoria) y algunas secciones de código comentadas sin funcionar.
