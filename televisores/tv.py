class TV:
      _num_tv = 0 

      def __init__(self, marca, estado):
          self._marca = marca
          self._canal = 1
          self._precio = 500
          self._estado = estado
          self._volumen = 1
          self._control = None
          TV._num_tv += 1  

      def turn_on(self):
          self._estado = True

      def turn_off(self):
          self._estado = False

      def get_estado(self):
          return self._estado

      def set_canal(self, canal):
          if self.get_estado() and 1 <= canal <= 120:
              self._canal = canal

      def get_canal(self):
          return self._canal

      def canal_up(self):
          self.set_canal(self.get_canal() + 1)

      def canal_down(self):
          self.set_canal(self.get_canal() - 1)

      def set_volumen(self, volumen):
          if 0 <= volumen <= 7 and self.get_estado():
              self._volumen = volumen

      def get_volumen(self):
          return self._volumen

      def volumen_up(self):
          self.set_volumen(self.get_volumen() + 1)

      def volumen_down(self):
          self.set_volumen(self.get_volumen() - 1)

      def set_control(self, control):
          self._control = control

      def get_control(self):
          return self._control

      def set_marca(self, marca):
          self._marca = marca

      def get_marca(self):
          return self._marca

      def set_precio(self, precio):
          self._precio = precio

      def get_precio(self):
          return self._precio

     
      def get_num_tv(cls):
          return cls._num_tv

      
      def set_num_tv(cls, num_tv):
          cls._num_tv = num_tv