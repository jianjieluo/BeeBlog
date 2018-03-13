@(Coding Language & Algorithm)[homework]

# *Algorithms* Chapter 8 8.3 Solution

## Description

`STINGY SAT` is th following problem: given a set of clauses (each a disjunction of literals) and an integer `k`,find a satisfying assignment in which at most `k` variables are `true`, if such an assignment exists. Prove that `STINGY SAT` is **NP-complete**.

## Solution

1. **证明`STINGY SAT`问题是NP的**。不难知道`STINGY SAT`问题在多项式的时间之内是可以验证的，只需要查看一下给出的值是不是最多只有k个为真并且把给出的值代入布尔表达式里面验证即可。
2. **证明由SAT问题转到`STINGY SAT`问题是可以在多项式时间内完成的**。 对于一个SAT问题，将k赋值为该SAT问题的变量的总数，即可以将其转换为`STINGY SAT`问题。
3. **证明如果`STINGY SAT`有解，则可以在多项式时间内找到对应的SAT问题的解**。如果`STINGY SAT`有解，该解各变量所赋的值也一定满足对应的SAT问题，因为它们的本质是相同的。
4.  **证明如果`STINGY SAT`无解，则对应的SAT问题无解**。考虑其逆否命题：**如果一个SAT问题有解，则可以找到它对应的`STINGY SAT`问题的解**。该命题是显然的，寻找过程的复杂度甚至是$O(1)$，因为该解可以直接满足对应的`STINGY SAT`问题，只是多了一个k的限制而已。


综上所述，SAT问题可以归约到`STINGY SAT`问题，所以`STINGY SAT`问题是**NP-Complete**的，证毕。