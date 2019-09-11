#TODO: 
# [] Leer archivo
# [] Leer csv
# [] Excepciones


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
    def __init__(self, filepath=""):
        self._filepath = filepath

    def setFile(self, filepath):
        ''''@param   '''
        self._filepath = filepath


    