class Node:
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration
        self.ES = 0
        self.EF = 0
        self.LS = 0
        self.LF = 0
        if type(duration) == tuple:
            self.t_oper = (self.duration[0] + 4*self.duration[1] + self.duration[2]) / 6
            self.var = ((self.duration[2] - self.duration[0]) / 6) **2
        else:
            self.t_oper = duration
            self.var = 0
        self.d_incoming = []
        self.d_outgoing = []

    def __str__(self):
        return f"Node({self.id}: D={self.duration}, ES={self.ES}, EF={self.EF}, LS={self.LS}, LF={self.LF})"

    def create_graph(N, M, durations, dependencies):
        nodes = [Node(i, durations[i]) for i in range(N)]

        for a, b in dependencies:
            nodes[a].d_outgoing.append(nodes[b])
            nodes[b].d_incoming.append(nodes[a])

        return nodes