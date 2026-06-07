from collections import defaultdict
#cmove = countermove, in another direction

def get_new_state(lock, state, move, cmove, movement): 
    
    print(f"Movement: {movement}{lock}")
    new_state = state.copy()
    if movement == "L": 
        new_state[lock] += 1
        for i in move[lock]: 
            new_state[i] += 1
        for i in cmove[lock]: 
            new_state[i] -= 1
    else: 
        new_state[lock] -= 1
        for i in move[lock]: 
            new_state[i] -= 1
        for i in cmove[lock]: 
            new_state[i] += 1

    return new_state


def crack(
        state: list[int], 
        move: dict[int, list[int]], 
        cmove: dict[int, list[int]],
        history: dict[str, bool] = defaultdict(lambda: False),
        combination: list[str] = [],
        old_state: list[int] | None = None,
        depth: int = 0
        ): 
    
    if state == [0, 0, 0, 0, 0, 0]:
        # win 
        print(f"Found with combination: {combination}")
        return
    
    print(f"Current state: {state}\n")

    if any(state[i] > 3 or state[i] < -3 for i in range(6)):
        # prune branch 
        # print(f'pruning with state: {state}')
        return

    if history["-".join(map(str, state))]:
        # prune branch 
        # print(f'state already visited: {state}')
        return
    
    history["-".join(map(str, state))] = True

    # FOR TESTING 
    if depth > 3: 
        # print(f'depth exceeded with combination: {combination}')
        return 

    # later change to 5 options as well. 
    for lock in range(6):
        new_state_left = get_new_state(
            lock, 
            state, 
            move, 
            cmove, "L")


        crack(new_state_left, move, cmove, history, combination+['L'+str(lock)], state, depth + 1)

        new_state_right = get_new_state(
            lock, 
            state, 
            move, 
            cmove, "R")
        
        crack(new_state_right, move, cmove, history, combination+['R'+str(lock)], state, depth + 1)


if __name__ == "__main__":
    state = [0, 0, 1, 0, 3, 3]
    move = {
    
        0: [], #1
        1: [2], #2
        2: [], #3
        3: [], #4
        4: [], #5
        5: [0] #6
    }
    cmove = {
        0: [1, 4], #1
        1: [], #2
        2: [0], #3
        3: [0, 4], #4
        4: [3], #5
        5: [] #6
    }
    crack(state, move, cmove)