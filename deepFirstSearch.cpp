#include<iostream>
#include<vector>
#include<utility>
#include<fstream>
#include<chrono>
#include<thread>

using namespace std;
using namespace chrono;

//Executa a busca DFS
long long int dfs( vector<vector<pair<int,int> > > &grafo, vector<int> &visitado, ofstream &writeFile, int atual = 0) {

//Marca o vertice atual como visitado
visitado[atual] = 1;

//Recebe o peso de todas as arestas
long long int answer = 0;

//Percorre todas as conexões do vertice atual
for(auto i : grafo[atual]) {
//Se o vertice verificado nao tiver sido visitado ainda, answer recebe seu peso + o dfs do respectivo vertice
if(!visitado[i.first]) {
writeFile << "Vertice " << atual+1 << " visita vertice " << i.first+1 << endl;

//Teoricamente serve para pausar por 500ms a execução para pordemos acompanhar, mas meu compilador não reconhece -Joseph
//this_thread::sleep_for(milliseconds(500));

answer += i.second;
answer += dfs(grafo, visitado, writeFile, i.first);

writeFile << "Vertice " << i.first+1 << " retorna ao vertice " << atual+1 << endl;
}
}
//Informa que o vertice atual esta retornando ao anterior
writeFile << "Vertice " << atual+1 << " nao possui mais vertices para buscar" << endl;


return answer;
}

int main() {
    //Registra o tempo inicial
    //auto inicio = chrono::steady_clock::now();

    //Armazena vertices em uma matriz, cada linha é um vertice, cada coluna é composto por um par que informa vertice e peso respectivamente
    vector<vector<pair<int,int> > > grafo;
    vector<int> visitado; //
    ifstream readFile;
    ofstream writeFile;
    readFile.open("16vertices.txt");
    writeFile.open("16verticesPeso.txt");

    int vertices, arestas;
    readFile >> vertices >> arestas;

    grafo.resize(vertices);
    visitado.resize(vertices, 0);
    for(int i=0; i<arestas; i++) {
        int x,y,z;
        readFile >> x >> y >> z;
        grafo[x-1].push_back(make_pair(y-1,z));
        grafo[y-1].push_back(make_pair(x-1,z));
    }

    writeFile << dfs(grafo, visitado, writeFile) << endl;
    for(int i=0; i<vertices; i++) visitado[i] = 0; //Teste em Prompt
    cout << dfs(grafo, visitado, writeFile) << "   " << endl;

    //Registra o tempo final
    //auto fim = chrono::steady_clock::now();

    //writeFile << chrono::duration <double, milli> (fim - inicio).count() << " ms" << endl;

    readFile.close();
    writeFile.close();

    return 0;
}