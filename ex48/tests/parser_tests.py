from nose.tools import *
from ex48.parser import *


def test_parse_sentence():
	assert_equal(parse_sentence([('noun', 'princess'), ('verb', 'go'), ('direction', 'north')]).subject, 'princess')
	assert_equal(parse_sentence([('noun', 'princess'), ('verb', 'go'), ('direction', 'north')]).verb, 'go')
	assert_equal(parse_sentence([('noun', 'princess'), ('verb', 'go'), ('direction', 'north')]).object, 'north')
	
def test_parse_sentence2():
	assert_equal(parse_sentence([('verb', 'go'), ('direction', 'north')]).subject, 'player')
	assert_equal(parse_sentence([('verb', 'go'), ('direction', 'north')]).verb, 'go')
	assert_equal(parse_sentence([('verb', 'go'), ('direction', 'north')]).object, 'north')
	
def test_parse_sentence3():
	assert_raises(ParserError, parse_sentence, [('direction', 'north'), ('verb', 'go'), ('noun', 'princess')])
	
