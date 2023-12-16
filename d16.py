with open('input/16/real.txt') as f:
    grid = [['@'] + list(line.strip()) + ['@'] for line in f]
grid.insert(0, [str('@') for _ in range(len(grid[0]))])
grid.append([str('@') for _ in range(len(grid[0]))])

def print_grid():
    for i, line in enumerate(grid):
        print(str(i).rjust(3), "".join(line))
    print()

def print_energised_map():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in energised:
                print('#', end='')
            else:
                print('.', end='')
        print()

'''
. empty space
/ mirror
\ mirror
| splitter
- splitter
'''

def beam_move(pos, ori) -> ((int, int), str):
    match ori:
        case 'l':
            new_pos = (pos[0], pos[1] - 1)
        case 'r':
            new_pos = (pos[0], pos[1] + 1)
        case 'u':
            new_pos = (pos[0] - 1, pos[1])
        case 'd':
            new_pos = (pos[0] + 1, pos[1])
    return (new_pos, ori)

def beam_action(pos, ori):
    sym = grid[pos[0]][pos[1]]
    match sym:
        case '/':
            match ori:
                case 'l':
                    beam_starts.insert(0, (((pos[0] + 1, pos[1]), 'd')))
                case 'r':
                    beam_starts.insert(0, (((pos[0] - 1, pos[1]), 'u')))
                case 'u':
                    beam_starts.insert(0, (((pos[0], pos[1] + 1), 'r')))
                case 'd':
                    beam_starts.insert(0, (((pos[0], pos[1] - 1), 'l')))
        case '\\':
            match ori:
                case 'l':
                    beam_starts.insert(0, (((pos[0] - 1, pos[1]), 'u')))
                case 'r':
                    beam_starts.insert(0, (((pos[0] + 1, pos[1]), 'd')))
                case 'u':
                    beam_starts.insert(0, (((pos[0], pos[1] - 1), 'l')))
                case 'd':
                    beam_starts.insert(0, (((pos[0], pos[1] + 1), 'r')))
        case '|':
            match ori:
                case 'l':
                    beam_starts.insert(0, (((pos[0] - 1, pos[1]), 'u')))
                    beam_starts.insert(0, (((pos[0] + 1, pos[1]), 'd')))
                case 'r':
                    beam_starts.insert(0, (((pos[0] - 1, pos[1]), 'u')))
                    beam_starts.insert(0, (((pos[0] + 1, pos[1]), 'd')))
                case 'u':
                    beam_starts.insert(0, (((pos[0] - 1, pos[1]), 'u')))
                case 'd':
                    beam_starts.insert(0, (((pos[0] + 1, pos[1]), 'd')))
        case '-':
            match ori:
                case 'l':
                    beam_starts.insert(0, (((pos[0], pos[1] - 1), 'l')))
                case 'r':
                    beam_starts.insert(0, (((pos[0], pos[1] + 1), 'r')))
                case 'u':
                    beam_starts.insert(0, (((pos[0], pos[1] - 1), 'l')))
                    beam_starts.insert(0, (((pos[0], pos[1] + 1), 'r')))
                case 'd':
                    beam_starts.insert(0, (((pos[0], pos[1] - 1), 'l')))
                    beam_starts.insert(0, (((pos[0], pos[1] + 1), 'r')))
        case '.':
            beam_starts.insert(0, (beam_move(pos, ori)))
        case _: # '@'
            return 0

all_energy_totals = set()
game_starts = []
for row_start in range(1, len(grid) - 1):
    game_starts.append(((row_start, 1), 'r'))
    game_starts.append(((row_start, len(grid[row_start]) - 2), 'l'))
for column_start in range(1, len(grid[row_start]) - 1):
    game_starts.append(((1, column_start), 'd'))
    game_starts.append(((len(grid) - 2, column_start), 'u'))

for start in game_starts:
    energised = set()
    beam_starts = [ start ]
    beam_history = set()

    while beam_starts: # is not empty
        #input()
        #print(len(energised))
        #print(f'beam starts: {beam_starts}')
        #print_grid()
        pos, ori = beam_starts.pop(0)
        if ((pos, ori)) in beam_history:
            continue
        else:
            beam_history.add((pos, ori))
        if beam_action(pos, ori) == 0:
            continue
        energised.add(pos)
        #pos, sym = beam_move(pos, ori)
    #print(beam_history)
    #print(len(beam_history))
    #print(energised)
    #print(f'energised: {len(energised)}')
    all_energy_totals.add(len(energised))

print(f'max energised: {max(all_energy_totals)}')
