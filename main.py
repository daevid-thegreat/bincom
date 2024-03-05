import math
import random
import psycopg2

# Sample data structure holding color and frequency
colors_data = [
	{"index": 1, "color": "GREEN", "frequency": 11},
	{"index": 2, "color": "YELLOW", "frequency": 4},
	{"index": 3, "color": "BROWN", "frequency": 6},
	{"index": 4, "color": "BLUE", "frequency": 28},
	{"index": 5, "color": "RED", "frequency": 11},
	{"index": 6, "color": "BLACK", "frequency": 1},
	{"index": 7, "color": "WHITE", "frequency": 14},
	{"index": 8, "color": "ORANGE", "frequency": 7},
	{"index": 9, "color": "PINK", "frequency": 5},
	{"index": 10, "color": "ARSH", "frequency": 1},
	{"index": 11, "color": "CREAM", "frequency": 2},
]


# Function to calculate mean color
def calculate_mean_color(colors):
	total_frequency = sum(color["frequency"] for color in colors)

	# Check if total_frequency is zero to avoid division by zero
	if total_frequency == 0:
		return None

	mean_color_index = sum(color["index"] * color["frequency"] for color in colors) / total_frequency
	# Round up the mean_color_index to the nearest integer
	mean_color_index = math.ceil(mean_color_index)

	# Find the color corresponding to the mean color index
	for color in colors:
		if color["index"] == mean_color_index:
			return color["color"]

	return None


# Function to find the most frequent color
def most_frequent_color(colors):
	highest_frequency_color = max(colors, key=lambda x: x["frequency"])
	return highest_frequency_color["color"]


# Function to calculate median color
def calculate_median_color(colors):
	sorted_colors = sorted(colors, key=lambda x: x["frequency"])
	n = len(sorted_colors)
	if n % 2 == 0:
		median_frequency = (sorted_colors[n // 2 - 1]["frequency"] + sorted_colors[n // 2]["frequency"]) / 2
	else:
		median_frequency = sorted_colors[n // 2]["frequency"]

	# Find the color corresponding to the median frequency
	for color in sorted_colors:
		if color["frequency"] == median_frequency:
			return color["color"]


# Function to calculate variance of colors
def calculate_variance(colors):
	total_frequency = sum(color["frequency"] for color in colors)
	mean_frequency = total_frequency / len(colors)
	color_variance = sum((color["frequency"] - mean_frequency) ** 2 for color in colors) / len(colors)
	return color_variance


# Function to save colors and their frequencies to PostgreSQL database
def save_to_database(colors):
	# Connect to PostgreSQL
	conn = psycopg2.connect(database="db_name", user="db_user", password="db_password", host="db_host",
	                        port="db_port")
	cur = conn.cursor()

	# Create table if not exists
	cur.execute('''CREATE TABLE IF NOT EXISTS colors (
                        id SERIAL PRIMARY KEY,
                        color VARCHAR(50) NOT NULL,
                        frequency INT NOT NULL
                    )''')

	# Insert colors and their frequencies
	for color in colors:
		cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color["color"], color["frequency"]))
		print("Inserted color:", color["color"])

	conn.commit()
	conn.close()


# Recursive searching algorithm
def recursive_search(arg, targ, start=0):
	if start >= len(arg):
		return False
	elif arg[start] == targ:
		return True
	else:
		return recursive_search(arg, targ, start + 1)


# Generate random 4 digits number of 0s and 1s and convert to base 10
def generate_and_convert():
	binary_number = ''.join([str(random.randint(0, 1)) for _ in range(4)])
	decimal_number = int(binary_number, 2)
	return binary_number, decimal_number


# Sum of the first 50 Fibonacci sequence
def fibonacci_sum():
	fib = [0, 1]
	for i in range(2, 51):
		fib.append(fib[i - 1] + fib[i - 2])
	return sum(fib)


if __name__ == "__main__":
	if True:
		mean_color = calculate_mean_color(colors_data)
		print("Mean color:", mean_color)

		most_frequent = most_frequent_color(colors_data)
		print("Most frequently worn color:", most_frequent)

		median_color = calculate_median_color(colors_data)
		print("Median color:", median_color)

		variance = calculate_variance(colors_data)
		print("Variance of colors:", variance)

		probability_red = sum(color["frequency"] for color in colors_data if color["color"] == "red") / sum(
			color["frequency"] for color in colors_data)
		print("Probability of choosing red color:", probability_red)

		# Save colors and their frequencies to PostgreSQL database
		save_to_database(colors_data)

		# Example of recursive searching algorithm
		arr = [1, 2, 3, 4, 5]
		target = 3
		print("Is {} present in {}: {}".format(target, arr, recursive_search(arr, target)))

		# Generate and convert random number
		binary, decimal = generate_and_convert()
		print("Generated binary number:", binary)
		print("Converted to base 10:", decimal)

		# Sum of first 50 Fibonacci numbers
		print("Sum of the first 50 Fibonacci sequence:", fibonacci_sum())
