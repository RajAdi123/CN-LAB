#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int pkts = 5;
    vector<int> packets = {2, 4, 1, 5, 4};
    int b_cap = 4;
    int rof = 3;
    vector<int> accept(pkts);
    vector<int> sent(pkts);
    vector<int> remaining(pkts);
    int b_rem = 0;

    for (int i = 0; i < pkts; i++)
    {
        if (b_rem + packets[i] <= b_cap)
        {
            accept[i] = packets[i];
            b_rem += packets[i];
        }
        else
        {
            accept[i] = -2;
        }

        if (b_rem != 0 && accept[i] != -2)
        {
            if (b_rem < rof)
            {
                sent[i] = b_rem;
                b_rem = 0;
            }
            else
            {
                sent[i] = rof;
                b_rem = b_rem - rof;
            }
        }
        else
        {
            sent[i] = 0;
        }

        remaining[i] = b_rem;
    }

    if (b_rem > 0)
    {
        while (b_rem > 0)
        {
            packets.push_back(-1);
            accept.push_back(b_rem);
            if (b_rem < rof)
            {
                sent.push_back(b_rem);
                b_rem = 0;
            }
            else
            {
                sent.push_back(rof);
                b_rem = b_rem - rof;
            }
            remaining.push_back(b_rem);
        }
    }

    cout << "--------------------------------------------------" << endl;
    cout << "Sl.No.    Pkt_Size    Accept    Sent    Reamaining" << endl;
    cout << "--------------------------------------------------" << endl;
    for (int i = 0; i < sent.size(); i++)
    {
        cout << (i + 1) << "\t\t" << packets[i] << "\t" << accept[i] << "\t" << sent[i] << "\t" << remaining[i] << endl;
    }
    return 0;
}

// -1 = in_bkt for Reference
// -2 = dropped for Reference