#Fizzbuzz function to return Fizz, Buzz and Fizzbuzz
def fizz_buzz(x):
	if (x%3) == 0:
		if (x%5) == 0:
			return "FizzBuzz"
		else:
			return "Fizz"
	elif (x%5) == 0:
		return "Buzz"
	else:
		return (x)
print(fizz_buzz(8))