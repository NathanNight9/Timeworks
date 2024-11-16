with open('5/input.txt', 'r') as file:
    content = file.read()
    numbers = [int(digit) for digit in content]

    while len(numbers) != 1:
        n_number = []
        n_number = [int(digit) for digit in str(sum(numbers))]
        numbers = n_number

with open('5/output.txt', 'w') as file:
        file.write(str(numbers[0]))

