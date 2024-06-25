from pokemon_proxy import Pokemon_Proxy
from pokemon_model import Pokemon_Model
import random

class Controller:
  def __init__(self,proxy:Pokemon_Proxy):
    self.proxy = proxy
    self.pokemon_list = []
    self.pokemon_type_set = set()

  def openMenu(self):
    self.__randomizePokemonList()
    self.__extractType()
    while True:
      try:
        print("\nSocio socio, menú Pokemon super tocho\n\n"
              "   1. Mostrar Pokemonoide\n"
              "   2. Crear un socio Pokemon\n"
              "   3. Editación de Pokemon\n"  #To do
              "   4. Eliminar un Pikachu\n"   #To do
              "   5. Cerrar el super Menú\n")
        selection = int(input("Qué quieres hacer socio?: ")) 
        match selection:
          case 1:
            self.__showListPokemonByName()
            pokemon_searched = str(input("\nSocio, ¿Qué bicho quieres ver?: "))
            self.__showPokemon(pokemon_searched)
          
          case 2:
            self.__createPokemon()

          case 3:
            self.__editPokemon()

          case 5:
            print("\nTschüss socio!\n")
            break
      except IndexError:
        print("\nNo has escogido bien la opción, prueba de nuevo\n")

  #Random list of Pokemon to use in menu
  def __randomizePokemonList(self):
    i = 0
    while i < 10:
      id_random = random.randint(1,1025)
      pokemon_random = self.proxy.requestPokemon(id_random)
      self.pokemon_list.append(pokemon_random)
      i += 1

  #To extract types of pokemon random list to use to give example in create Pokemon
  def __extractType(self):
    for pokemon in self.pokemon_list:
      for type in pokemon.types:
        self.pokemon_type_set.add(type)

  #To show the Pokemon list so the user can see it
  def __showListPokemonByName(self):
    print("\nEstos son los bichos que hay disponibles:\n")
    for pokemon in self.pokemon_list:
      print("- {}".format(pokemon.name.title()))

#Principal def: case 1, show Pokemon -----------------------------------------------------------------------------------
  def __showPokemon(self,name:str):
    name = name.lower()
    for pokemon in self.pokemon_list:
      if pokemon.name.lower() == name.lower():
        print(pokemon)
        return(0)
    print("\nSocio escribe bien, porfa")

#Principal def: case 2: create Pokemon -----------------------------------------------------------------------------------
  def __createPokemon(self):
    flow_contr = True
    while flow_contr:
      #Select name -------------------------------------------------------
      name:str = str(input("\n¿Qué nombre le quieres poner al bicho?: "))
      if self.__checkNameInList(name.lower()):
        print('\nNo se pueden repetir nombres, prueba de nuevo.')
      else:
        flow_contr = False
    #Select type/s -----------------------------------------------------
    print('\nAlgunos ejemplos de tipo:\n')
    for type in self.pokemon_type_set:
      print(" - {}".format(type.title()))
    types:str = str(input("\n¿Qué tipo/s le ponemos?: "))
    types_list = types.split(",")
    types_list = [item.strip() for item in types_list]
    #Select abilities --------------------------------------------------
    ability_finder = self.__exampleAbilities(types_list)
    if ability_finder == False:
      print('\nNo tenemos ejemplos disponibles de habilidades para el tipo de tu Pokemon\n')
    else:
      print("\nAquí tienes algunos ejemplos de habilidades para los tipos de tu Pokemon:\n")
      for ability in ability_finder:
        print("- {}".format(ability.title()))
    abilities:str = str(input("\nQué habilidades le ponemos al Pokemon?: "))
    abilities_list = abilities.split(",")
    abilities_list = [item.strip() for item in abilities_list]
    pok_id:int = self.__idGiver()
    newPokemon = Pokemon_Model(pok_id,name,abilities_list,types_list)
    self.pokemon_list.append(newPokemon)
    print("\n{} añadido de forma exitosa".format(name))

  #To give an id that it's not in the list of pokemon to the new pokemon
  def __idGiver(self):
    ids:list = []
    for pokemon in self.pokemon_list:
      ids.append(pokemon.id)
    id_toGive = max(ids)+1
    return id_toGive
  
  #To check if the name they chose for a new Pokemon exist in our list
  def __checkNameInList(self,newName:str):
    names:set = set()
    for pokemon in self.pokemon_list:
      names.add(pokemon.name.lower())
    if newName in names:
      return True
    return False

  #To give examples of abilities of ONE type to use in exampleAbilities()
  def __finderExampleAbilities(self,type_ex:str):
    for pokemon in self.pokemon_list:
      for type in pokemon.types:
        if type.lower() == type_ex.lower():
          return(pokemon.abilities)
    return(0)
  
  #To give examples of abilities to create Pokemon depending on types selected
  def __exampleAbilities(self,types_ex:list):
    abilities_given:set = set()
    exampleNotFound = False
    for type in types_ex:
      examples = self.__finderExampleAbilities(type)
      if examples == 0 and not abilities_given: #If def returns 0 and our set is empty then ...
        exampleNotFound = True
      else:
        for example in examples:
          exampleNotFound = False
          abilities_given.add(example.title())
    if exampleNotFound == True:
      return(False)
    else:
      return(abilities_given)
    
#Principal def: case 3: edit Pokemon -----------------------------------------------------------------------------------
  def __editPokemon(self, name:str):
    print("¿Qué quieres cambiar de {}?")


proxy = Pokemon_Proxy()
control = Controller(proxy)
control.openMenu()