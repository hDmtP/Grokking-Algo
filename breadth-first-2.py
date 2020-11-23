from collections import deque

# BUilding a Graph

graph = {}
graph["me"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []

print(graph)


def person_is_seller(name):
    return name[-1] == "y"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue: 
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a seller")
                break
            else:
                search_queue += graph[person]
                searched.append(person)


search("me")