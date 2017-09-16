#include <iostream>

using namespace std;

int arr[100];

int main(){

  int Test_Cases,i,j,Terms;
  cout << "Please enter the number of Test Cases: ";
  cin >> Test_Cases;

  for(i=0;i<Test_Cases;i++){
    cout << "Please enter the number of terms: ";
    cin >> Terms;

    for(j=0;j<Terms;j++){
      cout << "Please enter the terms: ";
      cin >> arr[j];
    }
  }

  int count = 1,front,end;
  front = 0;
  end = (sizeof(list)/sizeof(list[0]);
  while(end > 1){
    Temp = arr[0];
    for (i=1;i<Terms-1;i++){
      arr[i] = arr[i-1];
    }
    arr[Terms-1] = Temp;

    if ((sizeof(list)/sizeof(list[0]) < count){

    }
  }

  return 0;
}
