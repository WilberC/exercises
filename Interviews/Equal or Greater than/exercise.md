## Exercise

- [Equal or Greater than]()

## Instructions

- In the Python file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER. 
- Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.
- PD: For this example I will be using a json that simulates the Endpoint response
### Examples:

- Input:

```json
{
  "data": "key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"
}
```

- Output:

```python
2
```