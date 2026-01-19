# Matrix-semigroups

The file "BisymFactByMinimum.py" implements a factorization algorithm of a two-by-two bisymmetric matrix with relatively prime entries, to search for factorizations into non-negative integer matrices. Details can be found the be paper "Atoms in the Semigroup of Non-Negative Integer Matrices" by Dever, Goedhart, Heilbrunn, and Wong, which will soon be posted to the ArXiv.

Given a range of minimum entries m to M, the algorithm with search all two-by-two bisymmetric matrices with relatively prime entries and find all factorable matrices. All matrices with relatively prime entries that are not found by the algorithm are necessarily atoms. By the main theorem of our paper, the factors will necessarily be bisymmetric.

The file "BisymDataSorted4to500.csv" contains all factorizations of such matrices with minimum value up to m=500. The columns listed are x, y, a, b, c, d where
```math
\begin{pmatrix}x &y\\y &x\end{pmatrix} = \begin{pmatrix} a& b\\ b&a\end{pmatrix} \begin{pmatrix} c & d\\d&c\end{pmatrix}
