'''
Graph.py

Initializing the graph structure to define the order in which agents execute and how agents 
communicate with one another.

Author: Jackson Grove 1/15/2025
'''
from agent import *
from utils.start_end import START, END

class Graph:
    '''
    Graph structure to define the order in which agents execute and how agents communicate with one another.
    '''
    def __init__(self) -> None:
        # Initalizing hash map for edges
        self.edges = {
            START: [], 
            END: []
        }
        self.nodes = self.edges.keys()
    
    def add_node(self, agent: Agent) -> None:
        '''
        Adds a node to the graph. This will not be connected until an edge is added.

        Args:
            :agent (Agent): The Agent object to be added as a node.
        '''
        self.edges[agent] = []
    
    def add_edge(self, node1: Agent, node2: Agent) -> None:
        '''
        Adds an edge from node1 to node2, routing the output of node1 to the input of node2

        Args:
            :node1 (Agent): The node to route from, sending the output to node2's input
            :node2 (Agent): The node to route to, receiving the output of node1 as input
        '''
        self.edges[node1].append(node2)

    def invoke(self, user_prompt: str = "", show_thinking: bool = False) -> str:
        # Output the user prompt if there are no agents defined
        if len(self.nodes) == 2: # (When only START and END nodes are defined)
            return prompt
        
        # Execute each node in the graph until END is reached
        curr_node = self.edges[START][0]
        prompt = user_prompt
        author = 'user'
        while curr_node != END:
            output = curr_node.invoke(author, prompt, show_thinking)
            curr_node = self.edges[curr_node][0] # TODO: add handling for routing/choosing between nodes in the case of multiple edges
            # Return the final output once END is reached
            if curr_node == END:
                return output
            # Otherwise, continue executing through the graph
            prompt = output
            author = 'user'