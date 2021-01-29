import sys

game = []
a = int(input("What Size Game GoPy "))

def board_game():
    for i in range(0, a * a, a):
        row = []
        for j in range(a):
            row.append(i + j)
        global b
        b = game.append(row)

    def board():
        for x in range(len(game)):
            for y in range(len(game[x])):
                if str(game[x][y]).isalpha() == True:
                    print("", game[x][y], end="  ")
                elif game[x][y] <= 9:
                    print("", game[x][y], end="  ")
                elif game[x][y] > 9:
                    print(game[x][y], "", end=" ")
            print()

    board()

    while True:
        q = int(input("Player 1 turn --> "))
        if q not in range(a * a):
            print("Please enter a valid number")
        else:
            for i in range(a):
                for j in range(a):
                    if game[i][j] == q:

                        game[i][j:j + 1] = "X"
                        board()
        def winner():
            for i in range(a):
                for j in range(a):
                    if game[i].count("X") == len(game[i]):
                        print("Winner: X")
                        quit()

                    elif game[i].count("O") == len(game[i]):
                        print("Winner: O")
                        quit()
            for i in range(len(game[0])):
                j = []
                for k in game:
                    j.append(k[i])
                if j.count(j[0]) == len(j):
                    print(f"Winner: {j[0]}")
                    quit()
            diags = []
            for idx, reverse_idx in enumerate(reversed(range(len(game)))):
                diags.append(game[idx][reverse_idx])

            if diags.count(diags[0]) == len(diags):
                print(f"Winner: {diags[0]}")
                quit()

            diags = []
            for i in range(len(game)):
                diags.append(game[i][i])

            if diags.count(diags[0]) == len(diags):
                print(f"Winner: {diags[0]}")
                quit()
        winner()

        w = int(input("Player 2 turn --> "))
        if w not in range(a * a):
            print("Please enter a valid number")
        if w == q:
            print("The other player select this cell before ")
        else:
            for i in range(a):
                for j in range(a):
                    if game[i][j] == w:
                        game[i][j:j + 1] = "O"
                        board()
        winner()

board_game()




