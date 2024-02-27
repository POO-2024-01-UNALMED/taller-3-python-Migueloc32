class TV:
      _numTv = 0 

      def __init__(self, marca, estado):
          self._marca = marca
          self._canal = 1
          self._precio = 500
          self._estado = estado
          self._volumen = 1
          self._control = None
          TV._numTv += 1  

      def turnOn(self):
          self._estado = True

      def turnOff(self):
          self._estado = False

      def getEstado(self):
          return self._estado

      def setCanal(self, canal):
          if self.getEstado() and 1 <= canal <= 120:
              self._canal = canal

      def getCanal(self):
          return self._canal

      def canalUp(self):
          self.setCanal(self.getCanal() + 1)

      def canalDown(self):
          self.setCanal(self.getCanal() - 1)

      def setVolumen(self, volumen):
          if 0 <= volumen <= 7 and self.getEstado():
              self._volumen = volumen

      def getVolumen(self):
          return self._volumen

      def volumenUp(self):
          self.setVolumen(self.getVolumen() + 1)

      def volumenDown(self):
          self.setVolumen(self.getVolumen() - 1)

      def setControl(self, control):
          self._control = control

      def getControl(self):
          return self._control

      def setMarca(self, marca):
          self._marca = marca

      def getMarca(self):
          return self._marca

      def setPrecio(self, precio):
          self._precio = precio

      def getPrecio(self):
          return self._precio

      
      def getNumTv(cls):
          return cls._numTv

      
      def setNumTv(cls, numTv):
          cls._numTv = numTv