def nth_prime(n):
  num = 1
  if n == 1:
    return 2
  n -= 1
  while True:
    if n == 0:
      return num
    num += 2
    prime = True
    for i in range(3, round(num**0.5)+1):
      if num % i == 0:
        prime = False
        break
    if prime:
      n -= 1