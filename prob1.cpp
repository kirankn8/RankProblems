// Problem:

/*

Marc loves cupcakes, but he also likes to stay fit. He eats  cupcakes in one sitting, and each cupcake  has a calorie count, . 
After eating a cupcake with  calories, he must walk at least  (where  is the number cupcakes he has already eaten) miles to maintain his w
eight.

Given the individual calorie counts for each of the  cupcakes, find and print a long integer denoting the minimum number of miles Marc 
must walk to maintain his weight. Note that he can eat the cupcakes in any order.

Input Format

The first line contains an integer, , denoting the number of cupcakes. 
The second line contains  space-separated integers describing the respective calorie counts of each cupcake, .

Constraints

Output Format

Print a long integer denoting the minimum number of miles Marc must walk to maintain his weight.

Sample Input 0

3
1 3 2
Sample Output 0

11

*/
#include <bits/stdc++.h>

using namespace std;

long marcsCakewalk(vector <int> calorie, int no_caloires) {
    // Complete this function
    int n = no_caloires;
    long int sum = 0;
    sort(calorie.begin(), calorie.begin() + n, greater<int>());
    for(int calorie_i = 0; calorie_i < n; calorie_i++) { 
        sum = sum + (calorie[calorie_i] * pow(2, calorie_i));
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    vector<int> calorie(n);
    for(int calorie_i = 0; calorie_i < n; calorie_i++){
       cin >> calorie[calorie_i];
    }
    long result = marcsCakewalk(calorie, n);
    cout << result << endl;
    return 0;
}