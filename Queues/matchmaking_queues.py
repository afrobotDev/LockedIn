from queue_class import Queue


def matchmake(queue, user):
    action = user[1]
    usr = user[0]
    if action == "leave":
        queue.search_and_remove(user[0])
        
    if action == "join":
        queue.push(usr)
        
    queue_size = queue.size()
    if queue_size >= 4:

        user1 = queue.pop()
        user2 = queue.pop()

    else:
        return "No match found"

    return f"{user1} matched {user2}!"
