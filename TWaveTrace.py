from MainController import RobotController
from Mapping import MapBuilder

rc = RobotController()
mb = MapBuilder()
rd = 0


def choose_next_direction():
    global rd, rc, mb

    print("Next dir: ")
    try:
        rd = int(input())
    except ValueError:
        print("Try again")
        rd = int(input())

    return
    '''
    around_cells_discovering_state = mb.get_last_around_cells_states()

    update_sensors_values()
    update_map_builder()

    print("semen cells: " + str(around_cells_discovering_state))
    print("robot cells: " + str([rc.is_wall_front(), rc.is_wall_left(), rc.is_wall_back(), rc.is_wall_right()]))

    if (not rc.is_wall_front() and around_cells_discovering_state[0]) and \
            (not rc.is_wall_left() and around_cells_discovering_state[1]) and \
            (not rc.is_wall_back() and around_cells_discovering_state[2]) and \
            (not rc.is_wall_right() and around_cells_discovering_state[3]):
        rd = mb.get_direction_of_inverse_wave_trace()
    elif not rc.is_wall_front() and around_cells_discovering_state[0]:
        rd = 0
    elif not rc.is_wall_left() and around_cells_discovering_state[1]:
        rd = 1
    elif not rc.is_wall_back() and around_cells_discovering_state[2]:
        rd = 2
    elif not rc.is_wall_right() and around_cells_discovering_state[3]:
        rd = 3
    else:
        print("WHAT THE FUCK???")
        exit()
    '''


def update_sensors_values():
    for _ in range(10):
        for func in [rc.is_wall_front, rc.is_wall_left, rc.is_wall_back, rc.is_wall_right]:
            func()


def update_map_builder():
    global rd, mb, rc
    cells_amount = rc.get_cells_driven_since_last_time_amount()
    print(cells_amount)
    mb.update(rd, cells_amount, rc.get_walls_availability_array())


# the first map init
# update_sensors_values()
# mb.update(5, 0, [rc.is_wall_front(), rc.is_wall_left(), rc.is_wall_back(), rc.is_wall_right()])

# while not mb.is_map_built():
while True:
    rc.while_state_move_left()
    print("f")
    exit()
    update_sensors_values()
    print("Dir: " + str(rd))
    rc.do_any_align()
    print("Any align is done")
    if rd == 0:
        rc.while_state_move_straight()
        choose_next_direction()
    elif rd == 1:
        rc.while_state_move_left()
        choose_next_direction()
    elif rd == 2:
        rc.while_state_move_back()
        choose_next_direction()
    elif rd == 3:
        print(rc.while_state_move_right())
        choose_next_direction()

print("YEAH")
exit()
