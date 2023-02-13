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

### Problems
1) Sum of 'N' natural numbers (parameterized & functional recursion)  
2) Print all subsequences (pick and not pick)  




