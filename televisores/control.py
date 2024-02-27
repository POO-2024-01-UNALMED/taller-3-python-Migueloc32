class Control:
  def __init__(self):
      self._tv = None

  def canalUp(self):
      if self._tv:
          self._tv.setCanal(self._tv.getCanal() + 1)

  def canalDown(self):
      if self._tv:
          self._tv.setCanal(self._tv.getCanal() - 1)

  def volumenUp(self):
      if self._tv:
          self._tv.setVolumen(self._tv.getVolumen() + 1)

  def volumenDown(self):
      if self._tv:
          self._tv.setVolumen(self._tv.getVolumen() - 1)

  def enlazar(self, tv):
      self._tv = tv
      tv.setControl(self)

  def turnOn(self):
      if self._tv:
          self._tv.turnOn()

  def turnOff(self):
      if self._tv:
          self._tv.turnOff()

  def setCanal(self, canal):
      if self._tv:
          self._tv.setCanal(canal)

  def setVolumen(self, volumen):
      if self._tv:
          self._tv.setVolumen(volumen)

  def getTv(self):
      return self._tv

  def setTv(self, tv):
      self._tv = tv