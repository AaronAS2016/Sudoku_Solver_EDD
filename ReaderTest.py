import unittest
from reader import Reader

reader = Reader()


class ReaderTestsMethod(unittest.TestCase):

    def test_leer_datos_del_lector_board_1(self):
        board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]

        reader.setFile('resources/boards.csv')
        self.assertEqual(reader.readFileAsCSV(','), board)

    def test_leer_tablero_que_no_existe_la_ruta(self):
        reader.setFile('rutaquenoexiste////....')
        # check that s.split fails when the separator is not a string
        with self.assertRaises(ValueError):
            reader.readFileAsCSV()


if __name__ == '__main__':
    unittest.main()
