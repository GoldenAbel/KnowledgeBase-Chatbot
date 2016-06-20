#include<bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define LET(x,a) __typeof(a) x(a)
#define TR(v,it) for( LET(it,v.begin()) ; it != v.end(); it++)

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;

set<string> roles;
set<string> query;
vector<string> comments; 
set<string> qquery;

void normal(string &a)
{
    for(auto &x : a) if(x>='A' and x<='Z') x -= ('A' - 'a');
}
vector<double> SC;
vector<string> CM;
bool cmp(int a, int b)
{
    return SC[a] > SC[b];
}
int main(int argc, char** argv)
{
    ifstream nouns; nouns.open(argv[1]);
    ifstream replies; replies.open(argv[2]);
    ifstream characters; characters.open(argv[3]);
    ifstream qqueries; qqueries.open(argv[4]);

    string s; 
    while(qqueries>>s){ normal(s); qquery.insert(s);}
    while(nouns>>s){ normal(s); query.insert(s);}
    while(characters>>s)
    {
        normal(s);
        if(qquery.find(s) != query.end()) roles.insert(s);
    }
    double wn = 1; 
    double wr = 1;
    int i =0;
    VI RNK;
    while(getline(replies,s))
    {
        double score=0; 
        istringstream is(s); 
        string wrd;
        set<string> role_query;
        set<string> noun_query;
        while(is>>wrd)
        {
            normal(wrd);
            if(roles.find(wrd)!=roles.end())role_query.insert(wrd);
            if(query.find(wrd)!=query.end())noun_query.insert(wrd);
        }
        score = wn * noun_query.size() + wr * role_query.size();
        SC.PB(score);
        CM.PB(s);
        RNK.PB(i); i++;
    }
    sort(RNK.begin(), RNK.end(), cmp);
    for(auto x : RNK) cout<<CM[x]<<endl;
    return 0;	
}
