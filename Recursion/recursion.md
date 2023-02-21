# Recursion
A function is calling itself until a specific condition(Base Case) is met.  
fun(){  
&emsp;condition(Base Case){  
&emsp;&emsp;return val  
&emsp;}   
&emsp;fun()   
}  
### Key Words
-> Stack Space  
-> Base case  
-> Recursion Tree  
-> Pick not pick method  

### Recursion Tips and Tricks  
#### Count number of ways  
f(){  
&emsp;base Case  
&emsp;&emsp;return 1 if way is valid  
&emsp;&emsp;return 0 if way is invalid(optional in some cases)  
&emsp;leftSubTree = f()  
&emsp;rightSubTree = f()  
&emsp;return leftSubTree + rightSubTree  
}  

#### Pick not pick method  
f(i){  
&emsp;base Case  
&emsp;pick = (value +) f(i-1)  
&emsp;notpick = f(i-1)  
&emsp;total = pick + notpick  
&emsp;mini = min(pick, notpick)  
&emsp;maxi = max(pick, notpick)  
&emsp;return total | mini | maxi based on question  
}  

#### Infinite Supplies or Multiple use  
f(i, target){  
&emsp;base Case  
&emsp;<ins>pick = (value +) f(i, target) i th item is used multiple times</ins>  
&emsp;notpick = f(i-1, target)  
&emsp;total = pick + notpick  
&emsp;mini = min(pick, notpick)  
&emsp;maxi = max(pick, notpick)  
&emsp;return total | mini | maxi based on question  
}  

### Problems
1) Sum of 'N' natural numbers (parameterized & functional recursion)  
2) Print all subsequences (pick and not pick)  




