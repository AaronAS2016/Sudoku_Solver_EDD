class Writer:

    def __init__(self, result_file_path="", file_data=""):
        self._result_file_path = result_file_path
        self._file_data = file_data

    def setData(self, data):
        self._file_data = data
    
    def setResultPath(self,path):
        self._result_file_path = path
    
    def write(self, path=None, data=None):

        if path is None:
            path = self._result_file_path
        if data is None:
            data = self._file_data
    
        #TODO: Completar funcionalidad para escribir en un archivo