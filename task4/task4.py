import statistics
import sys

def read_numbers_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = [int(line.strip()) for line in file]
        if not numbers:
            raise ValueError("The file is empty.")
        return numbers
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: Invalid number in file or file is empty - {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading file {file_path}: {e}")
        sys.exit(1)

def min_moves_to_equal_elements(nums):
    if not nums:
        return 0

    median = int(statistics.median(nums))
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    nums = read_numbers_from_file(input_file)

    result = min_moves_to_equal_elements(nums)
    print(result)
