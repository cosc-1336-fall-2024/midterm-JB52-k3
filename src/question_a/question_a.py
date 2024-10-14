#write functions here, don't add input('') statements here!
def test_config():
    return True

def is_prime(num):
    prime = False
    testnums = range(1, (num + 1))
    count = 0
    for i in testnums:
        if num % i == 0:
            count += 1
    if count == 2:
        prime = True
    return prime
