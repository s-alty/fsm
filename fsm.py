import itertools
# TODO: could this be done with a generator instead of a class?
# What about a closure ?


class FSM:
    def __init__(self, alphabet, states, start_state, final_states, transition):
        self.alphabet = alphabet
        self.states = states
        self.start_state = start_state
        self.final_states = final_states
        self.transition = transition # a function from state, input to state
        self.current_state = self.start_state

    def reinit(self):
        self.current_state = self.start_state

    def send(self, symbol):
        # evaluates one symbol
        if symbol not in self.alphabet:
                raise ValueError('Received invalid input symbol: {}, Alphabet is {}'.format(symbol, self.alphabet))
        self.current_state = self.transition(self.current_state, symbol)
        return self.current_state

    def evaluate(self, inputs):
        ''' Run a series of inputs through the state machine, return whether or not the end state is one of the valid final states'''
        self.reinit()
        for symbol in inputs:
            self.send(symbol)
        return self.current_state in self.final_states

    def language(self):
        '''return infinite iterator of all accepted inputs'''
        def inputs_of_length_n(n):
            return itertools.product(self.alphabet, repeat=n)

        inputs_of_all_lengths = map(inputs_of_length_n, itertools.count())
        flattened = itertools.chain.from_iterable(inputs_of_all_lengths)
        return (inputs for inputs in flattened if self.evaluate(inputs))
