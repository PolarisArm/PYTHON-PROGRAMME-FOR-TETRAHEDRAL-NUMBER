# PYTHON-PROGRAMME-FOR-TETRAHEDRAL-NUMBER
Tetrahedral numbers or triangular pyramidal numbers are 3-dimensional figurate numbers representing tetrahedra (or tetrahedrons).<br>
Every Tetrahedral number is sum of first nth triangular number. <br>
__Formula:__
  __SUM((N*(N+1))/2)__

# Code:

```Python
 tetrahedral_number = 0
        i = 1
        while tetrahedral_number < n:
            tetrahedral_number += i * (i + 1) // 2
            i += 1
        return tetrahedral_number == n
```
