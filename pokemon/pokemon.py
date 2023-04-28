import random
import json

class Combat:
    def __init__(self, player_pokemon):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = self.get_random_pokemon()
        
    def get_random_pokemon(self):
        with open('pokemon.json', 'r') as f:
            pokemon_list = json.load(f)
            return random.choice(pokemon_list)

    def is_game_over(self):
        return self.player_pokemon.hp <= 0 or self.opponent_pokemon['hp'] <= 0

    def get_winner(self):
        if self.player_pokemon.hp <= 0:
            return self.opponent_pokemon['name']
        elif self.opponent_pokemon['hp'] <= 0:
            return self.player_pokemon.name

    def can_attack(self):
        return random.randint(0, 1) == 1

    def get_damage_multiplier(self, attacker_type, defender_type):
        if attacker_type == 'Normal':
            return 1
        elif attacker_type == 'Water':
            if defender_type == 'Fire':
                return 2
            elif defender_type == 'Ground':
                return 0.5
        elif attacker_type == 'Fire':
            if defender_type == 'Water':
                return 0.5
            elif defender_type == 'Ground':
                return 2
        elif attacker_type == 'Ground':
            if defender_type == 'Water':
                return 2
            elif defender_type == 'Fire':
                return 0.5
        return 1

    def attack(self, attacker, defender):
        damage_multiplier = self.get_damage_multiplier(attacker.type, defender.type)
        damage = int(attacker.attack * damage_multiplier) - defender.defense
        if damage < 0:
            damage = 0
        defender.hp -= damage
        print(f"{attacker.name} attaque {defender.name} et lui inflige {damage} points de dégâts.")

    def play_turn(self):
        if self.is_game_over():
            return

        if self.can_attack():
            print(f"{self.player_pokemon.name} attaque {self.opponent_pokemon['name']} !")
            self.attack(self.player_pokemon, self.opponent_pokemon)
        else:
            print(f"{self.player_pokemon.name} rate son attaque...")

        if not self.is_game_over() and self.can_attack():
            print(f"{self.opponent_pokemon['name']} contre-attaque !")
            self.attack(self.opponent_pokemon, self.player_pokemon)
        elif not self.is_game_over():
            print(f"{self.opponent_pokemon['name']} rate son attaque...")

    def run(self):
        print(f"Vous affrontez {self.opponent_pokemon['name']} !")

        while not self.is_game_over():
            self.play_turn()

        winner = self.get_winner()
        print(f"Le combat est terminé ! Le vainqueur est {winner} !")
        
        # Save encountered pokemon to pokedex
        with open('pokedex.json', 'r') as f:
            pokedex = json.load(f)
        if self.opponent_pokemon['name'] not in pokedex:
            pokedex[self.opponent_pokemon['name']] = 0
        pokedex[self.opponent_pokemon['name']] += 1
        with open('pokedex.json', 'w') as f:
            json.dump(pokedex, f)
