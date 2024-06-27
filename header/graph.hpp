#include <iostream>
#include <vector>

using namespace std;

class Node
{
public:
    int data;
    Node(int data);
};


class Graph
{
public:
    Graph(int V);
    vector<Node *> nodes;
    vector<vector<int>> edges;
    template <int... to>
    void addEdge(int from)
    {
        (this->edges[from].push_back(to), ...);
    }
    void firing(int node);
    void borrowing(int node);
    
    void setNodeData(int node, int data);
    void printGraph();
    int nodenum;
};



bool is_effecitve(Graph g);