def is_at_any_snake(snakes_positions, next_position):
  return snakes_positions.get(next_position)

def is_at_any_ladder(ladder_positions, next_position):
  return ladder_positions.get(next_position)

def best_next_jump(current_position, snakes_positions, ladder_positions):
  next_position = 0
  jump_size = 0
  for i in range(1,7):
    ladder = is_at_any_ladder(ladder_positions, current_position+i)

    if ladder and ladder-(current_position+i)>jump_size:
      # if ladder - i > jump_size :
      jump_size = ladder - i
      next_position = ladder
    elif i + current_position <= 30 and not is_at_any_snake(snakes_positions, current_position+i):
       if i> jump_size:
         jump_size = i
         next_position = current_position+i;

  return next_position


def get_throw_count(ladder_positions, snakes_positions, current_position, steps):
  next_positions = best_next_jump(current_position, snakes_positions, ladder_positions)

  if next_positions ==30:
    steps += 1
    return steps
  else:
    return get_throw_count(ladder_positions, snakes_positions, next_positions, steps+1)
  return steps


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      count = int(input())
      ladder_or_snake = list(map(int, input().strip().split()))
      snakes_positions = {}
      ladder_positions = {}
      ladder_count = 0
      for i in range(count):
        x = ladder_or_snake[i*2]
        y = ladder_or_snake[(i*2)+1]
        if x > y:
          snakes_positions[x] = y
          continue
        else:
          ladder_positions[x] = y
          ladder_count += 1
      print(get_throw_count(ladder_positions, snakes_positions, 1, 0))
      # print(ladder_positions, snakes_positions, ladder_count)


