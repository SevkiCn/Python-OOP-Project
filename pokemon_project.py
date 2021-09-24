#!/usr/bin/env python
# coding: utf-8

# In[78]:


class Pokemon:
  def __init__(self, name, level, type, health, max_health, is_knocked_out = False):
    self.name = name
    self.level = level
    self.type = type
    self.health = health
    self.max_health = max_health
    self.is_knocked_out = is_knocked_out

  def gain_health(self, gain):
    self.health += gain
    print("{} now has {} health.".format(self.name, self.health))
  
  def lose_health(self, lose):
    self.health = self.health - lose
    
    if self.health == 0:
       self.is_knocked_out = True
       print("The pokemon has been knocked out!!")
    else:
        print("{} now has {} health.".format(self.name, self.health))

  def revive(self):
    if self.is_knocked_out == True:
      self.is_knocked_out = False
      print("The pokemon has successfully revived!!")
    else:
      print("The pokemon is already alive !!")
      
  def show_status(self):
    print(""" 
    Name: {}
    Type: {}
    Level: {}
    Current Health: {}
    """.format(self.name, self.type, self.level, self.health))

  def attacc(self, other_pokemon):
    if self.type == "Fire" and other_pokemon.type == "Grass":
      other_pokemon.health = other_pokemon.health - (self.level * 2)
      print("{} damage dealt by attacker due to the advantage !!".format(self.level * 2))
    
    if self.type == "Grass" and other_pokemon.type == "Fire":
      other_pokemon.health = other_pokemon.health - (self.level * 1/2)
      print("{} damage dealt by attacker due to the disadvantage !!".format(self.level * 1/2))

    if self.type == "Water" and other_pokemon.type == "Fire":
      other_pokemon.health = other_pokemon.health - (self.level * 2)
      print("{} damage dealt by attacker due to the advantage !!".format(self.level * 2))          
    
    if self.type == "Fire" and other_pokemon.type == "Water":
      other_pokemon.health = other_pokemon.health - (self.level * 1/2)
      print("{} damage dealt by attacker due to the disadvantage !!".format(self.level * 1/2))   
    
    if self.type == "Grass" and other_pokemon.type == "Water":
      other_pokemon.health = other_pokemon.health - (self.level * 2)
      print("{} damage dealt by attacker due to the advantage !!".format(self.level * 2))
    
    if self.type == "Water" and other_pokemon.type == "Grass":
      other_pokemon.health = other_pokemon.health - (self.level * 1/2)
      print("{} damage dealt by attacker due to the disadvantage !!".format(self.level* 1/2))
        
  

class Trainer(Pokemon):

        
  def __init__(self, name, pokemons, num_of_potions, active_pokemon):
    self.name = name
    self.pokemons = pokemons
    self.num_of_potions = num_of_potions
    self.active_pokemon = active_pokemon
    self.pokemon_list = []
    
    for pokemon in pokemons:
        self.pokemon_list.append(pokemon.name)

    
  def show_status(self):
    print("""
    Trainer Name: {}
    Total Pokemons: {}
    Active Pokemon: {}
    Pokemon's health: {}
    Number of Potions Available: {} """.format(self.name, self.pokemon_list, self.active_pokemon.name, self.active_pokemon.health, self.num_of_potions))

  def use_potion(self, value):

    self.active_pokemon.health += value
    self.num_of_potions -= 1
    print("Your pokemon has gained {} health !!".format(value))

  def attacc_to_trainer(self, other_trainer):
    print("Oh no! {} just attacked to {}.".format(self.name, other_trainer.name))
    self.active_pokemon.attacc(other_trainer.active_pokemon)
    
    
    
  def switch_pokemon(self, new_pokemon):
    if self.active_pokemon == new_pokemon:
        print("Your current pokemon is already {}. ".format(self.active_pokemon.name))
    else:
        self.active_pokemon = new_pokemon
        print("You successfully changed your pokemon. {} is now ready to fight!!".format(self.active_pokemon.name))


# In[79]:


charizard = Pokemon("Charizard", 5, "Fire", 300, 500)
psyduck = Pokemon("Psyduck", 4, "Water", 500, 800)
exeggcute = Pokemon("Exeggcute", 6, "Grass", 250, 400)
squirtle = Pokemon("Squirtle", 8, "Water", 200, 300)

trainer_1 = Trainer("Ece", [charizard, psyduck], 5, charizard)
trainer_2 = Trainer("Şevki", [exeggcute, squirtle], 4, squirtle)



#charizard.show_status()
#charizard.gain_health(100)
#charizard.show_status()

#psyduck.attacc(charizard)

#charizard.show_status()

#trainer_1.use_potion(8)

#charizard.show_status()

#trainer_1.show_status()

#trainer_2.show_status()

#trainer_2.switch_pokemon(squirtle)
#trainer_2.switch_pokemon(exeggcute)

#trainer_2.show_status()

#trainer_1.attacc_to_trainer(trainer_2)

#trainer_2.show_status()#


# In[ ]:




