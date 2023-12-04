def main():
  total = 0
  total_cols = 0
  total_rows = 0
  layout = []
  found_nums = []
  found_symbols = []

  # num_coords = [[0, 0], [0, 2]]
  def valid(num_coords):
    # print(f"Checking {num_coords}")

    num_str = coords_to_str(num_coords)
    # print(f"checking {num_str}")
    # [0, 0]
    start_coords = num_coords[0]
    # [0, 2]
    end_coords = num_coords[1]
    # 0
    row_num = start_coords[0]
    # 0
    col_start = start_coords[1]
    # 2
    col_end = end_coords[1]


    is_valid = False
    check_start_row = row_num - 1 if row_num > 0 else row_num
    check_end_row = row_num + 1 if row_num < total_rows - 1 else row_num
    check_start_col = col_start - 1 if col_start > 0 else col_start
    check_end_col = col_end + 1 if col_end < total_cols - 1 else col_end
    # print(f"start at {check_start_row}, {check_start_col}, end at {check_end_row}, {check_end_col}")

    for row in list(range(check_start_row, check_end_row + 1)):
      for col in list(range(check_start_col, check_end_col + 1)):
        if is_valid == True:
          # print(f"returning valid true for {num_str}")
          return True
        # print(f"symbol checking {row}, {col}")
        if symbol(layout[row][col]):
          is_valid = True
          # print("valid")
    
    # print(f"returning valid: {is_valid} for {num_str}")
    return is_valid
    
  def coords_to_str(coords):
    row = coords[0][0]
    col_start = coords[0][1]
    col_end = coords[1][1]
    num_elements = layout[row][col_start:col_end + 1]
    num_str = ''.join(num_elements)
    return num_str 
    
  def symbol(char):
    if char != '.' and not char.isdigit():
      return True
    return False

  # with open('example.txt') as file:
  with open('input.txt') as file:
    for line in file:  
      line = line.strip()
      characters = list(line)
      layout.append(characters)
    total_cols = len(layout[0])
    total_rows = len(layout)
    
  for row_index, row in enumerate(layout):
    num_started = False
    num_start_position = 0
    for column_index, char in enumerate(row):
      if num_started == True and not char.isdigit():
        found_nums.append([[row_index, num_start_position], [row_index, column_index - 1]])
        num_started = False
      elif num_started == False and char.isdigit():
        num_start_position = column_index
        num_started = True
      if not symbol(char):
        found_symbols.append([row_index, column_index]) 
      if num_started == True and column_index == total_cols - 1:
        found_nums.append([[row_index, num_start_position], [row_index, column_index]])
    
  print(layout)
  print("\n")
  print(found_nums)
  print("\n")
  print(found_symbols)
  print("\n")

  for num in found_nums:
    # [[0, 2], [0, 4]]
    if valid(num):
      # print(f"valid num coords: {num}")
      num_str = coords_to_str(num)
      # print(f"valid {num_str}")
      total += int(num_str)
  
  print(total)

if __name__ == "__main__":
  main()