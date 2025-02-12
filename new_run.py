a = 5
b = 2

def make_sum(a, b):
    result = a + b
    return result

def run():
    result = make_sum(a, b)
    print('Calculated the sum of two numbers')
    print(a, b)
    return result

if __name__ == "__main__":
    run()
    