# Search

let states be nodes and transformation be the edges

every time we make BFS like search

keep track of the nodes we have been to  -> revised approach

uninformed search - DFS / BFS

find a heuristic function h(i) to estimate the distance to the goal 

let h(i) be the Manhattan distance

A* search: $f(i) = g(i)+h(i)$ 

where $g(i)$ cost to reach state i

 

A* is optimal if :

​	$h(i)$ is admissible (never over-estimate)

​	$h(i)$ is consistent ( $h(i) \le h(i')+c$  if i is c steps away from i)



#### Minimax search

to win the opponent in an adversarial way



Tic tac toe  game

Max player aims to maximize the score, while Min aims to minimize the score

go through all the possible state until get to the terminal state 

each time Min want to get the minimum value while Max want to get the maximum value

![image-20240123165331167](C:\Users\13123\AppData\Roaming\Typora\typora-user-images\image-20240123165331167.png)





##### Optimization

 

alpha-beta pruning

try to get a bound to reduce calculation

![image-20240123180230589](C:\Users\13123\AppData\Roaming\Typora\typora-user-images\image-20240123180230589.png)



depth limited minimax

get another expected function to estimate a score for a state, which is the utility function before





# Knowledge



### propositional logic

logical connectives

not and or implication biconditional (if and only if)



knowledge base : known to be true

entailment:

a entails b means if we know a is true then b must be true either



### inference

try to derive new sentences from the knowledge base



### Model checking algorithm

to determine whether KB entails a

we need to enumerate all possible models to check 



## optimization

and elimination

double negation elimination 

biconditional elimination

De Morgan's law :

​	 not(a and b) -> not a or not b

​	 not(a or b) -> not a and not b

distributive property





### Conversion to CNF

use the above several operations

to change a sentence into CNF expressions



## Inference by resolution

to determine whether KB entails a

check if KB and not a leads to a contradict:

​	convert it to CNF

​	keep checking to see if we can use resolution to produce new clause

​		If ever we produce an empty clause, then we have a contradiction

​		else, there is no new resolution

If so, KB entails a.





#### First-Order Logic



made up of Constant Symbols and Predicate Symbols

the Predicate Symbols are like the functions



##### universal quantification

$\forall$ 

##### existential quantification

$\exists$





