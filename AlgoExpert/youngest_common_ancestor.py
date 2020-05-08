class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    #find distance from descendantOne to root
	node = descendantOne
	distance1 = 0
	while node.ancestor:
		node = node.ancestor
		distance1 += 1
	#find distance from descendantTwo to root
	node = descendantTwo
	distance2 = 0
	while node.ancestor:
		node = node.ancestor
		distance2 += 1
	
	depth_difference = abs(distance1 - distance2)
	farther_node = descendantOne
	closer_node = descendantTwo
	if distance2 > distance1:
		farther_node, closer_node = closer_node, farther_node
	#move up longer branch until both branches are the same distance from the root
	for _ in range(depth_difference):
		farther_node = farther_node.ancestor
	#move up both branches until both sides meet
	while farther_node is not closer_node:
		farther_node = farther_node.ancestor
		closer_node = closer_node.ancestor
	
	return closer_node
	
		
	
	
