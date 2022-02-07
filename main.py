
def floyd(n, b, a, w):
    d = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    print(f'minimom path is {d[b][a]}')
    # print(d[b][a])


def get_all_floors():
    for i in range(len(dest_elevator_list)):
        for j in range(len(dest_elevator_list[i])):
            if all_floors.__contains__(dest_elevator_list[i][j]):
                continue
            else:
                all_floors.append(dest_elevator_list[i][j])


def get_pair_char():
    for i in range(len(dest_elevator_list)):
        max_each_item = int(len(dest_elevator_list[i]))-2

        for j in range(int(len(dest_elevator_list[i]))):
            if j <= max_each_item:
                char = dest_elevator_list[i][j:j+2:1]
            else:
                char = dest_elevator_list[i][j]+dest_elevator_list[i][0]
            pair_char_list.append(char)
15743
2635

def create_adjacency_matrix():
    for i in range(0, len(all_floors)):
        all_floors[i] = int(all_floors[i])
    for i in range(max(all_floors)+1):
        adjacency_matrix.append(
            [max_value for item in range(max(all_floors)+1)])


def set_connect_index_matrix():
    for i in range(len(pair_char_list)):
        row_matrix = int(pair_char_list[i][0])
        column_matrix = int(pair_char_list[i][1])
        adjacency_matrix[row_matrix][column_matrix] = 1


pair_char_list = []
max_value = 3000  # 3000 it means infinity
all_floors = []
dest_elevator_list = []
adjacency_matrix = []
count_elevator = int(input('count_elevator: '))
start_floor = int(input('start_floor: '))
end_floor = int(input('end_floor: '))
# count_elevator, start_floor, end_floor = map(int, input().split())
dest_elevator = input('dest_elevator: ')
while(dest_elevator != '000'):
    dest_elevator_list.append(dest_elevator[1:])
    dest_elevator = input('dest_elevator: ')
    # dest_elevator = input()
get_all_floors()
create_adjacency_matrix()
get_pair_char()
for i in range(len(adjacency_matrix)):
    adjacency_matrix[i][i] = 0
set_connect_index_matrix()
floyd(len(all_floors), start_floor, end_floor, adjacency_matrix)
