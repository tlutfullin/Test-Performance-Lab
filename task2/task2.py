import math
import sys

def read_circle_data(file_path):
    try:
        with open(file_path, "r") as file:
            x, y = map(float, file.readline().strip().split())
            r = float(file.readline().strip())
        if r <= 0:
            raise ValueError("Radius must be a positive number.")
        return (x, y), r
    except ValueError as ve:
        print(f"Error reading circle data: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading circle data: {e}")
        sys.exit(1)

def read_points(file_path):
    points = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                points.append(tuple(map(float, line.strip().split())))
        return points
    except ValueError as ve:
        print(f"Error reading points data: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading points data: {e}")
        sys.exit(1)

def point_position(circle_center, radius, point):
    x_center, y_center = circle_center
    x, y = point
    distance = math.sqrt((x - x_center) * (x - x_center) + (y - y_center) * (y - y_center))

    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_data_file> <points_file>")
        sys.exit(1)

    circle_data_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_center, radius = read_circle_data(circle_data_file)
    points = read_points(points_file)

    for point in points:
        position = point_position(circle_center, radius, point)
        print(position)