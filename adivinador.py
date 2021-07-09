import random
def calcular_random(**dato):
  ini = int(dato["I"])
  end = int(dato["F"])
  print("Rango(%d, %d)" % (ini, end))
  valor = random.randint(ini, end)
  return valor
print ("JUEGO DE ADIVINANZAS")
print ("=======================")
salir = ""
while salir != "s":
  entrada = input("(*) Favor ingrese un numero de 0 a 100: ")
  try:
    numero = int(entrada)
  except ValueError:
    numero = -1  
  if numero >= 0 and numero <= 100:
    estimacion = ""
    sugerido = 0
    encontrado = 0
    intento = 0
    inicio = 0 
    primero = 0
    fin = 100
    ultimo = 100      
    print("De acuerdo a las opciones a continuacion, favor indiquenos si la suposicion sugerida es:")
    print("a) Demasiado alta, b) Demasiado baja, c) Acertado :")
    while encontrado != 1 and salir != "s":
      sugerido = calcular_random(I = inicio, F = fin)
      intento = intento + 1
      print("Numero sugerido por el programa es: %d." % sugerido)
      estimacion = str(input("(*) Ingrese opcion :"))    
      if estimacion == "a":
        #inicio = 0 
        fin = sugerido  
        ultimo = fin
        if(primero > inicio):
          inicio = primero  
      elif estimacion == "b": 
        inicio = sugerido
        primero = inicio
        #fin = 100
        if(ultimo < fin):
          fin = ultimo
      elif estimacion == "c":
        if sugerido == numero:
          print("El programa logro adivinar, el numero ingresado es: %d." % numero)
          print("Num de intentos %d \n " % intento)
          encontrado = 1
        else:
          salir = str(input("No has acertado aun, para salir presione (s), para continuar (enter) :"))
          inicio = 0
          primero = 0
          fin = 100
          ultimo = 100 
      else:
        print ("Numero no encontrado, vuelva a jugar!!: ")
        inicio = 0
        primero = 0
        fin = 100
        ultimo = 100     
    #ingrese opcion de salir
    salir = str(input("Para salir presione (s), para continuar (enter) :"))
  else:
    print("Warning!! debe ingresar un numero entero en el rango de 0 a 100 ")
    salir = str(input("Para salir presione (s), para continuar (enter) :"))