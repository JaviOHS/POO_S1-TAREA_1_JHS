from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient, VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
from datetime import datetime
import time,os
from functools import reduce
validar = Valida()
path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
  def create(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ "*4)
      new_client_data = {}
      gotoxy(30,3);print(red_color + '​​🔴​​ AGREGAR CLIENTE 🔴​​​')
      json_file = JsonFile(path+'/archivos/clients.json')
      clients_data = json_file.read()
      new_client_data['dni'] =  validar.validar_dni_sistema(f"{cyan_color}- Ingrese DNI del cliente: {yellow_color}", 10,5)
      new_client_data['nombre'] = validar.solo_letras(f"{cyan_color}- Ingrese nombre del cliente: {yellow_color}",f"{red_color}- ¿Su nombre lleva números? ¡Intentelo de nuevo! 😡", 10, 6)
      new_client_data['apellido'] = validar.solo_letras(f"{cyan_color}- Ingrese el apellido del cliente: {yellow_color}",f"{red_color}- ¿Su apellido lleva números? ¡Intentelo de nuevo! 😡",10,7)
      new_client_data['valor'] = validar.solo_decimales(f"{cyan_color}- Ingrese el valor del cliente: {yellow_color}", f"{red_color}- ¡El valor debe ser uno o varios números! ​😹​🖐️​ {reset_color}", 10,8)
      new_client_data['tipo'] = 'VIP' if new_client_data['valor'] > 5000 else' Regular'
      
      gotoxy(10,10);option = input(f'{stick}¿Desea guardar cambios? (s/n) {stick}Reingresar datos (z) {stick}')
      gotoxy(10,10);print(' '*120)
      if option.lower() == 's':
        clients_data.append(new_client_data)
        json_file.save(clients_data)
        gotoxy(8,10);input(f'{yellow_color}​✅​ Cliente agregado con éxito. Presione ENTER para regresar. 👻    ')
        borrarPantalla()
        break
      elif option.lower() == 'z':
        gotoxy(12,10);print(blue_color + 'Reingresar datos... 😨​​​');time.sleep(1)
        borrarPantalla()
        continue
      elif option.lower() == 'n':
        gotoxy(12,10);print(red_color + 'CANCELADO: Regresando al menú principal... 🤐​​​');time.sleep(2)
        borrarPantalla()
        break
      else: 
        gotoxy(12,10);print(red_color + '- Ingrese opciones validas. 🤡​​');time.sleep(1)
  borrarPantalla()

  def update(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "︵ ‿ ︵ ‿ ︵＼ʕ •ᴥ•ʔ／︵ ‿ ︵ ‿ ︵"*3)
      gotoxy(25,3);print(red_color + '🔴 ACTUALIZAR INFO. DE CLIENTE 🔴')
      gotoxy(10,5);dni = input(f"{cyan_color}- Ingrese DNI del cliente:{yellow_color} ")
      gotoxy(10,5);print(' '*120)
      json_file = JsonFile(path+'/archivos/clients.json')
      clients_data = json_file.read()
      found_client = next(filter(lambda client: client['dni'] == dni, clients_data), None)
      if found_client:
        gotoxy(10,5);print(f"{purple_color}- INFORMACIÓN ACTUAL:")
        gotoxy(10,7);print(f"{cyan_color}- DNI:      {yellow_color}{found_client['dni']}")
        gotoxy(10,8);print(f"{cyan_color}- Nombre:   {yellow_color}{found_client['nombre']}")
        gotoxy(10,9);print(f"{cyan_color}- Apellido: {yellow_color}{found_client['apellido']}")
        gotoxy(10,10);print(f"{cyan_color}- Valor:    {yellow_color}{found_client['valor']}")
        gotoxy(4,12);option=input(f"{stick}Ingrese '1' para actualizar datos {stick}Ingrese '2' para salir {stick} ")    
        gotoxy(4,12);print(' '*200)
        if option == "1":
          while True:
            gotoxy(62,5);print(f"{purple_color}- ACTUALIZAR INFORMACIÓN:")
            gotoxy(62,7);print(f"{cyan_color}- DNI:      {yellow_color}{found_client['dni']}")
            found_client['nombre'] = validar.solo_letras(f"{cyan_color}- Nombre:   {yellow_color}",f"{red_color}- ¿Su nombre lleva números? ¡Intentelo de nuevo! 😡",62,8)
            found_client['apellido'] = validar.solo_letras(f"{cyan_color}- Apellido: {yellow_color}",f"{red_color}- ¿Su apellido lleva números? ¡Intentelo de nuevo! 😡",62,9)
            new_valor = validar.solo_decimales(f"{cyan_color}- Valor:    {yellow_color}",'¡El valor debe ser un flotante! ​😹​🖐️      ',62,10)
            found_client['valor'] = new_valor 
            found_client['tipo'] = 'VIP' if new_valor > 5000 else 'Regular'
            gotoxy(4,12);confirm = input(f"{stick}Ingrese '1' para guardar cambios {stick}Ingrese ENTER para salir {stick} ") 
            gotoxy(4,12);print(' '*100)   
            if confirm == "1":
              json_file.save(clients_data)
              gotoxy(10,12);input(yellow_color + '​✅​ Datos actualizados correctamente. Presione ENTER para regresar. 🙂   ​')
              break
            else:
              gotoxy(10,12);print('Salir sin guardar datos... 🤧​');time.sleep(2)
            break
        else:
          gotoxy(10,12);print(red_color + "Regresando al menu principal... 😟​ ​");time.sleep(2)
        break
      else:
        gotoxy(10,5);print(red_color + "- Sin resultados de busqueda. Inténtelo nuevamente. 🥶 ");time.sleep(2)
        borrarPantalla()
      break
  borrarPantalla()

  def delete(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color +'|' +"‿ ︵ ‿ ︵( ಥ ﹏ಥ ) ‿ ︵ ‿ ︵ | "*3)
      gotoxy(30,3);print(red_color + '🔴 ELIMINAR CLIENTE 🔴')
      gotoxy(10,5);delete_client = input(f"{cyan_color}- Ingrese DNI del cliente:{yellow_color} ")
      json_file = JsonFile(path+'/archivos/clients.json')
      clients_data = json_file.read()
      found_client = json_file.find('dni', delete_client)
      if found_client:
        json_file.print_all_clients(found_client)
        gotoxy(4,5);print(' '*300)
        gotoxy(4,5);option=input(f"{stick}Ingrese '1' para eliminar cliente {stick}Ingrese '2' para salir {stick} ") 
        gotoxy(4,5);print(' '*300)   
        if option == "1":
          gotoxy(15,5);confirm = input(red_color + "​💣​ ¿Está seguro de esta de decisión? (s/n) 💣​   ​")
          gotoxy(15,5);print(' '*180)
          if confirm.lower() == "s":
            clients_data.remove(found_client[0])
            json_file.save(clients_data)
            gotoxy(8,5);input(yellow_color + "​​​​✅​ Cliente eliminado exitosamente. Presione ENTER para regresar. ​​💀​    ")
            borrarPantalla()
            break
          else:
            gotoxy(30,5);print(red_color + "- CANCELADO: Regresando al menu principal... 😌​​ ​");time.sleep(2)
            borrarPantalla()
        else:
          gotoxy(10,5);print(red_color + "- CANCELADO: Regresando al menu principal... 😌​ ​");time.sleep(2)
          borrarPantalla()
        break
      else:
        gotoxy(10,5);print(' '*120)
        gotoxy(10,5);print(red_color + "- Sin resultados de busqueda. Inténtelo nuevamente. 🥶 ");time.sleep(2)
        borrarPantalla()
      break
  borrarPantalla()

  def consult(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "●～●～●～●～●～●～●～●～"*4)
      gotoxy(25,3);print(red_color + '🔴​​​ CONSULTAR INFO. DE CLIENTES 🔴​​​')
      gotoxy(4,5);print(f"{stick}{cyan_color}Ingrese '1' para buscar a un cliente en específico  {stick}{cyan_color}Ingrese '2' para visualiar la lista de clientes")
      gotoxy(4,6);option = input(f"{stick}{cyan_color}Presione ENTER para salir.                          {stick}{cyan_color}")
      json_file = JsonFile(path+'/archivos/clients.json')
      clients_data = json_file.read()
      if option == '1':
        gotoxy(4,5);print(' '*160);gotoxy(4,6);print(' '*160)
        gotoxy(10,5);dni = input(f"{cyan_color}- Ingrese DNI del cliente: {yellow_color}")
        found_client = json_file.find('dni',dni)
        if found_client:
          while True:
            json_file.print_all_clients(found_client)
            gotoxy(1,5);print(' '*120)
            borrarPantalla()
            break
        else:
          gotoxy(10,5);print(' '*120)
          gotoxy(10,5);print(red_color + "- Sin resultados de busqueda. Inténtelo nuevamente. 🥶 ");time.sleep(2)
          borrarPantalla()
        break
      elif option == '2':
        while True:
          gotoxy(4,5);print(' '*160);gotoxy(4,6);print(' '*160)
          json_file.print_all_clients(clients_data)
          borrarPantalla()
          break
      else:
        gotoxy(10, 8);print(f"{blue_color}- Regresando al menu principal... 😌​ ​");time.sleep(2)
        borrarPantalla()
      break
  borrarPantalla()

class CrudProducts(ICrud):
  def create(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ "*4)
      gotoxy(30,3);print(red_color + '​​🔴​​ AGREGAR PRODUCTO 🔴​​​')
      new_product_data = {}
      json_file = JsonFile(path+'/archivos/products.json')
      product_data = json_file.read()
      max_id = max(product_data, key=lambda x: x['id'])['id']
      new_product_data['id'] = max_id + 1
      while True:
        try:
          gotoxy(10, 5);new_product_data['descripcion'] = input(f"{cyan_color}- Ingrese nombre del producto:{yellow_color} ")
          if any(product['descripcion'] == new_product_data['descripcion'] for product in product_data):
            raise ValueError("¡El producto ya existe! ​😹​🖐️")
          break
        except ValueError as e:
          gotoxy(10,5);print(' '*120)
          gotoxy(10,5);print(f"{red_color}- {e}");time.sleep(2)
          gotoxy(10,5);print(' '*120)
          continue
      new_product_data['precio'] = validar.solo_decimales(f"{cyan_color}- Ingrese precio del producto:{yellow_color} ","- ¡El precio debe ser un número positivo! 😹​🖐️    ",10,6)
      new_product_data['stock'] = validar.solo_numeros(f"{cyan_color}-  Ingrese stock del producto:{yellow_color} ","- ¡El stock debe ser un número entero y positivo! 😹​🖐️    ",10,7)
      gotoxy(10,9);option = input(f'{stick}Desea guardar cambios? (s/n) {stick}Reingresar datos (z) {stick}')
      gotoxy(10,9);print(' '*120)
      if option.lower() == 's':
        product_data.append(new_product_data)
        json_file.save(product_data)
        gotoxy(8,9);input(f'{yellow_color}​✅​ Producto agregado con éxito. Presione ENTER para regresar. 👻   ')
        borrarPantalla()
        break
      elif option.lower() == 'z':
        gotoxy(12,9);print(blue_color + '- Reingresar datos... 😨​​​');time.sleep(1)
        borrarPantalla()
        continue
      else:
        gotoxy(12,9);print(green_color + '- Volviendo al menu principal... 🤐​​​');time.sleep(2)
        borrarPantalla()
        break
  borrarPantalla()
  
  def update(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "︵ ‿ ︵ ‿ ︵＼ʕ •ᴥ•ʔ／︵ ‿ ︵ ‿ ︵"*3)
      gotoxy(25,3);print(red_color + '🔴 ACTUALIZAR INFO. DE PRODUCTOS 🔴')
      try:
        gotoxy(10,5);product_id = int(input(f"{cyan_color}- Ingrese ID de producto:{yellow_color} "))
        gotoxy(10,5);print(' '*120)
        json_file = JsonFile(path+'/archivos/products.json')
        products_data = json_file.read()
        found_product = next(filter(lambda product: product['id'] == product_id, products_data), None)
      except: 
        gotoxy(10,5);print('- Sin resultados. Vuelva a intentarlo. 🚚​');time.sleep(2)
        break
      if found_product:
        gotoxy(10,5);print(f"{purple_color}- INFORMACIÓN ACTUAL:")
        gotoxy(10,7);print(f"{cyan_color}- Nombre:  {yellow_color}{found_product['descripcion']}")
        gotoxy(10,8);print(f"{cyan_color}- Precio:  {yellow_color}{found_product['precio']}")
        gotoxy(10,9);print(f"{cyan_color}- Stock:    {yellow_color}{found_product['stock']}")
        gotoxy(4,11);option = input(f"{stick}Ingrese '1' para actualizar datos {stick}Ingrese '2' para salir {stick} ")    
        gotoxy(4,11);print(' '*200)
        if option == "1":
          while True:
            gotoxy(50,5);print(f"{purple_color}- ACTUALIZAR INFORMACIÓN:")
            gotoxy(50,7);new_product_name=input(f"{cyan_color}- Nombre:  {yellow_color}")
            found_product['descripcion'] = new_product_name
            new_product_price = validar.solo_decimales(f"{cyan_color}- Precio:  {yellow_color}", '- ¡El precio debe ser un número positivo! 😹​🖐️',50,8)
            found_product['precio'] = new_product_price
            new_product_stock = validar.solo_numeros(f"{cyan_color}- Stock:  {yellow_color}", '- ¡El stock debe ser un número entero y positivo! 😹​🖐️',50,9)
            found_product['stock'] = new_product_stock
            gotoxy(4,11);confirm=input(f"{stick}Ingrese '1' para guardar cambios {stick}Ingrese 2 para cancelar y salir {stick} ") 
            gotoxy(4,11);print(' '*100)   
            if confirm == "1":
              json_file.save(products_data)
              gotoxy(10,11);input(yellow_color + '​✅​ Datos actualizados correctamente. Presione ENTER para regresar. ​😉    ​​')
              borrarPantalla()
              break
            else:
              gotoxy(50,11);print(red_color + '- Salir sin guardar datos... 🤧​');time.sleep(2)
            break
        else:
          gotoxy(10,12);print(red_color + "- Regresando al menu principal... 😟​​");time.sleep(2)
        break
      else:
        gotoxy(10,5);print(red_color + "- Sin resultados. Intentelo de nuevo. ​🚚​​");time.sleep(2)
      break
  borrarPantalla()

  def delete(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color +'|' +"‿ ︵ ‿ ︵( ಥ ﹏ಥ ) ‿ ︵ ‿ ︵ | "*4)
      gotoxy(30,3);print(red_color + '🔴 ELIMINAR PRODUCTO 🔴')
      gotoxy(4,5);print(f"{stick}{cyan_color}Ingrese '1' para eliminar un producto en específico  {stick}{cyan_color}Ingrese '2' para eliminar todos los productos")
      gotoxy(4,6);option = input(f"{stick}{cyan_color}Presione ENTER para salir                            {stick}")
      if option == "1":
        gotoxy(4,5);print(' '*120)
        gotoxy(4,6);print(' '*120)
        gotoxy(10,5);id_product = int(input(f"{cyan_color}- Ingrese ID del producto:{yellow_color} "))
        json_file = JsonFile(path+'/archivos/products.json')
        product_data = json_file.read()
        found_product = next(filter(lambda product: product['id'] == id_product, product_data), None)
        if found_product:
          gotoxy(10,7);print(f"{cyan_color}- Nombre:  {yellow_color}{found_product['descripcion']}")
          gotoxy(10,8);print(f"{cyan_color}- Precio:  {yellow_color}{found_product['precio']}")
          gotoxy(10,9);print(f"{cyan_color}- Stock:  {yellow_color}{found_product['stock']}")
          gotoxy(4,11);option=input(f"{stick}Ingrese '1' para eliminar producto {stick}Presione ENTER para salir {stick} ") 
          gotoxy(4,11);print(' '*300)   
          if option == "1":
            gotoxy(30, 11);confirm = input(red_color + "​💣​ ¿Está seguro de esta de decisión? (s/n) 💣​   ​")
            gotoxy(30,11);print(' '*180)
            if confirm.lower() == "s":
              product_data.remove(found_product)
              json_file.save(product_data)
              gotoxy(8, 11);input(yellow_color + "​​​✅​​ Producto eliminado exitosamente. Presione ENTER para regresar. ​​💀​   ​")
              borrarPantalla()
            else:
              gotoxy(30, 11);print(f"{red_color}- CANCELADO: {reset_color}Regresando al menu principal... 😌​​ ​");time.sleep(2)
              borrarPantalla()
              continue
          else:
            gotoxy(10, 11);print(f"{red_color}- CANCELADO: {reset_color}Regresando al menu principal... 😌​ ​");time.sleep(2)
            borrarPantalla()
            continue
          break
        else:
          gotoxy(10, 7);print(red_color + "- Sin resultados de busqueda. Inténtelo nuevamente. 🥶 ");time.sleep(2)
          borrarPantalla()
        break
      elif option == "2":
        gotoxy(4,5);print(' '*120)
        gotoxy(4,6);print(' '*120)
        gotoxy(20,5);delete = input(f"{red_color}ADVERTENCIA: {reset_color}¿Está seguro de eliminar todas los productos? (s/n) ⚠️​  ​")
        if delete.lower() == 's':
          gotoxy(30,6);confirm = input(f'💀​ ¿Está seguro de estar seguro? (s/n) 💀 ​')
          if confirm.lower() == 's':
            json_file = JsonFile(path+'/archivos/products.json')
            json_file.delete_all_products()
            gotoxy(10,8);input(f'{yellow_color} ✅​​ Todas los productos han sido eliminadas. Presione ENTER para salir. 💣    ​')
            borrarPantalla()
            break
          else:
            gotoxy(30,8);print(f"{red_color}- CANCELADO: {reset_color}Regresando al menu principal... 😌​​ ​");time.sleep(2)
            borrarPantalla()
            break
        else:
          gotoxy(30,7);print(f"{red_color}- CANCELADO: {reset_color}Regresando al menu principal... 😌​​ ​");time.sleep(2)
          borrarPantalla()
          break
      else:
        gotoxy(10,8);print(f'{blue_color}- Regresando al menu principal... 😌');time.sleep(2)
        break
  borrarPantalla()
  
  def consult(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "●～●～●～●～●～●～●～●～"*4)
      gotoxy(25,3);print(red_color + '🔴​​​ CONSULTAR INFO. DE PRODUCTOS 🔴​​​')
      gotoxy(4,5);print(f"{stick}{cyan_color}Ingrese '1' para consultar un producto en específico  {stick}{cyan_color}Ingrese '2' para visualizar todos los productos")
      gotoxy(4,6);option = input(f"{stick}{cyan_color}Presione ENTER para salir                             {stick}")
      json_file = JsonFile(path+'/archivos/products.json')
      products_data = json_file.read()
      if option == '1':
        while True:
          gotoxy(4,5);print(' '*120);gotoxy(4,6);print(' '*120)
          gotoxy(10,5);id_producto = int(input(f"{cyan_color}- Ingrese ID del producto:{yellow_color} "))
          found_product = next(filter(lambda product: product['id'] == id_producto, products_data), None)
          if found_product:
            product = json_file.find('id', id_producto)
            json_file.print_all_products(product)
            break
          else:
            gotoxy(10, 7);print(red_color + "- Sin resultados de busqueda. Inténtelo nuevamente. 🥶 ");time.sleep(2)
            borrarPantalla()
            break
      elif option == '2':
        while True:
          gotoxy(4,5);print(' '*120);gotoxy(4,6);print(' '*120)
          json_file = JsonFile(path+'/archivos/products.json')
          products_data = json_file.read()
          json_file.print_all_products(products_data)
          break
      else:
        gotoxy(10,8);print(f'{blue_color}- Regresando al menu principal... 😌');time.sleep(2)
        break
  borrarPantalla()

class CrudSales(ICrud):
  def create(self):
    while True:
      print('\033c', end='')
      validar = Valida()
      gotoxy(2,1);print(blue_color+"✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ "*4)
      gotoxy(30,3);print(purple_color+"🔴 REGISTRO DE VENTAS 🔴")
      gotoxy(17,5);print(Company.get_business_name())
      json_file = JsonFile(path+'/archivos/invoices.json')
      invoices = json_file.read()
      next_invoice_number = len(invoices) + 1
      gotoxy(5,7);print(f"{purple_color}Factura: {red_color}{next_invoice_number}")
      gotoxy(5,8);dni = input(purple_color+f"Cédula: {yellow_color}")
      json_file = JsonFile(path+'/archivos/clients.json')
      client = json_file.find("dni",dni)
      if not client:
        gotoxy(13,8);print(f"{red_color}El cliente no existe. 😡​");time.sleep(2)
        gotoxy(13,8);print(' '*25)
        continue
      gotoxy(5,9);print(f"{purple_color}Fecha: {cyan_color}{datetime.now()}")
      gotoxy(56,7);print(purple_color+"Subtotal : ")
      gotoxy(56,8);print(purple_color+"Descuento: ")
      gotoxy(76,7);print(purple_color+"Iva      : ")
      gotoxy(76,8);print(purple_color+"Total    : ")
      client = client[0]
      if client["tipo"] == "VIP":
        cli = VipClient(client["nombre"],client["apellido"], client["dni"])
      else:
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True)
      gotoxy(56,9);print(purple_color+f"Usuario: {red_color}{client['tipo']}")
      sale = Sale(cli)
      gotoxy(5,8);print(f'{purple_color}Usuario: {yellow_color}{cli.fullName()}')
      gotoxy(2,10);print(red_color+"--"*64+reset_color) 
      gotoxy(5,11);print(purple_color+"Línea"+blue_color) 
      gotoxy(12,11);print(purple_color+"ID_Artículo"+blue_color) 
      gotoxy(24,11);print(purple_color+"Descripción"+blue_color) 
      gotoxy(38,11);print(purple_color+"Precio"+blue_color) 
      gotoxy(48,11);print(purple_color+"Cantidad"+blue_color) 
      gotoxy(58,11);print(purple_color+"Subtotal"+blue_color)
      gotoxy(68,11);print(red_color +"| Finaliar Venta (n) | Continuar (ENTER) | Reingresar (z) | " +blue_color)
      loop_principal = True
      default = 1
      while loop_principal:
        line = 12 + default
        gotoxy(7,line);print(default)
        gotoxy(15,line);
        id = validar.solo_numeros('', f"{red_color}ERROR: Solo números. ​😠​{red_color}",15,line)
        json_file = JsonFile(path+'/archivos/products.json')
        prods = json_file.find("id",id)
        if not prods:
          gotoxy(15,line);print("- El producto no existe. 🥶​");time.sleep(2)
          gotoxy(15,line);print(' ' * 120)
          continue
        prods = prods[0]
        product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
        gotoxy(24,line);print(product.descrip)
        gotoxy(38,line);print(product.preci)
        qyt = validar.solo_numeros('',f"{red_color}ERROR: Solo números. ​😠{reset_color}",49,line)
        gotoxy(59,line);print(product.preci*qyt)
        gotoxy(77,line);key_pressed = input().lower()
        if key_pressed == "z": 
          gotoxy(15,line);print(' ' * 140)
          continue
        else:
          sale.add_detail(product,qyt)
          gotoxy(67,7);print(round(sale.subtotal,2))
          gotoxy(67,8);print(round(sale.discount,2))
          gotoxy(87,7);print(round(sale.iva,2))
          gotoxy(87,8);print(round(sale.total,2))
          gotoxy(76,line);print(green_color+"Well Done ✔"+blue_color) 
          default += 1
          line += 1
          if key_pressed == "n":        
            line += 1
            while True:
              gotoxy(5,line);print(cyan_color + f"| ¿Está seguro de grabar la venta? (s/n) | - Ingresar más productos: (z) |")
              gotoxy(82,line);procesar = input().lower()
              gotoxy(5,line);print(' '*120)
              if procesar == "s":
                gotoxy(25,line+1);print(yellow_color + "✅​ Venta realizada exitosamente. 😊");time.sleep(2)
                # print(sale.getJson())
                json_file = JsonFile(path+'/archivos/invoices.json')
                invoices = json_file.read()
                ult_invoices = invoices[-1]["factura"]+1
                data = sale.getJson()
                data["factura"]=ult_invoices
                invoices.append(data)
                json_file = JsonFile(path+'/archivos/invoices.json')
                json_file.save(invoices)
                time.sleep(3)
                loop_principal = False
                break
              elif procesar =="n":
                gotoxy(25,line);print(red_color + "- Venta Cancelada 🤣")    
                time.sleep(2)
                loop_principal = False
                break
              elif procesar =="z":
                gotoxy(25,line);print(green_color + "- Ingrese Productos Nuevamente 🤑​" + blue_color);time.sleep(2)
                gotoxy(25,line);print(' ' * 120)
                break
              else:
                gotoxy(90,line);print(red_color + '- ¡Ingrese una opción valida! 😤​');time.sleep(2)
                gotoxy(90,line);print(' ' * 80)
      if not loop_principal:
        break 
  borrarPantalla()

  def update(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      validar = Valida()
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "︵ ‿ ︵ ‿ ︵＼ʕ •ᴥ•ʔ／︵ ‿ ︵ ‿ ︵"*3)
      gotoxy(25,3);print(red_color + '🔴 ACTUALIZAR INFO. DE FACTURA 🔴')
      gotoxy(4,5);print(f"{stick}{cyan_color}Ingrese '1' para actualizar una factura  {stick}{cyan_color}Presione ENTER para salir  {stick} ")
      gotoxy(84,5);option=input(yellow_color);
      if option == "1":
        gotoxy(4,5);print(' '*120)
        while True:
          invoice = validar.solo_numeros(f"{purple_color}- Ingrese Factura: {yellow_color}",f'{red_color}​ ERROR: Debe ingresar el número de la factura. 😒​ {reset_color}​',10,5)
          json_file = JsonFile(path+'/archivos/invoices.json')
          invoices = json_file.find("factura",invoice)
          if not invoices:
            gotoxy(10,7);print(f'{red_color}- La factura no existe. Intentelo nuevamente. 🥴​​');time.sleep(2)
            borrarPantalla()
            break
          for invoice_data in invoices:
            gotoxy(10,5);print(' '*120)
            gotoxy(10,5);print(purple_color+ '- número de factura: '.upper() + yellow_color + f'{invoice}')
            gotoxy(10,7);print(f"{cyan_color}- Fecha: {yellow_color}{invoice_data['Fecha']}")
            gotoxy(10,8);print(f"{cyan_color}- Cliente: {yellow_color}{invoice_data['cliente']}")
            json_file_clients = JsonFile(path + '/archivos/clients.json')
            cli = json_file_clients.read()
            for factura in invoices:
              nombre_apellido_cliente = factura['cliente'].split()
              dni_cliente = None
              for cliente in cli:
                if nombre_apellido_cliente[0] in cliente['nombre'] and nombre_apellido_cliente[-1] in cliente['apellido']:
                  dni_cliente = cliente['dni']
                  break  
              if dni_cliente:
                gotoxy(10,9);print(f"{cyan_color}- DNI: {yellow_color}{dni_cliente}")
              else:
                  print(f"No se encontró el DNI del cliente para la factura {factura['factura']}")
            gotoxy(50,5);print(f'{purple_color}- ACTUALIZAR:')
            new_date = validar.solo_fecha(f"{cyan_color}- Nueva fecha (YYYY-MM-DD): {yellow_color}",f"{red_color}- Ingrese fecha en el formato correcto. 😐   ", 50,7)
            invoice_data['Fecha'] = new_date
            while True:
              json_file = JsonFile(path+'/archivos/clients.json')
              gotoxy(50,9);new_client_dni = input(f"{cyan_color}- DNI: {yellow_color}")
              clients = json_file.read()
              filtered_clients = filter(lambda client: client['dni'] == new_client_dni, clients)
              found_clients = list(filtered_clients)
              if found_clients:
                client = found_clients[0]
                invoice_data['cliente'] = f"{client['nombre']} {client['apellido']}"
                gotoxy(50, 8);print(f'{cyan_color}- Cliente: {yellow_color}{invoice_data["cliente"]}')
                break
              else:
                  gotoxy(50, 9)
                  print(f"{red_color}- ERROR: Usuario no encontrado. Intentelo de nuevo. 😨​{yellow_color}")
                  time.sleep(2)
                  gotoxy(50, 9)
                  print(' '*80)
                  continue
          gotoxy(2, 11);print(f"{purple_color}{'ID Producto':<15} {'Descripcion':<15} {'Precio':<10} {'Cantidad':<10} {red_color} {'| Finalizar (n)  | Continuar (ENTER)| Reingresar (z) |'}{yellow_color}")
          line=12
          invoice_data['detalle'] = []
          loop_principal = True
          while loop_principal:
            try:
              gotoxy(2,line);new_product = int(input())
              json_file = JsonFile(path+'/archivos/products.json')
              prods = json_file.find("id",new_product)
              if not prods:
                gotoxy(15,line);print("Producto no existe")
                gotoxy(15,line);print(' ' * 20)
                continue
              prods = prods[0]
              product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
              gotoxy(18,line);print(product.descrip)
              gotoxy(34,line);print(product.preci)
              new_quantity = validar.solo_numeros('',"ERROR: Solo números positivos y enteros. ​😠",48,line)
              gotoxy(62,line);option_x = input()
              gotoxy(62, line);print(' '*120)
              if option_x == "z":
                gotoxy(12, line);print(" "*120)
                continue
              elif option_x == "n":
                if prods:
                  gotoxy(76,line);print(green_color+"Well Done ✔"+blue_color) 
                  invoice_data['detalle'].append({'producto': prods['descripcion'], 'precio': prods['precio'], 'cantidad': new_quantity})
                  gotoxy(60, line);print(green_color + 'Well Done ✔️' + yellow_color)
                  gotoxy(10, line + 1);option_z = input('| ¿Desea guardar cambios? (s/n) | Agregar más cambios (z) |')
                  gotoxy(10, line + 1);print(' '*120)
                  if option_z.lower() == 's':
                    json_file.update_invoice(invoice_data)
                    json_file.replace(path + '/archivos/invoices.json', invoices)
                    line += 1
                    gotoxy(10, line);input(yellow_color + '✅ Cambios actualizados correctamente. Presione ENTER para salir. 😌 ​')
                    borrarPantalla()
                    loop_principal = False
                    break
                  elif option_z.lower() == 'z':
                    line += 1
                    continue
                  else:
                    line += 1
                    gotoxy(10, line);input(red_color + '- CANCELAR: No se realizaron cambios. Presione ENTER para salir. 🙃​')
                    borrarPantalla()
                    loop_principal = False
                    break
                else:
                  gotoxy(2, line);print('​- ERROR: No existe esa ID. Intentelo de nuevo. 🤥​');time.sleep(3)
                  gotoxy(2, line);print(" "*120)
                break
              else:
                if product:
                  invoice_data['detalle'].append({'producto': prods['descripcion'], 'precio': prods['precio'], 'cantidad': new_quantity})
                  gotoxy(60, line);print(green_color + 'Well Done ✔️' + yellow_color)
                  line += 1
                else:
                  gotoxy(2, line);print('- ERROR: No existe esa ID. Intentelo de nuevo. 🤥​');time.sleep(2)
                  gotoxy(2, line);print(" "*120)
                  continue
            except ValueError:
              gotoxy(12, line);print('- Ingrese opciones validas... 😤​');time.sleep(1)
              gotoxy(12, line);print(" "*80)  
          if not loop_principal:
            break
      else:
        gotoxy(20, 7);print(f'{red_color}- Regresando al menú principal. 😌​​​');time.sleep(1)
        break
  borrarPantalla()
    
  def delete(self):
    stick = f'{red_color}| - {reset_color}'
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color +'|' +"‿ ︵ ‿ ︵( ಥ ﹏ಥ ) ‿ ︵ ‿ ︵ | "*4)
      gotoxy(30,3);print(red_color+"🔴 ELIMINAR FACTURAS 🔴")
      gotoxy(4,5);print(f"{stick}{cyan_color}Ingrese '1' para eliminar una factura en específico  {stick}{cyan_color}Ingrese '2' para eliminar todas las facturas  ")
      gotoxy(4,6);option = input(f"{stick}{cyan_color}Presione ENTER para salir                            {stick}")
      if option == "1":
        gotoxy(4,5);print(' '*120)
        gotoxy(4,6);print(' '*120)
        while True:
          gotoxy(10,5);invoice= validar.solo_numeros(f"{purple_color}- Ingrese número de factura: {yellow_color}", f'{red_color}ERROR: ¡Debe ingresar un número! 🤬​', 10,5)
          json_file = JsonFile(path+'/archivos/invoices.json')
          invoices = json_file.find("factura",invoice)
          if invoices:
            gotoxy(10,5);print("  "*120)
            json_file.print_all_invoices(invoices)
            gotoxy(1,5);print(' '*190)
            gotoxy(5,5);delete = input(f"{stick}Ingrese 'x' para eliminar la factura {stick}Presione ENTER para salir {stick} ")
            if delete.lower() == 'x':
              gotoxy(1,5);print(' '*120)
              gotoxy(10,5);confirm = input(f"{blue_color}- ¿Está seguro de eliminar esta factura? (s/n) 🥶​")
              if confirm.lower() == 's':
                json_file = JsonFile(path+'/archivos/invoices.json')
                json_file.delete("factura", invoice)
                gotoxy(5,5);print(' '*190)
                gotoxy(5,5);input(f"{yellow_color}✅​ Factura eliminada exitosamente. Presione ENTER para salir. 😳   ​")
                borrarPantalla()
                break
              else:
                gotoxy(5,5);print(' '*190)
                gotoxy(5,5);print(f'{red_color}- Regresando al menú principal. 😌​​​');time.sleep(1)
                borrarPantalla()
                break
            else:
                gotoxy(5,5);print(' '*190)
                gotoxy(5,5);print(f'{red_color}- Regresando al menú principal. 😌​​​');time.sleep(1)
                borrarPantalla()
                break
          else:
            gotoxy(10,5);print(f'{red_color}- Busqueda sin éxito. Intentelo nuevamente. 😵​');time.sleep(2)
            gotoxy(10,5);print(" "*80)
          break
      elif option == "2":
        gotoxy(4,5);print(' '*120)
        gotoxy(4,6);print(' '*120)
        gotoxy(20,5);delete = input(f"{red_color}⚡​ ¿Está seguro de eliminar todas las facturas? (s/n) ⚡    ​")
        if delete.lower() == 's':
          gotoxy(25,6);confirm = input(f'💀​ ¿Está seguro de estar seguro? (s/n) 💀   ​')
          if confirm.lower() == 's':
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.delete_all()
            gotoxy(10,8);input(f'{yellow_color}✅​​ Todas las facturas han sido eliminadas. Presione ENTER para salir 💣  ​')
            borrarPantalla()
            break
          else:
            gotoxy(30,7);print(f'{red_color}- Regresando al menú principal. 😌​​​');time.sleep(1)
            borrarPantalla()
            break
        else:
          gotoxy(20,7);print(f'{red_color}- Regresando al menú principal. 😌​​​');time.sleep(1)
          borrarPantalla()
          break
      else:
        gotoxy(10,8);print('- Regresando al menú principal... 😌');time.sleep(1)
        break
  borrarPantalla()

  def consult(self):
    stick = f'{red_color}| - {reset_color}'
    line_div = f"{green_color}{"-" * 80}{reset_color}"
    while True:
      print('\033c', end='')
      gotoxy(2,1);print(purple_color + "●～●～●～●～●～●～●～●～"*5)
      gotoxy(20,3);print(purple_color+"🔴​​​ CONSULTAR INFO. DE VENTAS 🔴")
      gotoxy(4,5);print(f"{stick}{cyan_color}Ingrese '1' para hallar una factura                {stick}{cyan_color}Ingrese '2' para mostrar todas las facturas")
      gotoxy(4,6);print(f"{stick}{cyan_color}Ingrese '3' para mostrar las facturas de x cliente {stick}{cyan_color}Ingrese '4' para obtener información general")
      gotoxy(4,7);option = input(f"{stick}{cyan_color}Presione ENTER para salir                          {stick}{yellow_color}");
      json_file = JsonFile(path+'/archivos/invoices.json')
      if option == "1":
        while True:
          gotoxy(4,5);print(" "*120);gotoxy(4,6);print("  "*120);gotoxy(4,7);print("  "*120);gotoxy(4,8);print(" "*120)
          invoice = validar.solo_numeros(f"{purple_color}- Ingrese Factura: {yellow_color}",f'{red_color}- ERROR: Debe ingresar solo números. 🤬​',10,5)
          gotoxy(10,5);print("  "*20)
          invoices = json_file.find("factura",invoice)
          if invoices:
            json_file.print_all_invoices(invoices)
            break
          else:
            gotoxy(10,7); print(f'{red_color}Busqueda sin éxito. Intentelo nuevamente. 😵​');time.sleep(2)
            borrarPantalla()
          break
      elif option == "2":
        while True:
          gotoxy(4,5);print(" "*120);gotoxy(4,6);print("  "*120);gotoxy(4,7);print("  "*120);gotoxy(4,8);print(" "*120)
          invoices = json_file.read()
          if invoices:
            json_file.print_all_invoices(invoices)
            break
          else:
            gotoxy(10, 5);print(f"{red_color}No hay facturas disponibles.")
            input(f"{blue_color}Presione ENTER para salir. 😵​​​​")
            borrarPantalla()
          break
      elif option == "3":
        gotoxy(4,5);print(" "*120);gotoxy(4,6);print("  "*120);gotoxy(4,7);print("  "*120);gotoxy(4,8);print(" "*120)
        while True:
          gotoxy(10,5);client_name = input(f"{cyan_color}Ingrese nombre del cliente: {yellow_color}")
          invoices = json_file.find("cliente", client_name)
          if invoices:
            json_file.print_all_invoices(invoices)
            borrarPantalla()
            break
          else:
            gotoxy(10,5);print(' '*120)
            gotoxy(10,5);print(f"{red_color}- ¡No se encuentran resultados de facturas para el cliente '{client_name}'! 😫​");time.sleep(2)
            gotoxy(10,5);print(" "*80)
          break
      elif option == "4":
        gotoxy(4,5);print(" "*120);gotoxy(4,6);print("  "*120);gotoxy(4,7);print("  "*120);gotoxy(4,8);print(" "*120)
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoices = json_file.read()
        gotoxy(15,5);print(f"{cyan_color}Información general de ventas: {yellow_color}");gotoxy(4,6);print(line_div)
        total_clientes = len(set([i["cliente"] for i in invoices]));
        gotoxy(10,7);print(f'{yellow_color}- Total de clientes: {green_color}{total_clientes}');gotoxy(4,8);print(line_div)
        suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), invoices,0)
        gotoxy(10,9);print(f'{yellow_color}- Suma total de ventas: {green_color}{suma}');gotoxy(4,10);print(line_div)
        totales_map = list(map(lambda invoice: invoice["total"], invoices))
        max_invoice = max(totales_map)
        gotoxy(10,11);print(f'{yellow_color}- Máximo total de una factura: {green_color}{max_invoice}');gotoxy(4,12);print(line_div)
        min_invoice = min(totales_map)
        gotoxy(10,13);print(f'{yellow_color}- Mínimo total de una factura: {green_color}{min_invoice}');gotoxy(4,14);print(line_div)
        gotoxy(10,15);print(f'{yellow_color}- Lista de totales de todas las facturas:')
        line = 16
        for i in totales_map:
          gotoxy(10,line);print(green_color, i)
          line += 1
        line += 1
        gotoxy(4, line);print(line_div)
        gotoxy(8,line+1);input(f"{yellow_color}✅ Presione ENTER para regresar al menú principal. 😉​");borrarPantalla()
      else:
        gotoxy(10,9);print('- Regresando al menú principal... 😌');time.sleep(1)
        break
  borrarPantalla()
      
      
#Menu Proceso Principal
opc=''
while opc !='4':  
  borrarPantalla()
  arrow = blue_color +'➽───────────────❥' + yellow_color
  message = purple_color + '💻​ SISTEMA DE FACTURAS 💻​' + yellow_color
  menu_main = Menu(message,[f"1) Clientes  {arrow} 🧔​​",f"2) Productos {arrow} 🛒",f"3) Ventas    {arrow} 💵",f"4) Salir     {arrow} 🛫"],20,10)
  opc = menu_main.menu()
  options = [f"1) Ingresar   {arrow} 🗿",f"2) Actualizar {arrow} ​📣​",f"3) Eliminar   {arrow} ​🗑️",f"4) Consultar  {arrow} ​​🔍​",f"5) Salir      {arrow} 🛫​"]
  if opc == "1":
    opc1 = ''
    while opc1 !='5':
      borrarPantalla()
      clients = CrudClients()
      message = purple_color + '🧙​ MENÚ CLIENTES 🧙​' + yellow_color
      menu_clients = Menu(message,options,20,10)
      opc1 = menu_clients.menu()
      if opc1 == "1":
        clients.create();time.sleep(1)
      elif opc1 == "2":
        clients.update();time.sleep(1)
      elif opc1 == "3":
        clients.delete();time.sleep(1)
      elif opc1 == "4":
        clients.consult();time.sleep(1)
      print("Regresando al menu Clientes...")
      # time.sleep(2)            
  elif opc == "2":
    opc2 = ''
    while opc2 !='5':
      borrarPantalla()    
      message = purple_color + '​🚚​​ MENÚ PRODUCTOS ​🚚​​' + yellow_color
      product = CrudProducts()
      menu_products = Menu(message,options,20,10)
      opc2 = menu_products.menu()
      if opc2 == "1":
        product.create();time.sleep(1)
      elif opc2 == "2":
        product.update();time.sleep(1)
      elif opc2 == "3":
        product.delete();time.sleep(1)
      elif opc2 == "4":
        product.consult();time.sleep(1)

  elif opc == "3":
    opc3 =''
    while opc3 !='5':
      borrarPantalla()
      message = purple_color + '​💵​​​ MENÚ VENTAS ​💵​' + yellow_color
      sales = CrudSales()
      menu_sales = Menu(message,options,20,10)
      opc3 = menu_sales.menu()
      if opc3 == "1":
        sales.create();time.sleep(1)
      elif opc3 == "2":
        sales.update();time.sleep(1)
      elif opc3 == "3":
        sales.delete();time.sleep(1)
      elif opc3 == "4":
        sales.consult();time.sleep(1)
  print("Regresando al menu Principal...")
  # time.sleep(2)            

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()
