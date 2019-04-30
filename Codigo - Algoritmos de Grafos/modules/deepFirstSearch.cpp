#include<iostream>
#include<vector>
#include<utility>
#include<fstream>
#include<chrono>
#include<thread>

using namespace std;
using namespace chrono;

int n_vertices_visitados = 1;

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
writeFile <<  atual+1 << "~>" << i.first+1 << "  |  ";
n_vertices_visitados+=1;
//Teoricamente serve para pausar por 500ms a execução para pordemos acompanhar, mas meu compilador não reconhece -Joseph
//this_thread::sleep_for(milliseconds(500));

answer += i.second;
answer += dfs(grafo, visitado, writeFile, i.first);

writeFile << i.first+1 << "<~" << atual+1 << "  |  "; //Informa que o vértice atual esta retornando ao anterior
}
}

writeFile << atual+1 << "~>X  |  "; // Não tem mais para onde o vértice atual ir.


return answer;
}

int main(int argc, char** argv) {

    //Armazena vertices em uma matriz, cada linha é um vertice, cada coluna é composto por um par que informa vertice e peso respectivamente
    vector<vector<pair<int,int> > > grafo;
    vector<int> visitado; //
    ifstream readFile;
    ofstream writeFile;
    string path = "modules/Grafos/";
    string file = argv[1];
    path.append(file);
    string out = "modules/Resultados/";
    out.append((file.substr(0, file.size()-4)).append("_out.txt"));
    readFile.open(path);
    writeFile.open(out);

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

    // Escrevendo no arquivo:
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    writeFile << "Arquivo: " << file << endl << endl;
    writeFile << "x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x" << endl << endl;
    writeFile << "Caminhamento pelo grafo:" << endl << endl;
    auto inicio = chrono::steady_clock::now(); //Registra o tempo inicial
    int custo_total = dfs(grafo,visitado,writeFile);
    auto fim = chrono::steady_clock::now(); //Registra o tempo final

    string conexo = "desconexo";
    if(n_vertices_visitados == vertices)
        conexo = "conexo";

    writeFile << endl << endl << "x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x" << endl << endl;
    writeFile << "Número de vértices: " << vertices << endl;
    writeFile << "Número de arestas: " << arestas << endl;
    writeFile << "Número de vértices visitados: " << n_vertices_visitados << endl;
    writeFile << "O grafo é " << conexo << "!" << endl;
    writeFile << "Custo total da árvore: " << custo_total << endl;    
    writeFile << "Tempo de execução: " << chrono::duration <double, milli> (fim - inicio).count() << " Milissegundos" << endl << endl;
    writeFile << "x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x ~~~~~~~~~~~~ x" << endl << endl;
    writeFile << "Resultados salvos em: " << out << endl;
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    readFile.close();
    writeFile.close();

    return 0;
}
