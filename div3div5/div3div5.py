import logging

def div3or5 (i:int) -> bool:
    return i%3==0 or i%5==0

def test_filter():

    assert div3or5(3)
    assert div3or5(5)
    assert div3or5(15)
    assert div3or5(30)

    assert not div3or5(1)
    assert not div3or5(4)
    assert not div3or5(13)
    assert not div3or5(101)

def filter_and_sum(n:int,f:callable):
    return sum([i for i in range(n) if f(i)])

def test_sum_of_integers():
    # Sum of n integers is n*(n+1)/2
    for n in [0,1,5,10]:
        logging.debug(f'n={n} n*(n+1)/2={n*(n+1)//2}')
        assert filter_and_sum(n+1,lambda i: True) == n*(n+1)//2

# https://projecteuler.net/problem=1&lang=en
def test_sum_below_10():
    assert filter_and_sum(10,div3or5)==23

def test_sum_below_1000():
    logging.info(f'RESULT = {filter_and_sum(10000,div3or5)}')
