from functools import reduce

def main():
  multiply = lambda x, y: x * y

  # with open('example.txt', 'r') as file:
  with open('input.txt', 'r') as file:
    total = 0
    
    for line in file:  
      line = line.strip()
      game_desc, game_results = line.split(': ')
      game_number = game_desc.split(' ')[1]
      games = game_results.split('; ')
      max_seen = { 'red': 0, 'green': 0, 'blue': 0 }

      for game in games:
        cubes = game.split(', ')
        for cube in cubes:
          num, color = cube.split(' ')
          num = int(num)
          if int(num) > max_seen[color]:
            max_seen[color] = num
      
      max_values = max_seen.values()
      power = reduce(multiply, max_values)
      print(f"power is: {power}")
      total += power

    print(total)

if __name__ == "__main__":
  main()