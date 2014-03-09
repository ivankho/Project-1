from nose.tools import *
from ex48.parser import *


def test_parse_sentence():
	assert_equal(parse_sentence([('noun', 'princess'), ('verb', 'go'), ('direction', 'north')].getSubject()), \
	('princess'))