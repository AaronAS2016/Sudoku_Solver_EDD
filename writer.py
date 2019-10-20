import csv
import os


class Writer:

    def __init__(self, result_file_path="", file_data=""):
        self._result_file_path = result_file_path
        self._file_data = file_data

    def check_names(self, path):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname)

    def setData(self, data):
        self._file_data = data

    def setResultPath(self, path):
        self._result_file_path = path

    def writeAsCSV(self, path=None, data=None):

        if path is None:
            path = self._result_file_path
        if data is None:
            data = self._file_data

        try:
            with open(path, 'w') as csvWriter:
                writter = csv.writer(csvWriter)
                writter.writerows(data)
        except ValueError:
            print("Ocurrio un errro al intentar escribir el archivo: " + ValueError)

# Tests caseros


# TEST NRO1: CASO OK

listaTest = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 2, 34, 34, 5, 6, 7, 8, 2]
]

escritor = Writer('resources/test.csv', listaTest)
escritor.writeAsCSV()

# TEST NRO2: CASO NO OK

# escritor.setResultPath('C://asdmsadksa//aidhasdhsa////rutaquenoexi/steniagancho')
# escritor.writeAsCSV()

# TODO:
# []: Corregir TEST NRO2 (Opcional)
