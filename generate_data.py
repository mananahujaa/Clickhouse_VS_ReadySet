import random

def generate_data(num_rows):
  """Generates a random dataset of num_rows rows."""
  data = []
  for i in range(num_rows):
    data.append([random.randint(1, 100), random.randint(1, 100)])
  return data

def export_data(data, filename):
  """Exports the data into a file."""
  with open(filename, "w") as f:
    f.write("x,y\n")
    for row in data:
      f.write("%d,%d\n" % (row[0], row[1]))

if __name__ == "__main__":
  data = generate_data(100_100_000)
  export_data(data, "data.csv")

