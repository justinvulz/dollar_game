#include <iostream>
#include "../header/graph.hpp"


Node::Node(int data)
{
    this->data = data;
}


Graph::Graph(int V)
{
    for (int i = 0; i < V; i++)
    {
        Node *node = new Node(0);
        nodes.push_back(node);
    }
    for (int i =0 ; i < V; i++)
    {
        vector<int> edge;
        edges.push_back(edge);
    }

    this->nodenum = V;
}

void Graph::firing(int node)
{
    for (int i = 0; i < edges[node].size(); i++)
    {
        nodes[edges[node][i]]->data += 1;
    }
    nodes[node]->data -= edges[node].size();
}

void Graph::borrowing(int node)
{
    for (int i = 0; i < edges[node].size(); i++)
    {
        nodes[edges[node][i]]->data -= 1;
        nodes[node]->data += 1;
    }
}

void Graph::setNodeData(int node, int data)
{
    nodes[node]->data = data;
}

void Graph::printGraph()
{
    for (int i = 0; i < nodes.size(); i++)
    {
        cout << "Node " << i << " has data " << nodes[i]->data << " and is connected to: ";
        for (int j = 0; j < edges[i].size(); j++)
        {
            cout << edges[i][j] << " ";
        }
        cout << endl;
    }
}

bool is_effecitve(Graph g)
{
    for (int i = 0; i < g.nodenum; i++)
    {
        if (g.nodes[i]->data < 0)
        {
            return false;
        }
    }
    return true;
}