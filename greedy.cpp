#include <iostream>
#include "header\graph.hpp"
#include <algorithm>
#include <vector>
#include <set>

using namespace std;




int main()
{
    // Graph g(7);

    // g.addEdge<1>(0);
    // g.addEdge<6,2,0>(1);
    // g.addEdge<1,6>(2);
    // g.addEdge<6,4>(3);
    // g.addEdge<3,5,6>(4);
    // g.addEdge<4>(5);
    // g.addEdge<1,2,3,4>(6);
    
    // g.setNodeData(0, 1);
    // g.setNodeData(1, 0);
    // g.setNodeData(2, -1);
    // g.setNodeData(3, 2);
    // g.setNodeData(4, -2);
    // g.setNodeData(5, 1);
    // g.setNodeData(6, 2);

    Graph g(7);
    g.addEdge<1,6>(0);
    g.addEdge<0,2,6>(1);
    g.addEdge<1,6,5>(2);
    g.addEdge<4>(3);
    g.addEdge<3,5,6>(4);
    g.addEdge<2,4>(5);
    g.addEdge<0,1,2,4>(6);
    g.setNodeData(0, 2);
    g.setNodeData(1, 0);
    g.setNodeData(2, -2);
    g.setNodeData(3, 2);
    g.setNodeData(4,1);
    g.setNodeData(5, -2);
    g.setNodeData(6, 2);


    set<int> M;
    int ans[g.nodenum];
    bool winnable = true;

    for (int i = 0; i < g.nodenum; i++)
    {
        ans[i] = 0;
    }

    while (!is_effecitve(g))
    {

        if (M.size() != g.nodenum)
        {
            int dv = -1;
            for (int i = 0; i < g.nodenum; i++)
            {
                if (g.nodes[i]->data < 0)
                {
                    dv = i;
                    break;
                }
            }
            g.borrowing(dv);
            for(int i = 0; i < g.nodenum; i++)
            {
                if(i ==dv)
                    continue;
                ans[i]++;
            }
            
            if (M.count(dv)==0)
            {
                M.insert(dv);
            }
        }
        else
        {
            winnable = false;
            break;
        }
    }

    if (winnable)
    {
        cout << "The solution is: ";
        int minvalue = *min_element(ans, ans + g.nodenum);
        for (int i = 0; i < g.nodenum; i++)
        {
            ans[i]-= minvalue;
        }
        for (int i = 0; i < g.nodenum; i++)
        {
            cout << ans[i] << " ";
        }
    }
    else
    {
        cout << "No solution" << endl;
    }

    return 0;
}