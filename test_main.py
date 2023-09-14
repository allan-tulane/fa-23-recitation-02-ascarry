from main import *

def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 56.0
  assert simple_work_calc(20, 3, 2) == 506.75
  assert simple_work_calc(30, 4, 2) == 1954.0
  assert simple_work_calc(30, 2, 2) == 182
  assert simple_work_calc(2, 2, 2) == 4.0
  assert simple_work_calc(40, 1, 2) == 79.75

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 31.0
  assert work_calc(20, 1, 2, lambda n: n*n) == 533.8125
  assert work_calc(30, 3, 2, lambda n: n) == 638.625
  assert work_calc(10, 2, 2,lambda n: n*n) == 203.5
  assert work_calc(40, 1, 2,lambda n: n+n) == 158.5
  assert work_calc(8, 2, 2,lambda n: 2) == 22
