import random
import string

def generate_random_code(max_length):
    # Define the possible characters for the code
    characters = string.ascii_letters + string.digits + string.punctuation + " \t\n"

    # Generate random code of random length
    code_length = random.randint(1, max_length)
    code = ''.join(random.choice(characters) for _ in range(code_length))

    return code

def save_code_to_file(code, file_path):
    with open(file_path, 'w') as file:
        file.write(code)

def fuzz(num_iterations, max_length, output_directory):
    for i in range(num_iterations):
        # Generate random Python code
        code = generate_random_code(max_length)

        # Save the code to a file
        file_path = f"{output_directory}/fuzzed_code_{i}.py"
        save_code_to_file(code, file_path)

        print(f"Generated fuzzed code: {file_path}")

# Example usage
num_iterations = 10
max_length = 100
output_directory = "fuzzed_code"

fuzz(num_iterations, max_length, output_directory)
