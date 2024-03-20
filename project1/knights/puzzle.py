from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
A_says_0 = And(AKnave,AKnight)
knowledge0 = And(
    Or(AKnight,AKnave),
    Implication(AKnave,Not(AKnight)),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(A_says_0)),
    Implication(AKnight,A_says_0)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_says_1 = And(AKnave,BKnave)
knowledge1 = And(
    Or(AKnight,AKnave),
    Implication(AKnave,Not(AKnight)),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(A_says_1)),
    Implication(AKnight,A_says_1),
    Or(BKnight,BKnave),
    Implication(BKnave,Not(BKnight)),
    Implication(BKnight,Not(BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_says_2 = Or(
    And(AKnave,BKnave),
    And(AKnight,BKnight)
)
B_says_2 = Or(
    And(AKnave,BKnight),
    And(AKnight,BKnave)
)
knowledge2 = And(
    Or(AKnight,AKnave),
    Implication(AKnave,Not(AKnight)),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(A_says_2)),
    Implication(AKnight,A_says_2),
    Or(BKnight,BKnave),
    Implication(BKnave,Not(BKnight)),
    Implication(BKnight,Not(BKnave)),
    Implication(BKnave,Not(B_says_2)),
    Implication(BKnight,B_says_2)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

knowledge3 = And(
    Or(AKnight,AKnave),
    Implication(AKnave,Not(AKnight)),
    Implication(AKnight,Not(AKnave)),
    Or(BKnight,BKnave),
    Implication(BKnave,Not(BKnight)),
    Implication(BKnight,Not(BKnave)),
    Or(CKnave,CKnight),
    Implication(CKnave,Not(CKnight)),
    Implication(CKnight,Not(CKnave)),

    Implication(AKnave,And(Not(AKnave),Not(AKnight))),
    Implication(BKnight,AKnave),
    Implication(BKnave,AKnight),
    Implication(CKnight,AKnight),
    Implication(CKnave,AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
