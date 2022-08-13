from sqlalchemy.orm import Session
from sqlalchemy import select
from modelo import Palabra
from dbConfig import get_engine

engine = get_engine('root','admin','localhost',3306,'diccionario')
session = Session(engine)

opcion = -1
while opcion != 0:
  print('========= MENU ========')
  print('[1] Mostrar')
  print('[2] Agregar')
  print('[3] Actualizar')
  print('[4] Eliminar')
  print('[5] Buscar')
  print('[0] Salir')
  opcion = int(input('Opcion: '))

  if opcion == 1:
    lista = [i for i in session.scalars(select(Palabra))]
    if len(lista) == 0:
      print('No hay palabras!')
    else:
      for i in lista:
        print('-'*30)
        print(i)

  elif opcion == 2:
    palabra = Palabra(
      nombre = input('Nombre: ').lower(),
      significado = input('Significado: ').lower()
    )
    session.add(palabra)
    session.commit()
    print('Palabra agregada!')

  elif opcion == 3:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra:Palabra = session.scalar(select(Palabra).where(Palabra.nombre == nombre))
    if palabra:
      palabra.significado = input('Ingrese el nuevo significado: ')
      session.commit()
      print('Palabra actualizado!')
    else:
      print('La palabra no existe!')
  
  elif opcion == 4:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra:Palabra = session.scalar(select(Palabra).where(Palabra.nombre == nombre))
    if palabra:
      session.delete(palabra)
      session.commit()
      print('Palabra eliminada!')
    else:
      print('La palabra no existe!')
  
  elif opcion == 5:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra:Palabra = session.scalar(select(Palabra).where(Palabra.nombre == nombre))
    if palabra:
      print(palabra)
    else:
      print('La palabra no existe!')