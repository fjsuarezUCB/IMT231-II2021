from array1D import Array

class Array2D:
    def __init__(self, nRows, nCols):
        self._filas = Array(nRows)
        
        for i in range(nRows):
            self._filas[i] = Array(nCols)

    def numRows(self):
        return len(self._filas)

    def numCols(self):
        return len(self._filas[0])

    def clear(self, v):
        for fila in self._filas:
            fila.clear(v)

    def __getitem__(self, ndIndex): # ndIndex[0] = i1, ndIndex[1] = i2
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        fila = ndIndex[0]
        columna = ndIndex[1]
        assert fila >= 0 and fila < self.numRows() \
            and columna >= 0 and columna < self.numCols(), \
                "Subíndices fuera  de rango"
        array_interno = self._filas[fila]
        return array_interno[columna]

    def __setitem__(self, ndIndex, v):
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        fila = ndIndex[0]
        columna = ndIndex[1]
        assert fila >= 0 and fila < self.numRows() \
            and columna >= 0 and columna < self.numCols(), \
                "Subíndices fuera  de rango"
        array_interno = self._filas[fila]
        array_interno[columna] = v