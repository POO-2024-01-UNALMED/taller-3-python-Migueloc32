class Control:
  def __init__(self):
      self._tv = None

  def canal_up(self):
      if self._tv:
          self._tv.set_canal(self._tv.get_canal() + 1)

  def canal_down(self):
      if self._tv:
          self._tv.set_canal(self._tv.get_canal() - 1)

  def volumen_up(self):
      if self._tv:
          self._tv.set_volumen(self._tv.get_volumen() + 1)

  def volumen_down(self):
      if self._tv:
          self._tv.set_volumen(self._tv.get_volumen() - 1)

  def enlazar(self, tv):
      self._tv = tv
      tv.set_control(self)

  def turn_on(self):
      if self._tv:
          self._tv.turn_on()

  def turn_off(self):
      if self._tv:
          self._tv.turn_off()

  def set_canal(self, canal):
      if self._tv:
          self._tv.set_canal(canal)

  def set_volumen(self, volumen):
      if self._tv:
          self._tv.set_volumen(volumen)

  def get_tv(self):
      return self._tv

  def set_tv(self, tv):
      self._tv = tv