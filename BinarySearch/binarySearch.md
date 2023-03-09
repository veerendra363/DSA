# Binary Search  
Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).  

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

### Problems