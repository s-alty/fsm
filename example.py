from fsm import FSM


# Sipser 1.6
def transitions(state, symbol):
    # could alternatively use new case syntax
    # or a bunch of if statements
    return {
        ('q1', 0): 'q1',
        ('q1', 1): 'q2',
        ('q2', 0): 'q3',
        ('q2', 1): 'q2',
        ('q3', 0): 'q2',
        ('q3', 1): 'q2'
        }[(state, symbol)]

example = FSM(
    alphabet={0, 1},
    states={'q1', 'q2', 'q3'},
    start_state='q1',
    final_states={'q2'},
    transition=transitions
)

print(example.evaluate([1, 1, 0, 1]))
print(example.evaluate([1, 1, 0, 0, 0, 0]))
print(example.evaluate([1, 0, 1, 0, 0, 0]))
