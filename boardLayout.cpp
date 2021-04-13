/* Problem

{{0, 1, 0, 0, 0, 0},
{0, 1, 0, 0, 0, 0},
{0, 1, 0, 0, 0, 0},
{0, 1, 0, 0, 0, 0},
{0, 0, 0, 0, 1, 0}}

*/

#include <iostream>
#include <vector>
using std::vector;
using std::cout;


int main() {
  vector<vector<int>> board;
  for (int i = 0; i < 5; i++){
    vector<int> row;
    for (int x = 0; x < 6; x++){
      if (i != 4){
        if (x != 1){
          row.push_back(0);
        } else
          row.push_back(1);
      } else {
        if (x != 3){
          row.push_back(0);
        } else
          row.push_back(1);
      }
    }
    for (auto i: row)
    	cout << i << " ";
    cout << std::endl;
    board.push_back(row);
  }
  return 0;
}
