# File: scripts/visualization/visualize_flows.py

import csv
import networkx as nx
import matplotlib.pyplot as plt
import argparse

def read_cex_traces(input_file):
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def visualize_flows(traces, output_file):
    G = nx.DiGraph()
    
    # Add nodes for each unique address
    for trace in traces:
        G.add_node(trace['Signature'], type='Transaction')
        G.add_node(trace['CEX Address'], type='CEX')

        # Add edge for each transaction to CEX
        G.add_edge(trace['Signature'], trace['CEX Address'], amount=trace['Amount'], token=trace['Token'])
    
    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, font_weight='bold')
    
    # Edge labels
    edge_labels = {(u, v): f"{d['amount']} {d['token']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Transaction Flows to CEXs")
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize transaction flows to CEXs.")
    parser.add_argument('--input', type=str, required=True, help='Input CSV file with CEX traces')
    parser.add_argument('--output', type=str, default='docs/transaction_flow.png', help='Output image file path')
    
    args = parser.parse_args()
    
    traces = read_cex_traces(args.input)
    visualize_flows(traces, args.output)
