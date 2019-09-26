# TODO:
# [] Leer archivo
# [X] Leer csv
# [X] Excepciones
# [] Completar docs

import os
import csv


class Reader():
    """
    A class to read Files

    Attributes
    ----------

    filepath : str
        the path of the file that want to read

    Methods
    ----------

    setFile(filepath)
        change the Path of the class

    readFile
        return the content of the file

    readFileAsCSV
        return the content of the file of a csv


     """

    def __init__(self, filepath="", delimiter=","):
        self._filepath = filepath
        self._delimiter = delimiter

    def setDelimiter(self, delimiter):
        self._delimiter = delimiter

    def setFile(self, filepath):
        """
        Change the Path of the class

        Parameter
        --------

        filepath: str
            the new path of the file that want to read

        """
        self._filepath = filepath

    def checkIfExistFile(self):
        return os.path.exists(self._filepath)

    def readFileAsCSV(self, delimiter=None):

        # Use the default delimiter
        if delimiter is None:
            delimiter = self._delimiter

        if(self.checkIfExistFile()):

            try:
                with open(self._filepath, 'r') as readerCsv:
                    reader = csv.reader(readerCsv, delimiter=delimiter)
                    data = []
                    for row in reader:
                        data.append(row)

            except ValueError:
                print("Error trying to read the file: " + ValueError)
            return data
        else:
            print('Ups!, The filepath looks wrong, try to change the filepath')

# Test caseros


# Caso bueno
""" lector = Reader()
lector.setFile('resources/boards.csv')
print(lector.readFileAsCSV(',')) """

# Caso Malo
""" lector2 = Reader()
lector2.setFile('rutaquenoexisteniagancho')
print(lector2.readFileAsCSV()) """
