import numpy as np

from input_reader import MatrixParser

np.random.seed(69)
np.set_printoptions(formatter={'float': '{:.2f}'.format}, linewidth=np.inf, threshold=np.inf)


# matrixR = np.array([
# [100, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [100, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [100, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0],
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1]
# ])

class QAlgorithm:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.target = 0
        self.start = 0

        self.gamma = 0.8

        self.matrixQ = None
        self.matrixR = None


    def getAvailableActions(self, state):
        return [i for i in range(self.cols) if self.matrixR[state, i] >= 0]


    def getNextAction(self, state, availableActions):
        if len(set([self.matrixQ[state][action] for action in availableActions])) == 1:
            return np.random.choice(availableActions)
        else:
            return np.argmax(self.matrixQ[state])


    def updateQ(self, state, action):
        reward = self.matrixR[state, action]
        availableActions = self.getAvailableActions(action)
        maxQ = max([self.matrixQ[action, nextAction] for nextAction in availableActions])
        self.matrixQ[state, action] = reward + self.gamma * maxQ


    def train(self, iterations):
        limit = 10000
        for i in range(iterations):
            count = 0
            state = self.start
            path = [state]
            while state != self.target and count < limit:
                action = self.getNextAction(state, self.getAvailableActions(state))
                self.updateQ(state, action)
                state = action
                path.append(state)
                count += 1
        return path

    def update_matrix(self, matrix, states, original_cols):
        for state in states:
            row = state // original_cols
            col = state % original_cols
            matrix[row][col] = 4

        return matrix

    def get_output_matrix(self, input_matrix):
        m = MatrixParser()
        r_matrix = m.get_r_matrix(input_matrix)
        self.rows = m.x_size * m.y_size
        self.cols = m.x_size * m.y_size
        self.target = m.target
        self.start = m.start
        self.matrixQ = np.zeros((self.rows, self.cols))
        self.matrixR = np.array(r_matrix)

        path_list = self.train(1000)

        if len(path_list) > 2:
            path_list = path_list[1:-1]
        else:
            path_list = []

        return self.update_matrix(input_matrix, path_list, m.x_size)




