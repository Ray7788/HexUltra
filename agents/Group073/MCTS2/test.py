from Board import Board

b = Board.from_string("R000000000,00000000000,00000000000,00000000000,00000000000,00000000000,00000000000,00000000000,00000000000,00000000000,00000000000")
print(b._tiles[0][0].visited)