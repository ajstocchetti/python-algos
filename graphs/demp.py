from Graph import *

g = Graph()

g.add(1)
g.add(2)
g.add(3)
g.remove(4)

g.addV(1,2, 15)
g.addV(1,3, 21)
g.addV(2,3)
g.addV(3,2, 34)
g.addV(3,3, -1)

# g.express_yourself()

# g.dropV(1,2)
# g.express_yourself()
# g.remove(3)

g.inspect_node(3)

# g.express_yourself()
# g.get_incoming_edges(3)
