## Testing document

### Unit testing

To execute the unit tests, run the following command:

```poetry run invoke test```

The unit tests are executed using pytest and currently concentrate on verifying some simple functionalities of the game.

### Test coverage

For a coverage report, run the following command:

```poetry run invoke coverage-report```

Coverage for the program currently:

<img width="688" alt="Screenshot 2023-07-05 at 1 18 53" src="https://github.com/nicolaskivimaki/tiralabra-K23/assets/86207135/2360abd5-c5db-40c7-a558-66f1e7321c39">

### Game tests

The aim of the game tests is to verify that parts of the code responsible for maintaining basic operations required to run the game are working. For example, we test that it is possible to drop pieces onto the board, get empty columns and return whether a game is over or not. All of these are essential for the game to work.

### AI tests

With the AI unit tests, we aim to test and verify the correctness of the AI_engine class and the minimax algorithm. We have multiple different created game states to test whether the AI is able to find the best move and also show how the AI is not able to find the same move at a lower depth of search. We test a variety of different situations, from simple game states where a win/loss can be achieved with one correct move to more difficult states, where a win is certain with e.g. 2 or 7 correct moves.

We also test the heuristic evaluation function to verify that the function calculates the correct scores for moves in different scenarios.
