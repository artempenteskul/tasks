# task number - 841



# def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
#     keys = {0}
#     unvisited = set()
#
#     def visit_room(cur_room: int):
#         if cur_room in unvisited:
#             unvisited.remove(keys)
#
#         cur_room_keys = rooms[cur_room]
#         keys.update(cur_room_keys)
#         for cur_room_key in cur_room_keys:
#             if cur_room_key in unvisited:
#                 visit_room(cur_room_key)
#
#     for room, room_keys in enumerate(rooms):
#         if room not in keys:
#             unvisited.add(room)
#         else:
#             visit_room(room)
#
#     return True if not unvisited else False
#


def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    keys = {0}
    unvisited = set()

    def visit_room(cur_room: int):
        cur_room_keys = rooms[cur_room]
        keys.update(cur_room_keys)
        for cur_room_key in cur_room_keys:
            if cur_room_key in unvisited:
                unvisited.remove(cur_room_key)
                visit_room(cur_room_key)

    for room, room_keys in enumerate(rooms):
        if room not in keys:
            unvisited.add(room)
        else:
            visit_room(cur_room=room)

    return True if not unvisited else False


if __name__ == '__main__':
    input_rooms = [[1], [2], [3], []]
    print(f'Can visit all rooms with input: {can_visit_all_rooms(input_rooms)}')  # true

    input_rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(f'Can visit all rooms with input: {can_visit_all_rooms(input_rooms)}')  # false

    input_rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(f'Can visit all rooms with input: {can_visit_all_rooms(input_rooms)}')  # false

    input_rooms = [[6, 7, 8], [5, 4, 9], [], [8], [4], [], [1, 9, 2, 3], [7], [6, 5], [2, 3, 1]]
    print(f'Can visit all rooms with input: {can_visit_all_rooms(input_rooms)}')  # true
