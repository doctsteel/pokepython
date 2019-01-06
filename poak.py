import pokebase as pb
import random
import os

print('Welcome to Pokemon Fire Python')
print('this is a test, so please bear with me')
print('this is using PokeAPI and the pokebase python module')
os.system('clear')

def checkForWeakness(move, defender):
	if defender.types[0].type.name in pb.move(move).type.damage_relations.half_damage_to:
		print("Not very effective...")
		return 0.5
	if defender.types[0].type.name in pb.move(move).type.damage_relations.double_damage_to:
		print("It's super effective!!!")
		return 2
	if defender.types[0].type.name in pb.move(move).type.damage_relations.no_damage_to:
		print("No effect.")
		return 0

def sameType(attacking, movetype):
	if attacking.types[0].type.name == pb.move(move).type:
		return 1.5
	else:
		return 1


def calculateDamage(attacker, attackermove, defender):
	stab = sameType(attacker, attackermove)
	weakness_multiplier = checkForWeakness(attackermove, defender) * stab 
	if pb.move(attackermove).damage_class == 'physical':
		A = attacker.stats[4]
		D = defender.stats[3]
	if pb.move(attackermove).damage_class == 'special':
		A = attacker.stats[2]
		D = defender.stats[1]
	damage = ((((((2*50)/5)+2) * pb.move(attackermove).power * A / D)/50)+2) *  weakness_multiplier
	print('Dealt ' + damage + ' damage!')
	defender.stats[5] = defender.stats[5] - damage

def checkAccuracy(movename):
	print("The pokemon used {}!".format(movename))
	randomizer = random.randint(1,100)
	if pb.move(movename).accuracy > randomizer:
		return True
	else:
		print("But it missed!")
		return False

class generateRandomPokemon:
	def __init__(self, number):
		self.data = pb.pokemon(number)
		self.name = self.data.name
		self.abil = random.choice(self.data.abilities)
		self.movelist = [random.choice(self.data.moves), random.choice(self.data.moves), random.choice(self.data.moves),random.choice(self.data.moves)]
		self.stats = [self.data.stats[0].base_stat, self.data.stats[1].base_stat, self.data.stats[2].base_stat, self.data.stats[3].base_stat, self.data.stats[4].base_stat, self.data.stats[5].base_stat]
		 ##speed, sp defense, sp attack, defense, attack, hp, inTHIS  ORDER

class trainer:
	def __init__(self):
		self.pokemon1 = generateRandomPokemon(random.randint(1,800))
		self.pokemon2 = generateRandomPokemon(random.randint(1,800))
		self.pokemon3 = generateRandomPokemon(random.randint(1,800))
		self.activePokemon = self.pokemon1
		self.alivePokes = 3
	

	
def chooseMove(trainer):
		print("Which move to use? \n 1-{} \n 2-{} \n 3-{}\n 4-{}\n".format(trainer.activePokemon.movelist[0].move, trainer.activePokemon.movelist[1].move, trainer.activePokemon.movelist[2].move, trainer.activePokemon.movelist[3].move))
		action = input()
		if action == 1:
			return trainer.activePokemon.movelist[0].move
		if action == 2:
			return trainer.activePokemon.movelist[1].move
		if action == 3:
			return trainer.activePokemon.movelist[2].move
		if action == 4:
			return trainer.activePokemon.movelist[3].move

def checkKO():
	if player.activePokemon.stats[5] <= 0:
		print("Your pokemon fainted!")
		player.alivePokes -=1
		return True
	if enemy.activePokemon.stats[5] <= 0:
		print("The enemy pokemon fainted!")
		enemy.alivePokes -= 1
		return True
	else:
		return False

def checkPokemonLeft():
	if player.alivePokes > 0:
		return True
	if enemy.alivePokes > 0:
		return True
	else:
		return False
def changePokemon(trainer):
	if trainer.activePokemon.stats[5] < 0:
		if trainer.alivePokes == 2:
			trainer.activePokemon = trainer.pokemon2
			print(trainer.pokemon2.name + 'enters the battle!')
		if trainer.alivePokes == 1:
			print(trainer.pokemon3.name + 'enters the battle!')
			trainer.activePokemon = trainer.pokemon3

def checkSpeed(pokemon1, pokemon2):
	if pokemon1.stats[0] > pokemon2.stats[0]:
		return True
	else:
		return False

player = trainer();
enemy = trainer();


print('\n')
print('This is your team: \n')
print(player.pokemon1.name + " " + player.pokemon2.name +" "+ player.pokemon3.name + '\n')

print('The enemy team is: \n')
print(enemy.pokemon1.name + " " + enemy.pokemon2.name +" "+ enemy.pokemon3.name + '\n')




while True:
	playerchosen = chooseMove(player)
	enemychosen = chooseMove(enemy)
	if checkSpeed(player.activePokemon, enemy.activePokemon) == True:
		if checkAccuracy(playerchosen) == True:
			calculateDamage(player.activePokemon, playerchosen, enemy.activePokemon)
			if checkKO() == True:
				if checkPokemonLeft() == True:
					changePokemon(enemy)
				else:
					battleEnds()
					break
			else:
				if checkAccuracy(enemychosen) == True:
					calculateDamage(enemy.activePokemon, enemychosen, player.activePokemon)
					if checkKO() == True:
						if checkPokemonLeft() == True:
							changePokemon(player)
						else:
							battleEnds()
							break
		else:
			if checkAccuracy(enemychosen) == True:
					calculateDamage(enemy.activePokemon, enemychosen, player.activePokemon)
					if checkKO() == True:
						if checkPokemonLeft() == True:
							changePokemon(player)
						else:
							battleEnds()
							break
	else:
		if checkAccuracy(enemychosen) == True:
					calculateDamage(enemy.activePokemon, enemychosen, player.activePokemon)
					if checkKO() == True:
						if checkPokemonLeft() == True:
							changePokemon(player)
						else:
							battleEnds()
							break
					else:
						if checkAccuracy(playerchosen) == True:
							calculateDamage(player.activePokemon, playerchosen, enemy.activePokemon)
							if checkKO() == True:
								if checkPokemonLeft() == True:
									changePokemon(enemy)
								else:
									battleEnds()
									break
