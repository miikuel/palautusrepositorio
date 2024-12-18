KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if kapasiteetti < 0 or kasvatuskoko < 0:
            raise ValueError("Kapasiteetti ja kasvatuskoko eivät voi olla negatiivisia")
        self.kapasiteetti = KAPASITEETTI
        self.kasvatuskoko = OLETUSKASVATUS
        self.lista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        if n in self.lista[:self.alkioiden_lkm]:
            return True
        return False

    def lisaa(self, n):

        if self.alkioiden_lkm == 0:
            self.lista[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.lista[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.lista) == 0:
                taulukko_old = self.lista
                self.kopioi_lista(self.lista, taulukko_old)
                self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.lista)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(self.alkioiden_lkm):
            if n == self.lista[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lista[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.lista[j]
                self.lista[j] = self.lista[j + 1]
                self.lista[j + 1] = apu

            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lista[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lista[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
