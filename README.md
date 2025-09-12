# Matrix-semigroups

The file "BisymFactByMinimum.py" implements a factorization algorithm of a two-by-two bisymmetric matrix with relatively prime entries, to search for factorizations into non-negative integer matrices. Details can be found the be paper "Atoms in the Semigroup of Non-Negative Integer Matrices" by Dever, Goedhart, and Heilbrunn, which will soon be posted to the ArXiv.

Given a range of minimum entries m to M, the algorithm with search all two-by-two bisymmetric matrices with relatively prime entries and find all factorable matrices. All matrices with relatively prime entries that are not found by the algorithm are necessarily atoms.

The file "BisymmetricData.csv" contains all factorizations for such matrices with minimum value up to m=100. The columns listed are x, y, a, b, c, d, e, f, g, where
```math
\begin{pmatrix}x &y\\y &x\end{pmatrix} = \begin{pmatrix} a& b\\ c&d\end{pmatrix} \begin{pmatrix} d & e\\f&g\end{pmatrix}
```
The final column is "True" if the factors are bisymmetric, and "False" if the factors are not bisymmetric. All factors found have been bisymmetric.
