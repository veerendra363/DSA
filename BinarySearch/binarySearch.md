# Binary Search  
Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).  

(Binary Search PlayList)[https://www.youtube.com/playlist?list=PLgUwDviBIf0qYbL4TBaEWgb-ljVdhkM7R]  
python lib for binary search  
(bisect)[https://docs.python.org/3/library/bisect.html]  
### Binary Search Sudo Code
binarySearch(arr, x, low, high)  
&emsp;repeat till low = high  
&emsp;&emsp;mid = (low + high)/2  
&emsp;&emsp;&emsp;if (x == arr[mid])  
&emsp;&emsp;&emsp;&emsp;return mid  
  
&emsp;&emsp;&emsp;else if (x > arr[mid]) // x is on the right side  
&emsp;&emsp;&emsp;&emsp;low = mid + 1  
  
&emsp;&emsp;&emsp;else   // x is on the left side  
&emsp;&emsp;&emsp;&emsp;high = mid - 1  

### Key Words
#### Monotonic functions  
A function is said to be monotonic if it always maintains the order of its inputs. It is called monotonic increasing if increasing inputs result in increasing outputs, and monotonic decreasing if increasing inputs result in decreasing outputs.  
Ex:-  
f(x) = 2x  
f(x) = -x  

#### Search space  
Search space is a concept in computer science and optimization that refers to the set of all possible solutions to a problem. In other words, it is the range of values or configurations that can be searched or explored in order to find a solution.  



### Problems
1) Find First and Last Position of Element in Sorted Array  