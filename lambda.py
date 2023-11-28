# Resource: https://www.w3schools.com/python/python_lambda.asp
# Advanced Lambda Resource: https://realpython.com/python-lambda/

def odd_test(num):
  if num % 2 == 1:
    return True
  else:
    return False

print("Test 1:",odd_test(4))
print("Test 1:",odd_test(3))

lam_odd_test = lambda num: num % 2 == 1
print("Test 3:",lam_odd_test(4))
print("Test 3:",lam_odd_test(3))