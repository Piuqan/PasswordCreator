#program generujacy hasło o długości podanej przez użytkownika
import random

def generacjahasla(znaki,numeryczne,specjalne):
    znakiWielkie = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    znakiMale = "abcdefghijklmnopqrstuvwxyz"
    znakiNumeryczne = "0123456789"
    znakiSpecjalne = "!@#$%&*()[]{}"
    znakiWszystkie = znakiMale + znakiWielkie
    if numeryczne == "T":
        znakiWszystkie += znakiNumeryczne
    if specjalne == "T":
        znakiWszystkie += znakiSpecjalne
    haslo = ''
    for x in range(znaki): #tworzenie hasła
      haslo += random.choice(znakiWszystkie) #wybór losowego znaku do hasła
    print("Twoje wygenerowane hasło to : ",haslo)


try:
    znaki = int(input("Podaj liczbe znaków w haśle"))
    numeryczne = input("Czy chcesz żeby użyć znaków numerycznych? T/N")
    specjalne = input("Czy chcesz żeby użyć znaków specjalnych? T/N")
    generacjahasla(znaki, numeryczne, specjalne)
except:
    print("Coś poszło nie tak, spróbuj ponownie")
