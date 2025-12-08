import random

class Arma:
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        # # QUI devi usare i setter (property) invece di assegnare direttamente
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
        # Solo controlla che sia >= 1
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
        # Check 1: sia >= 1
        if nuovo_danno_massimo < 1:
            raise ValueError("Il danno massimo deve essere >= 1")
        
        # Check 2: sia >= danno_minimo
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
        if valore not in ["mischia", "distanza"]:
            raise ValueError("Il ")
        # # accetta solo "mischia" o "distanza"
        pass

    # ===========================
    # IMMUATO: questo va bene
    # ===========================
    def get_danno(self) -> int:
        return random.randint(self.__danno_minimo, self.__danno_massimo)

    def __str__(self):
        return f"{self.__nome} ({self.__danno_minimo}–{self.__danno_massimo} dmg, tipo: {self.__tipo})"

