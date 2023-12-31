def generate_fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

def main():
    try:
        # Get the number of terms from the user
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

        # Check if the input is a non-negative integer
        if num_terms < 0:
            print("Please enter a non-negative integer.")
        else:
            # Generate and display the Fibonacci sequence
            fibonacci_sequence = generate_fibonacci_sequence(num_terms)
            print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_sequence}")
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
main()
