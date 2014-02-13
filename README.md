pyC
===

Run C code from a python string.k

Notes
-----
* Requires gcc

Example
-------
```python
from pyC import runC
funcs = """
void f1() {
    printf("f1");
}
void run(int n) {
    int i;
    for (i = 0; i < n; i++) {
        f1();
    }
}
"""
r = """
printf("Running...");
run({});
"""
imports = ['<stdio.h>']
output = runC(funcs, r.format(10), imports)
print output
# Running...f1f1f1f1f1f1f1f1f1f1
```
