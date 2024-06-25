from pokemon_model import Pokemon_Model
import requests
import json

class Pokemon_Proxy:
  def requestPokemon(self,id:int):
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(id)
    r = requests.get(url)
    j = r.json()
    #name
    name_pok = j['name']
    #End name
    
    #Types
    types_req = j['types']
    types_pok:list = []
    for hab in types_req:
      types_pok.append(hab['type']['name'])
    #End types

    #Abilities
    abilities_req = j['abilities']
    abilities_pok:list = []
    for hab in abilities_req:
      abilities_pok.append(hab['ability']['name'])
    #End abilities

    resquested_Pokemon = Pokemon_Model(id,name_pok,abilities_pok,types_pok)
    return(resquested_Pokemon)
  