#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <vector>
#include <cmath>
using namespace std;

//fuction that gets string representing a binary number and returns the decimal value
int binaryToDecimal(string binary){
    int decimal = 0;
    int power = 0;
    for (int i = binary.length() - 1; i >= 0; i--){
        if (binary[i] == '1'){
            decimal += pow(2, power);
        }
        power++;
    }
    return decimal;
}

string reverseBinary(string binary){
    string reversed;
    for (int i = 0; i < binary.length(); i++){
        if (binary[i] == '0'){
            reversed.append("1");
        }
        else{
            reversed.append("0");
        }
    }
    return reversed;
}


int main(){
    fstream inFile;
    inFile.open("input3.txt",ios::in);
    if (inFile.is_open()){   
        cout << "File opened successfully" << endl;
        int count = 0;
        string tp, hNumber, hName[1000];
        while(getline(inFile, tp)){
            hName[count] = tp;
            count++;
        }
        for (int i = 0; i < 12; i++){
            int one = 0;
            int zero = 0;
            for (int index = 0; index < count; index++)
                if (hName[index][i] == '1')one++;else zero++;
            if (one >= zero)hNumber.append("1");else hNumber.append("0");
        }
        for(int i = 0; i < 12; i++)cout << hNumber[i];
        cout << endl << binaryToDecimal(hNumber) << endl
        << reverseBinary(hNumber)<< endl << binaryToDecimal(reverseBinary(hNumber)) << endl;
        cout <<"A1:"<< (binaryToDecimal(hNumber) * binaryToDecimal(reverseBinary(hNumber)))<< endl;
        inFile.close();
    }else cout << "Unable to open file";
}