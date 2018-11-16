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
def test_get_all_tiles():
	A=Board(2,2)
	A.change_tile(1,1,"Salut")
	A.change_tile(0,0,"Bonjour")
	A.change_tile(1,0,"Hi")
	A.change_tile(0,1,"Guten Tag")
	L=['Bonjour','Guten Tag','Hi','Salut']
	assert A.get_all_tiles()==L

def test_grid_to_string_with_size():
	A=Board(2,2)
	A.change_tile(1,1,"Salut")
	A.change_tile(0,0,"Bonjour")
	A.change_tile(1,0,"Hi")
	A.change_tile(0,1,"Guten")

	txt=""" ======== ========
|Bonjour |Guten   |
 ======== ========
|Hi      |Salut   |
 ======== ======== """
	assert A.grid_to_string_with_size()==txt
