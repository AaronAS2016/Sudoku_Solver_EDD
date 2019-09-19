import csv
from reader import Reader
from solver import Solver
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
        sudoku = Solver()

        while not salir:
            print ('1) Ingresar la ruta del archivo')
            print ('2) Guardar la ejecucion parcial')
            print ('3) recuperar ejecucion parcial y continuarla')
            print ('4) Salir')
            print ("Elija la opcion que desee ejecutar")

            opcion = self.pedir_numero()

            if opcion == 1:
                filePath = input("Ingrese la ruta del archivo aqui:")
                reader = Reader(filePath, ',')
                board = reader.readFileAsCSV()
                board_fixed = [[int(num) for num in sub] for sub in board]
                sudoku.print_board(board)
                print("\n")
                print("-------SOLUCION---------")
                print("\n")
                sudoku.print_board(sudoku.solve(board_fixed))

                opcion2 = input("¿Desea guardar los resultados en un archivo csv? (Y/N)")

                if opcion2 == 'y':
                    filePath2 = input("ingrese la ruta donde quiera guardar el archivo:")
                    datos = [sudoku.print_board(board)]
                    csvsalida = open('salidat.csv', 'w', newline='')
                    salida = csv.writer(csvsalida)
                    salida.writerows(datos)
                    del salida
                    csvfile.close()
                    salir = True
                else:
                    salir = True



            elif opcion == 2:
                print ("Opcion 2")


            elif opcion == 3:
                print("Opcion 3")


            elif opcion == 4:
                salir = True


            else:
                print ("Introduce un numero entre 1 y 4")

        print ("Fin")
    








