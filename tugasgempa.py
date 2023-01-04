class Gempa:
  def __init__(self, lokasi, skala):
    self.lokasi = lokasi
    self.skala = skala

  def dampak(self):
    if self.skala < 2.0:
      print(f"Skala Gempa = {self.skala}\nLokasi Gempa = {self.lokasi}\nDampak = Gempa tidak terasa.\n")
    elif self.skala >= 2.0 and self.skala < 4.0:
      print(f"Skala Gempa = {self.skala}\nLokasi Gempa = {self.lokasi}\nDampak = Bangunan retak-retak.\n")
    elif self.skala >= 4.0 and self.skala < 6.0:
      print(f"Skala Gempa = {self.skala}\nLokasi Gempa = {self.lokasi}\nDampak = Bangunan roboh.\n")
    elif self.skala >= 6.0 and self.skala < 10.0:
      print(f"Skala Gempa = {self.skala}\nLokasi Gempa = {self.lokasi}\nDampak = Bangunan roboh dan berpotensi tsunami.\n")

