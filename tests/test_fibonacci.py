
from functools import lru_cache

@lru_cache(maxsize=2000)
def fibonacci(n: int):
    return 1 if (n == 1 or n == 2) else fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(4) == 3
    assert fibonacci(6) == 8
    assert fibonacci(8) == 21
    assert fibonacci(10) == 55
    
    print("Test réussi ")
