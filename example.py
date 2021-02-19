import itertools

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

# here you can see that the state machine represents all inputs that have an even number of 0s after the last 1
all_accepted_inputs = example.language()
first_100 = list(itertools.islice(all_accepted_inputs, 100))
for input in first_100:
    print(input)


# Sipser 1.13
def transitions(state, symbol):
    if symbol == '<reset>': return 'q0'

    return {
        ('q0', 0): 'q0',
        ('q0', 1): 'q1',
        ('q0', 2): 'q2',
        ('q1', 0): 'q1',
        ('q1', 1): 'q2',
        ('q1', 2): 'q0',
        ('q2', 0): 'q2',
        ('q2', 1): 'q0',
        ('q2', 2): 'q1'
    }[state, symbol]


example2 = FSM(
    alphabet={0, 1, 2, '<reset>'},
    states={'q0', 'q1', 'q2'},
    start_state='q0',
    final_states={'q0'},
    transition=transitions
)

# using the state machine for computation
def is_sum_divisible_by_3(*numbers):
    example2.send('<reset>')
    for n in numbers:
        example2.send(n)
    return example2.current_state == 'q0'

print(is_sum_divisible_by_3(1, 2, 1, 1, 0, 1))
print(is_sum_divisible_by_3(1, 2, 1, 1, 0, 2))
