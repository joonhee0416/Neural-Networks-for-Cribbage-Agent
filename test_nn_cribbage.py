import sys
import time
import math
import itertools as it

from policy import CompositePolicy, RandomThrower, RandomPegger, GreedyThrower, GreedyPegger
from cribbage import Game, evaluate_policies
from my_policy import MyPolicy
from nn import NNPolicy

if __name__ == "__main__":
    games = 2
    run_time = 0
    game = Game()
    if len(sys.argv) > 1:
        if sys.argv[1] == "--nn":
            games = int(sys.argv[2]);
            submission = NNPolicy(game)
        else:
            games = int(sys.argv[1])
            submission = MyPolicy(game)
    
    benchmark = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
    total_games = 0

    match_values = list(it.chain(range(1, 4), range(-3, 0)))
    results = {value: 0 for value in match_values}
    start_time = time.time()
    while total_games == 0 or time.time() - start_time < run_time:
        batch_results = evaluate_policies(game, submission, benchmark, games)
        total_games += games
        for v in batch_results[3]:
            results[v] += batch_results[3][v]

    sum_squares = sum(results[v] * v * v for v in match_values)
    sum_values = sum(results[v] * v for v in match_values)
    mean = sum_values / total_games
    variance = sum_squares / total_games - math.pow(sum_values / total_games, 2)
    stddev = math.sqrt(variance)
    
    if (sys.argv[1] == "--nn"):
        print("NNPolicy Results Against Greedy")
    else:
        print("MyPolicy Results (no neural network) Against Greedy")
    print("NET:", mean)
    print("CONF:", mean - 2 * (stddev / math.sqrt(total_games)))
    print(results)


