class Menu():

    def pedir_numero(self):

        correcto = False

        while (not correcto):
            try:
                numero = int(input("Introduzca el numero de la opcion que desee ejecutar"))
                correcto = True
            except ValueError:
                print('Error, numero no valido. Introduzca el numero de la opcion que desee ejecutar')
            
        return numero

    def opciones(self):
        salir = False

        while not salir:
            print ('1) Ingresar la ruta del archivo')
            print ('2) Guardar la ejecucion parcial')
            print ('3) recuperar ejecucion parcial y continuarla')
            print ('4) Salir')
            print ("Elija la opcion que desee ejecutar")

            opcion = self.pedir_numero()

            if opcion == 1:
                input("Ingrese la ruta del archivo aqui:")

                


            elif opcion == 2:
                print ("Opcion 2")


            elif opcion == 3:
                print("Opcion 3")


            elif opcion == 4:
                salir = True


            else:
                print ("Introduce un numero entre 1 y 4")

        print ("Fin")
            







