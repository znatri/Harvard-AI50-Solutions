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
    Or(AKnight, AKnave), # Either A's a Knight or a Knave
    Implication(AKnave, Not(AKnight)), # If A's a Knave it cannot be knight
    Biconditional(AKnave, Not(And(AKnave, AKnight))) # If A is both a Knight and a Knave then he is lying.
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), # Either A's a Knight or a Knave
    Or(BKnight, BKnave), # Either B's a Knight or a Knave
    Implication(AKnave, Not(AKnight)), # If A's a Knave it cannot be knight
    Implication(BKnave, Not(BKnight)), # If B's a Knave it cannot be knight
    Biconditional(AKnave, Not(And(AKnave, BKnave))) # If A says he's a Knave and B's a Knave than he's lying, B must be a Knight. Knaves always lie.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    Or(AKnight, AKnave), # Either A's a Knight or a Knave
    Or(BKnight, BKnave), # Either B's a Knight or a Knave
    Implication(AKnave, Not(AKnight)), # If A's a Knave it cannot be knight
    Implication(BKnave, Not(BKnight)), # If B's a Knave it cannot be knight
    Biconditional(AKnave, Not(And(AKnave, BKnave))), # If A is a telling the truth then they both are same kind.
    Biconditional(BKnave, And(AKnight, BKnight)) # If B is telling the truth they both are different kinds.
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave), # Either A's a Knight or a Knave
    Or(BKnight, BKnave), # Either B's a Knight or a Knave
    Or(CKnight, CKnave), # Either C's a Knight or a Knave
    Implication(AKnave, Not(AKnight)), # If A's a Knave it cannot be Knight
    Implication(BKnave, Not(BKnight)), # If B's a Knave it cannot be Knight
    Implication(CKnave, Not(CKnight)), # If C's a Knave it cannot be Knight
    Biconditional(AKnight, Or(AKnight, AKnave)), # If A is telling the truth then it's either a Knight or a Knave.
    Biconditional(BKnight, Not(AKnight)), # If B is telling the truth then A is not a Knight
    Biconditional(BKnight, CKnave), # If B is telling the truth then C is a Knave
    Biconditional(Not(CKnave), AKnight) # If C is not a Knave then A is a Knight. C is telling the truth.
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
