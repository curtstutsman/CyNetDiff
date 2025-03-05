import networkx as nx
import matplotlib.pyplot as plt

# Define the edge list and corresponding influence values
edges = [(0, 3), (0, 6), (1, 8), (3, 9), (3, 2), (8, 3)]

influence = [0.5, 1.0, 1.0, 1.0, 1.0, 0.5]

G = nx.DiGraph()

# Add each edge with its corresponding influence value as an attribute
for (u, v), w in zip(edges, influence):
    G.add_edge(u, v, weight=w)

# Specify nodes that should be colored red
red_nodes = [0]  # Change this list to include your desired nodes

# Create a color map for nodes: red if in red_nodes, otherwise skyblue
node_colors = ["red" if node in red_nodes else "skyblue" for node in G.nodes()]

# Generate positions for the nodes using a force-directed layout.
pos = nx.spring_layout(G, seed=42, k=2)

# Create a very large figure
plt.figure(figsize=(24, 18))

# Draw nodes and their labels with the new color mapping
nx.draw_networkx_nodes(G, pos, node_size=500, node_color=node_colors)
nx.draw_networkx_labels(G, pos, font_weight='bold')

# Draw directed edges with a constant width (ignoring the influence for width)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, width=2, edge_color="gray")

# Retrieve and round the edge weights to 5 decimal places for display
edge_labels = nx.get_edge_attributes(G, 'weight')
edge_labels_rounded = {edge: round(weight, 5) for edge, weight in edge_labels.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_rounded, font_color='red', font_size=10)

# Set a title and display the plot
plt.title("Directed Network Visualization with Custom Colored Nodes", fontsize=20)
plt.axis('off')
plt.show()
