#!/usr/bin/python
from Warmup_1.sleep_in       import sleep_in
from Warmup_1.monkey_trouble import monkey_trouble
from Warmup_1.sum_double     import sum_double
from Warmup_1.diff21         import diff21
from Warmup_1.parrot_trouble import parrot_trouble
from Warmup_1.makes10        import makes10
from Warmup_1.near_hundred   import near_hundred
from Warmup_1.near_hundred   import near_hundred
from Warmup_1.pos_neg        import pos_neg
from Warmup_1.not_string     import not_string
from Warmup_1.missing_char   import missing_char
from Warmup_1.front_back     import front_back
from Warmup_1.front3         import front3

def print_challenge_name(challenge_name):
    challenge = challenge_name
    print("Code Challenge: %s: " %(challenge))

def test_sleep_in():
  print_challenge_name("Sleep In")

  weekday   = False
  vacation  = False
  print("Input : Weekend: %r   Vacation: %r" %(weekday, vacation))
  print("Output: %r" %(sleep_in(weekday, vacation)))
  print()

  weekday   = True
  vacation  = False
  print("Input : Weekend: %r   Vacation: %r" %(weekday, vacation))
  print("Output: %r" %(sleep_in(weekday, vacation)))
  print()

  weekday   = False
  vacation  = True
  print("Input : Weekend: %r   Vacation: %r" %(weekday, vacation))
  print("Output: %r" %(sleep_in(weekday, vacation)))
  print()

def test_monkey_trouble():
  challenge = "Monkey Trouble"

  print("Code Challenge: %s: " %(challenge))

  a_smile   = True
  b_smile   = True
  print("Input : Weekend: %r   Vacation: %r" %(a_smile, b_smile))
  print("Output: %r" %(monkey_trouble(a_smile, b_smile)))
  print()

  a_smile   = False
  b_smile   = False
  print("Input : Weekend: %r   Vacation: %r" %(a_smile, b_smile))
  print("Output: %r" %(monkey_trouble(a_smile, b_smile)))
  print()

  a_smile   = True
  b_smile   = False
  print("Input : Weekend: %r   Vacation: %r" %(a_smile, b_smile))
  print("Output: %r" %(monkey_trouble(a_smile, b_smile)))
  print()

def test_sum_double():
  print_challenge_name("Sum Double")

  a = 1
  b = 2
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %d" %(sum_double(a, b)))
  print()

  a = 3
  b = 2
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %d" %(sum_double(a, b)))
  print()

  a = 2
  b = 2
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %d" %(sum_double(a, b)))
  print()

def test_diff21():
  print_challenge_name("Difference 21")

  num = 19
  print("Input : %d" %(num))
  print("Output: %d" %(diff21(num)))
  print()

  num = 10
  print("Input : %d" %(num))
  print("Output: %d" %(diff21(num)))
  print()

  num = 21
  print("Input : %d" %(num))
  print("Output: %d" %(diff21(num)))
  print()

def test_parrot_trouble():
  print_challenge_name("Parrot Trouble")

  talking = True
  hour    = 6
  print("Input : Talking: %r   Hour: %d" %(talking, hour))
  print("Output: %r" %(parrot_trouble(talking, hour)))
  print()

  talking = True
  hour    = 7
  print("Input : Talking: %r   Hour: %d" %(talking, hour))
  print("Output: %r" %(parrot_trouble(talking, hour)))
  print()

  talking = False
  hour    = 6
  print("Input : Talking: %r   Hour: %d" %(talking, hour))
  print("Output: %r" %(parrot_trouble(talking, hour)))
  print()

def test_makes10():
  print_challenge_name("Makes 10")

  a = 9
  b = 10
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %r" %(makes10(a, b)))
  print()

  a = 9
  b = 9
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %r" %(makes10(a, b)))
  print()

  a = 1
  b = 9
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %r" %(makes10(a, b)))
  print()

def test_near_hundred():
  print_challenge_name("Near Hundred")

  num = 93
  print("Input : %d" %(num))
  print("Output: %r" %(near_hundred(num)))
  print()

  num = 90
  print("Input : %d" %(num))
  print("Output: %r" %(near_hundred(num)))
  print()

  num = 89
  print("Input : %d" %(num))
  print("Output: %r" %(near_hundred(num)))
  print()

def test_pos_neg():
  print_challenge_name("Pos Neg")

  a         = 1
  b         = -1
  negative  = False
  print("Input : First: %d   Second: %d  Negative: %r" %(a, b, negative))
  print("Output: %r" %(pos_neg(a, b, negative)))
  print()

  a         = -1
  b         = 1
  negative  = False
  print("Input : First: %d   Second: %d  Negative: %r" %(a, b, negative))
  print("Output: %r" %(pos_neg(a, b, negative)))
  print()

  a         = -4
  b         = -5
  negative  = True
  print("Input : First: %d   Second: %d  Negative: %r" %(a, b, negative))
  print("Output: %r" %(pos_neg(a, b, negative)))
  print()

def test_not_string():
  print_challenge_name("Not String")

  str = "candy"
  print("Input : %s" %(str))
  print("Output: %s" %(not_string(str)))
  print()

  str = "x"
  print("Input : %s" %(str))
  print("Output: %s" %(not_string(str)))
  print()

  str = "not bad"
  print("Input : %s" %(str))
  print("Output: %s" %(not_string(str)))
  print()

def test_missing_char():
  print_challenge_name("Missing Char")

  str   = "kitten"
  index = 1
  print("Input : String: %s   Index: %d" %(str,index))
  print("Output: %r" %(missing_char(str,index)))
  print()

  index = 0
  print("Input : String: %s   Index: %d" %(str,index))
  print("Output: %r" %(missing_char(str,index)))
  print()

  index = 4
  print("Input : String: %s   Index: %d" %(str,index))
  print("Output: %r" %(missing_char(str,index)))
  print()

def test_front_back():
  print_challenge_name("Front Back")

  str   = "code"
  print("Input : String: %s" %(str))
  print("Output: %r" %(front_back(str)))
  print()

  str   = "a"
  print("Input : String: %s" %(str))
  print("Output: %r" %(front_back(str)))
  print()

  str   = "ab"
  print("Input : String: %s" %(str))
  print("Output: %r" %(front_back(str)))
  print()

def test_front3():
  print_challenge_name("Front 3")

  str   = "Java"
  print("Input : String: %s" %(str))
  print("Output: %r" %(front3(str)))
  print()

  str   = "Chocolate"
  print("Input : String: %s" %(str))
  print("Output: %r" %(front3(str)))
  print()

  str   = "abc"
  print("Input : String: %s" %(str))
  print("Output: %r" %(front3(str)))
  print()
