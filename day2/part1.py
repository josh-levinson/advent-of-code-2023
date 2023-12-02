def main():
  MAX_BALLS = { 'red': 12, 'green': 13, 'blue': 14 }

  with open('input.txt', 'r') as file:
    total = 0
    
    for line in file:  
      line = line.strip()
      game_desc, game_results = line.split(': ')
      game_number = game_desc.split(' ')[1]
      games = game_results.split('; ')
      game_valid = True

      for game in games:
        if game_valid == False:
          break
        
        cubes = game.split(', ')
        for cube in cubes:
          num, color = cube.split(' ')
          if MAX_BALLS[color] < int(num):
            game_valid = False
      
      print(f"For game: {line}, game_valid is: {game_valid}")
      if game_valid:
        total += int(game_number)

    print(total)

if __name__ == "__main__":
  main()