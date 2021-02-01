import pygame as py
import sys

py.init()

#İnitialize constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0,0,255)
WINDOW_WIDTH=900
WINDOW_HEIGHT=640

#Set the name of the game
#Chess-board

py.display.set_caption('Chess Game')

#background of the screen
background=py.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
background.fill(WHITE)

#Grids of the chess-board
class Grid(py.sprite.Sprite):
    def __init__(self,x_pos,y_pos,sqr_number,number):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = number
        self.sqr_number = sqr_number
        # gets rect from images according to pieces' square number
        if self.sqr_number % 2 == 0:
            self.image = py.image.load("squareW.png")
            self.image = py.transform.scale(self.image,(80, 80))

        else:
            self.image = py.image.load("squareB.png")
            self.image = py.transform.scale(self.image,(80,80))

        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))

class checked_piece():
    def __init__(self):
        self.piece = None


#Pawn piece
class Pawn(py.sprite.Sprite):
    initial_pawn_x_pos = 40
    initial_black_pawn_y_pos = 120
    initial_white_pawn_y_pos = 520
    def __init__(self,color,grid):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.grid = grid
        self.x_pos = grid.rect.center[0]
        self.y_pos = grid.rect.center[1]
        self.color = color
        self.double_moved = False
        # gets rect from images according to pieces' color
        if self.color == "b":
            self.image = py.image.load("bp.png")
            self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))
        elif self.color == "w":
            self.image = py.image.load("wp.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))




#Knight class
class Knight(py.sprite.Sprite):
    initial_knight_x_pos = 120
    initial_white_knight_y_pos = 600
    initial_black_knight_y_pos = 40
    def __init__(self,color,grid):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.grid = grid
        self.x_pos = grid.rect.center[0]
        self.y_pos = grid.rect.center[1]
        self.color = color
        #gets rect from images according to pieces' color
        if self.color == "b":
            self.image = py.image.load("bN.png")
            self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))
        elif self.color == "w":
            self.image = py.image.load("wN.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def move(self):
        pass


class Bishop(py.sprite.Sprite):

    initial_bishop_x_pos = 200
    initial_white_bishop_y_pos = 600
    initial_black_bishop_y_pos = 40

    def __init__(self,color,grid):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.grid = grid
        self.x_pos = grid.rect.center[0]
        self.y_pos = grid.rect.center[1]
        self.color = color
        # gets rect from images according to pieces' color
        if self.color == "b":
            self.image = py.image.load("bB.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        elif self.color == "w":
            self.image = py.image.load("wB.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def move(self):
        pass

class Rook(py.sprite.Sprite):
    initial_rook_x_pos = 40
    initial_white_rook_y_pos = 600
    initial_black_rook_y_pos = 40

    def __init__(self,color,grid):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.grid = grid
        self.x_pos = grid.rect.center[0]
        self.y_pos = grid.rect.center[1]
        self.color = color
        self.moved = False
        # gets rect from images according to pieces' color
        if self.color == "b":
            self.image = py.image.load("bR.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        elif self.color == "w":
            self.image = py.image.load("wR.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def move(self):
        pass


class Queen(py.sprite.Sprite):
    initial_queen_x_pos = 280
    initial_white_queen_y_pos = 600
    initial_black_queen_y_pos = 40

    def __init__(self,color,grid):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.grid = grid
        self.x_pos = grid.rect.center[0]
        self.y_pos = grid.rect.center[1]
        self.color = color
        # gets rect from images according to pieces' color
        if self.color == "b":
            self.image = py.image.load("bQ.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        elif self.color == "w":
            self.image = py.image.load("wQ.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def move(self):
        pass


class King(py.sprite.Sprite):
    initial_king_x_pos = 360
    initial_white_king_y_pos = 600
    initial_black_king_y_pos = 40

    def __init__(self,color,grid):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.x_pos = grid.rect.center[0]
        self.y_pos = grid.rect.center[1]
        self.color = color
        self.grid = grid
        self.moved = False
        # gets rect from images according to pieces' color
        if self.color == "b":
            self.image = py.image.load("bK.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        elif self.color == "w":
            self.image = py.image.load("wK.png")
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def move(self):
        pass


import pygame as py


def P_Move(piece, ls, grid ):
    temp = ls + [grid.number]
    temp.remove(piece.grid.number)
    if piece.color == "w":
        for king in white_king:
            if check(king.grid, king.color, temp, grid.number):
                return
    else:
        for king in black_king:
            if check(king.grid, king.color, temp, grid.number):
                return

    if grid.number not in ls and piece.grid.x_pos == grid.x_pos:
        if (piece.color == "w" and grid.y_pos <= piece.grid.y_pos):
            if (piece.grid.y_pos == 520):
                if grid.y_pos >= 360:
                    return True

            elif grid.y_pos == piece.grid.y_pos - 80:
                return True

        elif (piece.color == "b" and grid.y_pos >= piece.grid.y_pos):
            if (piece.grid.y_pos == 120):
                if (grid.y_pos <= 280):
                    return True

            elif grid.y_pos == piece.grid.y_pos + 80:
                return True
        else:
            return

    elif grid.number in ls:
        for pieces in List_of_Pieces:
            for p in pieces.sprites():
                if p.grid.number == grid.number:
                    if piece.color != p.color and not isinstance(p, King):
                        temp = ls + [grid.number]
                        temp.remove(piece.grid.number)
                        if piece.color == "w":
                            for king in white_king:
                                if check(king.grid, king.color, temp, grid.number):
                                    return False
                        else:
                            for king in black_king:
                                if check(king.grid, king.color, temp, grid.number):
                                    return

                        if piece.color == "w":
                            if (p.grid.number + 9 == piece.grid.number) or (p.grid.number + 7 == piece.grid.number):
                                return True
                        else:
                            if (p.grid.number - 9 == piece.grid.number) or (p.grid.number - 7 == piece.grid.number):
                                return True

                        return

    elif (piece.color == "w" and piece.grid.rect.center[1] == 280) or (piece.color == "b" and piece.grid.rect.center[1] == 360) and grid.number not in ls:
        if piece.color == "w":
            for pawn in black_pawns:
                if pawn.double_moved == True and (pawn.grid.number == piece.grid.number - 1 or pawn.grid.number == piece.grid.number + 1):
                    if grid.number == pawn.grid.number - 8:
                        return True
                    else:
                        return True
        else:
            for pawn in white_pawns:
                if pawn.double_moved and (pawn.grid.number == piece.grid.number - 1 or pawn.grid.number == piece.grid.number + 1):
                    if grid.number == pawn.grid.number + 8:
                        return True


def K_move(piece, ls ,grid):
    number_list = [-15, 15, -17, 17, -6, 6, -10, 10]
    for nm in number_list:
        if (grid.number == piece.grid.number + nm):
            if grid.number not in ls:
                temp = ls + [grid.number]
                temp.remove(piece.grid.number)
                if piece.color == "w":
                    for king in white_king:
                        if check(king.grid, king.color, temp, grid.number):
                            return
                else:
                    for king in black_king:
                        if check(king.grid, king.color, temp, grid.number):
                            return
                return True

            elif grid.number in ls:
                for pieces in List_of_Pieces:
                    for p in pieces.sprites():
                        if p.grid.number == grid.number:
                            temp = ls + [p.grid.number]
                            temp.remove(piece.grid.number)
                            if piece.color == "w":
                                for king in white_king:
                                    if check(king.grid, king.color, temp, grid.number):
                                        return
                            else:
                                for king in black_king:
                                    if check(king.grid, king.color, temp, grid.number):
                                        return
                            if piece.color != p.color and not isinstance(p, King):
                                for nm in number_list:
                                    if (p.grid.number == piece.grid.number + nm):
                                        return True
                                else:
                                    return
                            else:
                                return
            else:
                return


def R_move(piece, ls , grid):
    if grid.number not in ls:
        temp = ls + [grid.number]
        temp.remove(piece.grid.number)
        if piece.color == "w":
            for king in white_king:
                if check(king.grid, king.color, temp, grid.number):
                    return
        else:
            for king in black_king:
                if check(king.grid, king.color, temp, grid.number):
                    return

        if grid.rect.center[1] == piece.grid.rect.center[1]:
            for nm in range(min(grid.number, piece.grid.number), max(grid.number, piece.grid.number) + 1):
                if nm in ls and nm != piece.grid.number:
                    return
            else:
                return True

        elif grid.rect.center[0] == piece.grid.rect.center[0]:
            for nm in range(min(grid.number, piece.grid.number + 8), max(grid.number, piece.grid.number) + 1, 8):
                if nm in list_of_numbers and nm != piece.grid.number:
                    return

            else:
                return True
    else:
        for pieces in List_of_Pieces:
            for p in pieces.sprites():
                if p.grid.number == grid.number:
                    temp = ls + [grid.number]
                    temp.remove(piece.grid.number)
                    if piece.color == "w":
                        for king in white_king:
                            if check(king.grid, king.color, temp, grid.number):
                                return
                    else:
                        for king in black_king:
                            if check(king.grid, king.color, temp, grid.number):
                                return

                    if piece.color != p.color and not isinstance(p, King):
                        if p.grid.rect.center[1] == piece.grid.rect.center[1]:
                            for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number) + 1):
                                if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                    return
                            else:
                                return True

                        elif p.grid.rect.center[0] == piece.grid.rect.center[0]:
                            for nm in range(min(p.grid.number, piece.grid.number + 8),max(p.grid.number, piece.grid.number) + 1, 8):
                                if nm in list_of_numbers and nm != piece.grid.number and nm != p.grid.number:
                                    return

                            else:
                                return True
                    else:
                        return


def B_move(piece, ls,grid):
    if grid.number not in ls:
        temp = ls + [grid.number]
        temp.remove(piece.grid.number)
        if piece.color == "w":
            for king in white_king:
                if check(king.grid, king.color, temp, grid.number):
                    return
        else:
            for king in black_king:
                if check(king.grid, king.color, temp, grid.number):
                    return
        if abs(grid.number - piece.grid.number) % 7 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
            for nm in range(min(grid.number, piece.grid.number), max(grid.number, piece.grid.number) + 1, 7):
                if nm in ls and nm != piece.grid.number:
                    return
            else:
                return True

        elif abs(grid.number - piece.grid.number) % 9 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
            for nm in range(min(grid.number, piece.grid.number), max(grid.number, piece.grid.number) + 1, 9):
                if nm in ls and nm != piece.grid.number:
                    return
            else:
                return True
    else:
        for pieces in List_of_Pieces:
            for p in pieces.sprites():
                if p.grid.number == grid.number:
                    temp = ls + [grid.number]
                    temp.remove(piece.grid.number)
                    if piece.color == "w":
                        for king in white_king.sprites():
                            if check(king.grid, king.color, temp, grid.number):
                                return
                    else:
                        for king in black_king.sprites():
                            if check(king.grid, king.color, temp, grid.number):
                                return
                    if piece.color != p.color and not isinstance(p, King):
                        if (abs(piece.grid.number - p.grid.number) % 7 == 0) and (p.grid.rect.center[1] != piece.grid.rect.center[1]):
                            for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number) + 1, 7):
                                if nm in ls and nm != p.grid.number and nm != piece.grid.number:
                                    return
                            else:
                                return True
                        elif (abs(piece.grid.number - p.grid.number) % 9 == 0) and (p.grid.rect.center[1] != piece.grid.rect.center[1]):
                            for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number) + 1, 9):
                                if nm in ls and nm != p.grid.number and nm != piece.grid.number:
                                    return
                            else:
                                return True
                    else:
                        return


def Q_move(piece, ls,grid):
    if grid.number not in ls:
        temp = ls + [grid.number]
        temp.remove(piece.grid.number)
        if piece.color == "w":
            for king in white_king.sprites():
                if check(king.grid, king.color, temp, grid.number):
                    return
        else:
            for king in black_king.sprites():
                if check(king.grid, king.color, temp, grid.number):
                    return
        if abs(grid.number - piece.grid.number) % 7 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
            for nm in range(min(grid.number, piece.grid.number),max(grid.number, piece.grid.number) + 1, 7):
                if nm in ls and nm != piece.grid.number and nm != grid.number:
                    return
            else:
                return True

        elif abs(grid.number - piece.grid.number) % 9 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
            for nm in range(min(grid.number, piece.grid.number),max(grid.number, piece.grid.number), 9):
                if nm in ls and nm != piece.grid.number and nm != grid.number:
                    return
            else:
                return True
        elif grid.rect.center[1] == piece.grid.rect.center[1]:
            for nm in range(min(grid.number, piece.grid.number),max(grid.number, piece.grid.number)):
                if nm in ls and nm != piece.grid.number and nm != grid.number:
                    return
            else:
                return True

        elif grid.rect.center[0] == piece.grid.rect.center[0]:
            for nm in range(min(grid.number, piece.grid.number),max(grid.number, piece.grid.number), 8):
                if nm in list_of_numbers and nm != piece.grid.number and nm != grid.number:
                    return

            else:
                return True
    else:
        for pieces in List_of_Pieces:
            for p in pieces.sprites():
                if p.grid.number == grid.number:
                    temp = ls + [grid.number]
                    temp.remove(piece.grid.number)
                    if piece.color == "w":
                        for king in white_king.sprites():
                            if check(king.grid, king.color, temp, grid.number):
                                return
                    else:
                        for king in black_king.sprites():
                            if check(king.grid, king.color, temp, grid.number):
                                return

                    if piece.color != p.color and not isinstance(p, King):
                        if abs(p.grid.number - piece.grid.number) % 7 == 0 and p.grid.rect.center[
                            1] != piece.grid.rect.center[1]:
                            for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number), 7):
                                if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                    return
                            else:
                                return True



                        elif abs(p.grid.number - piece.grid.number) % 9 == 0 and p.grid.rect.center[1] != \
                                piece.grid.rect.center[1]:
                            for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number), 9):
                                if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                    return
                            else:
                                return True
                        elif p.grid.rect.center[1] == piece.grid.rect.center[1]:
                            for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number)):
                                if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                    return
                            else:
                                return True

                        elif p.grid.rect.center[0] == piece.grid.rect.center[0]:
                            for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number), 8):
                                if nm in list_of_numbers and nm != piece.grid.number and nm != p.grid.number:
                                    return

                            else:
                                return True
                    else:
                        return


def Kg_move(piece, ls,grid):
    numbers = [6400, 12800]
    if grid.number not in ls:
        temp = ls + [grid.number]
        temp.remove(piece.grid.number)
        if piece.color == "w":
            for king in white_king.sprites():
                if check(grid, king.color, temp, grid.number):
                    return
        else:
            for king in black_king.sprites():
                if check(grid, king.color, temp, grid.number):
                    return

        for nm in numbers:
            if (pow(grid.rect.center[0] - piece.grid.rect.center[0], 2) + pow(grid.rect.center[1] - piece.grid.rect.center[1], 2)) == nm:
                return True
            else:
                pass
        else:
            return

    else:
        for pieces in List_of_Pieces:
            for p in pieces.sprites():
                if p.grid.number == grid.number:
                    if piece.color != p.color and not isinstance(p, King) and not check(grid, piece.color, ls,grid.number):
                        for nm in numbers:
                            if (pow(p.rect.center[0] - piece.grid.rect.center[0], 2) + pow(p.rect.center[1] - piece.grid.rect.center[1], 2)) == nm:
                                return True
                        else:
                            return
                else:
                    return


def checkmate(list_of_numbers,color):
    for pieces in List_of_Pieces:
        for p in pieces.sprites():
            for grid in chess_grids.sprites():
                if isinstance(p, Pawn) and P_Move(p, list_of_numbers, grid) and p.color == color:
                    return True

                elif isinstance(p, Knight) and K_move(p, list_of_numbers, grid) and p.color == color:
                    return True
                elif isinstance(p, Rook) and R_move(p, list_of_numbers, grid) and p.color == color:
                    return True

                elif isinstance(p, Bishop) and B_move(p, list_of_numbers, grid) and p.color == color:
                    return True

                elif isinstance(p, Queen) and Q_move(p, list_of_numbers, grid) and p.color == color:
                    return True

                elif isinstance(p, King) and Kg_move(p, list_of_numbers, grid) and p.color == color:
                    return True
    else:
        return False

def Pawn_Move(piece,ls,T):
    while True:
        for i in py.event.get():
            if i.type == py.MOUSEBUTTONUP:
                mv_pos = py.mouse.get_pos()
                if piece.rect.collidepoint(mv_pos):
                    return T
                for grid in chess_grids.sprites():
                    if grid.rect.collidepoint(mv_pos):
                        temp = ls + [grid.number]
                        temp.remove(piece.grid.number)
                        if piece.color == "w":
                            for king in white_king:
                                if check(king.grid, king.color, temp, grid.number):
                                    return T
                        else:
                            for king in black_king:
                                if check(king.grid, king.color, temp, grid.number):
                                    return T
                        if grid.number not in ls and piece.grid.x_pos == grid.x_pos:
                            if (piece.color == "w" and grid.y_pos <= piece.grid.y_pos):
                                if (piece.grid.y_pos == 520):
                                    if grid.y_pos >= 360:
                                        if grid.y_pos == 360:
                                            piece.double_moved = True
                                        if piece.grid.sqr_number % 2 == 0:

                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                            piece.grid = grid
                                            piece.rect.center = piece.grid.rect.center
                                            background.blit(piece.image, piece.rect)
                                            py.display.update(piece)

                                            return T+1

                                        else:

                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                            piece.grid = grid
                                            piece.rect.center = piece.grid.rect.center
                                            background.blit(piece.image, piece.rect)
                                            py.display.update(piece)

                                            return T+1

                                elif grid.y_pos == piece.grid.y_pos - 80:
                                    if piece.grid.sqr_number % 2 == 0:

                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1

                                    else:

                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1

                            elif (piece.color == "b" and grid.y_pos >= piece.grid.y_pos):
                                if (piece.grid.y_pos == 120):
                                    if (grid.y_pos <= 280):
                                        if grid.y_pos == 280:
                                            piece.double_moved = True
                                        if piece.grid.sqr_number % 2 == 0:
                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                            piece.grid = grid
                                            piece.rect.center = piece.grid.rect.center
                                            background.blit(piece.image, piece.rect)
                                            py.display.update(piece)

                                            return T+1
                                        else:
                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                            piece.grid = grid
                                            piece.rect.center = piece.grid.rect.center
                                            background.blit(piece.image, piece.rect)
                                            py.display.update(piece)

                                            return T+1

                                elif grid.y_pos == piece.grid.y_pos + 80:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                            else:
                                return T

                        elif grid.number in ls:
                            for pieces in List_of_Pieces:
                                for p in pieces.sprites():
                                    if p.rect.collidepoint(mv_pos):
                                        if piece.color != p.color and not isinstance(p,King):
                                            temp = ls + [grid.number]
                                            temp.remove(piece.grid.number)
                                            if piece.color == "w":
                                                for king in white_king:
                                                    if check(king.grid, king.color, temp, grid.number):
                                                        return T
                                            else:
                                                for king in black_king:
                                                    if check(king.grid, king.color, temp, grid.number):
                                                        return T
                                            if piece.color == "w":
                                                if (p.grid.number +9 == piece.grid.number) or (p.grid.number +7 == piece.grid.number):
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number %2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()

                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number %2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                            else:
                                                if (p.grid.number-9 == piece.grid.number) or (p.grid.number -7 == piece.grid.number):
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number %2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()

                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number %2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                        else:
                                            return T

                        elif (piece.color == "w" and piece.grid.rect.center[1] == 280) or (piece.color == "b" and piece.grid.rect.center[1] == 360) and grid.number not in ls:
                            if piece.color == "w":
                                for pawn in black_pawns:
                                    if pawn.double_moved == True and (pawn.grid.number  == piece.grid.number - 1 or pawn.grid.number == piece.grid.number + 1):
                                        if grid.number == pawn.grid.number - 8:
                                            if piece.grid.sqr_number % 2 == 0:
                                                background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                piece.grid = grid
                                                piece.rect.center = piece.grid.rect.center
                                                if grid.sqr_number % 2 == 0:
                                                    background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), grid.rect)
                                                    if pawn.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),pawn.grid.rect)
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),pawn.grid.rect)
                                                    pawn.kill()
                                                else:
                                                    background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), grid.rect)
                                                    if pawn.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),pawn.grid.rect)
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),pawn.grid.rect)
                                                    pawn.kill()
                                                background.blit(piece.image, piece.rect)
                                                py.display.update(piece)
                                                return T + 1
                                            else:
                                                background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                piece.grid = grid
                                                piece.rect.center = piece.grid.rect.center
                                                if grid.sqr_number % 2 == 0:
                                                    background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), grid.rect)
                                                    if pawn.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),pawn.grid.rect)
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),pawn.grid.rect)
                                                    pawn.kill()
                                                else:
                                                    background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), grid.rect)
                                                    if pawn.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),pawn.grid.rect)
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),pawn.grid.rect)
                                                    pawn.kill()
                                                background.blit(piece.image, piece.rect)
                                                py.display.update(piece)
                                                return T + 1
                            else:
                                for pawn in white_pawns:
                                        if pawn.double_moved and (pawn.grid.number  == piece.grid.number -1 or pawn.grid.number == piece.grid.number + 1):
                                            if grid.number == pawn.grid.number + 8:
                                                if piece.grid.sqr_number % 2 == 0:
                                                    background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                    piece.grid = grid
                                                    piece.rect.center = piece.grid.rect.center
                                                    if pawn.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), pawn.grid.rect)
                                                        pawn.kill()
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), pawn.grid.rect)
                                                        pawn.kill()

                                                    background.blit(piece.image, piece.rect)
                                                    py.display.update(piece)
                                                    return T + 1
                                                else:
                                                    background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                    piece.grid = grid
                                                    piece.rect.center = piece.grid.rect.center
                                                    if pawn.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), pawn.grid.rect)
                                                        pawn.kill()
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), pawn.grid.rect)
                                                        pawn.kill()
                                                    background.blit(piece.image, piece.rect)
                                                    py.display.update(piece)
                                                    return T + 1




def Knight_move(piece,ls,T):
    number_list = [-15,15,-17,17,-6,6,-10,10]
    while True:
        for i in py.event.get():
            if i.type == py.MOUSEBUTTONUP:
                mv_pos = py.mouse.get_pos()
                if piece.rect.collidepoint(mv_pos):
                    return T
                for grid in chess_grids.sprites():
                    if grid.rect.collidepoint(mv_pos):
                        for nm in number_list:
                            if (grid.number == piece.grid.number + nm):
                                if grid.number not in ls:
                                    temp = ls + [grid.number]
                                    temp.remove(piece.grid.number)
                                    if piece.color == "w":
                                        for king in white_king:
                                            if check(king.grid, king.color, temp, grid.number):
                                                return T
                                    else:
                                        for king in black_king:
                                            if check(king.grid, king.color, temp, grid.number):
                                                return T
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1

                                elif grid.number in ls:
                                    for pieces in List_of_Pieces:
                                        for p in pieces.sprites():
                                            if p.rect.collidepoint(mv_pos):
                                                for nm in number_list:
                                                    if (p.grid.number == piece.grid.number + nm):
                                                        break
                                                else:
                                                    return T

                                                temp = ls + [p.grid.number]
                                                temp.remove(piece.grid.number)
                                                if piece.color == "w":
                                                    for king in white_king:
                                                        if check(king.grid, king.color, temp, grid.number):
                                                            return T
                                                else:
                                                    for king in black_king:
                                                        if check(king.grid, king.color, temp, grid.number):
                                                            return T
                                                if piece.color != p.color and not isinstance(p,King):
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number %2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()

                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number %2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1

                                                else:
                                                    return T
                                else:
                                    return T



def Rook_move(piece,ls,T):
    while True:
        for i in py.event.get():
            if i.type == py.MOUSEBUTTONUP:
                mv_pos = py.mouse.get_pos()
                if piece.rect.collidepoint(mv_pos):
                    return T
                for grid in chess_grids.sprites():
                    if grid.rect.collidepoint(mv_pos):
                        if grid.number not in ls:
                            temp = ls + [grid.number]
                            temp.remove(piece.grid.number)
                            if piece.color == "w":
                                for king in white_king:
                                    if check(king.grid, king.color, temp, grid.number):
                                        return T
                            else:
                                for king in black_king:
                                    if check(king.grid, king.color, temp, grid.number):
                                        return T

                            if grid.rect.center[1] == piece.grid.rect.center[1]:
                                for nm in range(min(grid.number,piece.grid.number),max(grid.number,piece.grid.number)+1):
                                    if nm in ls and nm != piece.grid.number:
                                        return T
                                else:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)
                                        piece.moved = True
                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)
                                        piece.moved = True
                                        return T+1

                            elif grid.rect.center[0] == piece.grid.rect.center[0]:
                                for nm in range(min(grid.number,piece.grid.number+8),max(grid.number,piece.grid.number)+1,8):
                                    if nm in list_of_numbers and nm != piece.grid.number:
                                        return T

                                else:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)
                                        piece.moved = True
                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)
                                        piece.moved = True
                                        return T+1
                        else:
                            for pieces in List_of_Pieces:
                                for p in pieces.sprites():
                                    if p.rect.collidepoint(mv_pos):
                                        temp = ls + [grid.number]
                                        temp.remove(piece.grid.number)
                                        if piece.color == "w":
                                            for king in white_king:
                                                if check(king.grid, king.color, temp, grid.number):
                                                    return T
                                        else:
                                            for king in black_king:
                                                if check(king.grid, king.color, temp, grid.number):
                                                    return T
                                        if piece.color != p.color and not isinstance(p, King):
                                            if p.grid.rect.center[1] == piece.grid.rect.center[1]:
                                                for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number) + 1):
                                                    if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                                        return T
                                                else:
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        piece.moved = True
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        piece.moved = True
                                                        return T+1


                                            elif p.grid.rect.center[0] == piece.grid.rect.center[0]:
                                                for nm in range(min(p.grid.number, piece.grid.number + 8),max(p.grid.number, piece.grid.number) + 1, 8):
                                                    if nm in list_of_numbers and nm != piece.grid.number and nm != p.grid.number:
                                                        return T

                                                else:
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(
                                                            py.transform.scale(py.image.load("squareW.png"), (80, 80)),
                                                            piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        piece.moved = True
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)),piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        piece.moved = True
                                                        return T+1
                                        else:
                                            return T

def Bishop_move(piece, ls,T):
   while True:
       for i in py.event.get():
           if i.type == py.MOUSEBUTTONUP:
               mv_pos = py.mouse.get_pos()
               if piece.rect.collidepoint(mv_pos):
                   return T
               for grid in chess_grids.sprites():
                   if grid.rect.collidepoint(mv_pos):
                       if grid.number not in ls:
                           temp = ls + [grid.number]
                           temp.remove(piece.grid.number)
                           if piece.color == "w":
                               for king in white_king:
                                   if check(king.grid, king.color, temp, grid.number):
                                       return T
                           else:
                               for king in black_king:
                                   if check(king.grid, king.color, temp, grid.number):
                                       return T
                           if abs(grid.number - piece.grid.number) % 7 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
                               for nm in range(min(grid.number,piece.grid.number),max(grid.number,piece.grid.number)+1,7):
                                   if nm in ls and nm != piece.grid.number:
                                       return T
                               else:
                                   if piece.grid.sqr_number % 2 == 0:
                                       background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                       piece.grid = grid
                                       piece.rect.center = piece.grid.rect.center
                                       background.blit(piece.image, piece.rect)
                                       py.display.update(piece)

                                       return T+1
                                   else:
                                       background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                       piece.grid = grid
                                       piece.rect.center = piece.grid.rect.center
                                       background.blit(piece.image, piece.rect)
                                       py.display.update(piece)

                                       return T+1

                           elif abs(grid.number - piece.grid.number) % 9 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
                               for nm in range(min(grid.number,piece.grid.number),max(grid.number,piece.grid.number)+1,9):
                                   if nm in ls and nm != piece.grid.number:
                                       return T
                               else:
                                   if piece.grid.sqr_number % 2 == 0:
                                       background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                       piece.grid = grid
                                       piece.rect.center = piece.grid.rect.center
                                       background.blit(piece.image, piece.rect)
                                       py.display.update(piece)

                                       return T+1
                                   else:
                                       background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                       piece.grid = grid
                                       piece.rect.center = piece.grid.rect.center
                                       background.blit(piece.image, piece.rect)
                                       py.display.update(piece)

                                       return T+1
                       else:
                           for pieces in List_of_Pieces:
                               for p in pieces.sprites():
                                   if p.rect.collidepoint(mv_pos):
                                       temp = ls + [grid.number]
                                       temp.remove(piece.grid.number)
                                       if piece.color == "w":
                                           for king in white_king.sprites():
                                               if check(king.grid, king.color, temp, grid.number):
                                                   return T
                                       else:
                                           for king in black_king.sprites():
                                               if check(king.grid, king.color, temp, grid.number):
                                                   return T
                                       if piece.color != p.color and not isinstance(p, King):
                                           if (abs(piece.grid.number - p.grid.number) % 7 == 0) and (p.grid.rect.center[1] != piece.grid.rect.center[1]):
                                               for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number) + 1, 7):
                                                   if nm in ls and nm != p.grid.number and nm != piece.grid.number:
                                                       return T
                                               else:
                                                   if piece.grid.sqr_number % 2 == 0:
                                                       background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                       piece.grid = p.grid
                                                       piece.rect.center = piece.grid.rect.center
                                                       if p.grid.sqr_number % 2 == 0:
                                                           background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       else:
                                                           background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       background.blit(piece.image, piece.rect)
                                                       py.display.update(piece)
                                                       return T+1
                                                   else:
                                                       background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                       piece.grid = p.grid
                                                       piece.rect.center = piece.grid.rect.center
                                                       if p.grid.sqr_number % 2 == 0:
                                                           background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       else:
                                                           background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       background.blit(piece.image, piece.rect)
                                                       py.display.update(piece)
                                                       return T+1


                                           elif (abs(piece.grid.number - p.grid.number) % 9 == 0) and (p.grid.rect.center[1] != piece.grid.rect.center[1]):
                                               for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number) + 1, 9):
                                                   if nm in ls and nm != p.grid.number and nm != piece.grid.number:
                                                       return T
                                               else:
                                                   if piece.grid.sqr_number % 2 == 0:
                                                       background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                       piece.grid = p.grid
                                                       piece.rect.center = piece.grid.rect.center
                                                       if p.grid.sqr_number % 2 == 0:
                                                           background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       else:
                                                           background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       background.blit(piece.image, piece.rect)
                                                       py.display.update(piece)
                                                       return T+1
                                                   else:
                                                       background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                       piece.grid = p.grid
                                                       piece.rect.center = piece.grid.rect.center
                                                       if p.grid.sqr_number % 2 == 0:
                                                           background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       else:
                                                           background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                           p.kill()
                                                       background.blit(piece.image, piece.rect)
                                                       py.display.update(piece)
                                                       return T+1
                                       else:
                                           return T
                                                                                                                                                                  

def Queen_move(piece,ls,T):
    while True:
        for i in py.event.get():
            if i.type == py.MOUSEBUTTONUP:
                mv_pos = py.mouse.get_pos()
                if piece.rect.collidepoint(mv_pos):
                    return T
                for grid in chess_grids.sprites():
                    if grid.rect.collidepoint(mv_pos):
                        if grid.number not in ls:
                            temp = ls + [grid.number]
                            temp.remove(piece.grid.number)
                            if piece.color == "w":
                                for king in white_king.sprites():
                                    if check(king.grid, king.color, temp, grid.number):
                                        return T
                            else:
                                for king in black_king.sprites():
                                    if check(king.grid, king.color, temp, grid.number):
                                        return T
                            if abs(grid.number - piece.grid.number) % 7 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
                                for nm in range(min(grid.number,piece.grid.number),max(grid.number,piece.grid.number)+1,7):
                                    if nm in ls and nm != piece.grid.number and nm != grid.number:
                                        return T
                                else:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1

                            elif abs(grid.number - piece.grid.number) % 9 == 0 and grid.rect.center[1] != piece.grid.rect.center[1]:
                                for nm in range(min(grid.number,piece.grid.number),max(grid.number,piece.grid.number),9):
                                    if nm in ls and nm!= piece.grid.number and nm != grid.number:
                                        return T
                                else:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                            elif grid.rect.center[1] == piece.grid.rect.center[1]:
                                for nm in range(min(grid.number,piece.grid.number),max(grid.number,piece.grid.number)):
                                    if nm in ls and nm != piece.grid.number and nm != grid.number:
                                        return
                                else:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1

                            elif grid.rect.center[0] == piece.grid.rect.center[0]:
                                for nm in range(min(grid.number,piece.grid.number),max(grid.number,piece.grid.number),8):
                                    if (nm) in list_of_numbers and nm != piece.grid.number and nm != grid.number:
                                        return T

                                else:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)

                                        return T+1
                        else:
                            for pieces in List_of_Pieces:
                                for p in pieces.sprites():
                                    if p.rect.collidepoint(mv_pos):
                                        temp = ls + [grid.number]
                                        temp.remove(piece.grid.number)
                                        if piece.color == "w":
                                            for king in white_king.sprites():
                                                if check(king.grid, king.color, temp, grid.number):
                                                    return T
                                        else:
                                            for king in black_king.sprites():
                                                if check(king.grid, king.color, temp, grid.number):
                                                    return T
                                        if piece.color != p.color and not isinstance(p, King):
                                            if abs(p.grid.number - piece.grid.number) % 7 == 0 and p.grid.rect.center[1] != piece.grid.rect.center[1]:
                                                for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number), 7):
                                                    if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                                        return T
                                                else:
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1



                                            elif abs(p.grid.number - piece.grid.number) % 9 == 0 and p.grid.rect.center[1] != piece.grid.rect.center[1]:
                                                for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number), 9):
                                                    if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                                        return T
                                                else:
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1


                                            elif p.grid.rect.center[1] == piece.grid.rect.center[1]:
                                                for nm in range(min(p.grid.number, piece.grid.number),max(p.grid.number, piece.grid.number)):
                                                    if nm in ls and nm != piece.grid.number and nm != p.grid.number:
                                                        return T
                                                else:
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1

                                            elif p.grid.rect.center[0] == piece.grid.rect.center[0]:
                                                for nm in range(min(p.grid.number, piece.grid.number ),max(p.grid.number, piece.grid.number), 8):
                                                    if nm in list_of_numbers and nm != piece.grid.number and nm != p.grid.number:
                                                        return T

                                                else:
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        return T+1
                                        else:
                                            return T

def King_move(piece,ls,T):
    numbers = [6400,12800]
    while True:
        for i in py.event.get():
            if i.type == py.MOUSEBUTTONUP:
                mv_pos = py.mouse.get_pos()
                if piece.rect.collidepoint(mv_pos):
                    return T
                for grid in chess_grids.sprites():
                    if grid.rect.collidepoint(mv_pos):
                        if grid.number not in ls:
                            temp = ls + [grid.number]
                            temp.remove(piece.grid.number)
                            if piece.color == "w":
                                for king in white_king.sprites():
                                    if check(grid, king.color, temp, grid.number):
                                        return T
                            else:
                                for king in black_king.sprites():
                                    if check(grid, king.color, temp, grid.number):
                                        return T
                            for nm in numbers:
                                if (pow(grid.rect.center[0] - piece.grid.rect.center[0],2) + pow(grid.rect.center[1] - piece.grid.rect.center[1],2)) == nm:
                                    if piece.grid.sqr_number % 2 == 0:
                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)
                                        piece.moved = True
                                        return T+1
                                    else:
                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                        piece.grid = grid
                                        piece.rect.center = piece.grid.rect.center
                                        background.blit(piece.image, piece.rect)
                                        py.display.update(piece)
                                        piece.moved = True
                                        return T+1
                                else:
                                    pass
                            else:
                                return T

                        else:
                            for pieces in List_of_Pieces:
                                for p in pieces.sprites():
                                    if p.rect.collidepoint(mv_pos):
                                        if isinstance(p,Rook) and p.moved == False and piece.moved == False and not check(piece.grid, piece.color,ls,piece.grid.number):
                                            if piece.color == "w":
                                                if 61 not in ls and not 62 in ls:
                                                    for grid in chess_grids:
                                                        if grid.number == 62:
                                                            temp = ls + [62]
                                                            temp.remove(piece.grid.number)
                                                            for king in white_king.sprites():
                                                                if check(grid, king.color, temp, grid.number):
                                                                    return T
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            piece.grid = grid
                                                            piece.rect.center = piece.grid.rect.center
                                                            background.blit(piece.image, piece.rect)
                                                            py.display.update(piece)
                                                            for grid in chess_grids.sprites():
                                                                if grid.number == 61:
                                                                    background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), p.grid.rect)
                                                                    p.grid = grid
                                                                    p.rect.center = p.grid.rect.center
                                                                    background.blit(p.image, p.rect)
                                                                    py.display.update(p)
                                                                    break
                                                            piece.moved = True
                                                            return T+1
                                                elif 57 not in ls and 58 not in ls and 59 not in ls:
                                                    for grid in chess_grids.sprites():
                                                        if grid.number == 58:
                                                            temp = ls + [58]
                                                            temp.remove(piece.grid.number)
                                                            for king in white_king.sprites():
                                                                if check(grid, king.color, temp, grid.number):
                                                                    return T
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            piece.grid = grid
                                                            piece.rect.center = piece.grid.rect.center
                                                            background.blit(piece.image, piece.rect)
                                                            py.display.update(piece)
                                                            for grid in chess_grids.sprites():
                                                                if grid.number == 59:
                                                                    background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), p.grid.rect)
                                                                    p.grid = grid
                                                                    p.rect.center = p.grid.rect.center
                                                                    background.blit(p.image, p.rect)
                                                                    py.display.update(p)
                                                                    break
                                                            piece.moved = True
                                                            return T+1

                                            else:
                                                if p.grid.number == 7 and 5 not in ls and 6 not in ls:
                                                    for grid in chess_grids:
                                                        if grid.number == 6:
                                                            temp = ls + [6]
                                                            temp.remove(piece.grid.number)
                                                            for king in black_king.sprites():
                                                                if check(grid, king.color, temp, grid.number):
                                                                    return T
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            piece.grid = grid
                                                            piece.rect.center = piece.grid.rect.center
                                                            background.blit(piece.image, piece.rect)
                                                            py.display.update(piece)
                                                            for grid in chess_grids.sprites():
                                                                if grid.number == 5:
                                                                    background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), p.grid.rect)
                                                                    p.grid = grid
                                                                    p.rect.center = p.grid.rect.center
                                                                    background.blit(p.image, p.rect)
                                                                    py.display.update(p)
                                                                    break
                                                            piece.moved = True
                                                            return T+1

                                                elif p.grid.number == 0 and 1 not in ls and 2 not in ls and 3 not in ls:
                                                    for grid in chess_grids.sprites():
                                                        if grid.number == 2:
                                                            temp = ls + [2]
                                                            temp.remove(piece.grid.number)
                                                            for king in black_king.sprites() :
                                                                if check(grid, king.color, temp, grid.number):
                                                                    return T
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            piece.grid = grid
                                                            piece.rect.center = piece.grid.rect.center
                                                            background.blit(piece.image, piece.rect)
                                                            py.display.update(piece)
                                                            for grid in chess_grids.sprites():
                                                                if grid.number == 3:
                                                                    background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), p.grid.rect)
                                                                    p.grid = grid
                                                                    p.rect.center = p.grid.rect.center
                                                                    background.blit(p.image, p.rect)
                                                                    py.display.update(p)
                                                                    break
                                                            piece.moved = True
                                                            return T+1

                                        elif piece.color != p.color and not isinstance(p, King) and not check(grid,piece.color,ls,grid.number):
                                            for nm in numbers:
                                                if (pow(p.rect.center[0] - piece.grid.rect.center[0], 2) + pow(p.rect.center[1] - piece.grid.rect.center[1], 2)) == nm:
                                                    if piece.grid.sqr_number % 2 == 0:
                                                        background.blit(py.transform.scale(py.image.load("squareW.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        piece.moved = True
                                                        return T + 1
                                                    else:
                                                        background.blit(py.transform.scale(py.image.load("squareB.png"), (80, 80)),piece.grid.rect)
                                                        piece.grid = p.grid
                                                        piece.rect.center = piece.grid.rect.center
                                                        if p.grid.sqr_number % 2 == 0:
                                                            background.blit(py.transform.scale(py.image.load("squareW.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        else:
                                                            background.blit(py.transform.scale(py.image.load("squareB.png"),(80, 80)), piece.grid.rect)
                                                            p.kill()
                                                        background.blit(piece.image, piece.rect)
                                                        py.display.update(piece)
                                                        piece.moved = True
                                                        return T + 1
                                            else:
                                                return T
                                        else:
                                            return T
                            else:
                                return T


def check(grid,color,ls,mv_number):
    number_list = [-15, 15, -17, 17, -6, 6, -10, 10]
    numbers = [6400, 12800]
    for pieces in List_of_Pieces:
        for p in pieces.sprites():
            if isinstance(p, Pawn) and p.color != color and p.grid.number != mv_number:
                if p.color == "w":
                    if (p.grid.number - 7 == grid.number) or (p.grid.number - 9 == grid.number):
                        return True
                else:
                    if (p.grid.number + 9 == grid.number) or (p.grid.number + 7 == grid.number):
                        return True

            elif isinstance(p, Knight) and p.color != color and p.grid.number != mv_number:
                for nm in number_list:
                    if grid.number == p.grid.number + nm :
                        return True

            elif isinstance(p, Rook) and p.color != color and p.grid.number != mv_number:
                if p.grid.rect.center[1] == grid.rect.center[1]:
                    for nm in range(min(grid.number, p.grid.number), max(grid.number, p.grid.number) + 1):
                        if nm in ls and nm != p.grid.number and nm != grid.number:
                            break
                    else:
                        return True

                elif p.grid.rect.center[0] == grid.rect.center[0]:
                    for nm in range(min(grid.number, p.grid.number + 8),max(grid.number, p.grid.number) + 1, 8):
                        if nm in ls and nm != p.grid.number and nm != grid.number:
                            break
                    else:
                        return True

            elif isinstance(p, Bishop) and p.color != color and p.grid.number != mv_number:
                if abs(grid.number - p.grid.number) % 7 == 0 and p.grid.rect.center[1] != grid.rect.center[1]:
                    for nm in range(min(grid.number, p.grid.number), max(grid.number, p.grid.number)+1,7):
                        if nm in ls and nm != grid.number and nm!= p.grid.number:
                            break
                    else:
                        return True

                elif abs(p.grid.number - grid.number) % 9 == 0 and p.grid.rect.center[1] != grid.rect.center[1]:
                    for nm in range(min(p.grid.number, grid.number),max(p.grid.number, grid.number)+1 , 9):
                        if nm in ls and nm != grid.number and nm != p.grid.number:
                            break
                    else:
                        return True


            elif isinstance(p, Queen) and p.color != color and p.grid.number != mv_number:
                if abs(grid.number - p.grid.number) % 7 == 0 and p.grid.rect.center[1] != grid.rect.center[1]:
                    for nm in range(min(p.grid.number, grid.number), max(p.grid.number, grid.number) + 1,7):
                        if nm in ls and nm !=  grid.number and nm != p.grid.number:
                            break
                    else:
                        return True

                elif abs(p.grid.number - grid.number) % 9 == 0 and p.grid.rect.center[1] != grid.rect.center[1]:
                    for nm in range(min(p.grid.number, grid.number),max(grid.number, p.grid.number) + 1, 9):
                        if nm in ls and nm != grid.number and nm != p.grid.number:
                            break
                    else:
                        return True

                elif p.grid.rect.center[1] == grid.rect.center[1]:
                    for nm in range(min(p.grid.number, grid.number),max(p.grid.number, grid.number) + 1):
                        if nm in ls and nm != grid.number and nm != p.grid.number:
                            break
                    else:
                        return True

                elif p.grid.rect.center[0] == grid.rect.center[0]:
                    for nm in range(min(p.grid.number, grid.number),max(p.grid.number, grid.number) + 1, 8):
                        if nm in ls and nm != grid.number and nm != p.grid.number:
                            break
                    else:
                        return True
            elif isinstance(p, King) and p.color != color and p.grid.number != mv_number:
                for nm in numbers:
                    if (pow(grid.rect.center[0] - p.grid.rect.center[0], 2) + pow(grid.rect.center[1] - p.grid.rect.center[1], 2)) == nm:
                        return True

    else:
        return False

#Creates the grids of the board
def setup_Grids(group):
    number = 0
    for y in range(0,8):
        for x in range(0,8):
            grid = Grid(40 + 80 * x, 40 + 80 * y, y + x, number)
            group.add(grid)
            number += 1
    return group

chess_grids = setup_Grids(py.sprite.Group())

#Setup pawns on the screen
def setup_Pieces(black_piece_group,white_piece_group,piece):

    if piece == Pawn:
        for o in range(0, 8):
            black_piece_group.add(piece("b",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 8 + o ), None)))

        for l in range(0, 8):
            white_piece_group.add(piece("w",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 48 + l ), None)))



    elif piece == Knight:
        for f in range(0,2):

            black_piece_group.add(piece("b", grid=next((elem for elem in chess_grids.sprites() if elem.number == 1 + 5 * f), None)))

        for e in range(0, 2):

            white_piece_group.add( piece("w", grid=next((elem for elem in chess_grids.sprites() if elem.number == 57 + 5 * e), None)))


    elif piece == Bishop:
        for d in range(0,2):
            black_piece_group.add(piece("b",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 2 + 3 * d), None)))


        for c in range(0, 2):
            white_piece_group.add(piece("w",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 58 + 3 * c), None)))

    elif piece == Rook:
        for b in range(0, 2):
            black_piece_group.add(piece("b",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 0 + 7 * b), None)))

        for a in range(0, 2):
            white_piece_group.add(piece("w",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 56 + 7 * a), None)))


    elif piece == Queen:
        black_piece_group.add(piece("b",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 3), None)))
        white_piece_group.add(piece("w",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 59), None)))

    else:
        black_piece_group.add(piece("b",next((elem for elem in chess_grids.sprites() if elem.number == 4), None)))
        white_piece_group.add(piece("w",grid =  next((elem for elem in chess_grids.sprites() if elem.number == 60), None)))

    return black_piece_group,white_piece_group



#Pawns group
black_pawns,white_pawns = setup_Pieces(py.sprite.Group(),py.sprite.Group(),Pawn)

#Knights group
black_knights, white_knights = setup_Pieces(py.sprite.Group(),py.sprite.Group(),Knight)

#Bishops group
black_bishops, white_bishops = setup_Pieces(py.sprite.Group(),py.sprite.Group(),Bishop)

#Rooks group
black_rooks , white_rooks = setup_Pieces(py.sprite.Group(),py.sprite.Group(),Rook)

#Queens group
black_queen , white_queen = setup_Pieces(py.sprite.Group(),py.sprite.Group(),Queen)

#Kings group

black_king , white_king = setup_Pieces(py.sprite.Group(),py.sprite.Group(),King)

List_of_Pieces = [black_pawns , white_pawns , black_knights, white_knights , black_bishops, white_bishops , black_rooks , white_rooks ,black_queen , white_queen , black_king , white_king]

Kings = [black_king,white_king]
#All pieces


#Game screen
chess_grids.draw(background)

list_of_numbers = []

for x in List_of_Pieces:
    x.draw(background)

T=0
while True:
    for x in List_of_Pieces:
        for y in x.sprites():
            list_of_numbers.append(y.grid.number)

    for kings in Kings:
        for king in kings.sprites():
            if check(king.grid,king.color,list_of_numbers,king.grid.number):
                if not checkmate(list_of_numbers,king.color):
                    myfont = py.font.SysFont(None, 30)
                    textsurface = myfont.render('Checkmate', False, (0, 0, 0))
                    background.blit(textsurface, (720, 250))
                else:
                    myfont = py.font.SysFont(None, 30)
                    textsurface = myfont.render('Check', False, (0, 0, 0))
                    background.blit(textsurface, (720, 250))



    if T % 2 != 0:
        myfont = py.font.SysFont(None, 20)
        textsurface = myfont.render('Waiting white to move', False, (255, 255, 255))
        background.blit(textsurface, (680, 560))
        myfont = py.font.SysFont(None, 20)
        textsurface = myfont.render('Waiting black to move', False, (0, 0, 0))
        background.blit(textsurface, (680, 100))
    else:
        myfont = py.font.SysFont(None, 20)
        textsurface = myfont.render('Waiting black to move', False, (255, 255, 255))
        background.blit(textsurface, (680, 100))
        myfont = py.font.SysFont(None, 20)
        textsurface = myfont.render('Waiting white to move', False, (0, 0, 0))
        background.blit(textsurface, (680, 560))

    for t in py.event.get():
        if t.type == py.QUIT:
            py.quit()
            sys.exit(0)
        elif t.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            for pieces in List_of_Pieces:
                for p in pieces.sprites():
                    if p.rect.collidepoint(pos):
                        if (T % 2 ==0 and p.color == "w") or (T % 2 != 0 and p.color == "b"):
                            try:
                                if isinstance(p,Pawn):
                                    T = Pawn_Move(p,list_of_numbers,T)

                                elif isinstance(p,Knight):
                                    T = Knight_move(p,list_of_numbers,T)

                                elif isinstance(p,Rook):
                                    T = Rook_move(p,list_of_numbers,T)


                                elif isinstance(p,Bishop):
                                    T = Bishop_move(p,list_of_numbers,T)


                                elif isinstance(p,Queen):
                                    T = Queen_move(p,list_of_numbers,T)


                                elif isinstance(p,King):
                                    T = King_move(p,list_of_numbers,T)

                                myfont = py.font.SysFont(None, 30)
                                textsurface = myfont.render('Check', False, (255,255,255))
                                background.blit(textsurface, (720, 250))
                            except:
                                pass

    list_of_numbers = []

    py.display.flip()


