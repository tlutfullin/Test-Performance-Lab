import sys

def circular_array_path(n, m):
    if n <= 0 or m <= 0:
        raise ValueError("Both n and m must be positive integers.")

    circular_array = list(range(1, n + 1))
    path = []
    index = 0

    while True:
        path.append(circular_array[index])
        index = (index + m) % n
        if index == 0:
            break

    return "".join(map(str, path))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <n> <m>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])

        if n <= 0 or m <= 0:
            raise ValueError

        result = circular_array_path(n, m)
        print(result)

    except ValueError:
        print("Error: Both n and m must be positive integers.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)