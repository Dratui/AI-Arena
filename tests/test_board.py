from src.board import Board
import pytest

def test_change_tile():
	A=Board(4,4)
	A.change_tile(1,1,"Salut")
	assert A.grid==[[' ',' ',' ',' '],[' ','Salut',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]


def test_read_tile():
	A=Board(4,4)
	A.change_tile(1,1,"Salut")
	assert A.read_tile(1,1)=="Salut"

def test_transpose_grid_clockwise():
	A=Board(2,2)
	A.change_tile(1,1,"Bonjour")
	B=A.transpose_grid_clockwise()
	C=[[" "," "],["Bonjour"," "]]
	assert B==C

def test_transpose_grid_anticlockwise():
	A=Board(2,2)
	A.change_tile(1,1,"Bonjour")
	B=A.transpose_grid_anticlockwise()
	C=[[" ","Bonjour"],[" "," "]]
	assert B==C
