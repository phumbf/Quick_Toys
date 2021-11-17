//Program to convert from Roman numerals to Arabic numerals and vice versa

#include<iostream>
#include<map>
#include<iterator>
#include<vector>

void convertRoman(std::string &roman, int &num){

	//Map to store the correct values
	std::map<std::string,int> romanToNum;
	romanToNum["I"] = 1;
	romanToNum["V"] = 5;
	romanToNum["X"] = 10;
	romanToNum["L"] = 50;
	romanToNum["C"] = 100;
	romanToNum["D"] = 500;
	romanToNum["M"] = 1000;

	//Loop through the string
	for(int i=0; i<roman.length(); ++i){

		//Determine a pair of letters and convert 
		std::string firstString{roman[i]};
		std::string secondString{roman[i+1]};

		int first = romanToNum[firstString];
		int second = romanToNum[secondString];

		//If preceding number at least as big as latter then add it
		if(first >= second){
			num += first;
		}
		//...Otherwise need to subtract it from the second, then skip the second as well
		else{ 
			num += (second - first);
			++i;
		}
	}
}

//Convert 
void convertNumber(int num, std::string &roman){
	
	std::map<int,std::string> numToRoman;
	numToRoman[1] = "I";
	numToRoman[4] = "IV";
	numToRoman[5] = "V";
	numToRoman[9] = "IX";
	numToRoman[10] = "X";
	numToRoman[40] = "XL";
	numToRoman[50] = "L";
	numToRoman[90] = "XC";
	numToRoman[100] = "C";
	numToRoman[400] = "CD";
	numToRoman[500] = "D";
	numToRoman[900] = "CM";
	numToRoman[1000] = "M";

	std::vector<int> numVec = {1000,900,500,400,100,90,50,40,10,9,5,4,1};

	for(auto x : numVec){

		//Determine how many of each possible roman number there are
		int hm = num / x;

		//For each instance, add to the number
		for(int i=0; i<hm; ++i){
			roman += numToRoman[x];
			//Remove this from the number
			num -= x;
		}
	}
}

int main(int argc, char *argv[]){
	
	//User input 
	int num = atoi(argv[1]);
	std::string roman{""};
	convertNumber(num,roman);

	//Print the resulting roman numeral
	std::cout << "Converting input number to Roman gives: " << roman << std::endl;

	//Second integer to ensure correct behaviour
	int num2 = 0;
	convertRoman(roman,num2);

	//Error catching if bug
	try{
		if(num == num2){
			std::cout << "Converting this back to Arabic gives: " << num2 << std::endl;
			return 0;
		}
		else{
			throw(num2);
		}
	}
	catch(int myNum){
		std::cout << "ERROR" << std::endl;
		return 1;
	}
}
