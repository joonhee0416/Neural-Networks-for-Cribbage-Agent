# CPSC 474 Final Project: Using Neural Networks to Predict Optimal Keep Cards for Cribbage Pegging
# Joonhee Park

## Description of Project
Cribbage is a two-player, hidden information card game where the participants score points from pegging, their hands, and the crib in a race to 121 points. I trained a neural network to estimate the points earned by my agent (using my pegging policy from Assignment 1) minus the points earned by the greedy agent in one pegging round. I generated 1,000,000 lines of data for my neural network. The input for my neural network was an array of 13 values, each representing the 13 ranks in a deck of cards, with values of 0, 0.25, 0.5, 0.75, or 1 (for 0, 1, 2, 3, and 4 cards of that rank in hand as my agent enters the pegging stage). The output was a normalized float of my agent's resulting score from that pegging round as described above. My neural network used 3 layers of 50 neurons each and a mean squared error loss function. Given my model, my new keep policy added the expected pegging score when calculating the expected points gained for each possible hand. I also found that multiplying the expected pegging score by some constant when in the end game (less than 10 points away from 121) slightly improved results, which is included in the final version of the keep algorithm.

## Results
After running 2500 games for MyPolicy and for NNPolicy (both against the Greedy player), I was able to achieve a NET/CONF value of 0.256/0.21876536863698418 for MyPolicy and 0.3168/0.27000790220560744 for NNPolicy. It is clear that using the neural network to predict which hands would be good for pegging against a greedy player and taking this into account when choosing cards to keep increased my expected match points per game. This makes sense because I designed my pegging policy in Assignment 1 to perform well against the greedy player. I also found that a three-layer neural network performed slightly better than a two-layer neural network, although the difference was essentially negligible. My final model used 30 neurons per layer, which provided me with the best results.

One downside to the neural network approach is that it takes quite a long time to predict the expected pegging score given the model. To address this, I was able to refactor my keep function such that, instead of calling predict for every possible combinations of keep cards, I would call it once per call to keep(). This reduced my runtime from about 5 seconds per game to about 0.3 seconds per game. Still, calling predict on my model takes a significantly longer time than simply performing a hashtable lookup, which is something to consider when designing a game agent.

## How to run
First run `make` to build. Then run `./TestNNCribbage --nn 1000` to play 1000 games of NNPolicy against the Greedy player. Run `./TestNNCribbage 1000` to play 1000 games of MyPolicy (original Assignment 1 keep policy) against the Greedy player. Note that playing 1000 games using NNPolicy takes around 5 to 10 minutes, so perhaps `./TestNNCribbage 100` might be more efficient just to check that the code works and outperforms my original implementation.

To generate the training data and to train the neural network, run `python3 nn.py`. 
