from timeit import default_timer as timer

amphipod_costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

convert = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 0: '.', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}


def is_part_2(_data):
    return len(_data) != 8


def print_board(hallway, data):
    if not is_part_2(data):
        print("#############",
              "#{}#".format("".join([convert[h] for h in hallway])),
              "###{}#{}#{}#{}###".format(*[convert[d] for d in data[:4]]),
              "  #{}#{}#{}#{}#  ".format(*[convert[d] for d in data[4:]]),
              "  #########  ", sep='\n')
    else:
        print("#############",
              "#{}#".format("".join([convert[h] for h in hallway])),
              "###{}#{}#{}#{}###".format(*[convert[d] for d in data[: 4]]),
              "  #{}#{}#{}#{}#  ".format(*[convert[d] for d in data[4: 8]]),
              "  #{}#{}#{}#{}#  ".format(*[convert[d] for d in data[8:12]]),
              "  #{}#{}#{}#{}#  ".format(*[convert[d] for d in data[12:16]]),
              "  #########  ", sep='\n')


def check_all_correct(data) -> bool:
    if not is_part_2(data):
        return data == (1, 2, 3, 4,
                        1, 2, 3, 4)
    else:
        return data == (1, 2, 3, 4,
                        1, 2, 3, 4,
                        1, 2, 3, 4,
                        1, 2, 3, 4)


def check_correct_rooms(data) -> tuple[bool, bool, bool, bool]:
    if not is_part_2(data):
        return (data[0::4] == (1, 1),
                data[1::4] == (2, 2),
                data[2::4] == (3, 3),
                data[3::4] == (4, 4))
    else:
        return (data[0::4] == (1, 1, 1, 1),
                data[1::4] == (2, 2, 2, 2),
                data[2::4] == (3, 3, 3, 3),
                data[3::4] == (4, 4, 4, 4))


def calc_steps(room_idx, hallway_idx):
    level, room_type = divmod(room_idx, 4)
    entrance = entrance_index[room_type]
    return (level + 1) + abs(hallway_idx - entrance)


def check_amphipod_in_room_can_move(data, room_number) -> bool:
    room_state: tuple[int] = data[room_number::4]
    expected_amphipod = room_number + 1

    if not is_part_2(data):
        return room_state not in {(expected_amphipod, expected_amphipod), (0, expected_amphipod), (0, 0)}
    else:
        return room_state not in {
            (expected_amphipod, expected_amphipod, expected_amphipod, expected_amphipod),
            (0, expected_amphipod, expected_amphipod, expected_amphipod),
            (0, 0, expected_amphipod, expected_amphipod),
            (0, 0, 0, expected_amphipod),
            (0, 0, 0, 0)
        }


def move(_data, _hallway, room_idx: int, hallway_idx: int):
    # TODO: Change to tuple concatenation
    new_rooms = list(_data)
    new_rooms[room_idx] = 0
    new_hallw = list(_hallway)
    new_hallw[hallway_idx] = _data[room_idx]

    # todo: Calculate number of tiles moved
    amphipod_type = _data[room_idx]
    cost = calc_steps(room_idx, hallway_idx) * amphipod_costs[convert[amphipod_type]]

    return tuple(new_rooms), tuple(new_hallw), cost


def is_room_vacant(_data, amphipod_type) -> bool:
    room_state = _data[(amphipod_type - 1)::4]
    if not is_part_2(_data):
        return room_state in {(0, 0), (0, amphipod_type)}
    else:
        return room_state in {
            (0, amphipod_type, amphipod_type, amphipod_type),
            (0, 0, amphipod_type, amphipod_type),
            (0, 0, 0, amphipod_type),
            (0, 0, 0, 0),
        }


entrance_index = (2, 4, 6, 8)


def is_reachable_from_hallway_to_room(data, hallways, hallway_idx) -> bool:
    reachable = False
    amphipod_type = hallways[hallway_idx]
    if is_room_vacant(data, amphipod_type):
        entrance_idx = entrance_index[amphipod_type - 1]
        if hallway_idx == entrance_idx:
            reachable = True
        elif hallway_idx < entrance_idx:
            reachable = set(hallways[hallway_idx + 1: entrance_idx + 1]) == {0}
        else:
            reachable = set(hallways[entrance_idx: hallway_idx]) == {0}

    return reachable


def open_hallway_spots(_hallway):
    result = list(map(lambda h: h == 0, _hallway))
    # result[2] = False
    # result[4] = False
    # result[6] = False
    # result[8] = False
    return result


def move_from_hallway_to_room(_data, _hallway, hallway_idx):
    assert is_reachable_from_hallway_to_room(_data, _hallway, hallway_idx)

    amphipod_type = _hallway[hallway_idx]
    assert amphipod_type != 0
    correct_room = amphipod_type - 1
    l_hallway = list(_hallway)
    l_hallway[hallway_idx] = 0
    l_data = list(_data)

    current_index = correct_room + 3 * 4 if is_part_2(_data) else correct_room + 4
    while _data[current_index] != 0:
        current_index -= 4

    l_data[current_index] = amphipod_type
    cost = calc_steps(current_index, hallway_idx) * amphipod_costs[convert[amphipod_type]]

    assert cost != 0
    return tuple(l_data), tuple(l_hallway), cost





def get_next_states(data, hallways, moves) -> list[tuple]:
    global goals, min_cost

    # if min_cost == 47665:
    #     return

    if (data, hallways) in state_energy_dict:
        if state_energy_dict[(data, hallways)] < moves:
            return

    state_energy_dict[(data, hallways)] = moves

    if moves >= min_cost:
        return

    if check_all_correct(data):
        goals += 1
        print("GOAL:", goals, " - moves:", moves)
        if moves < min_cost:
            min_cost = moves

        return

    # print_board(hallways, data)
    # print()

    # CHECK HALLWAY -> ROOM
    for h_i, h in enumerate(hallways):
        if h != 0:  # Check if an amphipod resides on the current tile
            if is_reachable_from_hallway_to_room(data, hallways, h_i):
                # print("HALLWAY -> ROOM")
                new_rooms, new_hallw, move_cost = move_from_hallway_to_room(data, hallways, h_i)
                assert len(new_rooms) != 0  # TODO: Does this ever occur?
                assert move_cost != 0
                get_next_states(new_rooms, new_hallw, move_cost + moves)

    # CHECK ROOM -> HALLWAY
    for room, correct in enumerate(check_correct_rooms(data)):
        if not correct and check_amphipod_in_room_can_move(data, room):
            moving_amphipod_idx = room
            while data[moving_amphipod_idx] == 0:
                moving_amphipod_idx += 4

            open_hallway = open_hallway_spots(hallways)

            for i in range(entrance_index[room], -1, -1):

                if i in entrance_index:
                    continue

                if not open_hallway[i]:
                    # print("HALLWAY BLOCKED")
                    break

                # print("ROOM -> HALLWAY L")
                new_rooms, new_hallw, move_cost = move(data, hallways, moving_amphipod_idx, i)
                # if len(new_rooms) == 0:
                #     # print("DEADLOCK")
                #     break

                get_next_states(new_rooms, new_hallw, move_cost + moves)

            for i in range(entrance_index[room], 11):

                if i in entrance_index:
                    continue

                if not open_hallway[i]:
                    # print("HALLWAY BLOCKED")
                    break

                # print("ROOM -> HALLWAY R")
                new_rooms, new_hallw, move_cost = move(data, hallways, moving_amphipod_idx, i)
                # assert len(new_rooms) != 0
                get_next_states(new_rooms, new_hallw, move_cost + moves)


if __name__ == '__main__':

    with open("input", "r") as f:
        c = f.read().replace('\n', '').replace('.', '').replace('#', '').replace(' ', '')
        c = [convert[_c] for _c in c]

    data_part_1 = (
        c[0], c[1], c[2], c[3],
        c[4], c[5], c[6], c[7],
    )

    data_part_2 = (
        c[0], c[1], c[2], c[3],
        4, 3, 2, 1,
        4, 2, 1, 3,
        c[4], c[5], c[6], c[7],
    )

    for part, data in enumerate([data_part_1, data_part_2]):
        goals = 0
        min_cost = float("inf")
        state_energy_dict = dict()
        start = timer()
        hallway = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        get_next_states(data, hallway, 0)
        end = timer()
        print(f"PART {part+1}: {min_cost}")
        print(f"Time elapsed: {end - start:0.3f} seconds\n")

        # PART 1: 17400 - 3 min
        # PART 2: 46120 - 6 min
