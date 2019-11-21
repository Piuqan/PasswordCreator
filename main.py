#program generujacy hasło o długości podanej przez użytkownika
import random

def generacjahasla(znaki):
    znakiWielkie = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    znakiMale = "abcdefghijklmnopqrstuvwxyz"
    znakiNumeryczne = "0123456789"
    znakiSpecjalne = "!@#$%&*()[]{}"
    znakiWszystkie = znakiMale + znakiWielkie + znakiSpecjalne + znakiNumeryczne #lista wszystkich znaków
    haslo = ''
    for x in range(znaki): #tworzenie hasła
      haslo += random.choice(znakiWszystkie) #wybór losowego znaku do hasła
    print("Twoje wygenerowane hasło to : ",haslo)


try:
    znaki = int(input("Podaj liczbe znaków w haśle"))
    generacjahasla(znaki)
except:
    print("coś się spierdoliło")
