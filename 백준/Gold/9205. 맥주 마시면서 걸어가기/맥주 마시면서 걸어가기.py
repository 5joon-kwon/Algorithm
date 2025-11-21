from collections import deque

def bfs():
    # node queue for BFS
    q = deque()
    q.append(start_node)

    while q:
        # current node x, y
        x, y = q.popleft()

        # get distance between current node and dest node
        if abs(x - dest_node[0]) + abs(y - dest_node[1]) <= 1000:
            # distance <= 1000
            # friends will move happily
            print("happy")
            return

        # distance > 1000
        # if there is a convenience stores
        for i in range(conv_num):
            if not visited[i]:  # if not visited
                # new node will be the conv node
                nx, ny = conv_node[i]

                # chech the distance between curr node and conv node
                if abs(x - nx) + abs(y - ny) <= 1000:
                    # distance <= 1000 (happily move)
                    # append node queue
                    # and check visited (conv node)
                    q.append([nx, ny])
                    visited[i] = 1

    # after loop, we have to move sadly
    # there are no cases to move happily
    print("sad")
    return


## Main ##
T = int(input())
for _ in range(T):
    # number of convenience stores
    conv_num = int(input())

    # get start node
    start_node = [int(x) for x in input().split()]

    # get nodes of convenience stores
    conv_node = []
    for _ in range(conv_num):
        x,y = map(int, input().split())
        conv_node.append([x, y])

    # get destination node
    dest_node = [int(x) for x in input().split()]

    # check visited node
    visited = [0 for i in range(conv_num + 1)]

    bfs()