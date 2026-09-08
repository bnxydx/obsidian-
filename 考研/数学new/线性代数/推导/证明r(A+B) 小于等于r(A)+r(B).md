### 方法二：利用分块矩阵的初等变换
$$r(A + B) \le r(A) + r(B)$$
构造一个 $2m \times n$ 的分块矩阵，利用初等行变换不改变矩阵的秩：

1. 考虑分块矩阵：
    
    $$M = \begin{pmatrix} A \\ B \end{pmatrix}$$
    
2. 对 $M$ 进行初等行变换（把第 $m+1$ 到 $2m$ 行加到前 $m$ 行上）：
    
    $$\begin{pmatrix} E_m & E_m \\ O & E_m \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} = \begin{pmatrix} A + B \\ B \end{pmatrix}$$
    
    由于左乘满秩初等分块矩阵不改变秩，因此：
    
    $$r\begin{pmatrix} A + B \\ B \end{pmatrix} = r\begin{pmatrix} A \\ B \end{pmatrix}$$
    
3. 矩阵的子块的秩不会超过整体的秩：
    
    $$r(A + B) \le r\begin{pmatrix} A + B \\ B \end{pmatrix} = r\begin{pmatrix} A \\ B \end{pmatrix}$$
    
4. 而分块矩阵 $\begin{pmatrix} A \\ B \end{pmatrix}$ 由 $A$ 和 $B$ 的行向量拼接而成，其极大无关行向量的个数至多等于 $A$ 的行数基向量数加上 $B$ 的行数基向量数，即：
    
    $$r\begin{pmatrix} A \\ B \end{pmatrix} \le r(A) + r(B)$$
    

综合上述两步，即可得到：

$$r(A + B) \le r(A) + r(B)$$