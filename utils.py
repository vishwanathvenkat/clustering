import string
import random

def generate_color_codes(num_clusters):
  """
  Generates a list of random color code strings in various formats (hex, rgb)

  Args:
      num_clusters: The number of random color codes to generate.

  Returns:
      A list of random color code strings.
  """
  color_codes = []
  for _ in range(num_clusters):
    # Random choice between using hex or rgb format

      # Generate random RGB values (between 0 and 1)
      color_code = (random.random(), random.random(), random.random())
      color_codes.append(color_code)
  return color_codes