import random

class Arma:
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        # QUI devi usare i setter (property) invece di assegnare direttamente
        self.nome = nome
        self.danno_minimo = danno_minimo
        self.danno_massimo = danno_massimo
        self.tipo = tipo


    # ===========================
    # PROPERTY nome
    # ===========================
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        if nuovo_nome == "":
            raise ValueError("Il nome non può essere vuoto")
        else:
            self.__nome = nuovo_nome


    # ===========================
    # PROPERTY danno_minimo
    # ===========================
    @property
    def danno_minimo(self):
        return self.__danno_minimo

    @danno_minimo.setter
    def danno_minimo(self, nuovo_danno_minimo):
        if nuovo_danno_minimo < 1:
            raise ValueError("Il danno minimo deve essere >= 1")
        self.__danno_minimo = nuovo_danno_minimo


    # ===========================
    # PROPERTY danno_massimo
    # ===========================
    @property
    def danno_massimo(self):
        return self.__danno_massimo

    @danno_massimo.setter
    def danno_massimo(self, nuovo_danno_massimo):
        if nuovo_danno_massimo < 1:
            raise ValueError("Il danno massimo deve essere >= 1")

        # ATTENZIONE: self.__danno_minimo esiste solo dopo che il setter minimo è chiamato
        if nuovo_danno_massimo < self.__danno_minimo:
            raise ValueError("Il danno massimo non può essere minore del danno minimo")

        self.__danno_massimo = nuovo_danno_massimo


    # ===========================
    # PROPERTY tipo
    # ===========================
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valore):
        # accetta solo "mischia" o "distanza"
        if valore not in ["mischia", "distanza"]:
            raise ValueError("Il tipo deve essere 'mischia' oppure 'distanza'")

        self.__tipo = valore


    # ===========================
    # IMMUATO: questo va bene
    # ===========================
    def get_danno(self) -> int:
        return random.randint(self.__danno_minimo, self.__danno_massimo)

    def __str__(self):
        return f"{self.__nome} ({self.__danno_minimo}–{self.__danno_massimo} dmg, tipo: {self.__tipo})"


