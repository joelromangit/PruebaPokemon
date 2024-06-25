class Pokemon_Model:
  def __init__(self,id:int,name:str,abilities:list,types:list):
    self.id = id
    self.name = name
    self.abilities = abilities
    self.types = types

  def __str__(self):
    return("\nTu pokemon tiene id {}, nombre {}, tiene las habilidades {} y el socio es de tipo {}\n".format(self.id,self.name.title(),self.abilities,self.types))
