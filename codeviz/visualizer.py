# codeviz/visualizer.py

import matplotlib.pyplot as plt

def visualize_code(file_path):
try:
    # Extract module name from file path
        module_name = file_path.split("/")[-1].split(".")[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)


    source_code = inspect.getsource(module)

    tree = ast.parse(source_code)


    G = nx.DiGraph()
    cmap = cm.get_cmap('viridis')  # Select a colormap for nodes

    def traverse(node, parent=None):
      if parent:
        G.add_edge(parent.__class__.__name__, node.__class__.__name__)
      nodes.append(node.__class__.__name__)
      color = cmap(len(nodes) / len(tree.body))  
      G.add_node(node.__class__.__name__, color=color)  
      for child in ast.iter_child_nodes(node):
        traverse(child, node)

    nodes = []
    traverse(tree)
    return G
except (ImportError, FileNotFoundError) as e:
    print(f"Error: {e}")
    return None


file_path = "/Users/localadmin/Desktop/toCheck.py"
graph = visualize_code(file_path)

if graph:

  pos = nx.spring_layout(graph)


  import matplotlib.pyplot as plt
  plt.figure(figsize=(25, 15))
  nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color=[c[1] for c in graph.nodes(data='color')])
  plt.show()
else:
  print("Failed to process the file.")

# Your code visualization logic here
    # For demonstration, we'll just create a simple plot
    with open(file_path, 'r') as file:
        code = file.read()
    
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, code, fontsize=12, ha='center')
    ax.axis('off')
    
    return fig
