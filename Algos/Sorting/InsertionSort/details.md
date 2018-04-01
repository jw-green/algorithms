# Insertion Sort

| Best | Average          | Worst            | Concept |
| ---- | ---------------- | ---------------- | ------- |
| O(n) | O(n<sup>2</sup>) | O(n<sup>2</sup>) | Arrays  |

## Description

For each `i` from `0` to `n-1`, exchange `A[i]` with the entries that are smaller in `A[0]` through `A[i-1]`. As the index `i` travels from left to right, the entries to its left are in sorted order in the array, so the array is fully sorted when `i` reaches the right end.

## Implementation

### Pseudo

```psuedo
sort(A)
  for i = 1 to n - 1
    insert(A, i, A[i])
end

insert(A, pos, value)
  i = pos - 1
  while(i >= 0 and A[i] > value)
    A[i+1] = A[i]
    i = i - 1
  A[i+1] = value
end
```

### Python

```python
  code-here
```

## Tags
