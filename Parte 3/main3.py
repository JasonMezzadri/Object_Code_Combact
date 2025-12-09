from classe_personaggio3 import Personaggio
from classe_arma3 import Arma
from classe_pozione3 import Pozione
import random

if __name__ == "__main__":
    print("=== SIMULAZIONE COMBATTIMENTO — PARTE 3 ===\n")

    # ------------------------------------------------------
    # CREAZIONE PERSONAGGI
    # ------------------------------------------------------
    p1 = Personaggio("Gimli", 50, random.randint(8, 18), random.randint(8, 18))
    p2 = Personaggio("Legolas", 45, random.randint(8, 18), random.randint(8, 18))

    print(f"{p1.nome}: Forza={p1.forza}, Destrezza={p1.destrezza}")
    print(f"{p2.nome}: Forza={p2.forza}, Destrezza={p2.destrezza}\n")

    # ------------------------------------------------------
    # EQUIPAGGIO ARMI
    # ------------------------------------------------------
    if p1.forza >= p1.destrezza:
        arma1 = Arma("Spada a due mani", 8, 15, "mischia")
    else:
        arma1 = Arma("Arco", 6, 12, "distanza")
    p1.arma = arma1

    if p2.forza >= p2.destrezza:
        arma2 = Arma("Ascia", 8, 14, "mischia")
    else:
        arma2 = Arma("Balestra", 8, 13, "distanza")
    p2.arma = arma2

    print(f"{p1.nome} equipaggia: {p1.arma}")
    print(f"{p2.nome} equipaggia: {p2.arma}\n")

    # ------------------------------------------------------
    # AGGIUNTA POZIONI — PARTE 3
    # ------------------------------------------------------

    # --- Pozioni di cura (due per personaggio)
    cura1 = Pozione("Pozione di Cura", "cura", 15)
    cura2 = Pozione("Pozione di Cura", "cura", 15)

    cura3 = Pozione("Pozione di Cura", "cura", 15)
    cura4 = Pozione("Pozione di Cura", "cura", 15)

    # --- Buff basato su caratteristica dominante
    if p1.forza >= p1.destrezza:
        buff1 = Pozione("Pozione della Forza", "buff_forza", 3)
    else:
        buff1 = Pozione("Pozione della Destrezza", "buff_destrezza", 3)

    if p2.forza >= p2.destrezza:
        buff2 = Pozione("Pozione della Forza", "buff_forza", 3)
    else:
        buff2 = Pozione("Pozione della Destrezza", "buff_destrezza", 3)

    # --- Assegno le pozioni (il setter controlla max 3 e tipo)
    p1.pozioni = [cura1, cura2, buff1]
    p2.pozioni = [cura3, cura4, buff2]

    print(f"{p1.nome} ottiene 3 pozioni.")
    print(f"{p2.nome} ottiene 3 pozioni.\n")

    # ------------------------------------------------------
    # COMBATTIMENTO
    # ------------------------------------------------------
    print("=== INIZIO COMBATTIMENTO ===\n")

    turno = 1
    while p1.e_vivo() and p2.e_vivo():
        print(f"--- Turno {turno} ---")

        # =======================
        # TURNO DI p1
        # =======================
        poz = p1.decidi_se_usare_pozione(p2)
        if poz is not None:
            print(f"{p1.nome} usa {poz.nome}!")
            p1.usa_pozione(poz)

        danno1 = p1.attacca(p2)
        print(f"{p1.nome} attacca {p2.nome} e infligge {danno1} danni!")
        print(p2, "\n")

        if not p2.e_vivo():
            break

        # =======================
        # TURNO DI p2
        # =======================
        poz = p2.decidi_se_usare_pozione(p1)
        if poz is not None:
            print(f"{p2.nome} usa {poz.nome}!")
            p2.usa_pozione(poz)

        danno2 = p2.attacca(p1)
        print(f"{p2.nome} attacca {p1.nome} e infligge {danno2} danni!")
        print(p1, "\n")

        # =======================
        # FINE ROUND → aggiorna buff
        # =======================
        p1.aggiorna_buff()
        p2.aggiorna_buff()

        turno += 1

    print("=== FINE COMBATTIMENTO ===\n")

    # ------------------------------------------------------
    # RISULTATI
    # ------------------------------------------------------
    if not p1.e_vivo() and not p2.e_vivo():
        print("Pareggio! Entrambi sono caduti in battaglia.")
    elif p1.e_vivo():
        print(f"🏆 {p1.nome} vince il combattimento! {p1}")
    else:
        print(f"🏆 {p2.nome} vince il combattimento! {p2}")
