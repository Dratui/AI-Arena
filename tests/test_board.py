from src.board import Board
import pytest

def test_change_tile():
	A=Board(4,4)
	A.change_tile(1,1,"Salut")
	assert A.grid==[[' ',' ',' ',' '],[' ','Salut',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]

