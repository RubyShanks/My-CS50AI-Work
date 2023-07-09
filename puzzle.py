from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Biconditional(AKnight, Not(AKnave)), # If A is a Knight then A cannot be a knave and if A is not a knave then A must be a knight 
    Biconditional(AKnave, Not(AKnight)), # If A is a Knave then A cannot be a knight and if A is not a knight then A must be a knave

    Biconditional(AKnight, And(AKnight, AKnave)), # If A is a knight then his statement must be true and vice versa
    Biconditional(AKnave, Not(And(AKnight, AKnave))) # If A is a knave then his statement must be false and vice versa
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(BKnight, Not(BKnave)),

    Biconditional(AKnight, And(AKnave, BKnave)),
    Biconditional(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(BKnight, Not(BKnave)),

    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Biconditional(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
    Biconditional(CKnave, Not(CKnight)),
    
    Or( # A must have said one of the two statements, so 1 statement is said by A for sure
        And( # Assuming A said 'I am a knight', the following must be true
            Biconditional(AKnight, AKnight),
            Biconditional(AKnave, Not(AKnight))
        ),
        And( # Assuming A said 'I am a knave', the following must be true
            Biconditional(AKnight, AKnave),
            Biconditional(AKnave, Not(AKnave))
        )
    ),
    
    # If B is a knight, it must be true that A said 'I am a knave'
    Biconditional(BKnight, 
                  And( # If A said 'I am a knave', the following two conditions must hold
                      Biconditional(AKnight, AKnave),
                      Biconditional(AKnave, Not(AKnave))
                    )
                  ),
    # If B is a knave it must be false that A said 'I am a knave'. So A must have said 'I am a knight' 
    Biconditional(BKnave,
                  And(
                      Biconditional(AKnight, AKnight),
                      Biconditional(AKnave, Not(AKnight))
                    )
                  ),

    Biconditional(BKnight, CKnave),
    Biconditional(BKnave, Not(CKnave)),
    Biconditional(CKnight, AKnight),
    Biconditional(CKnave, Not(AKnight))
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