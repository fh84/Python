import random
import math
import numpy

class RandomMover:
	def move(self):
		return random.uniform(0,1)<0.5


class RandomPlayer:
    def __init__(self, p=0.5):
        self.p_defect = p
    def move(self, game):
        return random.uniform(0,1) < self.p_defect
    def record(self, game):
        pass


class SimpleGame:
    def __init__(self, player1, player2, payoffmat):
        # initialize instance attributes
        self.players = [ player1, player2 ]
        self.payoffmat = payoffmat
        self.history = list()
    def run(self, game_iter=4):
        # unpack the two players
        player1, player2 = self.players
        # each iteration, get new moves and append these to history
        for iteration in range(game_iter):
            newmoves = player1.move(self), player2.move(self)
            self.history.append(newmoves)
        # prompt players to record the game played (i.e., 'self')
        player1.record(self); player2.record(self)
    def payoff(self):
        # unpack the two players
        player1, player2 = self.players
        # generate a payoff pair for each game iteration
        for (m1,m2) in self.history:
        	payoffs1 = self.payoffmat[m1]
        	payoffs2 = self.payoffmat[m2] 
        # transpose to get a payoff sequence for each player
        #pay1, pay2 = numpy.transpose(payoffs)
        # return a mapping of each player to its mean payoff
        return { player1:numpy.mean(payoffs1), player2:numpy.mean(payoffs2) }
        

## GAME: SimpleGame with RandomPlayer
# create a payoff matrix and two players
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
player1 = RandomPlayer()
player2 = RandomPlayer()
# create and run the game
game = SimpleGame(player1, player2, PAYOFFMAT)
game.run()
# retrieve and print the payoffs
payoffs = game.payoff()
print "Player1 payoff: ", payoffs[player1]
print "Player2 payoff: ", payoffs[player2]

#########################################################################
#########################################################################
#########################################################################
##new game 

class SimplePlayer:
	def __init__(self, playertype):
		self.playertype = playertype
		self.reset()
	def reset(self):
		self.games_played = []
		self.players_played = []
	def move(self,game):
		return self.playertype.move(self,game)
	def record(self,game):
		self.games_played.append(game)
		opponent = game.opponents[self]
		self.players_played.append(opponent)


class CDIPlayerType:
	def __init__(self, p_cdi=(0.5,0.5,0.5)):
		self.p_cdi = p_cdi
	def move(self,player,game):
		opponent =game.opponents[player]
		last_move = game.get_last_move(opponent)
		if last_move is None:
			p_defect = self.p_cdi[-1]
		else:
			p_defect = self.p_cdi[last_move]
		return random.uniform(0,1) < p_defect	

class CDIGame(SimpleGame):
	def __init__(self,player1,player2,payoffmat):
		SimpleGame.__init__(self,player1,player2,payoffmat)
		self.opponents = {player1:player2,player2:player1}
	def get_last_move(self,player):
		if self.history:
			player_idx = self.players.index(player)
			last_move = self.history[-1][player_idx]
		else:
			last_move = None
		return last_move

## GAME: CDIGame with SimplePlayer
# create a payoff matrix and two players (with playertypes)
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
ptype1 = CDIPlayerType()
ptype2 = CDIPlayerType()
player1 = SimplePlayer(ptype1)
player2 = SimplePlayer(ptype2)
# create and run the game
game = CDIGame(player1, player2, PAYOFFMAT)
game.run()
# retrieve and print the payoffs
payoffs = game.payoff()
print "Player1 payoff: ", payoffs[player1]
print "Player2 payoff: ", payoffs[player2]


class SoupPlayer(SimplePlayer):
	def evolve(self):
		self.playertype = self.next_playertype
	def get_payoff(self):
		return sum( game.payoff()[self] for game in self.games_played)
	def choose_next_type(self):
		best_playertypes = topscore_playertypes(self)
		self.next_playertype = random.choice(best_playertypes)

class SoupRound:
	def __init__(self,players,playoffmat):
		self.players = players
		self.payoffmat = payoffmat
	def run(self):
		payoff_matrix = self.payoffmat
		for player1, player2 in random_pairs_of(self.players):
			game = CDIGame(player1,player2,payoff_matrix)
			game.run()
		