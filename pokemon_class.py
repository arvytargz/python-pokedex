import os

dex_running = True
page = 0

egg_list = [
    "Monster", "Human-Like", "Water 1", "Water 2", "Water 3", "Bug", "Mineral",
    "Flying", "Amorphous", "Field", "Fairy", "Ditto", "Grass", "Dragon",
    "Undiscovered"
]
type_list = [
    "Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting",
    "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon",
    "Dark", "Steel", "Fairy"
]

normal_dict = {
  "Normal": "Effective",
  "Fighting": "Super Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Effective",
  "Rock": "Effective",
  "Bug": "Effective",
  "Ghost": "Does Not Affect",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Effective",
  "Psychic": "Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

fighting_dict = {
  "Normal": "Effective",
  "Fighting": "Effective",
  "Flying": "Super Effective",
  "Poison": "Effective",
  "Ground": "Effective",
  "Rock": "Not Very Effective",
  "Bug": "Not Very Effective",
  "Ghost": "Effective",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Effective",
  "Psychic": "Super Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Not Very Effective",
  "Fairy": "Super Effective"
}

flying_dict = {
  "Normal": "Effective",
  "Fighting": "Not Very Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Does Not Affect",
  "Rock": "Super Effective",
  "Bug": "Not Very Effective",
  "Ghost": "Effective",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Not Very Effective",
  "Electric": "Super Effective",
  "Psychic": "Effective",
  "Ice": "Super Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

poison_dict = {
  "Normal": "Effective",
  "Fighting": "Not Very Effective",
  "Flying": "Effective",
  "Poison": "Not Very Effective",
  "Ground": "Super Effective",
  "Rock": "Effective",
  "Bug": "Not Very Effective",
  "Ghost": "Effective",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Not Very Effective",
  "Electric": "Effective",
  "Psychic": "Super Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Not Very Effective"
}

ground_dict = {
  "Normal": "Effective",
  "Fighting": "Effective",
  "Flying": "Effective",
  "Poison": "Not Very Effective",
  "Ground": "Effective",
  "Rock": "Not Very Effective",
  "Bug": "Effective",
  "Ghost": "Effective",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Super Effective",
  "Grass": "Super Effective",
  "Electric": "Does Not Affect",
  "Psychic": "Effective",
  "Ice": "Super Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

rock_dict = {
  "Normal": "Not Very Effective",
  "Fighting": "Super Effective",
  "Flying": "Not Very Effective",
  "Poison": "Not Very Effective",
  "Ground": "Super Effective",
  "Rock": "Effective",
  "Bug": "Effective",
  "Ghost": "Effective",
  "Steel": "Super Effective",
  "Fire": "Not Very Effective",
  "Water": "Super Effective",
  "Grass": "Super Effective",
  "Electric": "Effective",
  "Psychic": "Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

bug_dict = {
  "Normal": "Effective",
  "Fighting": "Not Very Effective",
  "Flying": "Super Effective",
  "Poison": "Effective",
  "Ground": "Not Very Effective",
  "Rock": "Super Effective",
  "Bug": "Effective",
  "Ghost": "Effective",
  "Steel": "Effective",
  "Fire": "Super Effective",
  "Water": "Effective",
  "Grass": "Not Very Effective",
  "Electric": "Effective",
  "Psychic": "Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

ghost_dict = {
  "Normal": "Does Not Affect",
  "Fighting": "Does Not Affect",
  "Flying": "Effective",
  "Poison": "Not Very Effective",
  "Ground": "Effective",
  "Rock": "Effective",
  "Bug": "Not Very Effective",
  "Ghost": "Super Effective",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Effective",
  "Psychic": "Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Super Effective",
  "Fairy": "Effective"
}

steel_dict = {
  "Normal": "Not Very Effective",
  "Fighting": "Super Effective",
  "Flying": "Not Very Effective",
  "Poison": "Does Not Affect",
  "Ground": "Super Effective",
  "Rock": "Not Very Effective",
  "Bug": "Not Very Effective",
  "Ghost": "Effective",
  "Steel": "Not Very Effective",
  "Fire": "Super Effective",
  "Water": "Effective",
  "Grass": "Not Very Effective",
  "Electric": "Effective",
  "Psychic": "Not Very Effective",
  "Ice": "Not Very Effective",
  "Dragon": "Not Very Effective",
  "Dark": "Effective",
  "Fairy": "Not Very Effective"
}

fire_dict = {
  "Normal": "Effective",
  "Fighting": "Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Super Effective",
  "Rock": "Super Effective",
  "Bug": "Not Very Effective",
  "Ghost": "Effective",
  "Steel": "Not Very Effective",
  "Fire": "Not Very Effective",
  "Water": "Super Effective",
  "Grass": "Not Very Effective",
  "Electric": "Effective",
  "Psychic": "Effective",
  "Ice": "Not Very Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Not Very Effective"
}

water_dict = {
  "Normal": "Effective",
  "Fighting": "Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Effective",
  "Rock": "Effective",
  "Bug": "Effective",
  "Ghost": "Effective",
  "Steel": "Not Very Effective",
  "Fire": "Not Very Effective",
  "Water": "Not Very Effective",
  "Grass": "Super Effective",
  "Electric": "Super Effective",
  "Psychic": "Effective",
  "Ice": "Not Very Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

grass_dict = {
  "Normal": "Effective",
  "Fighting": "Effective",
  "Flying": "Super Effective",
  "Poison": "Super Effective",
  "Ground": "Not Very Effective",
  "Rock": "Effective",
  "Bug": "Super Effective",
  "Ghost": "Effective",
  "Steel": "Effective",
  "Fire": "Super Effective",
  "Water": "Not Very Effective",
  "Grass": "Not Very Effective",
  "Electric": "Not Very Effective",
  "Psychic": "Effective",
  "Ice": "Super Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}
# this one below
electric_dict = {
  "Normal": "Effective",
  "Fighting": "Effective",
  "Flying": "Not Very Effective",
  "Poison": "Effective",
  "Ground": "Super Effective",
  "Rock": "Effective",
  "Bug": "Effective",
  "Ghost": "Effective",
  "Steel": "Not Very Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Not Very Effective",
  "Psychic": "Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

psychic_dict = {
  "Normal": "Effective",
  "Fighting": "Not Very Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Effective",
  "Rock": "Effective",
  "Bug": "Super Effective",
  "Ghost": "Super Effective",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Effective",
  "Psychic": "Not Very Effective",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Super Effective",
  "Fairy": "Effective"
}

ice_dict = {
  "Normal": "Effective",
  "Fighting": "Super Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Effective",
  "Rock": "Super Effective",
  "Bug": "Effective",
  "Ghost": "Effective",
  "Steel": "Super Effective",
  "Fire": "Super Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Effective",
  "Psychic": "Effective",
  "Ice": "Not Very Effective",
  "Dragon": "Effective",
  "Dark": "Effective",
  "Fairy": "Effective"
}

dragon_dict = {
  "Normal": "Effective",
  "Fighting": "Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Effective",
  "Rock": "Effective",
  "Bug": "Effective",
  "Ghost": "Effective",
  "Steel": "Effective",
  "Fire": "Not Very Effective",
  "Water": "Not Very Effective",
  "Grass": "Not Very Effective",
  "Electric": "Not Very Effective",
  "Psychic": "Effective",
  "Ice": "Super Effective",
  "Dragon": "Super Effective",
  "Dark": "Effective",
  "Fairy": "Super Effective"
}

dark_dict = {
  "Normal": "Effective",
  "Fighting": "Super Effective",
  "Flying": "Effective",
  "Poison": "Effective",
  "Ground": "Effective",
  "Rock": "Effective",
  "Bug": "Super Effective",
  "Ghost": "Not Very Effective",
  "Steel": "Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Effective",
  "Psychic": "Does Not Affect",
  "Ice": "Effective",
  "Dragon": "Effective",
  "Dark": "Not Very Effective",
  "Fairy": "Super Effective"
}

fairy_dict = {
  "Normal": "Effective",
  "Fighting": "Not Very Effective",
  "Flying": "Effective",
  "Poison": "Super Effective",
  "Ground": "Effective",
  "Rock": "Effective",
  "Bug": "Not Very Effective",
  "Ghost": "Effective",
  "Steel": "Super Effective",
  "Fire": "Effective",
  "Water": "Effective",
  "Grass": "Effective",
  "Electric": "Effective",
  "Psychic": "Effective",
  "Ice": "Effective",
  "Dragon": "Does Not Affect",
  "Dark": "Not Very Effective",
  "Fairy": "Effective"
}

head_colour     = "\033[38;5;1m"
red            = "\033[38;5;196m"
blue           = "\033[38;5;26m"
yellow         = "\033[38;5;226m"
green          = "\033[38;5;34m"
black          = "\033[38;5;236m"
brown          = "\033[38;5;130m"
purple         = "\033[38;5;128m"
gray           = "\033[38;5;248m"
white          = "\033[38;5;7m"
pink           = "\033[38;5;205m"

fighting_colour = "\033[38;5;160m"
flying_colour   = "\033[38;5;109m"
poison_colour   = "\033[38;5;91m"
ground_colour   = "\033[38;5;143m"
rock_colour     = "\033[38;5;3m"
bug_colour      = "\033[38;5;112m"
ghost_colour    = "\033[38;5;93m"
steel_colour    = "\033[38;5;250m"
fire_colour     = "\033[38;5;202m"
water_colour    = "\033[38;5;39m"
grass_colour    = "\033[38;5;10m"
electric_colour = "\033[38;5;220m"
psychic_colour  = "\033[38;5;198m"
ice_colour      = "\033[38;5;50m"
dragon_colour   = "\033[38;5;129m"
dark_colour     = "\033[38;5;242m"
fairy_colour    = "\033[38;5;9m"

class Pokemon:

  def __init__(self, 
               dex_num,
               gen, 
               name,
               species,
               status, 
               stat_total, 
               hp, 
               atk, 
               defense, 
               sp_atk, 
               sp_defense, 
               speed,
               types, 
               ability, 
               hidden_ability, 
               egg_group,
               friendship, 
               height, 
               weight, 
               percent_male, 
               level_rate,
               ascii,
               next_variant,
               colour,
               stage,
               variants
              ):
    self.dex_num = dex_num
    self.gen = gen
    self.name = name
    self.species = species
    self.status = status
    self.stat_total = stat_total
    self.hp = hp
    self.atk = atk
    self.defense = defense
    self.sp_atk = sp_atk
    self.sp_defense = sp_defense
    self.speed = speed
    self.types = types
    self.ability = ability
    self.hidden_ability = hidden_ability
    self.egg_group = egg_group
    self.friendship = friendship
    self.height = height
    self.weight = weight
    self.percent_male = percent_male
    self.level_rate = level_rate
    self.ascii = ascii
    self.next_variant = next_variant
    self.colour = colour
    self.stage = stage
    self.variants = variants

  def print_dex_one(self):
    os.system("clear")
    
    type_colours = []
    for i in self.types:
      match i:
        case "Normal":
          type_colours.append(white)
        case "Fighting":
          type_colours.append(fighting_colour)
        case "Flying":
          type_colours.append(flying_colour)
        case "Poison":
          type_colours.append(poison_colour)
        case "Ground":
          type_colours.append(ground_colour)
        case "Rock":
          type_colours.append(rock_colour)
        case "Bug":
          type_colours.append(bug_colour)
        case "Ghost":
          type_colours.append(ghost_colour)
        case "Steel":
          type_colours.append(steel_colour)
        case "Fire":
          type_colours.append(fire_colour)
        case "Water":
          type_colours.append(water_colour)
        case "Grass":
          type_colours.append(grass_colour)
        case "Electric":
          type_colours.append(electric_colour)
        case "Psychic":
          type_colours.append(psychic_colour)
        case "Ice":
          type_colours.append(ice_colour)
        case "Dragon":
          type_colours.append(dragon_colour)
        case "Dark":
          type_colours.append(dark_colour)
        case "Fairy":
          type_colours.append(fairy_colour)

    if self.status == "Legendary":
      print(f"{yellow}{self.dex_num}: {self.name}, The {self.species} (Legendary)")
    elif self.status == "Mythical":
      print(f"{yellow}{self.dex_num}: {self.name}, The {self.species} (Mythical)")
    else:
      print(f"{head_colour}{self.dex_num}: {self.name}, The {self.species}")
    
    print(f"{self.colour}{self.ascii}")
    
    print(f"{white}{self.stage}")
    
    if self.types[1] == "":
      print(f"{white}Type: {type_colours[0]}{self.types[0]}")
    else:
      print(f"{white}Types: {type_colours[0]}{self.types[0]}, {type_colours[1]}{self.types[1]}")

    if self.ability[1] == "":
      print(f"{white}Ability: {self.ability[0]}")
    else:
      print(f"{white}Abilities: {self.ability[0]}, {self.ability[1]}")

    if self.hidden_ability != "":
      print(f"{white}Hidden Ability: {self.hidden_ability}")

  def print_dex_two(self):
    os.system("clear")
    if self.status == "Legendary":
      print(f"{yellow}{self.dex_num}: {self.name}, The {self.species} (Legendary)")
    elif self.status == "Mythical":
      print(f"{yellow}{self.dex_num}: {self.name}, The {self.species} (Mythical)")
    else:
      print(f"{head_colour}{self.dex_num}: {self.name}, The {self.species}")

    print(f"{self.colour}{self.ascii}")
    
    print(f"{white}Height: {self.height}m")
    print(f"{white}Weight: {self.weight}kg")
    print(f"{white}Base Friendship: {self.friendship}")

    if self.egg_group[1] == "":
      print(f"{white}Egg Group: {self.egg_group[0]}")
    else:
      print(f"{white}Egg Groups: {self.egg_group[0]}, {self.egg_group[1]}")

    if self.percent_male == -1:
      print(f"{white}Gender Unknown")
    else:
      print(f"{white}Gender Ratio: {self.percent_male}% ♂, {100 - self.percent_male}% ♀")

  def print_dex_three(self):
    type_dicts = []
    for i in self.types:
      match i:
        case "Normal":
          type_dicts.append(normal_dict)
        case "Fighting":
          type_dicts.append(fighting_dict)
        case "Flying":
          type_dicts.append(flying_dict)
        case "Poison":
          type_dicts.append(poison_dict)
        case "Ground":
          type_dicts.append(ground_dict)
        case "Rock":
          type_dicts.append(rock_dict)
        case "Bug":
          type_dicts.append(bug_dict)
        case "Ghost":
          type_dicts.append(ghost_dict)
        case "Steel":
          type_dicts.append(steel_dict)
        case "Fire":
          type_dicts.append(fire_dict)
        case "Water":
          type_dicts.append(water_dict)
        case "Grass":
          type_dicts.append(grass_dict)
        case "Electric":
          type_dicts.append(electric_dict)
        case "Psychic":
          type_dicts.append(psychic_dict)
        case "Ice":
          type_dicts.append(ice_dict)
        case "Dragon":
          type_dicts.append(dragon_dict)
        case "Dark":
          type_dicts.append(dark_dict)
        case "Fairy":
          type_dicts.append(fairy_dict)
    super_effective_one = []
    super_effective_two = []
    not_very_effective = []
    final_super_effective = []
    final_does_not_affect = []

    for i in type_dicts[0]:
      if type_dicts[0].get(i) == "Super Effective":
        super_effective_one.append(i)
      elif type_dicts[0].get(i) == "Does Not Affect":
        final_does_not_affect.append(i)
      elif type_dicts[0].get(i) == "Not Very Effective":
        not_very_effective.append(i)

    if len(type_dicts) > 1:
      for i in type_dicts[1]:
        if type_dicts[1].get(i) == "Super Effective":
          super_effective_two.append(i)
        elif type_dicts[1].get(i) == "Does Not Affect":
          final_does_not_affect.append(i)
        elif type_dicts[1].get(i) == "Not Very Effective":
          not_very_effective.append(i)

    for i in super_effective_one:
      if i not in not_very_effective and i not in final_does_not_affect:
        final_super_effective.append(i)

    for i in super_effective_two:
      if i not in not_very_effective and i not in final_does_not_affect:
        final_super_effective.append(i)

    final_super_effective = list(dict.fromkeys(final_super_effective))
    final_does_not_affect = list(dict.fromkeys(final_does_not_affect))

    os.system("clear")
    if self.status == "Legendary":
      print(f"{yellow}{self.dex_num}: {self.name}, The {self.species} (Legendary)")
    elif self.status == "Mythical":
      print(f"{yellow}{self.dex_num}: {self.name}, The {self.species} (Mythical)")
    else:
      print(f"{head_colour}{self.dex_num}: {self.name}, The {self.species}")

    print(f"{self.colour}{self.ascii}")

    print(f"{white}Leveling Rate: {self.level_rate}")
    print(f"{white}Attack: {self.atk}\t\t\t\tDefense: {self.defense}")
    print(f"{white}Special Attack: {self.sp_atk}\t\t\tSpecial Defense: {self.sp_defense}")
    print(f"{white}Speed: {self.speed}\t\t\t\tHP: {self.hp}")
    
    print("Super Effective to: ", end="")
    for i in final_super_effective:
      print(f"{i}, ", end="")
    print()
    
    if len(final_does_not_affect) > 0:
      print("Immune to: ", end="")
      for i in final_does_not_affect:
        print(f"{i}, ", end="")
      print()