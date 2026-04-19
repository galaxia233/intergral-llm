# Problems in Mathematical Analysis III

Integration

W.J.Kaczor M.T.Nowak

# STUDENT MATHEMATICAL LIBRARY Volume 21

# Problems in Mathematical Analysis III

Integration

W.J. Kaczor

M. T. Nowak

# Editorial Board

David Bressoud, Chair Daniel L. Goroff Carl Pomerance

2000 Mathematics Subject Classification. Primary 00A07, 26A42; Secondary 26A45, 26A46, 26D15, 28A12.

For additional information and updates on this book, visit www.ams.org/bookpages/std-21

Library of Congress Cataloging-in-Publication Data

Kaczor, W. J. (Wieslawa J.), 1949-

[Zadania z analyzymatematycznej. English]

Problems in mathematical analysis. I. Real numbers, sequences and series / W. J. Kaczor, M. T. Nowak.

p. cm. (Student mathematical library, ISSN 1520-9121; v. 4)

Includes bibliographical references.

ISBN 0-8218-2050-8 (softcover ; alk. paper)

1. Mathematical analysis. I. Nowak, M. T. (Maria T.), 1951- II. Title. III. Series.

QA300K32513 2000

515'.076—dc21

99-087039

Copying and reprinting. Individual readers of this publication, and nonprofit libraries acting for them, are permitted to make fair use of the material, such as to copy a chapter for use in teaching or research. Permission is granted to quote brief passages from this publication in reviews, provided the customary acknowledgment of the source is given.

Republication, systematic copying, or multiple reproduction of any material in this publication is permitted only under license from the American Mathematical Society. Requests for such permission should be addressed to the Acquisitions Department, American Mathematical Society, 201 Charles Street, Providence, Rhode Island 02904-2294, USA. Requests can also be made by e-mail to reprint-permission@ams.org.

© 2003 by the American Mathematical Society. All rights reserved. The American Mathematical Society retains all rights except those granted to the United States Government. Printed in the United States of America.

The paper used in this book is acid-free and falls within the guidelines established to ensure permanence and durability. Visit the AMS home page at http://www.ams.org/

10987654321 080706050403

# Contents

Preface vii

# Part 1. Problems

Chapter 1. The Riemann-Stieltjes Integral 3   
$\S 1.1$ . Properties of the Riemann-Stieltjes Integral 3   
$\S 1.2$ Functions of Bounded Variation 10   
$\S 1.3$ . Further Properties of the Riemann-Stieltjes Integral 15   
$\S 1.4$ .Proper Integrals 21   
$\S 1.5$ . Improper Integrals 28   
$\S 1.6$ Integral Inequalities 42   
$\S 1.7$ Jordan Measure 52

Chapter 2. The Lebesgue Integral 59

$\S 2.1$ .Lebesgue Measure on the Real Line 59   
$\S 2.2$ .Lebesgue Measurable Functions 66   
$\S 2.3$ .Lebesgue Integration 71   
$\S 2.4$ Absolute Continuity, Differentiation and Integration 79

§2.5. Fourier Series 84

# Part 2. Solutions

Chapter 1. The Riemann-Stieltjes Integral 97

$\S 1.1$ . Properties of the Riemann-Stieltjes Integral 97   
$\S 1.2$ Functions of Bounded Variation 114   
$\S 1.3$ . Further Properties of the Riemann-Stieltjes Integral 126   
$\S 1.4$ .Proper Integrals 143   
$\S 1.5$ . Improper Integrals 164   
$\S 1.6$ Integral Inequalities 207   
§1.7. Jordan Measure 228

Chapter 2. The Lebesgue Integral 247

$\S 2.1$ .Lebesgue Measure on the Real Line 247   
$\S 2.2$ .Lebesgue Measurable Functions 268   
$\S 2.3$ .Lebesgue Integration 281   
$\S 2.4$ Absolute Continuity, Differentiation and Integration 296   
§2.5. Fourier Series 316

Bibliography - Books 351

Index 355

# Chapter 1

# The Riemann-Stieltjes Integral

# 1.1. Properties of the Riemann-Stieltjes Integral

We start with some basic notations, definitions and theorems. By a partition $P$ of a closed interval $[a,b]$ we mean a finite set of points $x_0, x_1, \ldots, x_n$ such that

$$
a = x _ {0} <   x _ {1} <   \dots <   x _ {n - 1} <   x _ {n} = b.
$$

The number $\mu(P) = \max\{x_i - x_{i-1} : i = 1,2,\ldots,n\}$ is called the mesh of $P$ .

For a function $\alpha$ monotonically increasing on $[a,b]$ we write

$$
\Delta \alpha_ {i} = \alpha (x _ {i}) - \alpha (x _ {i - 1}).
$$

If $f$ is a real function bounded on $[a, b]$ , we define the upper and lower Darboux sums of $f$ with respect to $\alpha$ and relative to $P$ , respectively, by

$$
U (P, f, \alpha) = \sum_ {i = 1} ^ {n} M _ {i} \Delta \alpha_ {i}, \quad L (P, f, \alpha) = \sum_ {i = 1} ^ {n} m _ {i} \Delta \alpha_ {i},
$$

where

$$
M _ {i} = \sup  _ {x \in \left[ x _ {i - 1}, x _ {i} \right]} f (x), \quad m _ {i} = \inf  _ {x \in \left[ x _ {i - 1}, x _ {i} \right]} f (x).
$$

We also put

$$
\overline {{\int_ {a} ^ {b}}} f d \alpha = \inf  U (P, f, \alpha), \quad \underline {{\int_ {a} ^ {b}}} f d \alpha = \sup  L (P, f, \alpha),
$$

where the infimum and the supremum are taken over all partitions $P$ of $[a, b]$ , and call them, respectively, the upper and the lower Riemann-Stieltjes integral. If the upper and the lower Riemann-Stieltjes integrals are equal, we denote the common value by $\int_{a}^{b} f dx$ and call it the Riemann-Stieltjes integral of $f$ with respect to $\alpha$ over $[a, b]$ . In this case we say that $f$ is integrable with respect to $\alpha$ , in the Riemann sense, and we write $f \in \mathcal{R}(\alpha)$ . In the special case of $\alpha(x) = x$ we get the Riemann integral. In this case the upper (lower) Darboux sum corresponding to a partition $P$ , and the upper (lower) Riemann integral are denoted, respectively, by $U(P, f)$ ( $L(P, f)$ ), and $\overline{\int_{a}^{b} f dx} \left( \underline{\int_{a}^{b} f dx} \right)$ . The Riemann integral of $f$ over $[a, b]$ is denoted by $\int_{a}^{b} f dx$ .

Moreover, corresponding to every partition $P$ of $[a, b]$ we choose points $t_1, t_2, \ldots, t_n$ such that $x_{i-1} \leq t_i \leq x_i$ , $i = 1, 2, \ldots, n$ , and consider the sum

$$
S (P, f, \alpha) = \sum_ {i = 1} ^ {n} f \left(t _ {i}\right) \Delta \alpha_ {i}.
$$

We say that

$$
\lim  _ {\mu (P) \rightarrow 0} S (P, f, \alpha) = A
$$

if, for every $\varepsilon > 0$ , there is $\delta > 0$ such that $\mu(P) < \delta$ implies that $|S(P, f, \alpha) - A| < \varepsilon$ for all admissible choices of $t_i$ . In the case when $\alpha(x) = x$ we set

$$
S (P, f) = \sum_ {i = 1} ^ {n} f (t _ {i}) (x _ {i} - x _ {i - 1}).
$$

Throughout this section, $f$ is always assumed to be bounded and $\alpha$ monotonically increasing on $[a, b]$ . In the solutions we will often use the following theorems (see, e.g., Rudin [28]).

Theorem 1. $f \in \mathcal{R}(\alpha)$ on $[a, b]$ if and only if for every $\varepsilon > 0$ there exists a partition $P$ such that

$$
U (P, f, \alpha) - L (P, f, \alpha) <   \varepsilon .
$$

Theorem 2. If $f$ is continuous on $[a, b]$ , then $f \in \mathcal{R}(\alpha)$ on $[a, b]$ .

1.1.1. Suppose $\alpha$ increases on $[a, b]$ , $a \leq c \leq b$ , $\alpha$ is continuous at $c$ , $f(c) = 1$ , and $f(x) = 0$ for $x \neq c$ . Show that $f \in \mathcal{R}(\alpha)$ and that $\int_{a}^{b} f d\alpha = 0$ .

1.1.2. Suppose $f$ is continuous on $[a, b]$ , $a < c < b$ , $\alpha(x) = 0$ if $x \in [a, c)$ , and $\alpha(x) = 1$ if $x \in [c, b]$ . Show that $\int_{a}^{b} f d\alpha = f(c)$ .

1.1.3. Let $0 < a < b$ and

$$
f (x) = \left\{ \begin{array}{l l} x & \text {i f} x \in [ a, b ] \cap \mathbb {Q}, \\ 0 & \text {i f} x \in [ a, b ] \setminus \mathbb {Q}. \end{array} \right.
$$

Find the upper and lower Riemann integrals of $f$ over $[a, b]$ .

1.1.4. Let $a > 0$ and

$$
f (x) = \left\{ \begin{array}{l l} x & \text {i f} x \in \{- a, a \} \cap \mathbb {Q}, \\ 0 & \text {i f} x \in \{- a, a \} \setminus \mathbb {Q}. \end{array} \right.
$$

Find the upper and lower Riemann integrals of $f$ over $[-a, a]$ .

1.1.5. Show that the so-called Riemann function

$$
f (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \text {i s i r r a t i o n a l o r} x = 0, \\ 1 / q & \text {i f} x = p / q, p \in \mathbb {Z}, q \in \mathbb {N}, \text {a n d} \\ & p, q \text {a r e c o - p r i m e ,} \end{array} \right.
$$

is Riemann integrable on every interval $[a,b]$ .

1.1.6. Let $f:[0,1] \to \mathbb{R}$ be defined by setting

$$
f (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x = \frac {1}{n}, n \in \mathbb {N}, \\ 0 & \text {o t h e r w i s e .} \end{array} \right.
$$

Show that $\int_0^1 f(x)dx = 0$

1.1.7. Show that $f:[0,1] \to \mathbb{R}$ defined by

$$
f (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x = 0, \\ \frac {1}{x} - \left[ \frac {1}{x} \right] & \text {o t h e r w i s e} \end{array} \right.
$$

is Riemann integrable on $[0,1]$ .

1.1.8. Define

$$
f (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \in [ - 1, 0 ], \\ 1 & \text {i f} x \in (0, 1 ], \end{array} \right. \quad \text {a n d} \quad \alpha (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \in [ - 1, 0), \\ 1 & \text {i f} x \in [ 0, 1 ]. \end{array} \right.
$$

Show that $f \in \mathcal{R}(\alpha)$ although $\lim_{\mu(P) \to 0} S(P, f, \alpha)$ does not exist.

1.1.9. Show that if $f$ and $\alpha$ have a common point of discontinuity in $[a, b]$ , then $\lim_{\mu(P) \to 0} S(P, f, \alpha)$ does not exist.

1.1.10. Prove that if $\lim_{\mu(P) \to 0} S(P, f, \alpha)$ exists, then $f \in \mathcal{R}(\alpha)$ on $[a, b]$ and

$$
\lim  _ {\mu (P) \rightarrow 0} S (P, f, \alpha) = \int_ {a} ^ {b} f d \alpha .
$$

Show also that for every $f$ continuous on $[a, b]$ , the above equality holds.

1.1.11. Show that if $f$ is bounded and $\alpha$ is continuous on $[a, b]$ , then $f \in \mathcal{R}(\alpha)$ if and only if $\lim_{\mu(P) \to 0} S(P, f, \alpha)$ exists.

1.1.12. Let

$$
\alpha (x) = \left\{ \begin{array}{l l} c & \text {i f} a \leq x <   x ^ {*}, \\ d & \text {i f} x ^ {*} <   x \leq b, \end{array} \right.
$$

where $c < d$ and $c \leq \alpha(x^*) \leq d$ . Show that if $f$ is bounded on $[a, b]$ and such that at least one of the functions $f$ or $\alpha$ is continuous from the left at $x^*$ and the other is continuous from the right at $x^*$ , then $f \in \mathcal{R}(\alpha)$ and

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f \left(x ^ {*}\right) (d - c).
$$

1.1.13. Suppose that $f$ is continuous on $[a, b]$ and $\alpha$ is a step function that is constant on the subintervals $(a, c_1), (c_1, c_2), \ldots, (c_m, b)$ , where $a < c_1 < c_2 < \cdots < c_m < b$ . Show that

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \alpha (x) = f (a) \left(\alpha \left(a ^ {+}\right) - \alpha (a)\right) + \sum_ {k = 1} ^ {m} f \left(c _ {k}\right) \left(\alpha \left(c _ {k} ^ {+}\right) - \alpha \left(c _ {k} ^ {-}\right)\right) \\ + f (b) (\alpha (b) - \alpha (b ^ {-})). \\ \end{array}
$$

1.1.14. Using Riemann integrals of suitably chosen functions, find the following limits:

(a) $\lim_{n\to \infty}\left(\frac{1}{n + 1} +\frac{1}{n + 2} +\dots +\frac{1}{3n}\right),$

(b) $\lim_{n\to \infty}n^{2}\left(\frac{1}{n^{3} + 1^{3}} +\frac{1}{n^{3} + 2^{3}} +\dots +\frac{1}{n^{3} + n^{3}}\right),$

(c) $\lim_{n\to \infty}\left(\frac{1^k + 2^k + \cdots + n^k}{n^{k + 1}}\right),\quad k\geq 0,$

(d) $\lim_{n\to \infty}\frac{1}{n}\sqrt[n]{(n + 1)(n + 2)\cdots(n + n)},$

(e) $\lim_{n\to \infty}\left(\sin \frac{n}{n^2 + 1^2} +\sin \frac{n}{n^2 + 2^2} +\dots +\sin \frac{n}{n^2 + n^2}\right),$

(f) $\lim_{n\to \infty}\left(\frac{2^{1 / n}}{n + 1} +\frac{2^{2 / n}}{n + 1 / 2} +\dots +\frac{2^{n / n}}{n + 1 / n}\right),$

(g) $\lim_{n\to \infty}\sqrt[n]{f(1 / n)f(2 / n)\ldots f(n / n)}$ where $f$ is a positive and continuous function on [0,1].

1.1.15. Show that the limit

$$
\lim  _ {n \rightarrow \infty} \left(\frac {\sin \frac {\pi}{n + 1}}{1} + \frac {\sin \frac {2 \pi}{n + 1}}{2} + \dots + \frac {\sin \frac {n \pi}{n + 1}}{n}\right)
$$

is positive.

1.1.16. Show that if $f$ is continuously differentiable on $[0, 1]$ , then

$$
\lim  _ {n \rightarrow \infty} n \left(\frac {1}{n} \sum_ {i = 1} ^ {n} f \left(\frac {i}{n}\right) - \int_ {0} ^ {1} f (x) d x\right) = \frac {f (1) - f (0)}{2}.
$$

Using this result, calculate

$$
\lim  _ {n \rightarrow \infty} n \left(\frac {1 ^ {k} + 2 ^ {k} + \cdots + n ^ {k}}{n ^ {k + 1}} - \frac {1}{k + 1}\right), \quad k \geq 0.
$$

1.1.17. For $k \geq 0$ , calculate

$$
\lim  _ {n \rightarrow \infty} \left(\frac {1 ^ {k} + 3 ^ {k} + \cdots + (2 n - 1) ^ {k}}{n ^ {k + 1}}\right).
$$

1.1.18. Suppose that $f$ is twice differentiable on $[0, 1]$ and $f''$ is bounded and Riemann integrable. Show that

$$
\lim  _ {n \rightarrow \infty} n ^ {2} \left(\int_ {0} ^ {1} f (x) d x - \frac {1}{n} \sum_ {i = 1} ^ {n} f \left(\frac {2 i - 1}{2 n}\right)\right) = \frac {f ^ {\prime} (1) - f ^ {\prime} (0)}{2 4}.
$$

1.1.19. For $n \in \mathbb{N}$ , define

$$
U _ {n} = \frac {1}{n + 1} + \frac {1}{n + 2} + \dots + \frac {1}{2 n}
$$

and

$$
V _ {n} = \frac {2}{2 n + 1} + \frac {2}{2 n + 3} + \dots + \frac {2}{4 n - 1}.
$$

Show that

$$
\lim  _ {n \rightarrow \infty} U _ {n} = \lim  _ {n \rightarrow \infty} V _ {n} = \ln 2.
$$

Moreover, using the results stated in 1.1.16 and 1.1.18, show that

$$
\lim  _ {n \rightarrow \infty} n (\ln 2 - U _ {n}) = \frac {1}{4} \quad \text {a n d} \quad \lim  _ {n \rightarrow \infty} n ^ {2} (\ln 2 - V _ {n}) = \frac {1}{3 2}.
$$

1.1.20. Show that if $f$ is Riemann integrable over $[a, b]$ , then $f$ can be changed at a finite number of points without affecting either the integrability of $f$ or the value of its integral.

1.1.21. Show that if $f$ is monotonic and $\alpha$ is continuous on $[a, b]$ , then $f \in \mathcal{R}(\alpha)$ .

1.1.22. Prove that if $f \in \mathcal{R}(\alpha)$ and $\alpha$ is neither continuous from the left nor from the right at a point in $[a, b]$ , then $f$ is continuous at this point.

1.1.23. Let $f$ be Riemann integrable and $\alpha$ continuous on $[a, b]$ . If $\alpha$ is differentiable on $[a, b]$ except for finitely many points and $\alpha'$ is Riemann integrable, then $f \in \mathcal{R}(\alpha)$ and

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = \int_ {a} ^ {b} f (x) \alpha^ {\prime} (x) d x.
$$

1.1.24. Let $f$ be Riemann integrable and $\alpha$ be continuous on $[a, b]$ except for finitely many points. If $\alpha$ is differentiable on $[a, b]$ except

for finitely many points and $\alpha'$ is Riemann integrable, then $f \in \mathcal{R}(\alpha)$ and

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \alpha (x) = \int_ {a} ^ {b} f (x) \alpha^ {\prime} (x) d x + f (a) \left(\alpha \left(a ^ {+}\right) - \alpha (a)\right) \\ + \sum_ {k = 1} ^ {m} f (c _ {k}) (\alpha (c _ {k} ^ {+}) - \alpha (c _ {k} ^ {-})) + f (b) (\alpha (b) - \alpha (b ^ {-})), \\ \end{array}
$$

where $c_k, k = 1,2,\ldots,m$ , are points of discontinuity of $\alpha$ in $(a,b)$ .

1.1.25. Calculate $\int_{-2}^{2}x^{2}d\alpha (x)$ , where

$$
\alpha (x) = \left\{ \begin{array}{l l} x + 2 & \text {i f} - 2 \leq x \leq - 1, \\ 2 & \text {i f} - 1 <   x <   0, \\ x ^ {2} + 3 & \text {i f} 0 \leq x \leq 2. \end{array} \right.
$$

1.1.26. Prove the First Mean Value Theorem. If $f$ is continuous and $\alpha$ is monotonically increasing on $[a, b]$ , then there is $c \in [a, b]$ such that

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f (c) (\alpha (b) - \alpha (a)).
$$

1.1.27. Show that if $f$ is continuous and $\alpha$ is strictly increasing on $[a, b]$ , then it is possible to choose $c \in (a, b)$ such that the equality in the first mean value theorem (stated above) holds.

1.1.28. (a) Let $f$ be continuous on $[0, 1]$ . For positive $a$ and $b$ , find the limit

$$
\lim  _ {e \rightarrow 0 ^ {+}} \int_ {a \varepsilon} ^ {b \varepsilon} \frac {f (x)}{x} d x.
$$

(b) Calculate

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} \frac {x ^ {n}}{1 + x} d x.
$$

1.1.29. Suppose $f$ is continuous and $\alpha$ is strictly increasing on $[a, b]$ ; define

$$
F (x) = \int_ {a} ^ {x} f (t) d \alpha (t).
$$

Show that for $x \in [a, b]$

$$
\lim  _ {h \rightarrow 0} \frac {F (x + h) - F (x)}{\alpha (x + h) - \alpha (x)} = f (x).
$$

1.1.30. Suppose $f$ is continuous on $[a, b]$ , $\alpha$ is both continuous and strictly increasing there, and the limit

$$
\lim  _ {h \rightarrow 0} \frac {f (x + h) - f (x)}{\alpha (x + h) - \alpha (x)} = \frac {d f}{d \alpha} (x)
$$

exists and is continuous on $[a,b]$ . Show that

$$
\int_ {a} ^ {b} \frac {d f}{d \alpha} (x) d \alpha (x) = f (b) - f (a).
$$

# 1.2. Functions of Bounded Variation

Recall that the total variation $V(f; a, b)$ of $f$ on $[a, b]$ is

$$
V (f; a, b) = \sup  \left\{\sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) | \right\},
$$

where the supremum is taken over all partitions $P = \{x_0, x_1, \ldots, x_n\}$ of $[a, b]$ . If $V(f; a, b) < +\infty$ , then $f$ is said to be of bounded variation on $[a, b]$ . We also define

$$
v _ {f} (x) = V (f; a, x), \quad a \leq x \leq b.
$$

Clearly, $v_{f}(a) = 0$ and $v_{f}$ is monotonically increasing on $[a,b]$ . The following theorem says that a function of bounded variation can be exhibited as a difference of two monotonic functions.

Theorem 1. If $f$ is of bounded variation on $[a, b]$ , then

$$
f (x) - f (a) = p (x) - q (x),
$$

where

$$
p (x) = \frac {1}{2} \left(v _ {f} (x) + f (x) - f (a)\right) \quad a n d \quad q (x) = \frac {1}{2} \left(v _ {f} (x) - f (x) + f (a)\right)
$$

are monotonically increasing on $[a,b]$ .

The functions $p$ and $q$ are called the positive and negative variation functions of $f$ , respectively.

1.2.1. Show that the function given by

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} \cos \frac {\pi}{x ^ {2}} & \text {i f} x \in (0, 1 ], \\ 0 & \text {i f} x = 0 \end{array} \right.
$$

is differentiable on $[0,1]$ but not of bounded variation.

1.2.2. Show that if $f$ has a bounded derivative on $[a, b]$ , then $f$ is of bounded variation.

1.2.3. Show that the function

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} \cos \frac {\pi}{x} & \text {i f} x \in (0, 1 ], \\ 0 & \text {i f} x = 0 \end{array} \right.
$$

is of bounded variation on $[0,1]$ .

1.2.4. Show that

$$
V (f; a, b) = f (b) - f (a)
$$

if and only if $\dot{f}$ is monotonically increasing on $[a, b]$ .

1.2.5. For $\alpha \in \mathbb{R}$ and $\beta > 0$ , define

$$
f (x) = \left\{ \begin{array}{l l} x ^ {\alpha} \cos \frac {\pi}{x ^ {\beta}} & \text {i f} x \in (0, 1 ], \\ 0 & \text {i f} x = 0. \end{array} \right.
$$

Show that $f$ is of bounded variation if and only if $\alpha > \beta$ .

1.2.6. Show that if $f$ is of bounded variation on $[a, b]$ , then $f$ is bounded on $[a, b]$ .

1.2.7. If $f$ and $g$ are of bounded variation on $[a, b]$ , then so is their product $fg$ . Moreover, if $\inf_{x \in [a, b]} |f(x)| > 0$ , then $g / f$ is also of bounded variation on $[a, b]$ .

1.2.8. Must the composition of two functions of bounded variation be of bounded variation?

1.2.9. If $f$ satisfies a Lipschitz condition and $g$ is of bounded variation, then the composite function $f \circ g$ is of bounded variation.

1.2.10. Show that if $f$ is of bounded variation on $[a, b]$ , then so is $|f|^p$ , $1 \leq p < +\infty$ .

1.2.11. Prove that if $f$ is continuous on $[a, b]$ and $|f|$ is of bounded variation on $[a, b]$ , then so is $f$ . Prove also that continuity is an essential hypothesis.

1.2.12. If $f$ and $g$ are of bounded variation on $[a, b]$ , then so is $h(x) = \max \{f(x), g(x)\}$ .

1.2.13. We say that $f: \mathbf{A} \to \mathbb{R}$ , $\mathbf{A} \subset \mathbb{R}$ , satisfies a Hölder condition (also called the Lipschitz condition of order $\alpha$ ) on $\mathbf{A}$ if there exist positive constants $M$ and $\alpha$ such that

$$
| f (x) - f \left(x ^ {\prime}\right) | \leq M | x - x ^ {\prime} | ^ {\alpha} \quad \text {f o r} \quad x, x ^ {\prime} \in \mathbf {A}.
$$

(a) Show that the function

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{\ln (1 / x)} & \text {i f} x \in (0, 1 / 2 ], \\ 0 & \text {i f} x = 0 \end{array} \right.
$$

is of bounded variation on $[0,1/2]$ and does not satisfy a Hölder condition.

(b) Set $x_{n} = \sum_{k=n}^{\infty} \frac{1}{k \ln^{2} k}, n = 2, 3, \ldots$ . Let $f$ be the continuous function on $[0, x_{2}]$ defined as follows:

$$
f (0) = f \left(x _ {n}\right) = 0, \quad f \left(\frac {x _ {n} + x _ {n + 1}}{2}\right) = \frac {1}{n}, \quad n = 2, 3, \dots ,
$$

and $f$ is linear on $[x_{n+1}, (x_n + x_{n+1}) / 2]$ and $[(x_n + x_{n+1}) / 2, x_n]$ . Prove that $f$ satisfies a Hölder condition for every $0 < \alpha < 1$ , and that $f$ is not of bounded variation on $[0, x_2]$ .

1.2.14. Suppose that $f: [a, \infty) \to \mathbb{R}$ is of bounded variation on every interval $[a, b]$ , $b > a$ , and put

$$
V (f; a, \infty) = \lim  _ {b \rightarrow \infty} V (f; a, b).
$$

Show that if $V(f; a, \infty) < \infty$ , then the finite limit $\lim_{x \to \infty} f(x)$ exists. Does the opposite implication hold?

1.2.15. For $f$ defined on $[a, b]$ and a partition $P = \{x_0, x_1, \ldots, x_n\}$ of $[a, b]$ , we form the sum

$$
V (f, P) = \sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) |.
$$

Prove that if $f$ is continuous on $[a, b]$ , then

$$
\lim  _ {\mu (P) \rightarrow 0} V (f, P) = V (f; a, b),
$$

that is, for any $\varepsilon > 0$ there exists $\delta > 0$ such that $\mu(P) < \delta$ implies

$$
V (f; a, b) - V (f, P) <   \varepsilon .
$$

1.2.16. For $f$ defined on $[a, b]$ and a partition $P = \{x_0, x_1, \ldots, x_n\}$ of $[a, b]$ , we form the sum

$$
W (f, P) = \sum_ {i = 1} ^ {n} \left(M _ {i} - m _ {i}\right),
$$

where

$$
M _ {i} = \sup  _ {x \in [ x _ {i - 1}, x _ {i} ]} f (x), \quad m _ {i} = \inf  _ {x \in [ x _ {i - 1}, x _ {i} ]} f (x).
$$

Using the result in the previous problem, show that if $f$ is continuous on $[a, b]$ , then

$$
\lim  _ {\mu (P) \rightarrow 0} W (f, P) = V (f; a, b).
$$

1.2.17. Suppose that $f$ is of bounded variation on $[a, b]$ , with $p$ and $q$ its corresponding positive and negative variation functions as defined in Theorem 1. Suppose also that $p_1$ and $q_1$ are increasing functions on $[a, b]$ such that $f = p_1 - q_1$ . Show that if $a \leq x < y \leq b$ , then

$$
p (x) - p (y) \leq p _ {1} (x) - p _ {1} (y) \quad \text {a n d} \quad q (x) - q (y) \leq q _ {1} (x) - q _ {1} (y).
$$

Conclude that $V(p; a, b) \leq V(p_1; a, b)$ and $V(q; a, b) \leq V(q_1; a, b)$ .

1.2.18. Suppose that $f$ is of bounded variation on $[a, b]$ and $f(x) \geq m > 0$ , $x \in [a, b]$ . Show that there are two monotonically increasing functions $g$ and $h$ such that

$$
f (x) = \frac {g (x)}{h (x)} \quad \text {f o r} \quad x \in [ a, b ].
$$

1.2.19. Compute the positive and negative variation functions of

(a) $f(x) = x^{3} - |x|,\quad x\in [-1,1],$   
(b) $f(x) = \cos x, \quad x \in [0, 2\pi]$ ,   
(c) $f(x) = x - [x],\quad x\in [0,3].$

1.2.20. Assume that $f$ is of bounded variation on $[a, b]$ . Prove that if $f$ is continuous from the right (left) at $x_0$ , then $v_f$ is also continuous from the right (left) at $x_0$ .

1.2.21. Show that the set of points of discontinuity of a function $f$ of bounded variation on $[a, b]$ is at most countable. Moreover, if

$\{x_{n}\}$ is the sequence of points of discontinuity of $f$ , then the function $g(x) = f(x) - s(x)$ , where $s(a) = 0$ and

$$
s (x) = f \left(a ^ {+}\right) - f (a) + \sum_ {x _ {n} <   x} \left(f \left(x _ {n} ^ {+}\right) - f \left(x _ {n} ^ {-}\right)\right) + f (x) - f \left(x ^ {-}\right)
$$

for $a < x \leq b$ , is continuous on $[a, b]$ . (The function $s$ is called the saltus function of $f$ .)

1.2.22. Let $f$ be of bounded variation on $[a, b]$ and let

$$
g (a) = 0 \quad \text {a n d} \quad g (x) = \frac {1}{x - a} \int_ {a} ^ {x} f (t) d t, \quad x \in (a, b ].
$$

Prove that $g$ is of bounded variation on $[a, b]$ .

1.2.23. Show that if $f$ satisfies a Lipschitz condition on $[a, b]$ , then $v_f$ also satisfies the Lipschitz condition with the same Lipschitz constant.   
1.2.24. Prove that if $f$ is of bounded variation on $[a, b]$ and enjoys the intermediate value property, then $f$ is continuous. Conclude that if $f'$ is of bounded variation on $[a, b]$ , then $f'$ is continuous.   
1.2.25. Prove that if $f$ is continuously differentiable on $[a, b]$ , then

$$
v _ {f} (x) = \int_ {a} ^ {x} | f ^ {\prime} (t) | d t.
$$

1.2.26. Show that if $f$ is continuous and $\alpha$ monotonically increasing on $[a, b]$ , then the function

$$
F (x) = \int_ {a} ^ {x} f (t) d \alpha (t), \quad x \in [ a, b ],
$$

is of bounded variation on $[a,b]$ .

1.2.27. If $f(x) = \lim_{n\to \infty}f_n(x)$ for $x\in [a,b]$ , then

$$
V (f; a, b) \leq \lim  _ {n \rightarrow \infty} V (f _ {n}; a, b).
$$

1.2.28. Suppose that the series $\sum_{n=1}^{\infty} a_n$ and $\sum_{n=1}^{\infty} b_n$ are absolutely convergent, and let $\{x_n\}$ be a sequence of distinct points in $(0,1)$ . Prove that the function $f$ defined by

$$
f (0) = 0, \quad f (x) = \sum_ {x _ {n} \leq x} a _ {n} + \sum_ {x _ {n} <   x} b _ {n}, \quad \text {f o r} \quad x \in (0, 1 ]
$$

is continuous at every $x \neq x_{n}$ , $n \in \mathbb{N}$ , and

$$
f \left(x _ {n}\right) - f \left(x _ {n} ^ {-}\right) = \dot {a} _ {n}, \quad f \left(x _ {n} ^ {+}\right) - f \left(x _ {n}\right) = b _ {n}.
$$

Prove also that

$$
V (f; 0, 1) = \sum_ {n = 1} ^ {\infty} \left(\left| a _ {n} \right| + \left| b _ {n} \right|\right).
$$

# 1.3. Further Properties of the Riemann-Stieltjes Integral

In this section we consider Riemann-Stieltjes integrals with respect to functions of bounded variation. If $\alpha$ is a function of bounded variation on $[a, b]$ , and if $\alpha = p - q$ , where $p$ and $q$ are monotonically increasing, then

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = \int_ {a} ^ {b} f (x) d p (x) - \int_ {a} ^ {b} f (x) d q (x),
$$

provided that $f \in \mathcal{R}(p)$ and $f \in \mathcal{R}(q)$ (see the definition in Section 1.1). This definition does not depend on a decomposition of $\alpha$ into a difference of two increasing functions.

Theorem 1. If functions $f$ and $\alpha$ are of bounded variation on $[a, b]$ and one of them is continuous, then

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f (b) \alpha (b) - f (a) \alpha (a) - \int_ {a} ^ {b} \alpha (x) d f (x).
$$

The above formula is called the partial integration formula.

Theorem 2. Suppose $f$ and $\varphi$ are continuous on $[a, b]$ and $\varphi$ is strictly increasing on $[a, b]$ . If $\psi$ is the inverse function of $\varphi$ , then

$$
\int_ {a} ^ {b} f (x) d x = \int_ {\varphi (a)} ^ {\varphi (b)} f (\psi (y)) d \psi (y).
$$

The formula in Theorem 2 is called the change of variable formula.

Theorem 3. Suppose that either $f$ is continuous and $\alpha$ is of bounded variation on $[a, b]$ , or $f$ and $\alpha$ are of bounded variation on $[a, b]$ and $\alpha$ is continuous. Then

$$
\left| \int_ {a} ^ {b} f (x) d \alpha (x) \right| \leq \int_ {a} ^ {b} | f (x) | d v _ {\alpha} (x),
$$

where $v_{\alpha}(x)$ denotes the variation of $\alpha$ on $[a, x]$ , $a \leq x \leq b$ .

1.3.1. Calculate $\int_{-1}^{2} x d\alpha(x)$ , where

$$
\alpha (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x = - 1, \\ 1 & \text {i f} - 1 <   x <   2, \\ - 1 & \text {i f} 2 \leq x \leq 3. \end{array} \right.
$$

1.3.2. Suppose $f$ is of bounded variation on $[0, 2\pi]$ and $f(0) = f(2\pi)$ . Show that each of the integrals

$$
\int_ {0} ^ {2 \pi} f (x) \cos n x d x \quad \text {a n d} \quad \int_ {0} ^ {2 \pi} f (x) \sin n x d x
$$

is not greater than $V(f; 0, 2\pi) / n$ in absolute value.

1.3.3. Suppose $f$ and $g$ are continuous on $[a, b]$ and $\alpha$ is of bounded variation, and define

$$
\beta (x) = \int_ {a} ^ {x} f (x) d \alpha (x), \quad a \leq x \leq b.
$$

Prove that

$$
\int_ {a} ^ {b} g (x) d \beta (x) = \int_ {a} ^ {b} g (x) f (x) d \alpha (x).
$$

1.3.4. Let $\{x_{n}\}$ be a sequence of distinct points in $(0,1)$ , suppose that $c_{n} > 0$ , $\sum_{n=1}^{\infty} c_{n} < \infty$ , and define

$$
\alpha (x) = \sum_ {n = 1} ^ {\infty} c _ {n} \rho (x - x _ {n}),
$$

where the function $\pmb{\rho}$ is given by

$$
\rho (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x <   0, \\ 1 & \text {i f} x \geq 0. \end{array} \right.
$$

Prove that if $f$ is continuous on $[0,1]$ , then

$$
\int_ {0} ^ {1} f d \alpha = \sum_ {n = 1} ^ {\infty} c _ {n} f (x _ {n}).
$$

1.3.5. Suppose that $\alpha$ is a continuous function of bounded variation on $[a, b]$ such that for every $f$ continuous on $[a, b]$ ,

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = 0.
$$

Show that $\alpha$ is constant on $[a,b]$ .

1.3.6. Let $\alpha$ be monotonically increasing on $[0, \pi]$ and such that

$$
\int_ {0} ^ {\pi} \sin x d \alpha (x) = \alpha (\pi) - \alpha (0).
$$

Show that

$$
\alpha (x) = \left\{ \begin{array}{l l} \alpha (0) & \text {i f} x \in [ 0, n / 2), \\ \alpha (\pi) & \text {i f} x \in (\pi / 2, \pi ]. \end{array} \right.
$$

1.3.7. Find a function $\alpha$ monotonically increasing on $[0, 1]$ and such that

$$
\int_ {0} ^ {1} f (x) d \alpha (x) = \frac {f (0) + f (1)}{2}
$$

for every $f$ continuous on $[0,1]$ .

1.3.8. Find a function $f$ continuous on $[a, b]$ and such that

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = \alpha (b) - \alpha (a)
$$

for every $\alpha$ monotonically increasing on $[a,b]$ .

1.3.9. Assume that $\alpha$ is of bounded variation on $[a, b]$ and the functions $f_n, n = 1, 2, \ldots$ , are Riemann-Stieltjes integrable with respect to $\alpha$ over $[a, b]$ . Prove that if $\{f_n\}$ converges uniformly on $[a, b]$ to $f$ , then $f$ is Riemann-Stieltjes integrable and

$$
\int_ {u} ^ {b} f (x) d \alpha (x) = \lim  _ {n \rightarrow \infty} \int_ {u} ^ {b} f _ {n} (x) d \alpha (x).
$$

1.3.10. Calculate

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} n x (1 - x ^ {2}) ^ {n} d x.
$$

1.3.11. For $\alpha$ of bounded variation on $[0, 1]$ , find

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} x ^ {n} d \alpha (x).
$$

1.3.12. Suppose that $\{\alpha_{n}\}$ is a sequence of functions whose total variations are uniformly bounded on $[a, b]$ , that is, there is a positive $M$ such that $V(\alpha_{n}; a, b) \leq M$ for all $n$ . Prove that if $\{\alpha_{n}\}$ is pointwise convergent to $\alpha$ on $[a, b]$ , then for every $f$ continuous on $[a, b]$ ,

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (x) d \alpha_ {n} (x) = \int_ {a} ^ {b} f (x) d \alpha (x).
$$

1.3.13. Suppose that $\{\alpha_{n}\}$ is a sequence of functions whose total variations are uniformly bounded on $[a, b]$ , and that $\{\alpha_{n}\}$ is pointwise convergent to $\alpha$ on $[a, b]$ . Suppose also that $\{f_{n}\}$ is a sequence of continuous functions uniformly convergent on $[a, b]$ to $f$ . Prove that

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f _ {n} (x) d \alpha_ {n} (x) = \int_ {a} ^ {b} f (x) d \alpha (x).
$$

1.3.14. Prove the following Helly selection theorem. Let $\{\alpha_{n}\}$ be a sequence of functions defined on $[a, b]$ such that $|\alpha_{n}(a)| \leq M$ and $V(\alpha_{n}; a, b) \leq M$ for $n \in \mathbb{N}$ . Then $\{\alpha_{n}\}$ contains a subsequence $\{\alpha_{n_{k}}\}$ convergent to a function $\alpha$ of bounded variation on $[a, b]$ , and for every continuous function $f$ ,

$$
\lim  _ {k \rightarrow \infty} \int_ {a} ^ {b} f (x) d \alpha_ {n _ {k}} (x) = \int_ {a} ^ {b} f (x) d \alpha (x).
$$

1.3.15. Prove the following theorem of Helly which generalizes the result in 1.3.12. Let $f$ be continuous and $\alpha$ of bounded variation on $[a, b]$ . If the sequence $\{\alpha_n\}$ of functions of uniformly bounded variation converges to $\alpha$ on a set $A$ dense in $[a, b]$ and such that $a, b \in A$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (x) d \alpha_ {n} (x) = \int_ {a} ^ {b} f (x) d \alpha (x).
$$

1.3.16. Prove the second mean value theorem. Suppose $f$ is monotonic and $\alpha$ is continuous and of bounded variation on $[a, b]$ . Then there is a point $c \in [a, b]$ such that

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \alpha (x) = f (a) \int_ {a} ^ {c} d \alpha (x) + f (b) \int_ {c} ^ {b} d \alpha (x) \\ = f (a) (\alpha (c) - \alpha (a)) + f (b) (\alpha (b) - \alpha (c)). \\ \end{array}
$$

1.3.17. Prove the following Bonnet forms of the second mean value theorem.

# 1.3. Further Properties ...

(a) If $f$ is a positive increasing function on $[a, b]$ and $\alpha$ is a continuous function of bounded variation on $[a, b]$ , then there is a point $c \in [a, b]$ such that

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f (b) \int_ {c} ^ {b} d \alpha (x) = f (b) (\alpha (b) - \alpha (c)).
$$

(b) If $f$ is a positive decreasing function on $[a, b]$ and $\alpha$ is a continuous function of bounded variation on $[a, b]$ , then there is a point $c \in [a, b]$ such that

$$
\int_ {a} ^ {b} f (x) d \alpha (x) - f (a) \int_ {a} ^ {c} d \alpha (x) - f (a) (\alpha (c) - \alpha (a)).
$$

1.3.18. For $0 < a < b$ , find

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} \frac {\sin (n x)}{x} d x.
$$

1.3.19. For $x > 0$ , prove that

(a) if $F(x) = \int_{x}^{x + 1}\sin (t^{2})dt$ , then $|F(x)|\leq 1 / x$   
(b) if $F(x) = \int_{x}^{x + 1}\sin (e^{t})dt$ , then $|F(x)|\leq 2 / (e^x)$ .

1.3.20. Show that if the functions $f, \alpha_{1}, \alpha_{2}$ are continuous and of bounded variation on $[a, b]$ , then

$$
\int_ {\alpha} ^ {b} f (x) d \left(\alpha_ {1} (x) \alpha_ {2} (x)\right) = \int_ {\alpha} ^ {b} f (x) \alpha_ {1} (x) d \alpha_ {2} (x) + \int_ {\alpha} ^ {b} f (x) \alpha_ {2} (x) d \alpha_ {1} (x).
$$

1.3.21. Show that if $f$ is continuous and of bounded variation on $[a, b]$ , then for a positive integer $n$ ,

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \left(\left(f (x)\right) ^ {n}\right) = n \int_ {a} ^ {b} (f (x)) ^ {n} d f (x) \\ = \frac {n}{n + 1} ((f (b)) ^ {n + 1} - (f (a)) ^ {n + 1}). \\ \end{array}
$$

1.3.22. Suppose that $\pmb{f}$ is continuous on [0,1]. Find the following limits:

(a) $\lim_{n\to \infty}\left(n\int_0^1 x^n f(x)dx\right),$   
(b) $\lim_{n\to \infty}\left(n\int_0^1 e^{-nx}f(x)dx\right),$

(c)

$$
\lim  _ {n \rightarrow \infty} \frac {\int_ {0} ^ {1} x ^ {n} f (x) d x}{\int_ {0} ^ {1} x ^ {n} e ^ {x ^ {2}} d x},
$$

(d) $\lim_{n\to \infty}\left(\sqrt{n}\int_0^1 f(x)\sin^{2n}(2\pi x)dx\right),$

(e)

$$
\lim  _ {n \rightarrow \infty} \frac {\int_ {0} ^ {1} f (x) \sin^ {2 n} (2 \pi x) d x}{\int_ {0} ^ {1} e ^ {x ^ {2}} \sin^ {2 n} (2 \pi x) d x}.
$$

1.3.23. Prove the following monotone convergence theorem for the Riemann integral. If $\{f_n\}$ is a decreasing sequence of Riemann integrable functions on $[a,b]$ which converges on $[a,b]$ to a Riemann integrable function $f$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f _ {n} (x) d x = \int_ {a} ^ {b} f (x) d x.
$$

1.3.24. Prove the following monotone convergence theorem for the lower Riemann integral. If $\{f_n\}$ is a decreasing sequence of bounded functions on $[a,b]$ , and if $\lim_{n\to \infty}f_n(x) = 0$ for $x\in [a,b]$ , then

$$
\lim  _ {n \rightarrow \infty} \underline {{\int_ {a} ^ {b}}} f _ {n} (x) d x = 0.
$$

1.3.25. Prove the following Arzelà theorem. If $\{f_n\}$ is a sequence of Riemann integrable functions on $[a, b]$ which converges on $[a, b]$ to a Riemann integrable function $f$ , and if there is a constant $M > 0$ such that $|f_n(x)| \leq M$ for all $x \in [a, b]$ and all $n \in \mathbb{N}$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f _ {n} (x) d x = \int_ {a} ^ {b} f (x) d x.
$$

1.3.26. Prove the following Fatou lemma for Riemann integrals. If $\{f_n\}$ is a sequence of nonnegative Riemann integrable functions on $[a, b]$ which converges on $[a, b]$ to a Riemann integrable function $f$ , then

$$
\int_ {a} ^ {b} f (x) d x \leq \lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f _ {n} (x) d x.
$$

# 1.4. Proper Integrals

1.4.1. For $n \in \mathbb{N}$ , calculate

(a) $\int_0^1\frac{|x - 1|}{|x - 2| + |x - 3|} dx,$

(b) $\int_0^{\frac{\pi}{2}}\sin^n xdx,\int_0^{\frac{\pi}{2}}\cos^n xdx,$

(c) $\int_{\frac{1}{c}}^{c}|\ln x|dx,$

(d) $\int_0^\pi \frac{x\sin x}{1 + \cos^2x} dx,$

(e) $\int_0^{\frac{\pi}{4}}\tan^{2n}xdx,$

f)

(g) $\int_0^{\frac{\pi}{2}}\frac{\sin^n x}{\sin^n x + \cos^n x} dx.$

1.4.2. For $n \in \mathbb{N}$ , use the integral $\int_0^1 (1 - x^2)^n dx$ to calculate

$$
\frac {1}{1} \binom {n} {0} - \frac {1}{3} \binom {n} {1} + \frac {1}{5} \binom {n} {2} - \dots + (- 1) ^ {n} \frac {1}{2 n + 1} \binom {n} {n}.
$$

1.4.3. Suppose that a function $f$ has an indefinite integral (or antiderivative) on an interval $I$ ; that is, there is a differentiable function $F$ such that $F'(x) = f(x)$ for $x \in I$ . Show that if a one-sided limit of $f$ at $x_0 \in I$ exists and is equal to $a$ , then $f(x_0) = a$ .

1.4.4. Let $f$ be defined by

$$
f (x) = \left\{ \begin{array}{l l} \sin \frac {1}{x} & \text {i f} x \neq 0, \\ c & \text {i f} x = 0, \end{array} \right.
$$

where $c \in [-1, 1]$ . For which values of $c$ does there exist an antiderivative of $f$ ?

1.4.5. Let $x_{n} = 1 / \sqrt{n}$ for $n \in \mathbb{N}$ . Construct a function $f$ continuous on $(0,1]$ and such that $f \geq 0$ on $[x_{2k}, x_{2k-1}]$ , $f \leq 0$ on $[x_{2k+1}, x_{2k}]$ and $F(x_{2k-1}) - F(x_{2k}) = F(x_{2k+1}) - F(x_{2k}) = 1 / k$ , where $F$ is an antiderivative of $f$ . Extend the function $f$ to $[0,1]$ by setting $f(0) = 0$ . Prove that $f$ has an antiderivative on $[0,1]$ , but $|f|$ does not.

1.4.6. Suppose $f$ is continuous on $[0, 1]$ . Show that

$$
\int_ {0} ^ {\pi} x f (\sin x) d x = \frac {\pi}{2} \int_ {0} ^ {\pi} f (\sin x) d x.
$$

Using this equality, compute

$$
\int_ {0} ^ {\pi} \frac {x \sin^ {2 n} x}{\sin^ {2 n} x + \cos^ {2 n} x} d x, \quad n \in \mathbb {N}.
$$

1.4.7. Assume that $f$ is continuous on $[-a, a]$ , $a > 0$ . Show that

(a)

$$
\int_ {- a} ^ {a} f (x) d x = 2 \int_ {0} ^ {a} f (x) d x, \quad \text {i f} f \text {i s e v e n},
$$

(b)

$$
\int_ {a} ^ {a} f (x) d x = 0, \quad \text {i f} f \text {i s o d d}.
$$

1.4.8. Let $f: \mathbb{R} \to \mathbb{R}$ be continuous and periodic with period $T > 0$ . Prove that for every real $a$ ,

$$
\int_ {a} ^ {a + T} f (x) d x = \int_ {0} ^ {T} f (x) d x.
$$

1.4.9. Let $f: \mathbb{R} \to \mathbb{R}$ be continuous and periodic with period $T > 0$ . Prove that for every $a < b$ ,

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (n x) d x = \frac {b - a}{T} \int_ {0} ^ {T} f (x) d x.
$$

1.4.10. Suppose that $f \in C([-1,1])$ . Find the following limits:

(a) $\lim_{n\to \infty}\frac{1}{n}\int_{0}^{n}f(\sin x)dx,$   
(b) $\lim_{n\to \infty}\frac{1}{n}\int_0^n f(|\sin x|)dx,$   
(c) $\lim_{n\to \infty}\int_0^1 xf(\sin (2\pi nx))dx.$

1.4.11. For $f \in C([a, b])$ , find the following limits:

(a) $\lim_{n\to \infty}\int_{a}^{b}f(x)\cos (nx)dx,\quad \lim_{n\to \infty}\int_{a}^{b}f(x)\sin (nx)dx,$   
(b) $\lim_{n\to \infty}\int_{a}^{b}f(x)\sin^{2}(nx)dx.$

1.4.12. Suppose $f \in C([0, \infty))$ and set

$$
a _ {n} = \int_ {0} ^ {1} f (n + x) d x \quad \text {f o r} \quad n = 0, 1, \dots
$$

Suppose also that $\lim_{n\to \infty}a_n = a$ . Find the limit $\lim_{n\to \infty}\int_0^1 f(nx)dx$ .

1.4.13. For a function $f$ positive and continuous on $[0, 1]$ , compute

$$
\int_ {0} ^ {1} \frac {f (x)}{f (x) + f (1 - x)} d x.
$$

1.4.14. Show that, if $f$ is continuous and even on $[-a, a]$ , $a > 0$ , then

$$
\int_ {- a} ^ {a} \frac {f (x)}{1 + e ^ {x}} d x = \int_ {0} ^ {a} f (x) d x.
$$

1.4.15. Show that if $f$ is nonnegative and continuous on $[a, b]$ and

$$
\int_ {a} ^ {b} f (x) d x = 0,
$$

then $f$ is identically zero on $[a, b]$ .

1.4.16. Show that if $f$ is continuous on $[a, b]$ and for each $\alpha, \beta, a \leq \alpha < \beta \leq b$ ,

$$
\int_ {a} ^ {\beta} f (x) d x = 0,
$$

then $\pmb{f}$ is identically zero on $[a, b]$ .

1.4.17. Let $f$ be continuous on $[a, b]$ and such that

$$
\int_ {a} ^ {b} f (x) g (x) d x = 0
$$

for every function $g$ continuous on $[a, b]$ . Show that $f$ is identically zero on $[a, b]$ .

1.4.18. Let $f$ be continuous on $[a, b]$ and let

$$
\int_ {a} ^ {b} f (x) g (x) d x = 0
$$

for every function $g$ continuous on $[a, b]$ and such that $g(a) = g(b) = 0$ . Show that $f$ is identically zero on $[a, b]$ .

1.4.19. Suppose that $f$ is continuous on $\mathbb{R}$ . Show that

(a) if $\int_{-x}^{x}f(t)dt = 0$ for every $x\in \mathbb{R}$ , then $f$ is an odd function,

(b) if $\int_{-x}^{x} f(t) dt = 2\int_{0}^{x} f(t) dt$ for every $x \in \mathbb{R}$ , then $f$ is an even function,

(c) given $T > 0$ , if $\int_{x}^{x + T} f(t) dt = \int_{0}^{T} f(t) dt$ for every $x \in \mathbb{R}$ , then $f$ is periodic with period $T > 0$ .

# 1.4.20. Compute

(a) $\lim_{n\to \infty}\left(n^{4}\int_{n}^{n + 1}\frac{xdx}{x^{5} + 1}\right),$   
(b) $\lim_{n\to \infty}\left(n^{3}\int_{n}^{2n}\frac{xdx}{x^{5} + 1}\right),$   
(c) $\lim_{n\to \infty}\int_{1}^{2}\ln \left(x + \frac{x^5}{n}\right)dx,$   
(d) $\lim_{n\to \infty}\left(\frac{1}{3\pi}\int_{\pi}^{2\pi}\frac{xdx}{\arctan(nx)}\right)^n.$

1.4.21. Find the following limits:

(a) $\lim_{R\to \infty}\int_{0}^{\pi /2}e^{-R\sin t}dt,$   
(b) $\lim_{n\to \infty}\int_0^\pi \sqrt[n]{x}\sin xdx,$   
(c) $\lim_{n\to \infty}\int_{0}^{\pi /2}\frac{\sin^{n}x}{\sqrt{1 + x}} dx.$

1.4.22. For a function $f$ continuous on $[0, 1]$ , find

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} f (x ^ {n}) d x.
$$

1.4.23. Show that, if $f$ is Riemann integrable on $[a,b]$ , then there is $\theta \in [a,b]$ such that

$$
\int_ {a} ^ {\theta} f (t) d t = \int_ {\theta} ^ {b} f (t) d t.
$$

1.4.24. Let $f$ be continuous on $[a, b]$ and let

$$
\int_ {a} ^ {b} f (x) d x = 0.
$$

Show that there is $\theta \in (a,b)$ such that

$$
\int_ {a} ^ {\theta} f (x) d x = f (\theta).
$$

1.4.25. Let $f \in C([a, b])$ , $a > 0$ , and let

$$
\int_ {a} ^ {b} f (x) d x = 0.
$$

Show that there is $\theta \in (a,b)$ such that

$$
\int_ {a} ^ {\theta} f (x) d x = \theta f (\theta).
$$

1.4.26. Suppose $f, g \in C([a, b])$ . Show that there is $\theta \in (a, b)$ such that

$$
g (\theta) \int_ {a} ^ {b} f (x) d x = f (\theta) \int_ {a} ^ {b} g (x) d x.
$$

1.4.27. Suppose $f, g \in C([a, b])$ . Show that there is $\theta \in (a, b)$ such that

$$
g (\theta) \int_ {a} ^ {\theta} f (x) d x = f (\theta) \int_ {\theta} ^ {b} g (x) d x.
$$

1.4.28. Suppose $f$ and $g$ are positive and continuous on $[a, b]$ . Show that there is $\theta \in (a, b)$ such that

$$
\frac {f (\theta)}{\int_ {a} ^ {\theta} f (x) d x} - \frac {g (\theta)}{\int_ {\theta} ^ {b} g (x) d x} = 1.
$$

1.4.29. Let $f$ be positive and continuous on [0,1]. Prove that for every $n \in \mathbb{N}$ there is $\theta(n)$ such that

$$
\frac {1}{n} \int_ {0} ^ {1} f (x) d x = \int_ {0} ^ {\theta (n)} f (x) d x + \int_ {1 - \theta (n)} ^ {1} f (x) d x.
$$

Find the limit $\lim_{n\to \infty}(n\theta (n))$

1.4.30. Let $f \in C^{1}([0,1])$ . Show that there is a $\theta \in (0,1)$ such that

$$
\int_ {0} ^ {1} f (x) d x = f (0) + \frac {1}{2} f ^ {\prime} (\theta).
$$

1.4.31. Let $f \in C^2([0,1])$ . Show that there is a $\theta \in (0,1)$ such that

$$
\int_ {0} ^ {1} f (x) d x = f (0) + \frac {1}{2} f ^ {\prime} (0) + \frac {1}{6} f ^ {\prime \prime} (\theta).
$$

1.4.32. Suppose $f \in C^{1}([0,1])$ and $f'(0) \neq 0$ . For $x \in (0,1]$ , let $\theta(x)$ be such that

$$
\int_ {0} ^ {x} f (t) d t = f (\theta (x)) x.
$$

Find the limit

$$
\lim  _ {x \rightarrow 0 ^ {+}} \frac {\theta (x)}{x}.
$$

1.4.33. Suppose $f$ is continuous, nonnegative and strictly increasing on $[a, b]$ . For $p > 0$ , let $\theta(p)$ denote the unique number such that

$$
(f (\theta (p)) ^ {p} = \frac {1}{b - a} \int_ {a} ^ {b} (f (x)) ^ {p} d x.
$$

Find $\lim_{p\to \infty}\theta (p)$

1.4.34. Suppose $f$ is continuous on $[a, b]$ and such that

$$
\int_ {a} ^ {b} x ^ {n} f (x) d x = 0
$$

for $n = 0,1,\ldots$ . Prove that $f$ is identically zero on $[a,b]$ .

1.4.35. Suppose $f$ is continuous on $[a, b]$ and such that

$$
\int_ {a} ^ {b} x ^ {n} f (x) d x = 0
$$

for $n = 0,1,\ldots ,N$ . Prove that $f$ has at least $N + 1$ zeros in $[a,b]$ .

1.4.36. Suppose that $f \in C([-a, a])$ , $a > 0$ . Show that

(a) if

$$
\int_ {- a} ^ {a} x ^ {2 n} f (x) d x = 0 \quad \text {f o r} n = 0, 1, \dots ,
$$

then $f$ is odd on $[-a, a]$ ,

(b) if

$$
\int_ {- a} ^ {a} x ^ {2 n + 1} f (x) d x = 0 \quad \text {f o r} n = 0, 1, \dots ,
$$

then $f$ is even on $[-a, a]$ .

1.4.37. For $f$ continuous on $\mathbb{R}$ , find

$$
\lim  _ {h \rightarrow 0} \frac {1}{h} \int_ {a} ^ {b} (f (x + h) - f (x)) d x.
$$

1.4.38. For $f$ continuous on $\mathbb{R}$ and $a < b$ , define

$$
g (x) = \int_ {a} ^ {b} f (x + t) d t.
$$

Find the derivative of $g$ .

1.4.39. Find the following limits:

(a) $\lim_{x\to \infty}\frac{1}{\sqrt{x}}\int_{1}^{x}\ln \left(1 + \frac{1}{\sqrt{t}}\right)dt,$   
(b) $\lim_{x\to 0}x\int_{x}^{1}\frac{\cos t}{t^2} dt,$   
(c) $\lim_{x\to 0^{+}}\frac{\int_{0}^{x^2}\sin{\sqrt{t}}dt}{x^3},$   
(d) $\lim_{x\to \infty}\left(\frac{1}{x^a}\int_0^x\ln \frac{P(t)}{Q(t)} dt\right)$ , where $a > 1$ , and $P$ and $Q$ are polynomials positive on $\mathbb{R}_+$ .

1.4.40. Find the following limits:

(a) $\lim_{x\to \infty}\left(\frac{1}{\ln x}\int_{0}^{x}\frac{1}{\sqrt[6]{1 + t^5}} dt\right),$   
(b) $\lim_{x\to 0}\left(\frac{1}{x}\int_{0}^{x}(1 + \sin t)^{\frac{1}{i}}dt\right),$   
(c) $\lim_{x\to 0^{+}}\left(\frac{1}{x^2}\int_{0}^{x}t^{1 + t}dt\right),$   
(d) $\lim_{x\to \infty}\left(\int_0^x e^{t^2}dt\right)^{1 / (x^2)}.$

1.4.41. Show that if $f$ is continuous on $[0, 1]$ , then

$$
\lim  _ {p \rightarrow \infty} \left(\int_ {0} ^ {1} | f (x) | ^ {p} d x\right) ^ {1 / p} = \max  _ {x \in [ 0, 1 ]} | f (x) |.
$$

1.4.42. Suppose that a real-valued function $f(x, y)$ is continuous on a rectangle $\mathbf{R} = [a, b] \times [c, d]$ . Show that

$$
I (y) = \int_ {a} ^ {b} f (x, y) d x
$$

is continuous on $[c,d]$

1.4.43. Suppose that a real-valued function $f(x, y)$ defined on a rectangle $\mathbf{R} = [a, b] \times [c, d]$ is Riemann integrable over $[a, b]$ for each $y \in [c, d]$ , and the partial derivative $\frac{\partial f}{\partial y}$ is continuous on $\mathbf{R}$ . Prove that

$$
\frac {d}{d y} \int_ {a} ^ {b} f (x, y) d x = \int_ {a} ^ {b} \frac {\partial f}{\partial y} (x, y) d x.
$$

1.4.44. Let $f$ be positive and continuous on $[0, 1]$ . Find

$$
\lim  _ {p \rightarrow 0} \left(\int_ {0} ^ {1} (f (x)) ^ {p} d x\right) ^ {1 / p}.
$$

1.4.45. Let $f$ be positive and continuous on [0, 1]. Find

$$
\lim  _ {p \rightarrow - \infty} \left(\int_ {0} ^ {1} (f (x)) ^ {p} d x\right) ^ {1 / p}.
$$

1.4.46. Prove that for every positive integer $N$ the equation

$$
\int_ {0} ^ {x} e ^ {- t} \left(1 + \frac {t}{1 !} + \frac {t ^ {2}}{2 !} + \dots + \frac {t ^ {2 N}}{(2 N) !}\right) d t = N
$$

has a solution in the interval $(N, 2N)$ .

1.4.47. Let $P$ be a polynomial of degree $n$ such that

$$
\int_ {0} ^ {1} x ^ {k} P (x) d x = 0 \quad \text {f o r} \quad k = 1, 2 \dots , n.
$$

Prove that

$$
\int_ {0} ^ {1} (P (x)) ^ {2} d x = (n + 1) ^ {2} \left(\int_ {0} ^ {1} P (x) d x\right) ^ {2}.
$$

1.4.48. Show that if $f$ is continuous on $\mathbf{R} = [a, b] \times [c, d]$ , then

$$
\int_ {c} ^ {d} \left(\int_ {a} ^ {b} f (x, y) d x\right) d y = \int_ {a} ^ {b} \left(\int_ {c} ^ {d} f (x, y) d y\right) d x.
$$

1.4.49. Prove that for $0 < a < b$ ,

$$
\int_ {0} ^ {1} \frac {x ^ {b} - x ^ {a}}{\ln x} d x = \ln \frac {1 + b}{1 + a}.
$$

# 1.5. Improper Integrals

Assume that $f$ is defined on $[a, \infty)$ and is Riemann integrable over any finite interval $[a, b]$ . Then we define

$$
\int_ {a} ^ {\infty} f (x) d x = \lim  _ {b \rightarrow \infty} \int_ {a} ^ {b} f (x) d x,
$$

provided that this limit exists and is finite. In this case we say that the improper integral on the left converges; otherwise, we say that it

diverges. The improper integral $\int_{-\infty}^{a} f(x) dx$ is defined analogously. The integral $\int_{-\infty}^{+\infty} f(x) dx$ is defined by

$$
\int_ {- \infty} ^ {+ \infty} f (x) d x = \int_ {- \infty} ^ {a} f (x) d x + \int_ {a} ^ {+ \infty} f (x) d x
$$

provided that both improper integrals on the right converge. The definition does not depend on the choice of $\pmb{a}$ .

For $f$ defined on $[a, b)$ and Riemann integrable over each closed subinterval of $[a, b)$ , the improper integral $\int_{a}^{b} f(x) dx$ is defined as

$$
\int_ {a} ^ {b} f (x) d x = \lim  _ {\eta \rightarrow 0 ^ {+}} \int_ {a} ^ {b - \eta} f (x) d x,
$$

provided the limit is finite. If $f$ is defined on $(a, b]$ and Riemann integrable over each closed subinterval of $(a, b]$ , the improper integral $\int_{a}^{b} f(x) dx$ is defined in a similar way.

1.5.1. For $n \in \mathbb{N}$ and positive $a$ , calculate

(a) $\int_0^{2\pi}\frac{dx}{\sin^4x + \cos^4x},$

(b) $\int_0^{\pi /2}\ln (\sin x)dx,$

(c) $\int_0^1 x^n (1 - x)^\alpha dx,\alpha > - 1,$

(d) $\int_0^1 (-\ln x)^n dx,$

(e) $\int_0^n\frac{1 - (1 - x / n)^n}{x} dx,$

(f) $\int_0^1 x^n\ln^n xdx,$

(g) $\int_0^\infty \frac{dx}{(1 + x^2)^n},$

(h) $\int_{1}^{\infty}\frac{dx}{x^{2}\sqrt{x^{2} - 1}},$

(i) $\int_0^\infty \frac{\ln x}{x^2 + a^2} dx,$

(j) $\int_0^\infty \frac{\ln x}{(x^2 + a^2)^2} dx,$

(k) $\int_0^\pi \ln (1 + \cos x)dx,$

(1) $\int_0^\infty \ln \left(x + \frac{1}{x}\right)\frac{dx}{1 + x^2}.$

1.5.2. For $0 < \alpha < 1$ , define

$$
f _ {\alpha} (x) = \left[ \frac {\alpha}{x} \right] - \alpha \left[ \frac {1}{x} \right], \quad 0 <   x <   1.
$$

Show that

$$
\int_ {0} ^ {1} f _ {\alpha} (x) d x = \alpha \ln \alpha .
$$

1.5.3. Suppose $f$ is monotone on the interval $(0, 1)$ and the improper integral $\int_0^1 f(x) dx$ exists. Show that

$$
\lim  _ {n \rightarrow \infty} \frac {f \left(\frac {1}{n}\right) + f \left(\frac {2}{n}\right) + \cdots + f \left(\frac {n - 1}{n}\right)}{n} = \int_ {0} ^ {1} f (x) d x.
$$

1.5.4. Suppose $f$ is monotone on the interval $(0, 1)$ and one of the limits $\lim_{x \to 0^+} f(x)$ or $\lim_{x \to 1^-} f(x)$ is finite. Show that if

$$
\lim  _ {n \rightarrow \infty} \frac {f \left(\frac {1}{n}\right) + f \left(\frac {2}{n}\right) + \cdots + f \left(\frac {n - 1}{n}\right)}{n}
$$

exists as a finite limit, then the improper integral $\int_0^1 f(x)dx$ exists.

1.5.5. Show by example that in the preceding problem the assumption that one of the one-sided limits is finite cannot be omitted.

1.5.6. Using the result in 1.5.3, find

(a) $\lim_{n\to \infty}\frac{\sqrt[n]{n!}}{n},$   
(b) $\lim_{n\to \infty}\sqrt[n]{\sin{\frac{\pi}{2n}}\sin{\frac{2\pi}{2n}}\dots \sin{\frac{(n - 1)\pi}{2n}}},$   
(c) $\lim_{n\to \infty}\left(\frac{1}{n}\sum_{k = 1}^{n}(\ln k)^2 -\left(\frac{1}{n}\sum_{k = 1}^{n}\ln k\right)^2\right).$

1.5.7. Suppose that the function $f: (0, 1] \to \mathbb{R}$ is monotone and for some $\alpha \in \mathbb{R}$ the improper integral $\int_0^1 x^\alpha f(x) dx$ exists. Show that $\lim_{x \to 0^+} x^{\alpha + 1} f(x) = 0$ .

1.5.8. Verify whether the following improper integrals converge or diverge:

(a) $\int_{2}^{\infty}\frac{dx}{x\ln x},$

(b) $\int_0^\infty \frac{\sin^2x}{1 + x^2} dx,$

(c) $\int_0^1 (-\ln x)^a dx,\quad a\in \mathbb{R},$

(d) $\int_0^1\frac{dx}{x^a(-\ln x)^b}, a,b\in \mathbb{R},$

(e) $\int_0^\infty \frac{x dx}{1 + x^2\sin^2x}.$

1.5.9. Suppose that $f$ and $g$ are positive on $[a, \infty)$ and $\int_{a}^{\infty} g(x) dx$ diverges. Show that at least one of the integrals

$$
\int_ {a} ^ {\infty} f (x) g (x) d x, \quad \int_ {a} ^ {\infty} \frac {g (x)}{f (x)} d x
$$

diverges.

1.5.10. Prove the following Cauchy theorem. In order that the improper integral $\int_{a}^{\infty} f(x) dx$ converge, a necessary and sufficient condition is that, given $\varepsilon > 0$ , there is $a_0 > a$ such that for $a_2 > a_1 > a_0$ ,

$$
\left| \int_ {a _ {1}} ^ {a _ {2}} f (x) d x \right| <   \varepsilon .
$$

1.5.11. Show that the improper integral $\int_{a}^{\infty} f(x) dx$ converges if and only if for every increasing sequence $\{a_n\}$ , $a_n > a$ , diverging to infinity the series

$$
\sum_ {n = 1} ^ {\infty} \int_ {a _ {n - 1}} ^ {a _ {n}} f (x) d x, \quad \text {w h e r e} \quad a _ {0} = a, \tag {1}
$$

converges. Moreover, in the case of convergence,

$$
\int_ {a} ^ {\infty} f (x) d x = \sum_ {n = 1} ^ {\infty} \int_ {a _ {n - 1}} ^ {a _ {n}} f (x) d x.
$$

Show also that if $f$ is nonnegative, a sufficient condition for the convergence of the improper integral is that there is an increasing sequence $\{a_n\}$ , $a_n > a$ , diverging to infinity for which the series (1) converges.

1.5.12. For positive $a$ , study the convergence of the integral

$$
\int_ {0} ^ {\infty} \frac {d x}{1 + x ^ {a} \sin^ {2} x}.
$$

1.5.13. Suppose $f$ is positive on $[0, \infty)$ and $\int_0^\infty f(x) dx$ exists. Must $f(x)$ tend to zero as $x \to \infty$ ?

1.5.14. Suppose $f$ is positive, differentiable on $[a, \infty)$ , and $|f'(x)| \leq 2$ for $x \geq a$ . Does the convergence of $\int_{a}^{\infty} f(x) dx$ imply that $f(x)$ tends to zero as $x \to \infty$ ?

1.5.15. Prove that if $f$ is uniformly continuous on $[a, \infty)$ and the improper integral $\int_{a}^{\infty} f(x) dx$ converges, then $\lim_{x \to \infty} f(x) = 0$ .

1.5.16. Assume that $f:[0,\infty) \to [0,\infty)$ is monotone decreasing. Prove that if

$$
\int_ {0} ^ {\infty} f (x) d x <   \infty ,
$$

then $\lim_{x\to \infty}xf(x) = 0$ . Show by example that the converse does not hold; that is, the condition $\lim_{x\to \infty}xf(x) = 0$ does not imply the convergence of $\int_0^\infty f(x)dx$ .

1.5.17. Assume that $f:[1,\infty) \to (e,\infty)$ is monotone increasing and $\int_{1}^{\infty} \frac{dx}{f(x)} = \infty$ .

(a) Prove that also $\int_{1}^{\infty}\frac{dx}{x\ln f(x)} = \infty .$

(b) Give an example of a function $f$ satisfying the above assumption for which $\int_{1}^{\infty} \frac{dx}{x \ln f(x) \ln(\ln f(x))}$ converges.

1.5.18. Let $f$ be a continuous function on $[0, \infty)$ such that

$$
\lim  _ {x \rightarrow \infty} \left(f (x) + \int_ {0} ^ {x} f (t) d t\right)
$$

exists as a finite limit. Prove that $\lim_{x\to \infty}f(x) = 0$

1.5.19. Let $f$ be a nonnegative and continuous function on $[0, \infty)$ and

$$
\int_ {0} ^ {\infty} f (x) d x <   \infty .
$$

Prove that

$$
\lim  _ {n \rightarrow \infty} \frac {1}{n} \int_ {0} ^ {n} x f (x) d x = 0.
$$

1.5.20. Suppose that $f$ is uniformly continuous on $[a, \infty)$ and the integrals $\int_{a}^{x} f(t) dt$ are uniformly bounded; that is, there is $M > 0$ such that

$$
\left| \int_ {a} ^ {x} f (t) d t \right| \leq M \quad \text {f o r} \quad x \in [ a, \infty).
$$

Show that $f$ is bounded on $[a, \infty)$ .

1.5.21. Prove that if $\int_{a}^{\infty}(f(x))^{2}dx$ and $\int_{a}^{\infty}(f''(x))^{2}dx$ converge, then $\int_{a}^{\infty}(f'(x))^{2}dx$ also converges.

1.5.22. Prove the following Abel test for convergence of improper integrals. Assume that the functions $f$ and $g$ defined on $[a, \infty)$ satisfy the following conditions:

(1) the improper integral $\int_{a}^{\infty} f(x) dx$ exists,   
(2) $g$ is monotone and bounded on $\{a,\infty\}$ ,

Then the improper integral

$$
\int_ {a} ^ {\infty} f (x) g (x) d x
$$

converges.

1.5.23. Prove the following Dirichlet test for convergence of improper integrals. Assume that the functions $f$ and $g$ defined on $[a, \infty)$ satisfy the following conditions:

(1) $f$ is properly integrable on each interval $[a, b]$ , $b > a$ , and the integrals $\int_{a}^{b} f(x) dx$ are uniformly bounded, that is, there exists $C > 0$ such that

$$
\left| \int_ {a} ^ {b} f (x) d x \right| \leq C \quad \text {f o r a l l} \quad b > a.
$$

(2) $g$ is monotone and $\lim_{x \to \infty} g(x) = 0$ .

Then the improper integral

$$
\int_ {a} ^ {\infty} f (x) g (x) d x
$$

converges.

1.5.24. For $\alpha > 0$ , study the convergence of the following integrals:

(a) $\int_{1}^{\infty}\frac{\sin x}{x^{\alpha}} dx,$

(b) $\int_{1}^{\infty}\frac{|\sin x|}{x} dx,$

(c) $\int_{1}^{\infty}\sin (x^{2})dx,$

(d) $\int_{1}^{\infty}e^{\sin x}\frac{\sin(2x)}{x^{\alpha}} dx,$

(e) $\int_{1}^{\infty}\ln^{\alpha}x\frac{\sin x}{x} dx.$

1.5.25. Assume that $f:[a,\infty) \to \mathbb{R}$ is continuous and periodic with period $T > 0$ , and $g:[a,\infty) \to \mathbb{R}$ is monotonic and $\lim_{x \to \infty} g(x) = 0$ . Prove that if $\int_{a}^{a + T} f(x) dx = 0$ , then the integral $\int_{a}^{\infty} f(x) g(x) dx$ converges. Moreover, prove that if $\int_{a}^{a + T} f(x) dx \neq 0$ , then the improper integral $\int_{a}^{\infty} f(x) g(x) dx$ converges if and only if $\int_{a}^{\infty} g(x) dx$ converges.

1.5.26. Use the result in the previous problem to study the convergence of the following integrals:

(a) $\int_0^\infty \frac{\sin(\sin x)}{x} e^{\cos x}dx,$

(b) $\int_0^\infty \frac{\sin(\sin x)}{x} e^{\sin x}dx.$

1.5.27. For $\alpha > 0$ , study the convergence of the integral

$$
\int_ {0} ^ {\infty} \frac {\sin x}{x ^ {\alpha} + \sin x} d x.
$$

1.5.28. Show that if $\int_{a}^{\infty}xf(x)dx$ , $a > 0$ , exists, then also $\int_{a}^{\infty}f(x)dx$ exists.

1.5.29. Assume that $f$ is monotone on $[0, \infty)$ and the improper integral $\int_0^\infty f(x) dx$ exists. Show that

$$
\lim  _ {h \rightarrow 0 ^ {+}} h \sum_ {n = 1} ^ {\infty} f (n h) = \int_ {0} ^ {\infty} f (x) d x.
$$

Use this result to find

$$
\lim  _ {h \rightarrow 0 ^ {+}} \sum_ {n = 1} ^ {\infty} \frac {h}{1 + h ^ {2} n ^ {2}}.
$$

1.5.30. For $\alpha > 0$ , set

$$
\Gamma (\alpha) = \int_ {0} ^ {\infty} e ^ {- x} x ^ {\alpha - 1} d x.
$$

Show that $\Gamma(\alpha)$ is finite for all positive $\alpha$ . $(\Gamma(\alpha)$ is called Euler's gamma function).

1.5.31. Use the result in 1.5.29 to show that for $\alpha >0$

$$
\Gamma (\alpha) = \lim  _ {n \rightarrow \infty} \frac {n ^ {\alpha - 1} n !}{\alpha (\alpha + 1) \dots (\alpha + n - 1)}.
$$

1.5.32. Use the formula given in the previous problem to show that for $\alpha > 0$ ,

$$
\Gamma (\alpha) = \frac {e ^ {- \gamma \alpha}}{\alpha} \prod_ {n = 1} ^ {\infty} e ^ {\alpha / k} \left(1 + \frac {\alpha}{k}\right) ^ {- 1},
$$

where $\gamma$ is Euler's constant (see, e.g., I, 2.1.41).

1.5.33. Show that

$$
\int_ {0} ^ {\infty} \frac {\sin x}{x} d x = \frac {\pi}{2}.
$$

1.5.34. Prove that

$$
\int_ {0} ^ {\infty} e ^ {- x ^ {2}} d x = \frac {\sqrt {\pi}}{2}.
$$

1.5.35. Let $f(x, y)$ be a function defined on $[a, \infty) \times A$ , where $A \subset \mathbb{R}$ . We say that the integral $\int_{a}^{\infty} f(x, y) dx$ converges uniformly on $A$ if, given $\varepsilon > 0$ , there is $a_0 > a$ such that

$$
\left| \int_ {a} ^ {\infty} f (x, y) d x - \int_ {a} ^ {b} f (x, y) d x \right| <   \varepsilon
$$

for all $b > a_0$ and $y \in \mathbf{A}$ . Show that if there is a function $\varphi(x)$ such that

$$
| f (x, y) | \leq \varphi (x) \quad \text {f o r} \quad x \in [ a, \infty), y \in A
$$

and $\int_{a}^{\infty}\varphi (x)dx$ converges, then the improper integral $\int_{a}^{\infty}f(x,y)dx$ converges uniformly on A.

1.5.36. Prove the following test for uniform convergence of an improper integral. Suppose that $\int_{a}^{\infty} f(x, y) dx$ converges uniformly on

A and $g(x, y)$ is monotonic with respect to $x$ and is bounded on $[a, \infty) \times A$ . Then

$$
\int_ {a} ^ {\infty} f (x, y) g (x, y) d x
$$

converges uniformly on $\mathbf{A}$

1.5.37. Conclude the following test from the previous problem. If the improper integral $\int_{a}^{\infty} f(x) dx$ converges and $g(x, y)$ is monotonic with respect to $x$ and is bounded on $[a, \infty) \times \mathbf{A}$ , then

$$
\int_ {a} ^ {\infty} f (x) g (x, y) d x
$$

converges uniformly on $\mathbf{A}$

1.5.38. Suppose that there is a positive $C$ such that

$$
\left| \int_ {a} ^ {b} f (x, y) d x \right| \leq C \quad \text {f o r a l l} \quad b > a, y \in A,
$$

and $g(x, y)$ is monotonic with respect to $x$ and $g(x, y)$ converges to zero as $x \to \infty$ uniformly on $\mathbf{A}$ . Then

$$
\int_ {a} ^ {\infty} f (x, y) g (x, y) d x
$$

converges uniformly on $\mathbf{A}$

1.5.39. Study the uniform convergence of the following improper integrals:

(a) $\int_0^\infty \frac{\sin ax}{x} dx,\quad a\in [a_0,\infty),a_0 > 0,$   
(b) $\int_0^\infty \frac{\sin ax}{x} dx,\quad a\in [0,\infty),$   
(c) $\int_0^\infty \frac{\cos a(x^2 + 1)}{x^2 + 1} dx,\quad a\in \mathbb{R},$   
(d) $\int_0^\infty e^{-ax}\cos x^2 dx,\quad a\in (0,\infty).$

1.5.40. Assume that the improper integral $\int_{a}^{\infty} f(x, y) dx$ converges uniformly on $A$ . Prove that if $f(x, y)$ converges to $\varphi(x)$ as $y \to$

$y_0$ uniformly on every interval $[a,b]$ , then the integral $\int_{a}^{\infty}\varphi (x)dx$ converges and

$$
\lim  _ {y \rightarrow y _ {0}} \int_ {a} ^ {\infty} f (x, y) d x = \int_ {a} ^ {\infty} \varphi (x) d x.
$$

1.5.41. Consider the example

$$
f _ {n} (x) = \left\{ \begin{array}{l l} \frac {n}{x ^ {3}} e ^ {- \frac {n}{2 x ^ {2}}} & \text {f o r} \quad x > 0, \\ 0 & \text {f o r} \quad x = 0, \end{array} \right.
$$

to show that the assumption of the uniform convergence of the improper integral $\int_{a}^{\infty} f(x, y) dx$ cannot be dropped from the theorem of 1.5.40.

1.5.42. Show that

(a) $\lim_{y\to 0^{+}}\int_{0}^{\infty}\frac{\sin x}{x} e^{-yx}dx = \frac{\pi}{2},$   
(b) $\lim_{y\to \infty}\int_{0}^{\infty}\sin x^{2}\arctan (yx)dx = \frac{\pi}{2}\int_{0}^{\infty}\sin x^{2}dx,$   
(c) $\lim_{n\to \infty}\int_{0}^{\infty}\frac{\sin x}{x}\left(1 + \frac{x}{n}\right)^{-n}dx = \int_{0}^{\infty}\frac{\sin x}{x} e^{-x}dx,$   
(d) $\lim_{y\to \infty}\int_{1}^{\infty}\frac{\arctan(yx)}{x^2\sqrt{x^2 - 1}} dx = \frac{\pi}{2},$   
(e) $\lim_{y\to 0^{+}}\int_{0}^{\infty}y^{2}\sin xe^{-y^{2}x^{2}}dx = 0.$

1.5.43. Suppose that a real-valued function $f(x, y)$ is continuous on $[a, \infty) \times [c, d]$ and the improper integral $\int_{a}^{\infty} f(x, y) dx$ converges uniformly on $[c, d]$ . Then the function

$$
I (y) = \int_ {a} ^ {\infty} f (x, y) d x
$$

is continuous on $[c,d]$ .

1.5.44. Suppose that a real-valued function $f(x, y)$ defined on $\mathbf{R} = [a, \infty) \times [c, d]$ is such that $\int_{a}^{\infty} f(x, y) dx$ converges for every $y \in [c, d]$ and $\frac{\partial f}{\partial y}$ is continuous on $\mathbf{R}$ . Suppose also that the integral $\int_{a}^{\infty} \frac{\partial f}{\partial y}(x, y) dx$ converges uniformly on $[c, d]$ . Prove that

$$
\frac {d}{d y} \int_ {a} ^ {\infty} f (x, y) d x = \int_ {a} ^ {\infty} \frac {\partial f}{\partial y} (x, y) d x.
$$

1.5.45. Use the result in 1.5.44 to calculate

(a) $\int_0^\infty e^{-ax^2}x^{2n}dx,\quad a > 0,n\in \mathbb{N},$   
(b) $\int_0^\infty \frac{dx}{(a + x^2)^{n + 1}},\quad a > 0,$ n E N,   
(c) $\int_0^\infty \frac{\sin(ax)}{x} e^{-x}dx,\quad a\in \mathbb{R},$   
(d) $\int_0^\infty \frac{1 - \cos(ax)}{x} e^{-x}dx,\quad a\in \mathbb{R}.$

1.5.46. Prove that

(a) $\int_{-\infty}^{\infty}e^{-x^2 /2}\cos (yx)dx = \sqrt{2\pi} e^{-y^2 /2},\quad y\in \mathbb{R},$   
(b) $\int_0^\infty e^{-x - y / x}\frac{dx}{\sqrt{x}} = \sqrt{\pi} e^{-2\sqrt{y}},\quad y > 0.$

1.5.47. Show that if a real-valued function $f(x, y)$ is continuous on $[a, \infty) \times [c, d]$ and the improper integral

$$
\int_ {a} ^ {\infty} f (x, y) d x
$$

converges uniformly on $[c,d]$ , then

$$
\int_ {c} ^ {d} \left(\int_ {a} ^ {\infty} f (x, y) d x\right) d y = \int_ {a} ^ {\infty} \left(\int_ {c} ^ {d} f (x, y) d y\right) d x.
$$

1.5.48. Use the above theorem to find

(a) $\int_0^\infty \frac{e^{-bx} - e^{-ax}}{x} dx,\quad a,b > 0,$   
(b) $\int_0^\infty \frac{\cos(bx) - \cos(ax)}{x^2} dx,\quad 0 <   a <   b.$

1.5.49. Assume that $f \in C^{1}([0, \infty))$ , $f'$ is monotonic on $[0, \infty)$ and $\lim_{x \to \infty} f(x) = l$ exists as a finite limit. Show that for $a, b > 0$ ,

$$
\int_ {0} ^ {\infty} \frac {f (b x) - f (a x)}{x} d x = (l - f (0)) \ln \frac {b}{a}.
$$

1.5.50. Let $f(x, y)$ be continuous on $[a, \infty) \times [c, \infty)$ and suppose that

(1) the improper integral $\int_{a}^{\infty} f(x, y) dx$ converges uniformly on each interval $[c, d]$ ,

(2) the improper integral $\int_{c}^{\infty} f(x, y) dy$ converges uniformly on each interval $[a, b]$ ,   
(3) the improper integrals $\int_{a}^{\infty}|f(x,y)|dx$ and $\int_{c}^{\infty}|f(x,y)|dy$ converge for $y\geq c$ and $x\geq a$ , respectively,   
(4) at least one of the improper integrals

$$
\begin{array}{l} \int_ {a} ^ {\infty} \left(\int_ {c} ^ {\infty} | f (x, y) | d y\right) d x, \quad \int_ {c} ^ {\infty} \left(\int_ {a} ^ {\infty} | f (x, y) | d x\right) d y \\ \text {c o n v e r g e s .} \end{array}
$$

Then

$$
\int_ {a} ^ {\infty} \left(\int_ {c} ^ {\infty} f (x, y) d y\right) d x = \int_ {c} ^ {\infty} \left(\int_ {a} ^ {\infty} f (x, y) d x\right) d y,
$$

and both integrals converge.

# 1.5.51. Prove that

$$
\int_ {0} ^ {\infty} \cos x ^ {2} d x = \frac {1}{2} \int_ {0} ^ {\infty} \frac {\cos x}{\sqrt {x}} d x = \frac {1}{2} \sqrt {\frac {\pi}{2}}
$$

and

$$
\int_ {0} ^ {\infty} \sin x ^ {2} d x = \frac {1}{2} \int_ {0} ^ {\infty} \frac {\sin x}{\sqrt {x}} d x = \frac {1}{2} \sqrt {\frac {\pi}{2}}.
$$

(The improper integrals $\int_0^\infty \cos x^2 dx$ and $\int_0^\infty \cos x^2 dx$ are called Fresnel's integrals.)

1.5.52. Suppose that $f(x, y)$ is defined on $[a, b) \times A$ and for each $y \in A$ , $f$ is Riemann integrable over each interval $[a, b - \eta]$ , where $0 < \eta < b - a$ . Suppose also that $f(x, y)$ converges to $\varphi(x)$ as $y \to y_0$ uniformly on each of these intervals. If the improper integral $\int_{a}^{b} f(x, y) dx$ converges uniformly on $A$ (that is, given $\varepsilon > 0$ , there is $\eta_0$ such that

$$
\left| \int_ {b - \eta} ^ {b} f (x, y) d x \right| <   \varepsilon
$$

for all $0 < \eta < \eta_0 < b - a$ and $y \in \mathbf{A}$ ) then

$$
\lim  _ {y \rightarrow y _ {0}} \int_ {a} ^ {b} f (x, y) d x = \int_ {a} ^ {b} \varphi (x) d x.
$$

1.5.53. Suppose that $f_n : [a, b) \to \mathbb{R}$ , $n \in \mathbb{N}$ , is Riemann integrable on each interval $[a, b - \eta]$ , where $0 < \eta < b - a$ , and $f_n(x)$ converges to $\varphi(x)$ as $n \to \infty$ uniformly on each of these intervals. Suppose also that there is a positive function $f(x)$ such that $|f_n(x)| \leq f(x)$ for all $x \in [a, b)$ and $n \in \mathbb{N}$ , and the integral $\int_{a}^{b} f(x) dx$ exists. Then

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f _ {n} (x) d x = \int_ {a} ^ {b} \varphi (x) d x.
$$

1.5.54. Show that

$$
\lim  _ {y \rightarrow \infty} \int_ {0} ^ {\infty} e ^ {- x ^ {y}} d x = 1.
$$

1.5.55. Show that

$$
\Gamma (x) = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {n} \left(1 - \frac {t}{n}\right) ^ {n} t ^ {x - 1} d t, \quad x > 0.
$$

1.5.56. Prove that

$$
\int_ {0} ^ {\infty} \left(\frac {\sin x}{x}\right) ^ {2} d x = \frac {\pi}{2}.
$$

1.5.57. Show that for $0 < a < 1$ ,

$$
\int_ {0} ^ {\infty} \frac {x ^ {a - 1}}{1 + x} d x = \frac {1}{a} + \sum_ {k = 1} ^ {\infty} (- 1) ^ {k} \left(\frac {1}{a + k} + \frac {1}{a - k}\right) = \frac {\pi}{\sin \pi a}.
$$

1.5.58. Show that for $a, b \in (0, 1)$ ,

$$
\int_ {0} ^ {\infty} \frac {x ^ {a - 1} - x ^ {b - 1}}{1 - x} d x = \pi (\cot \pi a - \cot \pi b).
$$

1.5.59. Express the integrand as a power series to find

(a) $\int_0^1\frac{\ln(1 - x)}{x} dx,$

(b) $\int_0^1\frac{\ln(1 + x)}{x} dx,$

(c) $\int_0^1\frac{\ln(1 + x^2)}{x} dx,$

(d) $\int_0^1\frac{\ln x\ln^2(1 - x)}{x} dx.$

1.5.60. Use the identity

$$
\frac {1}{2 n + 1} = \int_ {0} ^ {1} x ^ {2 n} d x, \quad n = 0, 1, 2, \dots ,
$$

to find the sum of the series

(a) $\sum_{n = 0}^{\infty}(-1)^{n}\left(\frac{1}{4n + 1} +\frac{1}{4n + 3}\right),$   
(b) $1 + \sum_{n = 1}^{\infty}\left(\frac{1}{8n + 1} -\frac{1}{8n - 1}\right).$

1.5.61. Use the result in 1.5.1(c) to determine the sum of the series

(a) $\sum_{n = 0}^{\infty}\frac{1}{(2n + 1)(2n + 2)(2n + 3)},$   
(b) $\sum_{n = 1}^{\infty}\frac{1}{2n(2n + 1)(2n + 2)}.$

1.5.62. Show that

$$
\int_ {0} ^ {1} x ^ {- x} d x = \sum_ {n = 1} ^ {\infty} n ^ {- n}.
$$

1.5.63. Find the value of the integral $\int_0^\infty \frac{xe^{-x}}{1 + e^{-x}} dx$ .

1.5.64. For positive $a$ and $b$ , define

$$
B (a, b) = \int_ {0} ^ {1} x ^ {a - 1} (1 - x) ^ {b - 1} d x.
$$

$(B(a,b)$ is called Euler's beta function.) Prove that for $0 < a < 1$

$$
B (a, 1 - a) = \int_ {0} ^ {\infty} \frac {y ^ {a - 1}}{1 + y} d y = \frac {\pi}{\sin a \pi}.
$$

1.5.65. Show that for $a, b > 0$ ,

$$
B (a, b) = \frac {\Gamma (a) \Gamma (b)}{\Gamma (a + b)},
$$

and conclude that

$$
\Gamma (a) \Gamma (1 - a) = \frac {\pi}{\sin \pi a}
$$

for $0 < a < 1$ .

1.5.66. Find $\lim_{a\to 0^{+}}a\Gamma (a)$

1.5.67. Calculate $\int_0^1\ln \Gamma (a)da$

1.5.68. For $a > 0$ , derive the following duplication formula:

$$
2 ^ {2 a} \frac {\Gamma (a) \Gamma (a + 1 / 2)}{\Gamma (2 a)} = 2 \sqrt {\pi}.
$$

1.5.69. Verify the following equalities:

(a) $\int_0^{\pi /2}\tan^a xdx = \frac{\pi}{2\cos(\pi a / 2)},\quad |a| <   1,$   
(b) $\int_0^\pi \frac{dx}{\sqrt{3 - \cos x}} = \frac{1}{4\sqrt{\pi}} (\Gamma (1 / 4))^2,$   
(c) $\int_0^{\pi /2}\sin^{a - 1}xdx = 2^{a - 2}B(a / 2,a / 2),\quad a > 0.$

1.5.70. Derive the following Stirling formula:

$$
\lim  _ {n \rightarrow \infty} \frac {n !}{\sqrt {2 \pi} n ^ {n + 1 / 2} e ^ {- n}} = 1.
$$

1.5.71. Show that for $a > 0$ ,

$$
\frac {\Gamma^ {\prime} (a)}{\Gamma (a)} = \int_ {0} ^ {\infty} \left(e ^ {- x} - \frac {1}{(1 + x) ^ {a}}\right) \frac {d x}{x}.
$$

1.5.72. Find the following limits:

(a) $\lim_{x\to \infty}\frac{\sqrt{x}\Gamma(x + 1 / 2)}{\Gamma(x + 1)},$   
(b) $\lim_{x\to \infty}x^{a}B(a,x),\quad a > 0.$

# 1.6. Integral Inequalities

1.6.1. Prove the following Schwarz inequality. If $f$ and $g$ are Riemann integrable on $[a, b]$ , then

$$
\left(\int_ {a} ^ {b} f (x) g (x) d x\right) ^ {2} \leq \int_ {a} ^ {b} f ^ {2} (x) d x \int_ {a} ^ {b} g ^ {2} (x) d x.
$$

Moreover, if $f$ and $g$ are continuous on $[a, b]$ , then the equality holds if and only if there are $\lambda_1$ and $\lambda_2$ such that $|\lambda_1| + |\lambda_2| > 0$ and $\lambda_1 f(x) = \lambda_2 g(x)$ for $x \in [a, b]$ .

1.6.2. Show that if $f$ is Riemann integrable on $[a, b]$ , then

$$
\left(\int_ {a} ^ {b} f (x) \sin x d x\right) ^ {2} + \left(\int_ {a} ^ {b} f (x) \cos x d x\right) ^ {2} \leq (b - a) \int_ {a} ^ {b} f ^ {2} (x) d x.
$$

1.6.3. Show that if $f$ is positive and Riemann integrable on $[a, b]$ , then

$$
(b - a) ^ {2} \leq \int_ {a} ^ {b} f (x) d x \int_ {a} ^ {b} \frac {d x}{f (x)}.
$$

Moreover, if $0 < m \leq f(x) \leq M$ , then

$$
\int_ {a} ^ {b} f (x) d x \int_ {a} ^ {b} \frac {d x}{f (x)} \leq \frac {(m + M) ^ {2}}{4 m M} (b - a) ^ {2}.
$$

1.6.4. Let $f$ and $g$ be Riemann integrable on $[a, b]$ and let

$$
m _ {1} \leq f (x) \leq M _ {1} \quad \text {a n d} \quad m _ {2} \leq g (x) \leq M _ {2}, \quad x \in [ a, b ].
$$

Show that

$$
\begin{array}{l} \left| \frac {1}{b - a} \int_ {a} ^ {b} f (x) g (x) d x - \frac {1}{(b - a) ^ {2}} \int_ {a} ^ {b} f (x) d x \int_ {a} ^ {b} g (x) d x \right| \\ \leq \frac {1}{4} (M _ {1} - m _ {1}) (M _ {2} - m _ {2}). \\ \end{array}
$$

1.6.5. Suppose $f \in C^{1}([a, b])$ , $f(a) = f(b) = 0$ and $\int_{a}^{b} f^{2}(x) dx = 1$ . Show that

$$
\int_ {a} ^ {b} x f (x) f ^ {\prime} (x) d x = - \frac {1}{2}
$$

and

$$
\frac {1}{4} \leq \int_ {a} ^ {b} \left(f ^ {\prime} (x)\right) ^ {2} d x \int_ {a} ^ {b} x ^ {2} f ^ {2} (x) d x.
$$

1.6.6. Find

$$
\min  _ {f \in A} \int_ {0} ^ {1} (1 + x ^ {2}) f ^ {2} (x) d x,
$$

where

$$
\mathcal {A} = \left\{f \in C ([ 0, 1 ]): \int_ {0} ^ {1} f (x) d x = 1 \right\},
$$

and find a function for which the minimum is attained.

1.6.7. Assume that $f:[a,b] \to [m,M]$ and $\int_{a}^{b}f(x)dx = 0$ . Prove that

$$
\int_ {a} ^ {b} f ^ {2} (x) d x \leq - m M (b - a).
$$

1.6.8. Show that if $f$ is continuous on $[0, 1]$ , differentiable on $(0, 1)$ , $f(0) = 0$ , and $0 < f'(x) \leq 1$ on $(0, 1)$ , then

$$
\left(\int_ {0} ^ {1} f (x) d x\right) ^ {2} \geq \int_ {0} ^ {1} (f (x)) ^ {3} d x.
$$

Show also that equality occurs if and only if $f(x) = x$ .

1.6.9. Let $f \in C([a, b])$ be monotonically increasing on $[a, b]$ . Show that for $x \in (a, b)$ ,

$$
\frac {1}{x - a} \int_ {a} ^ {x} f (t) d t \leq \frac {1}{b - a} \int_ {a} ^ {b} f (t) d t \leq \frac {1}{b - x} \int_ {x} ^ {b} f (t) d t.
$$

1.6.10. Prove the following Chebyshev inequality: If functions $f$ and $g$ are either both increasing or both decreasing on $[a, b]$ , then

$$
\frac {1}{b - a} \int_ {a} ^ {b} f (x) d x \frac {1}{b - a} \int_ {a} ^ {b} g (x) d x \leq \frac {1}{b - a} \int_ {a} ^ {b} f (x) g (x) d x.
$$

If one of the functions is increasing and the other decreasing, then the above inequality reverses.

1.6.11. Prove the following generalization of the Chebyshev inequality: Let $p$ be positive and Riemann integrable on $[a, b]$ . If the functions $f$ and $g$ are either both increasing or both decreasing on that interval, then

$$
\int_ {a} ^ {b} p (x) f (x) d x \int_ {a} ^ {b} p (x) g (x) d x \leq \int_ {a} ^ {b} p (x) d x \int_ {a} ^ {b} p (x) f (x) g (x) d x.
$$

If one of the functions is increasing and the other decreasing, then the above inequality reverses.

1.6.12. Assume that $f$ and $g$ are monotonically increasing on $[0, a]$ . Show that

$$
\int_ {0} ^ {a} f (x) g (x) d x \geq \int_ {0} ^ {a} f (a - x) g (x) d x.
$$

1.6.13. Let $q$ be positive and decreasing on $[a, b]$ , $a > 0$ . Show that

$$
\frac {\int_ {a} ^ {b} x q ^ {2} (x) d x}{\int_ {a} ^ {b} x q (x) d x} \leq \frac {\int_ {a} ^ {b} q ^ {2} (x) d x}{\int_ {a} ^ {b} q (x) d x}.
$$

1.6.14. Show that if $f$ is a convex function on $[a, b]$ , then

$$
f \left(\frac {a + b}{2}\right) (b - a) \leq \int_ {a} ^ {b} f (x) d x \leq \frac {f (a) + f (b)}{2} (b - a).
$$

1.6.15. Given positive real numbers $x$ and $y$ , let $A, G$ and $L$ be their arithmetic, geometric and logarithmic means, respectively (see, e.g., II, 2.5.41 for the definition of the logarithmic mean). Use the previous result to show that for $x \neq y$ , $A^L < G^A$ if both $x$ and $y$ are at least $e^{3/2}$ and $A^L > G^A$ if both $x$ and $y$ are at most $e^{3/2}$ .

1.6.16. Show that if $f \in C([a, b])$ is positive and strictly concave on $[a, b]$ , then

$$
\int_ {a} ^ {b} f (x) d x > \frac {1}{2} (b - a) \max  _ {x \in [ a, b ]} f (x).
$$

1.6.17. Suppose $f, g$ are continuously differentiable on $[0,b]$ , $f', g'$ are nonnegative on $[0,b]$ , and $f$ is nonconstant with $f(0) = 0$ . Then for $0 < a \leq b$ ,

$$
f (a) g (b) \leq \int_ {0} ^ {a} g (x) f ^ {\prime} (x) d x + \int_ {0} ^ {b} g ^ {\prime} (x) f (x) d x.
$$

The equality holds if and only if $a = b$ or $g$ is a constant function.

1.6.18. Suppose $f \in C^{1}([0,c])$ , $c > 0$ , is strictly increasing on $[0,c]$ and $f(0) = 0$ . Show that for $x \in [0,c]$ ,

$$
\int_ {0} ^ {x} f (t) d t + \int_ {0} ^ {f (x)} f ^ {- 1} (t) d t = x f (x),
$$

where $f^{-1}$ denotes the inverse of $f$ .

1.6.19. Use the result in the previous problem to prove the Young inequality. Under the assumption of 1.6.18,

$$
\int_ {0} ^ {a} f (t) d t + \int_ {0} ^ {b} f ^ {- 1} (t) d t \geq a b
$$

for any $a \in [0, c]$ and $b \in [0, f(c)]$ . Moreover, the equality holds if and only if $b = f(a)$ .

1.6.20. Show that for $a, b \geq 0$ ,

$$
(1 + a) \ln (1 + a) - (1 + a) + (e ^ {b} - b) \geq a b.
$$

1.6.21. Prove the following converse of the Young inequality: Suppose that $f$ and $g$ are continuously differentiable and strictly increasing on $[0, \infty)$ and such that $f(0) = g(0) = 0$ , $g^{-1}(x) \geq f(x)$ for $x \geq 0$ . If for positive $a$ and $b$

$$
a b \leq \int_ {0} ^ {a} f (x) d x + \int_ {0} ^ {b} g (x) d x,
$$

then $f$ and $g$ are inverse.

1.6.22. Let

$$
\mathcal {A} = \left\{f \in \mathcal {R} ([ 0, 1 ]): \int_ {0} ^ {1} f (x) d x = 3, \int_ {0} ^ {1} x f (x) d x = 2 \right\}.
$$

Find

$$
\min  _ {f \in \mathcal {A}} \int_ {0} ^ {1} f ^ {2} (x) d x
$$

and a function for which the minimum is attained.

1.6.23. Let

$$
\mathcal {A} = \left\{f \in C ^ {2} ([ 0, 1 ]): f (0) = f (1) = 0, f ^ {\prime} (0) = a \right\}.
$$

Find

$$
\min  _ {f \in A} \int_ {0} ^ {1} (f ^ {\prime \prime} (x)) ^ {2} d x
$$

and a function for which the minimum is attained.

1.6.24. Does there exist a function $f$ continuously differentiable on $[0, 2]$ and such that $f(0) = f(2) = 1$ , $|f'(x)| \leq 1$ for $x \in [0, 2]$ and $\left| \int_0^2 f(x) dx \right| \leq 1$ ?

1.6.25. Suppose $f$ is continuously differentiable on $[a, b]$ and $f(a) = f(b) = 0$ . Show that

$$
\max  _ {x \in [ a, b ]} | f ^ {\prime} (x) | \geq \frac {4}{(b - a) ^ {2}} \int_ {a} ^ {b} | f (x) | d x.
$$

1.6.26. Prove the following Hölder inequality: If functions $f_1, f_2, \ldots, f_n$ are nonnegative and Riemann integrable on $[a, b]$ , and positive real numbers $\alpha_1, \alpha_2, \ldots, \alpha_n$ satisfy $\sum_{i=1}^{n} \alpha_i = 1$ , then

$$
\int_ {a} ^ {b} \prod_ {i = 1} ^ {n} f _ {i} ^ {\alpha_ {i}} (x) d x \leq \prod_ {i = 1} ^ {n} \left(\int_ {a} ^ {b} f _ {i} (x) d x\right) ^ {\alpha_ {i}}.
$$

1.6.27. Suppose that $f$ and $g$ are nonnegative and Riemann integrable on $[a, b]$ . For $p \neq 0$ let $q$ be its conjugate, that is, $\frac{1}{p} + \frac{1}{q} = 1$ . Using the previous result, prove that

(a) if $p > 1$ , then

$$
\int_ {a} ^ {b} f (x) g (x) d x \leq \left(\int_ {a} ^ {b} f ^ {p} (x) d x\right) ^ {1 / p} \left(\int_ {a} ^ {b} g ^ {q} (x) d x\right) ^ {1 / q},
$$

(b) if $p < 0$ or $0 < p < 1$ , and $f, g$ are positive, then

$$
\int_ {a} ^ {b} f (x) g (x) d x \geq \left(\int_ {a} ^ {b} f ^ {p} (x) d x\right) ^ {1 / p} \left(\int_ {a} ^ {b} g ^ {q} (x) d x\right) ^ {1 / q}.
$$

1.6.28. Suppose that $f$ is continuous on $[0, 1]$ and there is $a > 0$ such that $0 \leq f(x) \leq a^{2/3}$ for $x \in [0, 1]$ . Show that if $\int_0^1 f(x) dx = a$ , then $\int_0^1 \sqrt{f(x)} dx \geq a^{2/3}$ .

1.6.29. Suppose that $f$ is Riemann integrable on $[a, b]$ and $m \leq f(x) \leq M$ . Prove that if $\varphi$ is continuous and convex on $[m, M]$ , then

$$
\varphi \left(\frac {1}{b - a} \int_ {a} ^ {b} f (x) d x\right) \leq \frac {1}{b - a} \int_ {a} ^ {b} \varphi (f (x)) d x.
$$

This inequality is called Jensen's inequality.

1.6.30. Prove the following generalization of the Jensen inequality stated in the last problem. Suppose that $f$ and $p$ are Riemann integrable on $[a, b]$ , $m \leq f(x) \leq M$ , $p(x) \geq 0$ and $\int_{a}^{b} p(x) dx > 0$ . If $\varphi$ is continuous and convex on $[m, M]$ , then

$$
\varphi \left(\frac {1}{\int_ {a} ^ {b} p (x) d x} \int_ {a} ^ {b} p (x) f (x) d x\right) \leq \frac {1}{\int_ {a} ^ {b} p (x) d x} \int_ {a} ^ {b} p (x) \varphi (f (x)) d x.
$$

1.6.31. Let $f$ be Riemann integrable on [0, 1] and $|f(x)| \leq 1$ , $x \in [0, 1]$ . Show that

$$
\int_ {0} ^ {1} \sqrt {1 - f ^ {2} (x)} d x \leq \sqrt {1 - \left(\int_ {0} ^ {1} f (x) d x\right) ^ {2}}.
$$

1.6.32. Let $f$ be nonnegative and decreasing on $[0, 1]$ . Prove that for nonnegative $a$ and $b$ ,

$$
\begin{array}{l} \left(1 - \left(\frac {a - b}{a + b + 1}\right) ^ {2}\right) \int_ {0} ^ {1} x ^ {2 a} f (x) d x \int_ {0} ^ {1} x ^ {2 b} f (x) d x \\ \geq \left(\int_ {0} ^ {1} x ^ {a + b} f (x) d x\right) ^ {2}. \\ \end{array}
$$

1.6.33. Let $f$ be nonnegative and increasing on $[0, 1]$ . Prove that for nonnegative $a$ and $b$ ,

$$
\begin{array}{l} \left(1 - \left(\frac {a - b}{a + b + 1}\right) ^ {2}\right) \int_ {0} ^ {1} x ^ {2 a} f (x) d x \int_ {0} ^ {1} x ^ {2 b} f (x) d x \\ \leq \left(\int_ {0} ^ {1} x ^ {a + b} f (x) d x\right) ^ {2}. \\ \end{array}
$$

1.6.34. Let $f$ be continuous on $[a, b]$ and put $f(x) = 0$ for $x \notin [a, b]$ . For $h > 0$ , we define $f_h$ by setting

$$
f _ {h} (x) = \frac {1}{2 h} \int_ {x - h} ^ {x + h} f (t) d t.
$$

Show that

$$
\int_ {a} ^ {b} | f _ {h} (x) | d x \leq \int_ {a} ^ {b} | f (x) | d x.
$$

1.6.35. Prove the Minkowski inequality for integrals. Assume that $f_1, f_2, \ldots, f_n$ are nonnegative and Riemann integrable on $[a, b]$ .

(a) If $k > 1$ , then

$$
\begin{array}{l} \left(\int_ {a} ^ {b} \left(f _ {1} (x) + \dots + f _ {n} (x)\right) ^ {k} d x\right) ^ {\frac {1}{k}} \\ \leq \left(\int_ {a} ^ {b} f _ {1} ^ {k} (x) d x\right) ^ {\frac {1}{k}} + \dots + \left(\int_ {a} ^ {b} f _ {n} ^ {k} (x) d x\right) ^ {\frac {1}{k}}. \\ \end{array}
$$

(b) If $0 < k < 1$ and $f, g$ are positive, then

$$
\begin{array}{l} \left(\int_ {a} ^ {b} \left(f _ {1} (x) + \dots + f _ {n} (x)\right) ^ {k} d x\right) ^ {\frac {1}{k}} \\ \geq \left(\int_ {a} ^ {b} f _ {1} ^ {k} (x) d x\right) ^ {\frac {1}{k}} + \dots + \left(\int_ {a} ^ {b} f _ {n} ^ {k} (x) d x\right) ^ {\frac {1}{k}}. \\ \end{array}
$$

1.6.36. Assume that $f_1, f_2, \ldots, f_n$ are nonnegative and Riemann integrable on $[a, b]$ .

(a) If $k > 1$ , then

$$
\int_ {a} ^ {b} \left(f _ {1} (x) + \dots + f _ {n} (x)\right) ^ {k} d x \geq \int_ {a} ^ {b} f _ {1} ^ {k} (x) d x + \dots + \int_ {a} ^ {b} f _ {n} ^ {k} (x) d x.
$$

(b) If $0 < k < 1$ , then

$$
\int_ {a} ^ {b} \left(f _ {1} (x) + \dots + f _ {n} (x)\right) ^ {k} d x \leq \int_ {a} ^ {b} f _ {1} ^ {k} (x) d x + \dots + \int_ {a} ^ {b} f _ {n} ^ {k} (x) d x.
$$

1.6.37. Prove the following inequality of Steffensen: If $g$ is Riemann integrable on $[a, b]$ and $0 \leq g(x) \leq 1$ for every $x \in [a, b]$ , and $f$ decreases on that interval, then

$$
\int_ {b - \lambda} ^ {b} f (x) d x \leq \int_ {a} ^ {b} f (x) g (x) d x \leq \int_ {a} ^ {a + \lambda} f (x) d x,
$$

where

$$
\lambda = \int_ {a} ^ {b} g (x) d x.
$$

1.6.38. Prove the following Bellman generalization of Steffensen's inequality: If $g$ is Riemann integrable on $[0, 1]$ and $0 \leq g(x) \leq 1$ for every $x \in [0, 1]$ , and $f$ is nonnegative and decreasing on that interval, then for $p \geq 1$

$$
\left(\int_ {0} ^ {1} f (x) g (x) d x\right) ^ {p} \leq \int_ {0} ^ {\lambda} (f (x)) ^ {p} d x,
$$

where

$$
\lambda = \left(\int_ {0} ^ {1} g (x) d x\right) ^ {p}.
$$

1.6.39. Using 1.6.38, show that if $g$ is Riemann integrable on $[a,b]$ , $0 \leq g(x) \leq 1$ for every $x \in [a,b]$ , and if $f$ is nonnegative and decreasing on that interval, then for $p > 1$

$$
\frac {1}{(b - a) ^ {p - 1}} \left(\int_ {a} ^ {b} f (x) g (x) d x\right) ^ {p} \leq \int_ {a} ^ {a + \lambda} (f (x)) ^ {p} d x,
$$

where

$$
\lambda = \frac {1}{(b - a) ^ {p - 1}} \left(\int_ {a} ^ {b} g (x) d x\right) ^ {p}.
$$

1.6.40. Prove the following variant of Steffensen's inequality due to R. Apéry. Let $f$ be a nonnegative and decreasing function on $[0, \infty)$ and let $g$ be a function defined on $[0, \infty)$ such that $0 \leq g(x) \leq A$ ( $A > 0$ ) with $\int_0^\infty g(x) dx < \infty$ . Then

$$
\int_ {0} ^ {\infty} f (x) g (x) d x \leq A \int_ {0} ^ {\lambda} f (x) d x,
$$

where

$$
\lambda = \frac {1}{A} \int_ {0} ^ {\infty} g (x) d x.
$$

1.6.41. Prove the following Bellman generalization of Steffensen's inequality. Let $f:[a,b] \to \mathbb{R}$ be a nonnegative decreasing function and let $g:[a,b] \to \mathbb{R}$ be a nonnegative and Riemann integrable function such that

$$
0 \leq g (x) \left(\int_ {a} ^ {b} g (t) d t\right) ^ {p - 1} \leq 1, \quad x \in [ a, b ].
$$

If $p \geq 1$ , then

$$
\left(\int_ {a} ^ {b} g (x) f (x) d x\right) ^ {p} \leq \int_ {a} ^ {a + \lambda} (f (x)) ^ {p} d x,
$$

where

$$
\lambda = \left(\int_ {a} ^ {b} g (x) d x\right) ^ {p}.
$$

Moreover, prove that if $0 < p \leq 1$ , then

$$
\left(\int_ {a} ^ {b} g (x) f (x) d x\right) ^ {p} \geq \int_ {b - \lambda} ^ {b} (f (x)) ^ {p} d x
$$

with $\lambda$ defined above.

1.6.42. Let $g_1$ and $g_2$ be functions integrable on $[a, b]$ such that for every $x \in [a, b]$

$$
\int_ {a} ^ {x} g _ {1} (t) d t \geq \int_ {a} ^ {x} g _ {2} (t) d t
$$

and

$$
\int_ {a} ^ {b} g _ {1} (t) d t = \int_ {a} ^ {b} g _ {2} (t) d t.
$$

Show that if $f$ is increasing on $[a, b]$ , then

$$
\int_ {a} ^ {b} f (t) g _ {1} (t) d t \leq \int_ {a} ^ {b} f (t) g _ {2} (t) d t,
$$

and if $f$ is decreasing on $[a, b]$ , then

$$
\int_ {a} ^ {b} f (t) g _ {1} (t) d t \geq \int_ {a} ^ {b} f (t) g _ {2} (t) d t.
$$

1.6.43. Use the Steffensen inequality to prove that if $f$ is continuously differentiable on $[a, b]$ and $m \leq f'(x) \leq M$ ( $m < M$ ) for $x \in [a, b]$ , then

$$
m + \frac {(M - m) \lambda^ {2}}{(b - a) ^ {2}} \leq \frac {f (b) - f (a)}{b - a} \leq M - \frac {(M - m) (b - a - \lambda) ^ {2}}{(b - a) ^ {2}},
$$

where

$$
\lambda = \frac {f (b) - f (a) - m (b - a)}{M - m}.
$$

1.6.44. Prove that if $f$ is continuously differentiable on $[a, b]$ and $m \leq f'(x) \leq M$ ( $m < M$ ) for $x \in [a, b]$ , then

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f (x) d x - \frac {f (a) + f (b)}{2} (b - a) \right| \\ \leq \frac {(f (b) - f (a) - m (b - a)) (M (b - a) - f (b) + f (a))}{2 (M - m)}. \\ \end{array}
$$

1.6.45. Prove the following Opial inequality: If $f$ is continuously differentiable on $[0, a]$ and $f(0) = 0$ , then

$$
\int_ {0} ^ {a} | f (x) f ^ {\prime} (x) | d x \leq \frac {a}{2} \int_ {0} ^ {a} \left(f ^ {\prime} (x)\right) ^ {2} d x.
$$

1.6.46. Prove the following generalization of Opial's inequality. If $f \in C^{n}([0, a])$ is such that $f(0) = f'(0) = \dots = f^{(n-1)}(0) = 0, n \geq 1$ , then

$$
\int_ {0} ^ {a} | f (x) f ^ {(n - 1)} (x) | d x \leq \frac {a ^ {n}}{2} \int_ {0} ^ {a} (f ^ {(n)} (x)) ^ {2} d x.
$$

1.6.47. Prove this generalization of Opial's inequality. If $f$ is continuously differentiable on $[0, a]$ , $f(0) = 0$ and $p \geq 0, q \geq 1$ , then

$$
\int_ {0} ^ {a} | f (x) | ^ {p} | f ^ {\prime} (x) | ^ {q} d x \leq \frac {q a ^ {p}}{p + q} \int_ {0} ^ {a} | f ^ {\prime} (x) | ^ {p + q} d x.
$$

1.6.48. Suppose $f \in C^{2n}([a, b])$ is such that $f^{(k)}(a) = f^{(k)}(b) = 0$ for $k = 0, 1, \ldots, n - 1$ . Prove that if $M = \max_{x \in [a, b]} |f^{(2n)}(x)|$ , then

$$
\left| \int_ {a} ^ {b} f (x) d x \right| \leq \frac {(n !) ^ {2} (b - a) ^ {2 n + 1}}{(2 n) ! (2 n + 1) !} M.
$$

# 1.7. Jordan Measure

For $a_i \leq b_i, i = 1,2,\ldots,p$ , the volume of the interval $\mathbf{R} = [a_1,b_1] \times [a_2,b_2] \times \cdots \times [a_p,b_p]$ is the number $|\mathbf{R}| = (b_1 - a_1)(b_2 - a_2) \cdots (b_p - a_p)$ . In the case $p = 1$ or $p = 2$ , the number $|\mathbf{R}|$ is called the length and the area of $\mathbf{R}$ , respectively. We say that two intervals are separate if they have at most boundary points in common. A union of finitely many intervals is called an elementary set. Any elementary set $\mathbf{E}$ can be expressed (in infinitely many ways) as a union of pairwise separate intervals $\mathbf{R}_1, \ldots, \mathbf{R}_n$ . Then the volume of the elementary set $\mathbf{E}$ is the number $|\mathbf{E}| = |\mathbf{R}_1| + \cdots + |\mathbf{R}_n|$ . The volume $|\mathbf{E}|$ does not depend on the choice of the $\mathbf{R}_i$ . For a nonempty set $\mathbf{A} \subset \mathbb{R}^p$ , we put $|\mathbf{A}|_* = \sup |\mathbf{E}|$ , where the supremum is taken over all elementary sets $\mathbf{E}$ contained in $\mathbf{A}$ . The number $|\mathbf{A}|_*$ is called the inner volume (or the Jordan inner measure) of $\mathbf{A}$ . If $\mathbf{A}$ is unbounded, its inner Jordan measure may be infinite. If $\mathbf{A}$ is bounded, then its outer volume (or the Jordan outer measure) is the number $|\mathbf{A}|^* = \inf |\mathbf{E}|$ , where the infimum is taken over all elementary sets $\mathbf{E}$ containing $\mathbf{A}$ . If $\mathbf{A}$ is unbounded, then $|\mathbf{A}|^* = \lim_{k\to\infty}|\mathbf{A} \cap \mathbf{R}_k|^*$ , where $\mathbf{R}_k = [-k,k] \times \cdots \times [-k,k] \subset \mathbb{R}^p$ . If $|\mathbf{A}|_* = |\mathbf{A}|^* = |\mathbf{A}|$ , we say that $\mathbf{A}$ has volume $|\mathbf{A}|$ (or is Jordan measurable and its Jordan measure is $|\mathbf{A}|$ ). In the case when $|\mathbf{A}| = 0$ , we say that $|a| = |a|_0 = |a|_1 = |a|_2 = |a|_3 = |a|_4 = |a|_5 = |a|_6 = |a|_7 = |a|_8 = |a|_9 = |a|_{10} = |a|_{11} = |a|_{12} = |a|_{13} = |a|_{14} = |a|_{15} = |a|_{16} = |a|_{17} = |a|_{18} = |a|_{19} = |a|_{20} = |a|_{21} = |a|_{22} = |a|_{23} = |a|_{24} = |a|_{25} = |a|_{26} = |a|_{27} = |a|_{28} = |a|_{29} = |a|_{30} = |a|_{31} = |a|_{32} = |a|_{33} = |a|_{34} = |a|_{35} = |a|_{36} = |a|_{37} = |a|_{38} = |a|_{39} = |a|_{40} = |a|_{41} = |a|_{42} = |a|_{43} = |a|_{44} = |a|_{45} = |a|_{46} = |a|_{47} = |a|_{48} = |a|_{49} = |a|_{50} = |a|_{51} = |a|_{52} = |a|_{53} = |a|_{54} = |a|_{55} = |a|_{56} = |a|_{57} = |a|_{58} = |a|_{59} = |a|_{60} = |a|_{61} = |a|_{62} = |a|_{63} = |a|_{64} = |a|_{65} = |a|_{66} = |a|_{67} = |a|_{68} = |a|_{69} = |a|_{70} = |a|_{71} = |a|_{72} = |a|_{73} = |a|_{74} = |a|_{75} = |a|_{76} = |a|_{77} = |a|_{78} = |a|_{79} = |a|_{80} = |a|_{81} = |a|_{82} = |a|_{83} = |a|_{84} = |a|_{85} = |a|_{86} = |a|_{87} = |a|_{88} = |a|_{89} = |a|_{90} = |a|_{91} = |a|_{92} = |a|_{93} = |a|_{94} = |a|_{95} = |a|_{96} = |a|_{97} = |a|_{98} = |a|_{99} = |\mathbf{A}|^*$ .

+∞ we assume additionally that $\mathbf{A} \cap \mathbf{R}$ is Jordan measurable for any interval $\mathbf{R}$ . Moreover, we assume that $|\varnothing| = 0$ .

1.7.1. Show that a bounded set $\mathbf{A}$ is Jordan measurable if and only if, given $\varepsilon > 0$ , there are two elementary sets $\mathbf{E}_1$ and $\mathbf{E}_2$ such that $\mathbf{E}_1 \subset \mathbf{A} \subset \mathbf{E}_2$ and $|\mathbf{E}_2| - |\mathbf{E}_1| < \varepsilon$ .

1.7.2. Show that if $\mathbf{A}_1, \ldots, \mathbf{A}_n$ are bounded, Jordan measurable and pairwise separate, that is, $\mathbf{A}_i^\circ \cap \mathbf{A}_j^\circ = \emptyset$ for $i \neq j$ , then

$$
\left| \mathbf {A} _ {1} \cup \dots \cup \mathbf {A} _ {n} \right| = \left| \mathbf {A} _ {1} \right| + \dots + \left| \mathbf {A} _ {n} \right|.
$$

1.7.3. Show that if $\mathbf{A}_1$ and $\mathbf{A}_2$ are Jordan measurable, then so are $\mathbf{A}_1 \cup \mathbf{A}_2$ and $\mathbf{A}_1 \cap \mathbf{A}_2$ , and

$$
\left| \mathbf {A} _ {1} \cup \mathbf {A} _ {2} \right| + \left| \mathbf {A} _ {1} \cap \mathbf {A} _ {2} \right| = \left| \mathbf {A} _ {1} \right| + \left| \mathbf {A} _ {2} \right|.
$$

1.7.4. Show that if $\mathbf{A}_1$ and $\mathbf{A}_2$ are Jordan measurable, $\mathbf{A}_1 \subset \mathbf{A}_2$ , and $|\mathbf{A}_1| < +\infty$ , then $\mathbf{A}_2 \setminus \mathbf{A}_1$ is Jordan measurable and $|\mathbf{A}_2 \setminus \mathbf{A}_1| = |\mathbf{A}_2| - |\mathbf{A}_1|$ .

1.7.5. Show that the set

$$
\mathbf {A} = \{(x, y) \in \mathbb {R} ^ {2}: x \in [ 0, 1 ], y \in [ 0, 1 ] \backslash \mathbb {Q} \}
$$

is not Jordan measurable.

1.7.6. Show that the set

$$
\mathbf {B} = \{(x, y) \in \mathbb {R} ^ {2}: x \in [ 0, 1 ], y \in [ 0, 1 ] \backslash \{1 / n: n \in \mathbb {N} \} \}
$$

is Jordan measurable.

1.7.7. Show that if $|\mathbf{B}|^* = 0$ , then for any bounded $\mathbf{A}$

$$
| \mathbf {A} \cup \mathbf {B} | _ {\bullet} = | \mathbf {A} | _ {\bullet}.
$$

Give an example to show that $|\mathbf{B}|_{*} = 0$ is not sufficient for this equality to hold.

1.7.8. Show that if $\mathbf{A}$ is Jordan measurable, then its interior and closure are Jordan measurable and

$$
| \mathbf {A} | = | \mathbf {A} ^ {\circ} | = | \overline {{\mathbf {A}}} |.
$$

1.7.9. Show that $\mathbf{A}$ is Jordan measurable if and only if the Jordan measure of its boundary $\partial \mathbf{A}$ is zero.

1.7.10. Prove that the assumption that $\mathbf{A}_1, \ldots, \mathbf{A}_n$ are bounded can be dropped from the assertion given in 1.7.2.

1.7.11. Let $\mathbf{C} \subset [0,1]$ denote the Cantor set (for the definition of the Cantor set see, e.g., the solution to II, 1.3.1). Show that $|\mathbf{C}| = 0$ .

1.7.12. Let $\mathbf{A}$ be a Cantor-like set defined as follows. Given $\alpha \in (0,1)$ , we remove from $[0,1]$ an open interval $\left(\frac{1}{2} -\frac{\alpha}{4},\frac{1}{2} +\frac{\alpha}{4}\right)$ and denote by $\mathbf{E}_1$ the union of the two remaining closed intervals. Next we remove the open middle intervals of length $\alpha /2^3$ of the two intervals constituting $\mathbf{E}_1$ and denote by $\mathbf{E}_2$ the union of the four remaining closed intervals. We repeat the process with each of the four intervals, removing the open middle intervals of length $\alpha /2^5$ . Continuing the process, we obtain the sequence $\{\mathbf{E}_n\}$ of sets, where $\mathbf{E}_n$ is the union of $2^n$ closed intervals, and we put $\mathbf{A} = \bigcap_{n = 1}^{\infty}\mathbf{E}_n$ . Show that $\mathbf{A}$ is not Jordan measurable.

1.7.13. Is $\mathbf{A} = \{1 + \frac{1}{n+1}, 2 + \frac{1}{n+1}, \dots : n \in \mathbb{N}\}$ a Jordan measurable subset of $\mathbb{R}$ ?

1.7.14. Let $\{r_k\}$ be the sequence of all rationals contained in $[0,1]$ and let $\mathbf{I}_k$ be an open interval centered at $r_k$ , $k \in \mathbb{N}$ , of length $1/2^{k+1}$ . Show that the set $\mathbf{A} = \bigcup_{k=1}^{\infty} \mathbf{I}_k$ is not Jordan measurable.

1.7.15. Give examples of nonmeasurable open sets and nonmeasurable closed sets.

1.7.16. Let $\mathbf{A} \subset [a, b]$ . If $\chi_{\mathbf{A}}$ is the characteristic function of $\mathbf{A}$ , then

$$
| \mathbf {A} | _ {*} = \underline {{\int_ {a} ^ {b}}} \chi_ {\mathbf {A}} (x) d x \quad \text {a n d} \quad | \mathbf {A} | ^ {*} = \overline {{\int_ {a} ^ {b}}} \chi_ {\mathbf {A}} (x) d x.
$$

1.7.17. For a nonnegative and bounded function $f$ on an interval $[a, b]$ , put $\mathbf{A}_f = \{(x, y) \in \mathbb{R}^2 : a \leq x \leq b, 0 \leq y \leq f(x)\}$ . Prove that

$$
\left| \mathrm {A} _ {f} \right| _ {*} = \underline {{\int_ {a} ^ {b}}} f (x) d x, \quad \text {a n d} \quad \left| \mathrm {A} _ {f} \right| ^ {*} = \overline {{\int_ {a} ^ {b}}} f (x) d x.
$$

1.7.18. Let $f$ be a bounded function on $[a, b]$ . For $\varepsilon > 0$ define

$$
\mathbf {J} _ {\varepsilon} = \{x \in [ a, b ], o _ {f} (x) \geq \varepsilon \},
$$

where $o_f(x)$ denotes the oscillation of $f$ at $x$ (see, e.g., II, 1.7.12). Prove that $f$ is Riemann integrable on $[a,b]$ if and only if $|\mathbf{J}_{\varepsilon}| = 0$ for every $\varepsilon > 0$ .

1.7.19. Show that a bounded set $\mathbf{A}$ is Jordan measurable if and only if there exist two sequences $\{\mathbf{B}_n\}$ and $\{\mathbf{C}_n\}$ of Jordan measurable sets such that $\mathbf{B}_n \subset \mathbf{A} \subset \mathbf{C}_n$ and $\lim_{n \to \infty} |\mathbf{B}_n| = \lim_{n \to \infty} |\mathbf{C}_n| = |\mathbf{A}|$ .

1.7.20. Show that the set

$$
\mathbf {A} = \left\{(x, y) \in \mathbb {R} ^ {2}: 0 <   x \leq 1, 0 \leq y \leq \left| \sin \frac {1}{x} \right| \right\}
$$

is Jordan measurable.

1.7.21. Set $\mathbf{A} = \{(x,y)\in \mathbb{R}^2:(x - 1)^2 +y^2\leq 1\}$ and

$$
\mathbf {K} _ {n} = \left\{(x, y) \in \mathbb {R} ^ {2}: \left(x - \frac {1}{n}\right) ^ {2} + y ^ {2} \leq \frac {1}{4 ^ {2 n}} \right\}.
$$

Show that the set $\mathbf{A} \setminus \bigcup_{n=1}^{\infty} \mathbf{K}_n$ is Jordan measurable.

1.7.22. Derive the following formula for the Jordan measure of sets defined by inequalities in the polar coordinates $(r, \theta)$ . If $f$ is a nonnegative and continuous function on $[\alpha, \beta], \beta - \alpha < 2\pi$ , then the set $\mathbf{A} = \{(r, \theta) : \alpha \leq \theta \leq \beta, 0 \leq r \leq f(\theta)\}$ is Jordan measurable, and its area is

$$
| \mathbf {A} | = \frac {1}{2} \int_ {\alpha} ^ {\beta} f ^ {2} (\theta) d \theta .
$$

1.7.23. Find the area of one of the congruent loops of the lemniscate $r^2 = a^2 \cos(2\theta)$ , where $a > 0$ is fixed.

1.7.24. The curve $r = a(1 + \cos(3\theta))$ , $a > 0$ , consists of three congruent leaves, tangent to each other at the origin. Find the area of one of the leaves.

1.7.25. Find the area of the limacon $r = a + b\cos \theta$ , where positive numbers $a$ and $b$ are given, distinguishing the cases in which $a > b$ , $a = b$ , and $a < b$ .

1.7.26. Find the area of the loop of the curve $x^5 + y^5 = 5ax^2y^2$ , where $a > 0$ is given.

1.7.27. Find the area of the region that lies within the limacon $r = 1 + 2\cos \theta$ and outside the circle $r = 2$ .

1.7.28. Suppose $f$ is nonnegative and continuous on $[a, b]$ . A plane region $\mathbf{A}_f = \{(x, y) \in \mathbb{R}^2 : a \leq b, 0 \leq y \leq f(x)\}$ is revolved about the $x$ -axis, generating a solid of revolution $\mathbf{V}$ with volume $|\mathbf{V}|$ . Prove that

$$
| \mathbf {V} | = \pi \int_ {a} ^ {b} f ^ {2} (x) d x.
$$

1.7.29. Suppose $f$ is nonnegative and continuous on $[a, b]$ and $0 < a$ . Prove that the volume of the solid $V$ generated by the plane region $\mathbf{A}_f = \{(x, y) \in \mathbb{R}^2 : a \leq b, 0 \leq y \leq f(x)\}$ when it revolves about the $y$ -axis is given by

$$
| \mathbf {V} | = 2 \pi \int_ {a} ^ {b} x f (x) d x.
$$

1.7.30. Find the volume of a torus obtained by revolving the disk $\{(x, y) \in \mathbb{R}^2 : (x - a)^2 + y^2 \leq r^2\}$ , where $0 < a < r$ , about the $y$ -axis.

1.7.31. Find the volume of a solid obtained by revolving an unbounded region under the graph of $f(x) = e^{-x}\sqrt{\sin x}$ over the set $\bigcup_{k=0}^{\infty}[2k\pi, (2k+1)\pi]$ about the $x$ -axis.

1.7.32. Show that the length $L$ of the ellipse

$$
\left(\frac {x}{a}\right) ^ {2} + \left(\frac {y}{b}\right) ^ {2} = 1
$$

satisfies

$$
\pi (a + b) <   L <   \pi \sqrt {2 \left(a ^ {2} + b ^ {2}\right)}.
$$

1.7.33. Show that the length of the ellipse

$$
\left(\frac {x}{a}\right) ^ {2} + \left(\frac {y}{b}\right) ^ {2} = 1, \quad a > b > 0,
$$

is given by

$$
L = 2 \pi a \left(1 - \sum_ {n = 1} ^ {\infty} \left(\frac {(2 n - 1) ! !}{(2 n) ! !}\right) ^ {2} \frac {e ^ {2 n}}{2 n - 1}\right),
$$

where $e = \frac{\sqrt{a^2 - b^2}}{a}$ is the eccentricity of the ellipse.

1.7.34. Derive the following formula for the length of a curve in the polar coordinates $(r, \theta)$ . If $f$ is continuously differentiable on $[\alpha, \beta]$ , then the length $L$ of the curve $r = f(\theta)$ , $\alpha \leq \theta \leq \beta$ , is given by

$$
L = \int_ {\alpha} ^ {\beta} \sqrt {(f (\theta)) ^ {2} + (f ^ {\prime} (\theta)) ^ {2}} d \theta .
$$

1.7.35. Find the length of the curve with polar equation

(a) $r = a\sin^3{\frac{\theta}{3}},\quad 0\leq \theta \leq 3\pi .$   
(b) $r = \frac{1}{1 + \cos\theta}, - \frac{\pi}{2}\leq \theta \leq \frac{\pi}{2}.$

1.7.36. Find the length of the curve with polar equation

$$
\theta = \frac {1}{2} \left(r + \frac {1}{r}\right), \quad 1 \leq r \leq 3.
$$

1.7.37. Find the length of the curve

$$
r = 1 + \cos t, \quad \theta = t - \tan \frac {t}{2}, \quad 0 \leq t \leq \beta ,
$$

where $(r,\theta)$ are polar coordinates and $0 < \beta < \pi$ .

# Chapter 2

# The Lebesgue Integral

# 2.1. Lebesgue Measure on the Real Line

For $\mathbf{A} \subset \mathbb{R}$ , we consider a countable collection of closed intervals $\{\mathbf{I}_n\}$ , $\mathbf{I}_n = [a_n, b_n]$ , $a_n \leq b_n$ , that cover $\mathbf{A}$ , that is, $\mathbf{A} \subset \bigcup_{n=1}^{\infty} \mathbf{I}_n$ and we define the Lebesgue outer measure $m^*(\mathbf{A})$ of $\mathbf{A}$ by

$$
m ^ {*} (\mathbf {A}) = \inf  \sum_ {n = 1} ^ {\infty} | \mathbf {I} _ {n} | = \inf  \sum_ {n = 1} ^ {\infty} (b _ {n} - a _ {n}),
$$

where the infimum is taken over all countable coverings of $\mathbf{A}$ by closed intervals. Clearly, the closed intervals in the definition of the Lebesgue outer measure can be replaced by open intervals $(a_n, b_n)$ . The Lebesgue outer measure enjoys the following properties:

(i) If $\mathbf{A} \subset \mathbf{B}$ , then $m^*(\mathbf{A}) \leq m^*(\mathbf{B})$ .   
(ii) $m^{*}\left(\bigcup_{n = 1}^{\infty}\mathbf{A}_{n}\right)\leq \sum_{n = 1}^{\infty}m^{*}(\mathbf{A}_{n}).$

A set $\mathbf{A}$ is said to be Lebesgue measurable (or measurable), if for each set $\mathbf{E} \subset \mathbb{R}$ the Carathéodory condition

$$
m ^ {*} (\mathbf {E}) = m ^ {*} (\mathbf {E} \cap \mathbf {A}) + m ^ {*} (\mathbf {E} \backslash \mathbf {A})
$$

is satisfied. The set $\mathfrak{M}$ of all Lebesgue measurable subsets of $\mathbb{R}$ is a $\sigma$ -algebra; that is, the complement of a measurable set is measurable and the union of a countable collection of measurable sets is measurable.

Recall that the collection $\mathfrak{B}$ of Borel sets is the smallest $\sigma$ -algebra which contains all of the open sets in $\mathbb{R}$ . Every Borel set is measurable. If $\mathbf{A}$ is a measurable set, we define the Lebesgue measure $m(\mathbf{A})$ to be the outer measure of $\mathbf{A}$ . The measure $m$ is countably additive on $\mathfrak{M}$ ; that is, if the sets $\mathbf{A}_n$ are pairwise disjoint, then

$$
m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = \sum_ {n = 1} ^ {\infty} m (\mathbf {A} _ {n}).
$$

2.1.1. Show that if $m^{*}(\mathbf{A}) = 0$ , then $\mathbf{A}$ is measurable.

2.1.2. Let $\mathbf{S} = \bigcup_{n=1}^{\infty} \mathbf{I}_n$ , where $\mathbf{I}_n, n \in \mathbb{N}$ , are closed intervals. Show that $m(\mathbf{S}) = |\mathbf{S}|_*$ , where $|\mathbf{S}|_*$ denotes the inner Jordan measure.

2.1.3. Let $\mathbf{S}_1 = \bigcup_{n=1}^{\infty} \mathbf{I}_n$ and $\mathbf{S}_2 = \bigcup_{n=1}^{\infty} \mathbf{K}_n$ , where $\mathbf{I}_n, \mathbf{K}_n, n \in \mathbb{N}$ , are closed intervals. Show that

$$
m \left(\mathbf {S} _ {1} \cup \mathbf {S} _ {2}\right) + m \left(\mathbf {S} _ {1} \cap \mathbf {S} _ {2}\right) = m \left(\mathbf {S} _ {1}\right) + m \left(\mathbf {S} _ {2}\right).
$$

2.1.4. Show that for any two sets $\mathbf{A}$ and $\mathbf{B}$ ,

$$
m ^ {*} (\mathbf {A} \cup \mathbf {B}) + m ^ {*} (\mathbf {A} \cap \mathbf {B}) \leq m ^ {*} (\mathbf {A}) + m ^ {*} (\mathbf {B}).
$$

2.1.5. For an open set $\mathbf{G}$ , let $\mathbf{A} \subset \mathbf{G}$ and $\mathbf{B} \cap \mathbf{G} = \emptyset$ . Show that

$$
m ^ {*} (\mathbf {A} \cup \mathbf {B}) = m ^ {*} (\mathbf {A}) + m ^ {*} (\mathbf {B}).
$$

2.1.6. Suppose that $\mathbf{A}$ and $\mathbf{B}$ have positive distance, that is,

$$
d (\mathbf {A}, \mathbf {B}) = \inf  \{| x - y |: x \in \mathbf {A}, y \in \mathbf {B} \} > 0.
$$

Then

$$
m ^ {\bullet} (\mathbf {A} \cup \mathbf {B}) = m ^ {\bullet} (\mathbf {A}) + m ^ {\bullet} (\mathbf {B}).
$$

2.1.7. Show that if $m(\mathbf{A}) = 0$ , then for any $\mathbf{B}$

$$
m ^ {*} (\mathbf {A} \cup \mathbf {B}) = m ^ {*} (\mathbf {B} \setminus \mathbf {A}) = m ^ {*} (\mathbf {B}).
$$

2.1.8. Show that if $\mathbf{A}$ is a measurable set of finite measure, then for any $\mathbf{B} \supset \mathbf{A}$ ,

$$
m ^ {*} (\mathbf {B} \backslash \mathbf {A}) = m ^ {*} (\mathbf {B}) - m (\mathbf {A}).
$$

2.1.9. Show that if $\mathbf{A}$ and $\mathbf{B}$ are measurable, then

$$
m (\mathbf {A} \cup \mathbf {B}) + m (\mathbf {A} \cap \mathbf {B}) = m (\mathbf {A}) + m (\mathbf {B}).
$$

2.1.10. Show that if $m^*(\mathbf{A}) < \infty$ and there is a measurable subset $\mathbf{A}_1$ of $\mathbf{A}$ such that $m(\mathbf{A}_1) = m^*(\mathbf{A})$ , then $\mathbf{A}$ is measurable.

2.1.11. Let $\mathbf{A}$ be any set in $\mathbb{R}$ . Show that for each $\varepsilon > 0$ there is an open set $\mathbf{G}$ such that $\mathbf{A} \subset \mathbf{G}$ and $m(\mathbf{G}) \leq m^{*}(\mathbf{A}) + \varepsilon$ . Show also that there is a $\mathcal{G}_{\delta}$ set $\mathbf{A}_2$ such that $\mathbf{A} \subset \mathbf{A}_2$ and $m(\mathbf{A}_2) = m^{*}(\mathbf{A})$ .

2.1.12. Prove that for $\mathbf{A} \subset \mathbb{R}$ the following statements are equivalent:

(i) $\mathbf{A}$ is measurable.

(ii) Given $\varepsilon > 0$ , there is an open set $\mathbf{G} \supset \mathbf{A}$ such that

$$
m ^ {*} (\mathbf {G} \backslash \mathbf {A}) <   \varepsilon .
$$

(iii) There is a $\mathcal{G}_{\delta}$ set $\mathbf{U} \supset \mathbf{A}$ such that $m^{*}(\mathbf{U} \setminus \mathbf{A}) = 0$ .

(iv) Given $\varepsilon > 0$ , there is a closed set $\mathbf{F} \subset \mathbf{A}$ such that

$$
m ^ {*} (\mathbf {A} \backslash \mathbf {F}) <   \varepsilon .
$$

(v) There is an $\mathcal{F}_{\sigma}$ set $\mathbf{V} \subset \mathbf{A}$ such that $m^{*}(\mathbf{A} \setminus \mathbf{V}) = 0$ .

2.1.13. Show that if $m^{*}(\mathbf{A}) < \infty$ , then $\mathbf{A}$ is measurable if and only if for each $\varepsilon > 0$ there is a finite union $\mathbf{W}$ of open intervals such that $m^{*}(\mathbf{W} \triangle \mathbf{A}) < \varepsilon$ , where $\mathbf{W} \triangle \mathbf{A}$ is the symmetric difference for $\mathbf{W}$ and $\mathbf{A}$ , that is, $\mathbf{W} \triangle \mathbf{A} = (\mathbf{W} \setminus \mathbf{A}) \cup (\mathbf{A} \setminus \mathbf{W})$ .

2.1.14. For $\mathbf{A} \subset \mathbb{R}$ , define the Lebesgue inner measure $m_{*}(\mathbf{A})$ of $\mathbf{A}$ by setting

$$
m _ {*} (\mathbf {A}) = \sup  \{m (\mathbf {B}): \mathbf {B} \in \mathfrak {M}, \mathbf {B} \subset \mathbf {A} \},
$$

where $\mathfrak{M}$ denotes the $\sigma$ -algebra of all measurable subsets of $\mathbb{R}$ . Prove:

(a) If $\mathbf{A}$ is measurable, then $m_{*}(\mathbf{A}) = m^{*}(\mathbf{A})$ .   
(b) If $\mathbf{A}$ is a subset of a bounded closed interval $\mathbf{I}$ , then

$$
m _ {*} (\mathbf {A}) = | \mathbf {I} | - m ^ {*} (\mathbf {I} \backslash \mathbf {A}).
$$

(c) If $m_{*}(\mathbf{A}) = m^{*}(\mathbf{A}) < \infty$ , then $\mathbf{A}$ is measurable.   
(d) For any sets $\mathbf{A}$ and $\mathbf{C}$ ,

$$
m _ {*} (\mathbf {A} \cup \mathbf {C}) + m _ {*} (\mathbf {A} \cap \mathbf {C}) \geq m _ {*} (\mathbf {A}) + m _ {*} (\mathbf {C}).
$$

(e) If $\mathbf{A}_n, n = 1,2,\ldots$ , arc pairwise disjoint, then

$$
m _ {\bullet} \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) \geq \sum_ {n = 1} ^ {\infty} m _ {*} (\mathbf {A} _ {n}).
$$

(f) If $\mathbf{M}$ is of measure zero, then $m_{*}(\mathbf{A} \cup \mathbf{M}) = m_{*}(\mathbf{A})$ .

2.1.15. Prove that $\mathbf{A} \subset \mathbf{I}$ , where $\mathbf{I}$ is a bounded and closed interval, is measurable if and only if

$$
| \mathbf {I} | = m ^ {*} (\mathbf {A}) + m ^ {*} (\mathbf {I} \backslash \mathbf {A}).
$$

2.1.16. Let $\mathbf{A}$ and $\mathbf{B}$ be given sets of finite outer measures. Show that $m^{*}(\mathbf{A} \cup \mathbf{B}) = m^{*}(\mathbf{A}) + m^{*}(\mathbf{B})$ if and only if there are measurable sets $\mathbf{A}_{1}$ and $\mathbf{B}_{1}$ such that $\mathbf{A} \subset \mathbf{A}_{1}, \mathbf{B} \subset \mathbf{B}_{1}$ and $m(\mathbf{A}_{1} \cap \mathbf{B}_{1}) = 0$ .

2.1.17. Let $\mathbf{A}$ and $\mathbf{B}$ be given sets of finite outer measures. Show that if $m^{*}(\mathbf{A} \cup \mathbf{B}) = m^{*}(\mathbf{A}) + m^{*}(\mathbf{B})$ , then $m_{*}(\mathbf{A} \cup \mathbf{B}) = m_{*}(\mathbf{A}) + m_{*}(\mathbf{B})$ .

2.1.18. Prove that if $\{\mathbf{A}_n\}$ is an increasing sequence of measurable sets, then

$$
m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = \lim  _ {n \rightarrow \infty} m (\mathbf {A} _ {n}).
$$

2.1.19. Prove that if $\{\mathbf{A}_n\}$ is a decreasing sequence of measurable sets and $m(\mathbf{A}_k)$ is finite for at least one $k$ , then

$$
m \left(\bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = \lim  _ {n \rightarrow \infty} m (\mathbf {A} _ {n}).
$$

Show also that the assumption that $m(\mathbf{A}_k) < \infty$ for some $k$ cannot be omitted.

2.1.20. For a sequence $\{\mathbf{A}_n\}$ of sets in $\mathbb{R}$ , we define the limit superior and the limit inferior of $\{\mathbf{A}_n\}$ by setting

$$
\varlimsup_ {n \rightarrow \infty} \mathbf {A} _ {n} = \bigcap_ {k = 1} ^ {\infty} \bigcup_ {n = k} ^ {\infty} \mathbf {A} _ {n} \quad \text {a n d} \quad \varliminf_ {n \rightarrow \infty} \mathbf {A} _ {n} = \bigcup_ {k = 1} ^ {\infty} \bigcap_ {n = k} ^ {\infty} \mathbf {A} _ {n}.
$$

(a) Show that if $\mathbf{A}_n, n \in \mathbb{N}$ , are measurable, then

$$
m \left(\lim  _ {n \rightarrow \infty} A _ {n}\right) \leq \lim  _ {n \rightarrow \infty} m (A _ {n}).
$$

(b) Show that if, moreover, $m(\mathbf{A}_n \cup \mathbf{A}_{n+1} \cup \ldots) < \infty$ for at least one $n$ , then

$$
m \left(\varlimsup_ {n \rightarrow \infty} A _ {n}\right) \geq \varliminf_ {n \rightarrow \infty} m (A _ {n}).
$$

2.1.21. We say that a sequence $\{\mathbf{A}_n\}$ of sets in $\mathbb{R}$ converges if $\lim_{n\to \infty}\mathbf{A}_n = \lim_{n\to \infty}\mathbf{A}_n$ , and we denote the common value by $\lim_{n\to \infty}\mathbf{A}_n$ .

(a) Show that a monotonic sequence of sets converges.   
(b) Show that, if a sequence $\{\mathbf{A}_n\}$ of measurable sets, $\mathbf{A}_n \subset \mathbf{B}$ , where $m^*(\mathbf{B}) < \infty$ , converges, then

$$
m \left(\lim  _ {n \rightarrow \infty} \mathbf {A} _ {n}\right) = \lim  _ {n \rightarrow \infty} m (\mathbf {A} _ {n}).
$$

2.1.22. Show that the Lebesgue measure of the set $\mathbf{A}$ defined in 1.7.12 is equal to $1 - \alpha$ .   
2.1.23. Let $\mathbf{A}$ be the set of points in [0, 1] such that $x$ is in $\mathbf{A}$ if and only if the decimal expansion of $x$ does not require the use of the digit 7. Show that $\mathbf{A}$ has Lebesgue measure zero.   
2.1.24. Let $\mathbf{B} \subset \mathbb{R}$ be the set of all numbers whose decimal expansions do not require the use of the digit 7 after the decimal point. Show that $\mathbf{B}$ has Lebesgue measure zero.   
2.1.25. Let $\mathbf{A}$ be the set of points in $[0,1]$ which admit of binary expansions with zeroes in all even positions. Show that $\mathbf{A}$ is a nowhere dense set of Lebesgue measure zero.   
2.1.26. Find the Lebesgue measure of the set of points in $[0, 1]$ which admit decimal expansions containing all the digits $1, 2, \ldots, 9$ .   
2.1.27. What is the Lebesgue measure of the set of points in $[0,1]$ which admit decimal expansions $0.d_{1}d_{2}d_{3}\ldots$ such that no sequence $d_{3k+1}d_{3k+2}d_{3k+3}$ consists of three consecutive 2's?   
2.1.28. Let $\mathbf{A}$ be the union of intervals centered at points of the Cantor set and each of length 0.1. Find the Lebesgue measure of $\mathbf{A}$ .   
2.1.29. Show that if $\mathbf{A}$ is a bounded measurable set of measure $m(\mathbf{A}) = p > 0$ , then for each $q \in (0, p)$ there is a measurable set $\mathbf{B} \subset \mathbf{A}$ of measure $q$ .   
2.1.30. Show that if $0 < m(\mathbf{A}) \leq \infty$ , then for each positive $q < m(\mathbf{A})$ there is a measurable set $\mathbf{B} \subset \mathbf{A}$ of measure $q$ .   
2.1.31. Show that if $0 < m(\mathbf{A}) \leq \infty$ , then for each positive $q < m(\mathbf{A})$ there is a perfect set $\mathbf{B} \subset \mathbf{A}$ of measure $q$ .   
2.1.32. Show that any set $\mathbf{A}$ of positive Lebesgue measure has the cardinality of the continuum.

2.1.33. Show that any nonempty and closed set $\mathbf{A} \subset \mathbb{R}$ of Lebesgue measure zero is nowhere dense.   
2.1.34. Suppose that $\mathbf{A} \subset \mathbb{R}$ is a nowhere dense set of Lebesgue measure zero. Must its closure be of Lebesgue measure zero?   
2.1.35. Show that if $\mathbf{A} \subset [a, b]$ and $m(\mathbf{A}) > 0$ , then there are $x$ and $y$ in $\mathbf{A}$ such that $|x - y|$ is an irrational number.   
2.1.36. Does there exist a countable collection of nowhere dense and perfect subsets of $[0,1]$ whose union is of Lebesgue measure 1?   
2.1.37. Does there exist a nowhere dense and perfect subset of $[0, 1]$ of Lebesgue measure 1?   
2.1.38. Give an example of a measurable set $\mathbf{A} \subset \mathbb{R}$ with the following property: For each interval $(\alpha, \beta)$ ,

$$
m (\mathbf {A} \cap (\alpha , \beta)) > 0 \quad \text {a n d} \quad m ((\mathbb {R} \backslash \mathbf {A}) \cap (\alpha , \beta)) > 0.
$$

2.1.39. Assume that a measurable set $\mathbf{A} \subset \mathbb{R}$ has the property that for each $\delta > 0$ , $m(\mathbf{A} \cap (-\delta, \delta)) > 0$ and $0 \in \mathbf{A}$ . Prove that there exists a perfect set $\mathbf{B} \subset \mathbf{A}$ such that $m(\mathbf{B} \cap (-\delta, \delta)) > 0$ for every $\delta > 0$ .   
2.1.40. A measurable set $\mathbf{A} \subset \mathbb{R}$ is said to have density $d$ at $x$ if the limit

$$
\lim  _ {h \rightarrow 0 ^ {+}} \frac {m (A \cap [ x - h , x + h ])}{2 h}
$$

exists and is equal to $d$ . If $d = 1$ , then $x$ is called a point of density of $\mathbf{A}$ , and if $d = 0$ , then $x$ is called a point of dispersion of $\mathbf{A}$ . Find the points of density and points of dispersion of $\mathbf{A} = (-1,0) \cup (0,1) \cup \{2\}$ .

2.1.41. Given $\alpha \in (0,1)$ , construct a set $\mathbf{A}$ whose density at $x_0 \in \mathbb{R}$ is equal to $\alpha$ .   
2.1.42. Let $\mathbf{A}$ be a measurable set such that $0 \in \mathbf{A}$ is a point of density of $\mathbf{A}$ . Prove that there is a perfect set $\mathbf{B} \subset \mathbf{A}$ such that $\mathbf{0}$ is a point of density of $\mathbf{B}$ .   
2.1.43. If $x$ and $y$ are in [0, 1), we define the sum $x + y (\bmod 1)$ to be $x + y$ , if $x + y < 1$ , and to be $x + y - 1$ , if $x + y \geq 1$ . For $A \subset [0, 1)$ and $a \in [0, 1)$ , we define the translate modulo 1 of $A$ to be the set

$$
\mathbf {A} + a (\mathrm {m o d} \mathbf {1}) = \{x + a (\mathrm {m o d} \mathbf {1}): x \in \mathbf {A} \}.
$$

Show that $m^{*}(\mathbf{A}) = m^{*}(\mathbf{A} + a(\mathrm{mod} 1))$ .

2.1.44. Show that if $\mathbf{A} \subset [0,1)$ and $a \in [0,1)$ , then the set $\mathbf{A} + a (\bmod 1)$ is measurable if and only if $\mathbf{A}$ is measurable and

$$
m (\mathbf {A} + a (\mathrm {m o d} 1)) = m (\mathbf {A}).
$$

2.1.45. We say that $x, y \in [0, 1)$ are equivalent, and write $x \sim y$ , if and only if $x - y$ is a rational. This equivalence relation partitions $[0, 1)$ into an uncountable family of disjoint equivalence classes. By the axiom of choice there is a set $V$ which contains exactly one element from each equivalence class. We call any such a set a Vitali set. Prove that a Vitali set is nonmeasurable.

2.1.46. Show that if $\mathbf{A}$ is a measurable subset of a Vitali set $\mathbf{V}$ , then $m(\mathbf{A}) = 0$ .

2.1.47. Show, by example, that the converse of the result stated in 2.1.17 is not true; that is, there exist sets $\mathbf{A}$ and $\mathbf{B}$ such that $m_{*}(\mathbf{A} \cup \mathbf{B}) = m_{*}(\mathbf{A}) + m_{*}(\mathbf{B})$ but $m^{*}(\mathbf{A} \cup \mathbf{B}) < m^{*}(\mathbf{A}) + m^{*}(\mathbf{B})$ .

2.1.48. Show that any set of positive outer measure contains a non-measurable subset.

2.1.49. Give an example of a sequence $\{\mathbf{A}_n\}$ of pairwise disjoint sets such that

$$
m ^ {*} \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) <   \sum_ {n = 1} ^ {\infty} m ^ {*} (\mathbf {A} _ {n}).
$$

2.1.50. Give an example of a decreasing sequence $\{\mathbf{A}_n\}$ of sets such that $m^{*}(\mathbf{A}_{1}) < \infty$ and

$$
m ^ {*} \left(\bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) <   \lim  _ {n \rightarrow \infty} m ^ {*} (\mathbf {A} _ {n}).
$$

2.1.51. Show that if $\mathbf{A}$ is a measurable set of positive measure, then there is $\delta > 0$ such that $\mathbf{A} \cap (\mathbf{A} + x)$ is nonempty whenever $|x| < \delta$ .

2.1.52. Let $\mathbf{V}_k$ , $k = 0,1,\ldots$ , be the sets defined in the solution to 2.1.45. Show that each of the sets $\mathbf{A}_n = \bigcup_{k=0}^{n} \mathbf{V}_k$ is nonmeasurable.

2.1.53. Suppose that $\mathbf{A} \subset \mathbb{R}$ is a measurable set for which there is a positive $c$ such that $m(\mathbf{A} \cap \mathbf{I}) \geq c|\mathbf{I}|$ for every interval $\mathbf{I}$ . Show that the complement of $\mathbf{A}$ is of measure zero.

2.1.54. Prove that there is a set $\mathbf{A} \subset \mathbb{R}$ such that each Lebesgue measurable set that is included in $\mathbf{A}$ or in $\mathbf{A}^c$ has Lebesgue measure zero.

2.1.55. Prove the following Lebesgue criterion for Riemann integrability: A bounded function on a closed bounded interval is Riemann integrable if and only if the set of discontinuities of $f$ has Lebesgue measure zero.

2.1.56. For $f: [a, b] \to \mathbb{R}$ , let $\mathbf{D}$ denote the set of discontinuities of $f$ and $\mathbf{L}$ the set of points where $f$ has a left-hand limit. Show that $\mathbf{D} \cap \mathbf{L}$ is countable. Conclude the following criterion for Riemann integrability: a bounded function on $[a, b]$ is Riemann integrable if and only if the set $[a, b] \setminus \mathbf{L}$ has Lebesgue measure zero.

2.1.57. Let $f:[0,1] \to \mathbb{R}$ be continuous with $f(0) = f(1) = 0$ . Show that the Lebesgue measure of

$$
\mathbf {A} = \{h \in [ 0, 1 ]: f (x + h) = f (x) \text {f o r s o m e} x \in [ 0, 1 ] \}
$$

is at least $1 / 2$

# 2.2. Lebesgue Measurable Functions

An extended real-valued function $f: \mathbf{A} \to \overline{\mathbb{R}}$ defined on a measurable set $\mathbf{A} \subset \mathbb{R}$ is said to be Lebesgue measurable (or measurable for short) on $\mathbf{A}$ if $f^{-1}((c, \infty]) = \{x \in \mathbf{A}: f(x) > c\}$ is a Lebesgue measurable subset of $\mathbf{A}$ for every real number $c$ . We have

Theorem 1. The following statements are equivalent:

(i) $f$ is Lebesgue measurable on $\mathbf{A}$ .

(ii) $f^{-1}([c, \infty]) = \{x \in \mathbf{A} : f(x) \geq c\}$ is a Lebesgue measurable subset of $\mathbf{A}$ for every real $c$ .

(iii) $f^{-1}([-\infty, c)) = \{x \in \mathbf{A} : f(x) < c\}$ is a Lebesgue measurable subset of $\mathbf{A}$ for every real $c$ .

(iv) $f^{-1}([-\infty, c]) = \{x \in A : f(x) \leq c\}$ is a Lebesgue measurable subset of $A$ for every real $c$ .

We will also use the following.

Theorem 2. Let $f$ and $g$ be measurable real-valued functions defined on $A$ , let $F$ be a real-valued function continuous on $\mathbb{R}^2$ , and put $h(x) = F(f(x), g(x))$ for $x \in A$ . Then $h$ is measurable on $A$ . In particular, $f + g$ and $fg$ are measurable.

Theorem 3. Let $\{f_n\}$ be a sequence of measurable functions on $\mathbf{A}$ ; then $h_1(x) = \sup \{f_n(x): n \in \mathbb{N}\}$ and $h_2(x) = \varlimsup_{n \to \infty} f_n(x)$ are also measurable on $\mathbf{A}$ . In particular, if $f$ and $g$ are measurable on $\mathbf{A}$ , then so are $\max \{f, g\}$ and $\min \{f, g\}$ .

A property is said to hold almost everywhere (abbreviated a.e.) on a measurable set if the set of points where it fails to hold is a set of measure zero. In particular, we say that $f = g$ a.e. if $f$ and $g$ have the same domain A and $m(\{x \in A : f(x) \neq g(x)\}) = 0$ .

Suppose $\mathbf{A} = \bigcup_{i=1}^{n} \mathbf{A}_{i}$ , where the sets $\mathbf{A}_{i}$ are measurable and pairwise disjoint. A function $\varphi$ defined on $\mathbf{A}$ by

$$
\varphi (x) = \sum_ {i = 1} ^ {n} c _ {i} \chi_ {\mathbf {A} _ {i}} (x),
$$

where $c_1, c_2, \ldots, c_n$ are real numbers, is said to be a simple function.

The following theorem is called the approximation theorem for measurable functions.

Theorem 4. For every measurable function $f$ defined on a measurable set $A$ , there is a sequence $\{\varphi_n\}$ of simple functions which converges pointwise to $f$ . In case $f$ is nonnegative, the sequence $\{\varphi_n\}$ may be constructed so that it is monotonically increasing. In case $f$ is bounded on $A$ , the sequence $\{\varphi_n\}$ may be chosen so that the convergence is uniform on $A$ .

2.2.1. Show that if $f$ is measurable, then so is $|f|$ . Does the measurability of $|f|$ imply the measurability of $f$ ?

2.2.2. Give examples of nonmeasurable functions $f$ and $g$ such that

(a) $f + g$ is measurable,   
(b) $fg$ is measurable.

2.2.3. Let $f$ be a real-valued function defined on $\mathbb{R}$ . Show that the measurability of the set $\{x : f(x) = c\}$ for every real $c$ is not sufficient for $f$ to be measurable.

2.2.4. Let $\mathbf{C}$ be a dense subset of $\mathbb{R}$ . Show that a function $f$ defined on a measurable set $\mathbf{A}$ is measurable if and only if $\{x \in \mathbf{A} : f(x) \geq c\}$ is measurable for every $c \in \mathbf{C}$ .

2.2.5. Show that a real-valued function $f$ defined on a measurable set $A$ is measurable if and only if $f^{-1}(G)$ is measurable for every open $G \subset \mathbb{R}$ .

2.2.6. Show that if a real-valued function $f$ defined on $\mathbb{R}$ is measurable, then $f^{-1}(\mathbf{B})$ is measurable for every Borel set $\mathbf{B} \subset \mathbb{R}$ .

2.2.7. Prove that continuous real-valued functions defined on measurable sets are measurable.

2.2.8. Suppose extended-valued functions $f$ and $g$ are defined on a measurable set $\mathbf{A}$ . Prove that if $f$ is a measurable function and $f = g$ a.e., then $g$ is measurable.

2.2.9. Prove that every Riemann integrable function defined on $[a, b]$ is measurable on $[a, b]$ .

2.2.10. Show that each function of bounded variation on $[a, b]$ is measurable.

2.2.11. Define the Cantor function $\varphi : [0,1] \to [0,1]$ as follows: If $x$ is an element of the Cantor set $\mathbf{C}$ and $x = \sum_{n=1}^{\infty} \frac{a_n}{3^n}$ with $a_n = 0$ or $a_n = 2$ , then we put

$$
\varphi (x) = \varphi \left(\sum_ {n = 1} ^ {\infty} \frac {a _ {n}}{3 ^ {n}}\right) = \sum_ {n = 1} ^ {\infty} \frac {a _ {n}}{2} \frac {1}{2 ^ {n}};
$$

that is, if $a_n$ is the $n$ th ternary digit for $x$ , then the $n$ th binary digit for $\varphi(x)$ is $a_n / 2$ . We extend $\varphi$ to [0,1] by setting

$$
\varphi (x) = \sup  \left\{\varphi (y): y \subset \mathbf {C}, y <   x \right\}.
$$

Show that the Cantor function maps the Cantor set $\mathbf{C}$ onto $[0,1]$ . Show also that $\varphi$ is increasing and continuous on $[0,1]$ and $\varphi'(x) = 0$ a.e. on $[0,1]$ .

2.2.12. Prove that if $f$ is a one-one continuous mapping of $\mathbb{R}$ onto $\mathbb{R}$ , then $f$ maps Borel sets onto Borel sets.

2.2.13. Give an example of

(a) a measurable function $f$ and a measurable set $A$ such that $f(A)$ is nonmeasurable,

(b) a measurable function $g$ and a measurable set $\mathbf{B}$ such that $g^{-1}(\mathbf{B})$ is nonmeasurable.

2.2.14. Give an example of a measurable set that is not Borel.

2.2.15. Assume that $f$ is continuous on $[a, b]$ . Show that $f$ satisfies the condition

$$
\mathbf {E} \subset [ a, b ] \quad \text {a n d} \quad m (\mathbf {E}) = 0 \quad \text {i m p l i e s} \quad m (f (\mathbf {E})) = 0
$$

if and only if

for any measurable $\mathbf{A} \subset [a, b]$ its image $f(\mathbf{A})$ is measurable.

2.2.16. Suppose that a real-valued function $g$ is measurable on $\mathbf{A}$ and $f$ is continuous on $g(\mathbf{A})$ . Show that $f \circ g$ is measurable.

2.2.17. Suppose that $g$ is continuous on $[a, b]$ and $h$ is real-valued and measurable on $g([a, b])$ . Must $h \circ g$ be measurable?

2.2.18. Suppose that a real-valued function $g$ is measurable on $\mathbf{A}$ and $f$ defined on $\mathbb{R}$ is such that for every open set $\mathbf{G}$ , the inverse image $f^{-1}(\mathbf{G})$ is a Borel set. Show that $f \circ g$ is measurable.

2.2.19. Give an example of a measurable function whose inverse is not measurable.

2.2.20. Let $f$ be a function differentiable on $[a, b]$ . Show that $f'$ is measurable on $[a, b]$ .

2.2.21. Let $\mathbf{A} \subset \mathbb{R}$ be a measurable set of finite measure and $f$ a measurable function on $\mathbf{A}$ which is finite almost everywhere. Then, given $\varepsilon > 0$ , there is a measurable set $\mathbf{B} \subset \mathbf{A}$ such that $m(\mathbf{A} \setminus \mathbf{B}) < \varepsilon$ and $f$ restricted to $\mathbf{B}$ is bounded.

2.2.22. Prove the following Egorov theorem. Let $\mathbf{A} \subset \mathbb{R}$ be a measurable set of finite measure. If $\{f_n\}$ is a sequence of measurable functions which converges to a real-valued function $f$ almost everywhere on $\mathbf{A}$ , then, given $\varepsilon > 0$ , there exists a measurable subset $\mathbf{B}$ of $\mathbf{A}$ such that $m(\mathbf{A} \setminus \mathbf{B}) < \varepsilon$ and the sequence $\{f_n\}$ converges uniformly to $f$ on $\mathbf{B}$ .

2.2.23. Show by example that the assumption $m(\mathbf{A}) < \infty$ is essential in the Egorov theorem.

2.2.24. Suppose that $\mathbf{A}$ is measurable and $\{f_n\}$ is a sequence of measurable functions which converges to $f$ almost everywhere on $\mathbf{A}$ . Prove that there is a set $\mathbf{B} \subset \mathbf{A}$ such that $\mathbf{B} = \bigcup_{i=1}^{\infty} \mathbf{B}_i$ , $m(\mathbf{A} \setminus \mathbf{B}) = 0$ and the sequence $\{f_n\}$ converges uniformly to $f$ on every $\mathbf{B}_i$ .

2.2.25. Let $\{\mathbf{V}_n\}$ be the sequence of sets defined in the solution to 2.1.45 and let $\{f_n\}$ be the sequence of functions on $[0,1)$ defined by $f_{n} = \chi_{\bigcup_{i = n}^{\infty}}\mathbf{v}_{i}$ . Show that $f_{n}\rightarrow 0$ on $[0,1)$ , but the assertion of the Fgorov theorem does not hold, that is, there is $\varepsilon >0$ such that on any measurable subset $\mathbf{B}$ of $[0,1)$ with $m([0,1)\setminus \mathbf{B}) < \varepsilon$ the convergence is not uniform.

2.2.26. Construct a sequence $\{f_n\}$ of measurable functions on $[0,1]$ such that the sequence converges everywhere on $[0,1]$ but for every set $\mathbf{B} \subset [0,1]$ of measure 1, the sequence fails to converge uniformly on $\mathbf{B}$ .

2.2.27. Prove the following Lusin theorem: In order that a real-valued function $f$ defined on a measurable set $\mathbf{A}$ be measurable, a necessary and sufficient condition is that for every $\varepsilon > 0$ there is a closed set $\mathbf{F} \subset \mathbf{A}$ such that $m(\mathbf{A} \setminus \mathbf{F}) < \varepsilon$ and $f$ restricted to $\mathbf{F}$ is continuous.

2.2.28. Using the result in 2.1.38, construct a function $f$ , measurable on $\mathbb{R}$ , such that for any set $\mathbf{E}$ of measure zero, $f$ is not continuous at any point in $\mathbb{R} \setminus \mathbf{E}$ .

2.2.29. Let $f: [0, a] \to \mathbb{R}$ be a measurable function. Show that there exists a monotone decreasing function $g$ on $[0, a]$ such that for any real $y$ ,

$$
m (\{x \in [ 0, a ]: f (x) > y \}) = m (\{x \in [ 0, a ]: g (x) > y \}).
$$

2.2.30. Let $\{f_n\}$ be a sequence of real-valued functions measurable on $\mathbf{A}$ . We say that $\{f_n\}$ converges in measure to a measurable function $f$ if for every $\varepsilon > 0$ , $\lim_{n \to \infty} m(\{x \in \mathbf{A} : |f_n(x) - f(x)| > \varepsilon\}) = 0$ . Show that if a sequence $\{f_n\}$ converges in measure to $f$ and $\{f_n\}$ converges in measure to $g$ , then $f = g$ a.e. on $\mathbf{A}$ .

2.2.31. Prove the following theorem of Lebesgue. If $m(\mathbf{A}) < \infty$ and $\{f_n\}$ converges to $f$ a.e. on $\mathbf{A}$ , then $\{f_n\}$ converges in measure to $f$ .

2.2.32. Show by example that the assumption $m(\mathbf{A}) < \infty$ is essential in the Lebesgue theorem stated above.

2.2.33. Give an example of a sequence of measurable functions on the interval $[0,1]$ that converges in measure on $[0,1]$ but is not convergent at any point of that interval.

2.2.34. Let $\{f_n\}$ be the marching sequence defined in the solution to the previous problem. Find a subsequence of it that converges to the zero function a.e. on $[0,1]$ .

2.2.35. Prove the following Riesz theorem. Every sequence $\{f_n\}$ convergent in measure to $f$ on $\mathbf{A}$ contains a subsequence converging to $f$ a.e. on $\mathbf{A}$ .

2.2.36. Let $\{f_n\}$ be a sequence of monotonically increasing functions on $(a, b)$ . Show that if the sequence converges in measure to $f$ , then $\lim_{n \to \infty} f_n(x) = f(x)$ at each point $x$ of continuity of $f$ .

2.2.37. Prove the following Fréchet theorem. If $f$ is a real-valued measurable function on $\mathbf{A}$ , then there is an $\mathcal{F}_{\sigma}$ set $\mathbf{H}$ such that $m(\mathbf{A} \setminus \mathbf{H}) = 0$ and $f$ restricted to $\mathbf{H}$ is in the first Baire class (that is, $f$ is a pointwise limit of a sequence of continuous functions on $\mathbf{H}$ ).

2.2.38. Prove the following Vitali theorem. If $f$ is a real-valued measurable function on $\mathbf{A}$ , then there is a function $g$ in the second Baire class (that is, $g$ is a pointwise limit of a sequence of functions in the first Baire class on $\mathbf{A}$ ) such $f = g$ a.e.

# 2.3. Lebesgue Integration

The Lebesgue integral of a simple function $\varphi(x) = \sum_{i=1}^{n} c_i \chi_{\mathbf{A}_i}(x)$ on $\mathbf{A}$ , where $\mathbf{A} = \bigcup_{i=1}^{n} \mathbf{A}_i$ , and the $\mathbf{A}_i$ are pairwise disjoint measurable sets, is defined as

$$
\int_ {A} \varphi d m = \sum_ {i = 1} ^ {n} c _ {i} m (A _ {i}).
$$

If $f$ is measurable and nonnegative on $\mathbf{A}$ , we define

$$
\int_ {\mathbf {A}} f d m = \sup  \int_ {\mathbf {A}} \varphi d m,
$$

where the supremum is taken over all simple functions $\varphi$ such that $0 \leq \varphi \leq f$ . The function $f$ is said to be integrable (or summable) on $\mathbf{A}$ in the Lebesgue sense if its integral over $\mathbf{A}$ is finite. If $f$ is measurable on $\mathbf{A}$ , then we define

$$
\int_ {A} f d m = \int_ {A} f ^ {+} d m - \int_ {A} f ^ {-} d m,
$$

where $f^+ = \max \{f, 0\}$ and $f^- = -\min \{f, 0\}$ . We say that $f$ is integrable on $\mathbf{A}$ if $f^+$ and $f^-$ are integrable on $\mathbf{A}$ .

Let $p$ be a positive real number. A measurable function $f$ defined on $\mathbf{A}$ is said to belong to the space $L^p(\mathbf{A})$ if $\int_{\mathbf{A}} |f|^p dm < \infty$ . In this case we will write $\| f \|_p = \left( \int_{\mathbf{A}} |f|^p dm \right)^{1/p}$ . In the case when $\mathbf{A} = [a, b]$ we write $f \in L^p[a, b]$ .

A measurable function $f$ defined on $\mathbf{A}$ is said to be essentially bounded if $m(\{x \in \mathbf{A} : |f(x)| > r\}) = 0$ for some real number $r$ . In this case we define the essential supremum of $f$ by

$$
\| f \| _ {\infty} = \inf  \{r: m (\{x \in \mathbf {A}: | f (x) | > r \}) = 0 \}.
$$

Then the set $\mathbf{E} = \{x\in \mathbf{A}:|f(x)| > \| f\|_{\infty}\}$ is of measure zero and $|f(x)|\leq \| f\|_{\infty}$ outside $\mathbf{E}$ . Thus $|f(x)|\leq \| f\|_{\infty}$ a.e.

We will often use the following theorems:

Theorem 1 (Lebesgue's Monotone Convergence Theorem). Suppose $\{f_n\}$ is an increasing sequence of nonnegative measurable functions on $\mathbf{A}$ . If $f(x) = \lim_{n\to \infty}f_n(x)$ , $x\in \mathbf{A}$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} f _ {n} d m = \int_ {\mathbf {A}} f d m.
$$

Theorem 2 (Fatou's Theorem). Suppose $\{f_n\}$ is a sequence of nonnegative and measurable functions on $\mathbf{A}$ . Then

$$
\int_ {A} \underline {{\lim }} f _ {n} d m \leq \underline {{\lim }} _ {n \rightarrow \infty} \int_ {A} f _ {n} d m.
$$

Theorem 3 (Lebesgue's Dominated Convergence Theorem). Suppose $\{f_n\}$ is a sequence of measurable functions on $\mathbf{A}$ and $f(x) = \lim_{n \to \infty} f_n(x)$ , $x \in \mathbf{A}$ . If there exists a function $g$ integrable on $\mathbf{A}$ and such that $|f_n(x)| \leq g(x)$ , $n = 1, 2, \ldots, x \in \mathbf{A}$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} f _ {n} d m = \int_ {\mathbf {A}} f d m.
$$

Theorem 4. If $f$ is Riemann integrable on $[a, b]$ , then $f$ is Lebesgue integrable and

$$
\int_ {a} ^ {b} f (x) d x = \int_ {[ a, b ]} f d m.
$$

2.3.1. Find the Lebesgue integral of the function $f$ defined by setting

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} & \text {i f} \quad x \in [ 0, 1 ] \setminus \mathbb {Q}, \\ 1 & \text {i f} \quad x \in [ 0, 1 ] \cap \mathbb {Q}. \end{array} \right.
$$

Is the function Riemann integrable on $[0,1]$ ?

2.3.2. Let $f$ be defined on $[0,1]$ as follows: $f(x) = 0$ if $x$ is an element of the Cantor set $\mathbf{C}$ and $f(x) = n$ on each removed interval of length $1/3^n$ (see, e.g., the solution to II, 1.3.1 for the definition of $\mathbf{C}$ ). Find $\int_{[0,1]} f dm$ .

2.3.3. Let $\mathbf{C}$ denote the Cantor set. Find $\int_{[0,1]} f dm$ , where

$$
f (x) = \left\{ \begin{array}{l l} \sin (\pi x) & \text {i f} \quad x \in [ 0, 1 / 2 ] \setminus \mathbf {C}, \\ \cos (\pi x) & \text {i f} \quad x \in [ 1 / 2, 1 ] \setminus \mathbf {C}, \\ x ^ {2} & \text {i f} \quad x \in \mathbf {C}. \end{array} \right.
$$

2.3.4. Prove that if $f$ is Lebesgue integrable on $\mathbf{A}$ , then, given $\varepsilon > 0$ , there is $\delta > 0$ such that $\int_{\mathbb{B}} |f| dm < \varepsilon$ whenever $\mathbf{B} \subset \mathbf{A}$ and $m(\mathbf{B}) < \delta$ ; that is, the Lebesgue integral is absolutely continuous with respect to the Lebesgue measure.

2.3.5. Show that if $f$ is a Lebesgue integrable function on $\mathbf{A}$ and $\mathbf{A}_n = \{x \in \mathbf{A} : |f(x)| \geq n\}$ , then $\lim_{n \to \infty} n \cdot m(\dot{\mathbf{A}}_n) = 0$ .

2.3.6. Show that if $f \geq 0$ on a set $\mathbf{A}$ of positive measure and $\int_{\mathbf{A}} f dm = 0$ , then $f = 0$ a.e. on $\mathbf{A}$ .

2.3.7. Show that if $\int_{\mathbf{B}} f dm = 0$ for every measurable subset $\mathbf{B}$ of $\mathbf{A}$ , $m(\mathbf{A}) > 0$ , then $f - 0$ a.c. on $\mathbf{A}$ .

2.3.8. Show that if $f$ is Lebesgue integrable on $\mathbf{A}$ and

$$
\left| \int_ {A} f d m \right| = \int_ {A} | f | d m,
$$

then either $f \geq 0$ a.e. on $\mathbf{A}$ or $f \leq 0$ a.e. on $\mathbf{A}$

2.3.9. Prove that if $\{f_n\}$ is a sequence of nonnegative and measurable functions on $\mathbf{A}$ such that $\lim_{n\to \infty}\int_{\mathbf{A}}f_ndm = 0$ , then $\{f_n\}$ converges to 0 in measure. Show by example that convergence in measure cannot be replaced by a.e. convergence.

2.3.10. For a sequence $\{f_n\}$ of measurable functions on a set $\mathbf{A}$ of finite measure, show that

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} \frac {| f _ {n} |}{1 + | f _ {n} |} d m = 0
$$

if and only if $\{f_n\}$ converges to 0 in measure. Show by example that the assumption $m(\mathbf{A}) < \infty$ cannot be omitted.

2.3.11. Suppose $f$ is nonnegative and measurable on a set $\mathbf{A}$ of finite measure. Prove that $f$ is Lebesgue integrable on $\mathbf{A}$ if and only if the series $\sum_{k=0}^{\infty} km(\mathbf{A}_k)$ , where $\mathbf{A}_k = \{x \in \mathbf{A} : k \leq f(x) < k + 1\}$ , converges.

2.3.12. Suppose $f$ is nonnegative and measurable on a set $\mathbf{A}$ of finite measure. Prove that $f$ is Lebesgue integrable on $\mathbf{A}$ if and only if the series $\sum_{k=0}^{\infty} m(\mathbf{B}_k)$ , where $\mathbf{B}_k = \{x \in \mathbf{A} : f(x) \geq k\}$ , converges.

2.3.13. Suppose $f$ is nonnegative and integrable on a set $A$ of finite measure. For $\varepsilon > 0$ , define

$$
S (\varepsilon) = \sum_ {n = 0} ^ {\infty} n \varepsilon m \left(\mathbf {A} _ {n}\right), \quad \text {w h e r e} \mathbf {A} _ {n} = \{x \in \mathbf {A}: n \varepsilon \leq f (x) <   (n + 1) \varepsilon \}.
$$

Prove that

$$
\lim  _ {\varepsilon \rightarrow 0} S (\varepsilon) = \int_ {A} f d m.
$$

2.3.14. Let $\{f_n\}$ be a sequence of nonnegative functions converging to $f$ on $\mathbb{R}$ , and suppose that $\lim_{n \to \infty} \int_{\mathbb{R}} f_n dm - \int_{\mathbb{R}} f dm < \infty$ . Show that for each measurable set $\mathbf{A}$ ,

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} f _ {n} d m = \int_ {\mathbf {A}} f d m.
$$

2.3.15. Suppose that $\{f_n\}$ is a sequence of real-valued functions integrable on a set $\mathbf{A}$ of finite measure. Show that if the sequence is uniformly convergent on $\mathbf{A}$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} f _ {n} d m = \int_ {\mathbf {A}} \lim  _ {n \rightarrow \infty} f _ {n} d m.
$$

2.3.16. Let $\{f_n\}$ be a sequence of functions converging to $f$ on $\mathbf{A}$ such that $\int_{\mathbf{A}} |f_n|^p dm < \infty$ and $\int_{\mathbf{A}} |f|^p dm < \infty, 1 \leq p < \infty$ . Show that

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} | f _ {n} | ^ {p} d m = \int_ {\mathbf {A}} | f | ^ {p} d m
$$

if and only if

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} | f _ {n} - f | ^ {p} d m = 0.
$$

2.3.17. Suppose that $\{f_n\}$ is a sequence of measurable functions on $\mathbf{A}$ such that $|f_n| \leq g$ , where $g$ is integrable on $\mathbf{A}$ . Show that

$$
\int_ {A} \lim  _ {n \rightarrow \infty} f _ {n} d m \leq \lim  _ {n \rightarrow \infty} \int_ {A} f _ {n} d m \leq \varlimsup_ {n \rightarrow \infty} \int_ {A} f _ {n} d m \leq \int_ {A} \varliminf_ {n \rightarrow \infty} f _ {n} d m.
$$

2.3.18. Let $f_{n}(x) = nx^{n - 1} - (n + 1)x^{n}, x \in (0,1)$ . Show that

$$
\int_ {(0, 1)} \sum_ {n = 1} ^ {\infty} f _ {n} d m \neq \sum_ {n = 1} ^ {\infty} \int_ {(0, 1)} f _ {n} d m
$$

and $\sum_{n = 1}^{\infty}\int_{(0,1)}|f_n|dm = \infty .$

2.3.19. Let $\{f_n\}$ be a sequence of measurable functions on $\mathbf{A}$ such that $\sum_{n=1}^{\infty} \int_{\mathbf{A}} |f_n| dm < \infty$ . Show that $\sum_{n=1}^{\infty} f_n$ is integrable on $\mathbf{A}$ and

$$
\int_ {A} \sum_ {n = 1} ^ {\infty} f _ {n} d m = \sum_ {n = 1} ^ {\infty} \int_ {A} f _ {n} d m.
$$

2.3.20. We say that functions $f_{n}, n = 1,2,\ldots$ , integrable on $\mathbf{A}$ are equi-integrable if for every $\varepsilon > 0$ there is $\delta > 0$ such that for every measurable subset $\mathbf{B}$ of $\mathbf{A}$ , $\int_{\mathbf{B}} |f_{n}| dm < \varepsilon$ for $n = 1,2,\ldots$ whenever $m(\mathbf{B}) < \delta$ . Show that if $\{f_{n}\}$ is a convergent sequence of equi-integrable functions on a set $\mathbf{A}$ of finite measure, then

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} f _ {n} d m = \int_ {\mathbf {A}} \lim  _ {n \rightarrow \infty} f _ {n} d m.
$$

2.3.21. Prove the following version of Lebesgue's dominated convergence theorem. Suppose $\{f_n\}$ is a sequence of measurable functions converging in measure on $\mathbf{A}$ to $f$ . If there exists a function $g$ integrable on $\mathbf{A}$ and such that $|f_n(x)| \leq g(x)$ , $n = 1, 2, \ldots, x \in \mathbf{A}$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} f _ {n} d m = \int_ {\mathbf {A}} f d m.
$$

2.3.22. Show that the theorem stated in 2.3.20 remains true when convergence is replaced by convergence in measure.

2.3.23. Suppose the sequence $\{f_n\}$ converges in measure to $f$ on a set $\mathbf{A}$ of finite measure, and $|f_n(x)| \leq C$ for $x \in \mathbf{A}, n = 1, 2, \ldots$ . Show that if $g$ is continuous on $[-C, C]$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} g (f _ {n}) d m = \int_ {\mathbf {A}} g (f) d m.
$$

2.3.24. Suppose that $\{f_n\}$ is a sequence of functions defined on a set $\mathbf{A}$ of finite measure that converges in measure on $\mathbf{A}$ to $f$ . Show that

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} \sin (f _ {n}) d m = \int_ {\mathbf {A}} \sin (f) d m.
$$

2.3.25. Suppose $f \in L^{p}[a, b]$ , $1 \leq p < \infty$ . Show that, given $\varepsilon > 0$ , there is

(i) a simple function $\varphi$ such that $\int_{[a,b]}|f - \varphi|^p dm < \varepsilon$ ,   
(ii) a step function $\psi$ such that $\int_{[a,b]}|f - \psi|^p dm < \varepsilon$ .

2.3.26. Find a measurable function $f$ bounded on $[a, b]$ and such that

$$
\| f - \psi \| _ {\infty} = \sup  \left\{| f (x) - \psi (x) |: x \in [ a, b ] \right\} \geq 1 / 2
$$

for all step functions $\psi$ .

2.3.27. Suppose $f \in L^{p}[a, b]$ , $1 \leq p < \infty$ . Show that, given $\varepsilon > 0$ , there is a continuous function $g$ such that $\int_{[a, b]} |f - g|^{p} dm < \varepsilon$ .

2.3.28. Show, by example, that the result in the previous problem is false if $p = \infty$ .

2.3.29. Suppose that $g$ satisfies a Lipschitz condition on $\mathbb{R}$ . Prove that if $\{f_n\}$ is a sequence of measurable functions on $[a, b]$ that converges in measure to $f$ and there is a Lebesgue integrable function $G$ such that $|f_n(x)| \leq G(x)$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {[ a, b ]} g (f _ {n}) d m = \int_ {[ a, b ]} g (f) d m.
$$

2.3.30. Suppose that $1 \leq p < \infty$ , and that $f$ is measurable on $\mathbf{A}$ and such that $|f|^p$ is integrable on $\mathbf{A}$ . Prove that, given $\varepsilon > 0$ , there is a continuous function $g$ vanishing outside a finite interval and such that

$$
\int_ {A} | f - g | ^ {p} d m <   \varepsilon .
$$

2.3.31. Let $\{f_n\}$ be a sequence of functions in $L^p[a, b]$ , $1 < p < \infty$ , which converge almost everywhere on $[a, b]$ to $f$ . Suppose that there is a constant $C$ such that $\| f_n \|_p \leq C$ for $n = 1, 2, \ldots$ . Prove that for each $g$ in $L^q[a, b]$ , $1/p + 1/q = 1$ ,

$$
\lim  _ {n \rightarrow \infty} \int_ {[ a, b ]} f _ {n} g d m = \int_ {[ a, b ]} f g d m.
$$

2.3.32. Let $\{f_n\}$ be a sequence of functions in $L^p [a,b]$ , $1\leq p < \infty$ , which converges in norm to $f\in L^{p}[a,b]$ , and let $\{g_{n}\}$ be a sequence of measurable functions such that $|g_{n}|\leq C$ for $n = 1,2,\ldots$ , and $g_{n}\to g$ a.e. Show that $f_{n}g_{n}\rightarrow fg$ in $L^p [a,b]$ .

2.3.33. Show that if $f$ is an essentially bounded function on $[a, b]$ , then

$$
\lim  _ {p \rightarrow \infty} \left(\int_ {[ a, b ]} | f | ^ {p} d m\right) ^ {1 / p} = \| f \| _ {\infty}.
$$

(Compare with 1.4.41.)

2.3.34. Prove the Jensen inequality for Lebesgue integrals (see also 1.6.29). Suppose that $f$ is Lebesgue integrable on $[a, b]$ . If $\varphi$ is convex on $\mathbb{R}$ , then

$$
\varphi \left(\frac {1}{b - a} \int_ {[ a, b ]} f d m\right) \leq \frac {1}{b - a} \int_ {[ a, b ]} \varphi (f) d m.
$$

2.3.35. Show that if $m(\mathbf{A}) < \infty$ and $0 < p_1 < p_2 < \infty$ , then $L^{p_2}(\mathbf{A}) \subset L^{p_1}(\mathbf{A})$ , and the inequality

$$
\| f \| _ {p _ {1}} \leq \| f \| _ {p _ {2}} (m (\mathbf {A})) ^ {\frac {1}{p _ {1}} - \frac {1}{p _ {2}}}
$$

holds for $f\in L^{p_2}(\mathbf{A})$

2.3.36. Show that if $f \in L^{p_1}(\mathbf{A}) \cap L^{p_2}(\mathbf{A})$ , where $0 < p_1 < p_2 < \infty$ and if $p_1 < r < p_2$ , then $f \in L^r (\mathbf{A})$ , and the function $\varphi$ defined by $\varphi (r) = \ln \| f\|_{r}^{r}$ is convex on $[p_1,p_2]$ .

2.3.37. Prove that if $f \in L^{1}[a, b]$ and $f \neq 0$ a.e. on $[a, b]$ , then

$$
\lim  _ {p \rightarrow 0 ^ {+}} \left(\frac {1}{b - a} \int_ {[ a, b ]} | f | ^ {p} d m\right) ^ {1 / p} = \exp \left(\frac {1}{b - a} \int_ {[ a, b ]} \ln | f | d m\right).
$$

2.3.38. For any $t \in \mathbb{R}$ , the translate of $f$ by $t$ is defined by setting $f_t(x) = f(x + t)$ . Let $f$ be integrable on $\mathbb{R}$ . Show that:

(a) $\int_{\mathbb{R}} f dm = \int_{\mathbb{R}} f_t dm.$

(b) If $g$ is a bounded measurable function, then

$$
\lim  _ {t \rightarrow 0} \int_ {\mathbb {R}} | g (f - f _ {t}) | d m = 0.
$$

2.3.39. Suppose that $1 \leq p < \infty$ and $f \in L^{p}(\mathbb{R})$ ; that is, $\int_{\mathbb{R}} |f|^{p} dm < \infty$ . Prove that $\lim_{t \to 0} \int_{\mathbb{R}} |f - f_{t}|^{p} dm = 0$ , where $f_{t}$ is the translate of $f$ by $t$ defined in the previous problem.

2.3.40. Suppose that $f$ is nonnegative and measurable on a set $\mathbf{A}$ such that $0 < m(\mathbf{A}) < \infty$ . Suppose also that there are positive $\alpha$ and $\beta$ such that

$$
\frac {1}{m (\mathbf {A})} \int_ {\mathbf {A}} f d m \geq \alpha \quad \text {a n d} \quad \frac {1}{m (\mathbf {A})} \int_ {\mathbf {A}} f ^ {2} d m \leq \beta .
$$

Show that if $0 < \delta < 1$ and $\mathbf{A}_{\delta} = \{x \in \mathbf{A} : f(x) \geq \alpha \delta\}$ , then

$$
m (\mathbf {A} _ {\delta}) \geq m (\mathbf {A}) (1 - \delta) ^ {2} \frac {\alpha^ {2}}{\beta}.
$$

# 2.4. Absolute Continuity, Differentiation and Integration

A real-valued function $f$ defined on $[a, b]$ is said to be absolutely continuous on $[a, b]$ if, given $\varepsilon > 0$ , there is $\delta > 0$ such that

$$
\sum_ {k = 1} ^ {n} | f (x _ {k}) - f \left(x _ {k} ^ {\prime}\right) | <   \varepsilon
$$

for every finite collection $\{(x_k, x_k')\}$ of pairwise disjoint open intervals of $[a, b]$ with

$$
\sum_ {k = 1} ^ {n} \left(x _ {k} ^ {\prime} - x _ {k}\right) <   \delta .
$$

From now on we will deal only with Lebesgue integrals, and we will write $\int_{a}^{b} f(x) dx$ instead of $\int_{\{a, b\}} f dm$ . We will use the following well-known theorems.

Theorem 1. Let $f$ be an increasing real-valued function on $[a, b]$ . Then $f$ is differentiable almost everywhere. The derivative $f'$ is measurable, and

$$
\int_ {a} ^ {b} f ^ {\prime} (x) d x \leq f (b) - f (a).
$$

Theorem 2. A function $f$ on $[a, b]$ has the form

$$
f (x) = f (a) + \int_ {a} ^ {x} g (t) d t
$$

for some integrable function $g$ on $[a, b]$ if and only if $f$ is absolutely continuous on $[a, b]$ . In this case we have $g(x) = f'(x)$ a.e. on $[a, b]$ .

2.4.1. Prove that if $f$ is absolutely continuous on $[a, b]$ , then it is of bounded variation on $[a, b]$ .

2.4.2. Give an example of a function continuous on $[a, b]$ but not absolutely continuous on that interval.

# 2.4.3. Let

$$
f (x) = \left\{ \begin{array}{l l} x ^ {\alpha} \sin \frac {1}{x ^ {\beta}} & \text {i f} \quad x \in (0, 1 ], \\ 0 & \text {i f} \quad x = 0. \end{array} \right.
$$

Show that if $0 < \beta < \alpha$ , then $f$ is absolutely continuous on $[0,1]$ , but if $0 < \alpha \leq \beta$ , then it is not absolutely continuous.

# 2.4.4. Let

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} | \sin (1 / x) | & \text {i f} \quad x \in (0, 1 ], \\ 0 & \text {i f} \quad x = 0, \end{array} \right.
$$

$g(x) = \sqrt{x}$ . Show that $f$ and $g$ are absolutely continuous on $[0,1]$ , and that the composite $f(g)$ is absolutely continuous but $g(f)$ is not.

2.4.5. Show that if $f$ and $g$ are absolutely continuous and $g$ is monotone, then $f(g)$ is absolutely continuous.

2.4.6. Show that an absolutely continuous function $f:[a,b] \to \mathbb{R}$ transforms

(a) sets of measure zero into sets of measure zero,   
(b) measurable sets into measurable sets.

2.4.7. Is a continuous function of bounded variation on $[a, b]$ , $a < b$ , absolutely continuous on $[a, b]$ ?

2.4.8. Let $f$ be a continuous real-valued function on $[a, b]$ . For $y \in \mathbb{R}$ , let $\mathbf{A}_y = \{x \in [a, b] : f(x) = y\}$ . Define the so-called Banach indicatrix of $f$ by setting

$$
v (y) = \left\{ \begin{array}{l l} \| \mathbf {A} _ {y} & \text {i f} \quad \mathbf {A} _ {y} \text {i s f i n i t e ,} \\ \infty & \text {i f} \quad \mathbf {A} _ {y} \text {i s i n f i n i t e ,} \end{array} \right.
$$

where $\sharp \mathbf{A}_y$ denotes the number of elements of $\mathbf{A}_y$ . Show that $v$ is measurable and

$$
\int_ {\mathbb {R}} v (y) d y = V (f; a, b).
$$

2.4.9. Prove the following theorem of Banach and Zarecki. If $f$ is continuous and of bounded variation on $[a, b]$ and if $f$ maps sets of measure zero into sets of measure zero, then $f$ is absolutely continuous on $[a, b]$ .

2.4.10. Let $f$ and $g$ be absolutely continuous. Show that $f(g)$ is absolutely continuous if and only if it is of bounded variation.

2.4.11. Suppose $f$ is integrable on $[a, b]$ and define $F(x) = \int_{a}^{x} f(t) dt$ . Prove that

$$
V (F; n, b) = \int_ {a} ^ {b} | f (t) | d t.
$$

(Compare with 1.2.21.)

2.4.12. Assume that $g$ is strictly increasing and absolutely continuous on $[a, b]$ with $g(a) = c$ and $g(b) = d$ .

(a) Show that for any measurable set $\mathbf{E} \subset [a, b]$ ,

$$
m (g (\mathbf {E})) = \int_ {\mathbf {E}} g ^ {\prime} d m.
$$

(b) If $\mathbf{H} = \{x\in [a,b]:g'(x)\neq 0\}$ and $\mathbf{A}$ is a subset of $[c,d]$ with $m(\mathbf{A}) = 0$ then $g^{-1}(\mathbf{A})\cap \mathbf{H}$ has measure zero.

(c) If $\mathbf{B}$ is a measurable subset of $[c,d]$ and $\mathbf{H}$ is as in (b), then $\mathbf{C} = g^{-1}(\mathbf{B})\cap \mathbf{H}$ is measurable and

$$
m (\mathbf {B}) = \int_ {\mathbf {C}} g ^ {\prime} d m = \int_ {a} ^ {b} \chi_ {\mathbf {B}} (g (x)) g ^ {\prime} (x) d x.
$$

2.4.13. Using the result in the preceding problem, prove the following change of variable formula for Lebesgue integrals. Assume that $g$ is strictly increasing and absolutely continuous on $[a, b]$ with $g(a) = c$ and $g(b) = d$ . If $f$ is integrable on $[c, d]$ , then

$$
\int_ {c} ^ {d} f (t) d t = \int_ {a} ^ {b} f (g (x)) g ^ {\prime} (x) d x.
$$

2.4.14. Let $f$ and $g$ be integrable on $[a, b]$ , and set

$$
F (x) = \alpha + \int_ {a} ^ {x} f (t) d t \quad \text {a n d} \quad G (x) = \beta + \int_ {a} ^ {x} g (t) d t.
$$

Prove that

$$
\int_ {a} ^ {b} G (t) f (t) d t + \int_ {a} ^ {b} g (t) F (t) d t = F (b) G (b) - F (a) G (a).
$$

2.4.15. Prove the following formula for integration by parts for Lebesgue integrals and absolutely continuous functions. If $f$ and $g$ are absolutely continuous functions on $[a, b]$ , then

$$
\int_ {a} ^ {b} f (t) g ^ {\prime} (t) d t + \int_ {a} ^ {b} f ^ {\prime} (t) g (t) d t = f (b) g (b) - f (a) g (a).
$$

2.4.16. A monotone function $f$ on $[a, b]$ is called singular if $f' = 0$ . a.e. Show that any monotone increasing function is the sum of an absolutely continuous function and a singular function.

2.4.17. Construct a function $f$ which is strictly increasing, continuous and singular on [0, 1].

2.4.18. Prove that a function $f$ on $\mathbb{R}$ has the form

$$
f (x) = \int_ {(- \infty , x ]} \varphi d m = \int_ {- \infty} ^ {x} \varphi (t) d t,
$$

with some integrable function $\varphi$ on $\mathbb{R}$ , if and only if $f$ is absolutely continuous on $[-K, K]$ for all $K > 0$ , $\lim_{x \to -\infty} f(x) = 0$ and $V(f; -\infty, \infty) = \lim_{K \to +\infty} V(f; -K, K) < \infty$ .

2.4.19. Show that if $f$ and $g$ are functions on $\mathbb{R}$ satisfying the conditions of the preceding problem, then

$$
\begin{array}{l} \int_ {\mathbb {R}} f (t) g ^ {\prime} (t) d t + \int_ {\mathbb {R}} f ^ {\prime} (t) g (t) d t = \int_ {\mathbb {R}} f ^ {\prime} (t) d t \cdot \int_ {\mathbb {R}} g ^ {\prime} (t) d t \\ = \lim  _ {x \rightarrow \infty} f (x) \cdot \lim  _ {x \rightarrow \infty} g (x). \\ \end{array}
$$

2.4.20. Let $f \in L^{p}[a, b]$ , $1 \leq p < \infty$ , and put $f(x) = 0$ for $x \notin [a, b]$ . For $h > 0$ , we define $f_{h}$ by setting

$$
f _ {h} (x) = \frac {1}{2 h} \int_ {x - h} ^ {x + h} f (t) d t.
$$

Show that $f_h$ is continuous and $\| f_h \|_p \leq \| f \|_p$ (compare with 1.6.34).

2.4.21. Prove that in the notation and under the assumptions of 2.4.20, $\lim_{h\to 0}\| f_h - f\| _p = 0$

2.4.22. Suppose that $f \in L^{1}[a, b]$ and that $x \in (a, b)$ is such that $f(x) \neq \pm \infty$ . Then $x$ is called a Lebesgue point for $f$ if

$$
\lim  _ {h \rightarrow 0} \frac {1}{h} \int_ {x} ^ {x + h} | f (t) - f (x) | d t = 0.
$$

Show that if $x$ is a Lebesgue point for $f$ , then the function $F(x) = \int_{a}^{x} f(t) dt$ is differentiable at $x$ and $F'(x) - f(x)$ .

2.4.23. Show that each point of continuity of $f \in L^{1}[a,b]$ is a Lebesgue point for $f$ .   
2.4.24. Prove that almost every point of $[a, b]$ is a Lebesgue point for $f \in L^{1}[a, b]$ .   
2.4.25. Show that almost all points of a measurable set $\mathbf{A}$ are points of density of $\mathbf{A}$ . (See 2.1.40 for the definition of a point of density.)   
2.4.26. A set $\mathbf{A} \subset \mathbb{R}$ is said to have outer density $d$ at $x$ if the limit

$$
\lim  _ {h \rightarrow 0 ^ {+}} \frac {m ^ {*} (\mathbf {A} \cap [ x - h , x + h ])}{2 h}
$$

exists and is equal to $d$ . If $d = 1$ , then $x$ is called a point of outer density of $A$ , and if $d = 0$ , then $x$ is called a point of outer dispersion of $A$ . Prove the following generalization of the result in the previous problem. If $A$ is any set (measurable or not), then almost all points in $A$ are points of its outer density. A necessary and sufficient condition that $A$ be measurable is that almost all points in $A^c$ are points of outer dispersion of $A$ .

2.4.27. Assume that a real-valued function $f$ (measurable or not) is defined on $[a, b]$ . We say that $x_0 \in [a, b]$ is a point of approximate continuity of $f$ , if for each $\varepsilon > 0$ ,

$$
\lim  _ {h \rightarrow 0} \frac {m ^ {*} ([ x _ {0} - h , x _ {0} + h ] \cap \{x \in [ a , b ] : | f (x) - f (x _ {0}) | \geq \varepsilon \})}{2 h} = 0.
$$

Prove that a real-valued function $f$ is measurable on $[a, b]$ if and only if almost all points of $[a, b]$ are points of approximate continuity of $f$ .

2.4.28. Show that a Lebesgue integrable function on $[a, b]$ is approximately continuous at each of its Lebesgue points. Show by example that the converse is not true.

2.4.29. Show that if $f$ is measurable and bounded on $[a, b]$ , then $x \in (a, b)$ is a Lebesgue point for $f$ if and only if $x$ is a point of approximate continuity of $f$ .

2.4.30. An alternate definition of approximate continuity is that $f$ is approximately continuous at $x_0$ provided there is a measurable set $A$ such that $x_0$ is a point of density for $A$ and such that the restriction of $f$ to $A$ is continuous at $x_0$ . Show that this definition is equivalent to the one given in 2.4.27.

2.4.31. Give an example of a bounded function $f:[0,1] \to \mathbb{R}$ which is not Riemann integrable but is a derivative of some function $F$ on [0,1].

2.4.32. Suppose $f$ is integrable on $[a, b]$ and for $t \in \mathbb{R}$ define $G(t) = m(\{x \in [a, b] : f(x) < t\})$ . Prove that

$$
\int_ {a} ^ {b} f (x) d x = \int_ {- \infty} ^ {\infty} t d (G (t)),
$$

where

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} t d (G (t)) = \int_ {- \infty} ^ {0} t d (G (t)) + \int_ {0} ^ {\infty} t d (G (t)) \\ = \lim  _ {A \rightarrow - \infty} \int_ {A} ^ {0} t d (G (t)) + \lim  _ {B \rightarrow \infty} \int_ {0} ^ {B} t d (G (t)). \\ \end{array}
$$

# 2.5. Fourier Series

For $f \in L^{1}[-\pi, \pi]$ , the Fourier coefficients of $f$ are given by

$$
a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x d x, \quad b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \sin n x d x.
$$

The series

$$
\frac {1}{2} a _ {0} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x)
$$

is the Fourier series of $f$ , and we write

$$
f (x) \sim \frac {1}{2} a _ {0} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right).
$$

We denote by $s_n(x)$ the $n$ th partial sum of the Fourier series of $f$ ; that is, $s_n(x) = \frac{1}{2} a_0 + \sum_{k=1}^{n} (a_k \cos kx + b_k \sin kx)$ .

2.5.1. Show that if $\rho_{n} = \sqrt{a_{n}^{2} + b_{n}^{2}}$ , then

$$
\sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right) = \sum_ {n = 1} ^ {\infty} \rho_ {n} \sin \left(n x + \alpha_ {n}\right),
$$

with some $\alpha_{n}$

2.5.2. Show that if $a_n$ and $b_n$ are the Fourier coefficients of $f \in L^1[-\pi, \pi]$ , then

$$
\lim  _ {n \rightarrow \infty} a _ {n} = \lim  _ {n \rightarrow \infty} b _ {n} = 0.
$$

2.5.3. Suppose that $f$ is a 2π-periodic function that satisfies the Lipschitz condition of order $\alpha$ ( $0 < \alpha \leq 1$ ); that is, $f(x + h) - f(x) = O(|h|^{\alpha})$ as $h \to 0$ uniformly with respect to $x$ . Show that if $a_n$ and $b_n$ are the Fourier coefficients of $f$ , then

$$
a _ {n} = O \left(n ^ {- \alpha}\right) \quad \text {a n d} \quad b _ {n} = O \left(n ^ {- \alpha}\right).
$$

2.5.4. Show that if $f$ is of bounded variation on $[-\pi, \pi]$ , then

$$
a _ {n} = O (n ^ {- 1}) \quad \text {a n d} \quad b _ {n} = O (n ^ {- 1}).
$$

2.5.5. Show that if $f$ is a $2\pi$ -periodic function that is absolutely continuous on $[-\pi, \pi]$ , then

$$
a _ {n} = o (n ^ {- 1}) \quad a n d \quad b _ {n} = o (n ^ {- 1}).
$$

2.5.6. Show that if $f$ is a 2π-periodic function and $f \in C^k(\mathbb{R})$ , then

$$
a _ {n} = o \left(n ^ {- k}\right) \quad \text {a n d} \quad b _ {n} = o \left(n ^ {- k}\right).
$$

2.5.7. Show that for $f \in L^{1}[-\pi, \pi]$ , the $n$ th partial sum of the Fourier series of $f$ , that is, $s_{n}(x) = \frac{1}{2} a_{0} + \sum_{k=1}^{n} (a_{k} \cos kx + b_{k} \sin kx)$ , is given by

$$
s _ {n} (x) = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (t) \frac {\sin \left(n + \frac {1}{2}\right) (t - x)}{2 \sin \frac {1}{2} (t - x)} d t.
$$

2.5.8. Assume that $f$ is a periodic function on $\mathbb{R}$ with period $2\pi$ , and that $f$ is integrable on $[-\pi, \pi]$ . Show that if $s_n$ denotes the $n$ th partial sum of the Fourier series of $f$ , then

$$
s _ {n} (x) = \frac {1}{\pi} \int_ {0} ^ {\pi} \left(f (x + t) + f (x - t)\right) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t.
$$

2.5.9. Prove the Dini-Lipschitz test for convergence of Fourier series. Suppose $f$ is a periodic function on $\mathbb{R}$ with period $2\pi$ that is integrable on $[-\pi, \pi]$ . If $f$ satisfies the condition $|f(x_0 + t) - f(x_0)| \leq L |t|^{\alpha}$ for $|t| < \delta$ with some positive $L, \delta$ and $0 < \alpha \leq 1$ , then the Fourier series of $f$ at $x_0$ converges to $f(x_0)$ .

2.5.10. Prove the Dirichlet-Jordan test for convergence of Fourier series. Assume that $f$ is a $2\pi$ -periodic function integrable on $[-\pi, \pi]$ and that $f$ is of bounded variation on $[x_0 - \delta, x_0 + \delta]$ . Show that the Fourier series of $f$ at $x_0$ converges to $\frac{1}{2} (f(x_0^+) + f(x_0^-))$ .

2.5.11. Show by example that the Dirichlet-Jordan test does not include the Dini-Lipschitz test and that the Dini-Lipschitz test does not include the Dirichlet-Jordan test.

2.5.12. Show that

$$
\frac {\pi - x}{2} = \sum_ {n = 1} ^ {\infty} \frac {\sin n x}{n}, \quad 0 <   x <   2 \pi ,
$$

and deduce that

$$
\frac {\pi}{4} = \sum_ {n = 1} ^ {\infty} \frac {\sin (2 n - 1) x}{2 n - 1}, \quad 0 <   x <   \pi ,
$$

$$
\frac {\pi}{4} = 1 - \frac {1}{3} + \frac {1}{5} - \frac {1}{7} + \dots ,
$$

$$
\frac {\pi}{2 \sqrt {3}} = 1 - \frac {1}{5} + \frac {1}{7} - \frac {1}{1 1} + \frac {1}{1 3} - \dots .
$$

2.5.13. For $x \in (0, 2\pi)$ , find the sums of the following series:

$$
\sum_ {n = 1} ^ {\infty} \frac {\cos n x}{n ^ {2}} \quad \text {a n d} \quad \sum_ {n = 1} ^ {\infty} \frac {\sin n x}{n ^ {3}}.
$$

2.5.14. Show that in 2.5.4 big $O$ 's cannot be replaced by little $o$ 's.

2.5.15. Let $f$ be a $2\pi$ -periodic function such that $f(x) = \frac{\pi - x}{2}$ for $x \in [0, 2\pi)$ , and let $s_n(x)$ denote the $n$ th partial sum of its Fourier series (see 2.5.12). Show that if $x_n$ is the smallest positive number at which $s_n(x)$ attains its local maximum, then $\lim_{n \to \infty} s_n(x_n) = \int_0^\pi \frac{\sin x}{x} dx$ .

2.5.16. Show that for $a \neq 0$ ,

$$
e ^ {a x} = \frac {e ^ {2 a \pi} - 1}{\pi} \left(\frac {1}{2 a} + \sum_ {n = 1} ^ {\infty} \frac {a \cos n x - n \sin n x}{a ^ {2} + n ^ {2}}\right), \quad 0 <   x <   2 \pi ,
$$

$$
e ^ {a x} = \frac {e ^ {a \pi} - 1}{a \pi} + \frac {2}{\pi} \sum_ {n = 1} ^ {\infty} ((- 1) ^ {n} e ^ {a \pi} - 1) \frac {a \cos n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   \pi ,
$$

$$
e ^ {a x} = \frac {2}{\pi} \sum_ {n = 1} ^ {\infty} (1 - (- 1) ^ {n} e ^ {a \pi}) \frac {n \sin n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   \pi .
$$

Find the sums of the above series when $x = 0$ .

2.5.17. For $0 < x < 2\pi$ and $a \neq 0$ , find the sums of the following series:

$$
\sum_ {n = 1} ^ {\infty} \frac {a \cos n x}{a ^ {2} + n ^ {2}}, \quad \sum_ {n = 1} ^ {\infty} \frac {n \sin n x}{a ^ {2} + n ^ {2}}.
$$

2.5.18. Show that

$$
x ^ {2} = \frac {\pi^ {2}}{3} + 4 \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} \frac {\cos n x}{n ^ {2}}, - \pi \leq x \leq \pi .
$$

Using this equality, show that

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}} = \frac {\pi^ {2}}{6} \quad \text {a n d} \quad \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n + 1}}{n ^ {2}} = \frac {\pi^ {2}}{1 2}.
$$

2.5.19. Suppose $f \in I^{1}[-\pi, \pi]$ and $a_{n}, b_{n}$ are the Fourier coefficients of $f$ . Show that

(a) if $f(x + \pi) = f(x)$ for $x \in [-\pi, 0]$ , then $a_{2n-1} = b_{2n-1} = 0$ ,   
(b) if $f(x + \pi) = -f(x)$ for $x \in [-\pi, 0]$ , then $a_{2n} = b_{2n} = 0$ .

2.5.20. Show that for $0 < x < \pi$ ,

$$
\cos x = \frac {8}{\pi} \sum_ {n = 1} ^ {\infty} \frac {n \sin 2 n x}{4 n ^ {2} - 1} \quad \text {a n d} \quad \sin x = \frac {2}{\pi} - \frac {4}{\pi} \sum_ {n = 1} ^ {\infty} \frac {\cos 2 n x}{4 n ^ {2} - 1}.
$$

2.5.21. Show that

$$
\ln \left| 2 \sin \frac {x}{2} \right| = - \sum_ {n = 1} ^ {\infty} \frac {\cos n x}{n} \quad \text {f o r} \quad x \neq 2 k \pi \quad (k \in \mathbb {Z}),
$$

and

$$
\ln \left| 2 \cos \frac {x}{2} \right| = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n + 1} \frac {\cos n x}{n} \quad \text {f o r} \quad x \neq (2 k + 1) \pi \quad (k \in \mathbb {Z}).
$$

2.5.22. Suppose a $2\pi$ -periodic function $f$ is in $L^1[-\pi, \pi]$ and $a_n, b_n$ are the Fourier coefficients of $f$ . Show that for $x \in [0, 2\pi]$ ,

$$
\int_ {0} ^ {x} \left(f (t) - \frac {1}{2} a _ {0}\right) d t = \sum_ {n = 1} ^ {\infty} \frac {a _ {n} \sin n x + b _ {n} (1 - \cos n x)}{n}.
$$

2.5.23. Prove that under the assumptions of the previous problem, the series $\sum_{n=1}^{\infty} \frac{b_n}{n}$ converges. Use this result to show that $\sum_{n=2}^{\infty} \frac{\sin nx}{\ln n}$ is not a Fourier series of any integrable function.

2.5.24. Prove that if $f \in L^{2}[-\pi, \pi]$ , then

$$
\frac {1}{2} a _ {0} ^ {2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \leq \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f ^ {2} (x) d x.
$$

(This inequality is known as Bessel's inequality.)

2.5.25. Use the results given in 2.5.22 and 2.5.24 to prove that if $f \in L^{2}[-\pi, \pi]$ , then for any measurable set $\mathbf{A} \subset [-\pi, \pi]$ ,

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} (f (x) - s _ {n} (x)) d x = 0,
$$

where $s_n$ denotes the $n$ th partial sum of the Fourier series of $f$ .

2.5.26. Show that if $f, g \in L^{2}[-\pi, \pi]$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {- \pi} ^ {\pi} g (x) (f (x) - s _ {n} (x)) d x = 0,
$$

where $s_n$ denotes the $n$ th partial sum of the Fourier series of $f$ .

2.5.27. Show that if $f, g \in L^{2}[-\pi, \pi]$ and

$$
\begin{array}{l} f (x) \sim \frac {1}{2} a _ {0} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right), \\ g (x) \sim \frac {1}{2} \alpha_ {0} + \sum_ {n = 1} ^ {\infty} (\alpha_ {n} \cos n x + \beta_ {n} \sin n x), \\ \end{array}
$$

then

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) g (x) d x = \frac {1}{2} a _ {0} \alpha_ {0} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \alpha_ {n} + b _ {n} \beta_ {n}\right).
$$

2.5.28. Show that if $f \in L^{2}[0, 2\pi]$ and $a_{n}, b_{n}$ are its Fourier coefficients, then

$$
\sum_ {n = 1} ^ {\infty} \frac {b _ {n}}{n} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} (\pi - x) f (x) d x.
$$

2.5.29. Show that if $f, g \in L^{1}[-\pi, \pi]$ have the same Fourier series, then $f = g$ a.e. on $[-\pi, \pi]$ .

2.5.30. Use Parseval's formula

(a) to sum the series

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {4}}, \quad \sum_ {n = 1} ^ {\infty} \frac {1}{(a ^ {2} + n ^ {2}) ^ {2}}, \quad \sum_ {n = 1} ^ {\infty} \frac {n ^ {2}}{(a ^ {2} + n ^ {2}) ^ {2}},
$$

(b) to compute

$$
\int_ {- \pi} ^ {\pi} \cos^ {6} x d x \quad \text {a n d} \quad \int_ {- \pi} ^ {\pi} \cos^ {8} x d x.
$$

2.5.31. Show that if $f \in L^{2}[-\pi, \pi]$ and $a_{n}, b_{n}$ are the Fourier coefficients of $f$ , then the series $\sum_{n=1}^{\infty} \frac{|a_{n}| + |b_{n}|}{n}$ converges.

2.5.32. Show that if a $2\pi$ -periodic function $f$ is continuously differentiable on $\mathbb{R}$ , then

$$
\max  _ {x \in \mathbb {R}} | f (x) - s _ {n} (x) | = o \left(n ^ {- 1 / 2}\right).
$$

2.5.33. Prove the following Bernstein theorem. If $f$ is $2\pi$ -periodic and satisfies the condition $|f(x + h) - f(x)| \leq L|h|^{\alpha}$ with some $L > 0$ and $\alpha > 1/2$ , then the series $\sum_{n=1}^{\infty} \sqrt{a_n^2 + b_n^2}$ converges.

2.5.34. Show that if $f$ is $2\pi$ -periodic and satisfies the Lipschitz condition $|f(x + h) - f(x)| \leq L|h|^{\alpha}$ with some $L > 0$ and $0 < \alpha \leq 1$ , then the series $\sum_{n=1}^{\infty} (|a_n|^{\beta} + |b_n|^{\beta})$ converges for $\beta > \frac{2}{2\alpha + 1}$ .

2.5.35. Suppose that $f$ is $2\pi$ -periodic and satisfies the condition $|f(x + h) - f(x)| \leq L|h|^{\alpha}$ with some positive $L$ and $\alpha$ . Show that if $f$ is of bounded variation on $[0, 2\pi]$ , then the series $\sum_{n=1}^{\infty} \sqrt{a_n^2 + b_n^2}$ converges.

2.5.36. Give an example of a continuous and $2\pi$ -periodic function whose Fourier series fails to converge on $\mathbb{R}$ .

2.5.37. Show that if a $2\pi$ -periodic function $f$ is bounded on $\mathbb{R}$ , then $|s_n(x)| = O(\ln n)$ .

2.5.38. Let $L_{ii}$ be the Lebesgue constants given by

$$
L _ {n} = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) x}{\sin \frac {x}{2}} \right| d x, \quad n \in \mathbb {N}.
$$

Show that $L_{n} = \frac{4}{\pi^{2}}\ln n + O(1)$

2.5.39. Show that if a $2\pi$ -periodic function $f$ is continuous on $\mathbb{R}$ , then $|s_n(x)| = o(\ln n)$ .

2.5.40. Assume that $f$ is $2\pi$ -periodic on $\mathbb{R}$ and $f \in L^{1}[-\pi, \pi]$ . Use the formula given in 2.5.8 to show that if

$$
\sigma_ {n} (x) = \frac {s _ {0} (x) + s _ {1} (x) + \cdots + s _ {n - 1} (x)}{n}
$$

(which is called the nth Cesàro mean of the Fourier series for $f$ ), then

$$
\sigma_ {n} (x) = \frac {1}{2 \pi n} \int_ {0} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} (f (x + t) + f (x - t)) d t.
$$

2.5.41. Show that if $f$ is $2\pi$ -periodic and $m \leq f(x) \leq M$ for all $x$ , then $m \leq \sigma_n(x) \leq M$ for all $x \in \mathbb{R}$ and $n \in \mathbb{N}$ . Show also that if for some $n$ and $x$ we have $\sigma_n(x) - M (\sigma_n(x) - m)$ , then $f(x) - M$ (resp. $f(x) = m$ ) a.e.

2.5.42. Show that if $f$ is $2\pi$ -periodic, $m \leq f(x) \leq M$ for all $x$ and

$$
n | a _ {n} | \leq A, \quad n | b _ {n} | \leq B, \quad n = 1, 2, \dots ,
$$

then for all values of $n$ and $\dot{x}$ ,

$$
m - A - B \leq s _ {n} (x) \leq M + A + B.
$$

Use the result in 2.5.12 to conclude that

$$
\left| \frac {\sin x}{1} + \frac {\sin 2 x}{2} + \dots + \frac {\sin n x}{n} \right| \leq \frac {\pi}{2} + 1
$$

for all values of $n$ and $x$ .

2.5.43. Assume that $\{c_n\}$ is a monotonically decreasing sequence of nonnegative numbers and there is a positive $A$ such that $n c_n \leq A$ for $n \in \mathbb{N}$ . Show that

$$
\left| \sum_ {k = 1} ^ {n} c _ {k} \sin k x \right| \leq A (\pi + 1)
$$

for all values of $n$ and $x$ .

2.5.44. Assume that $f$ is an odd function on $[-\pi, \pi]$ such that $|f(x)| \leq M$ for $x \in [-\pi, \pi]$ and its Fourier coefficients $b_n$ are nonnegative. Show that

$$
\left| s _ {n} (x) \right| = \left| \sum_ {k = 1} ^ {n} b _ {k} \sin k x \right| \leq 5 M.
$$

2.5.45. Assume that $f$ is an even function on $[-\pi, \pi]$ such that $|f(x)| \leq M$ for $x \in [-\pi, \pi]$ , and its Fourier coefficients $a_n$ are non-negative. Show that $\sum_{k=1}^{\infty} a_k < \infty$ .

2.5.46. Use the result in 2.5.12 to show that the function

$$
f (x) = \sum_ {n = 1} ^ {\infty} \frac {n ^ {3}}{n ^ {4} + 1} \sin n x
$$

is in $C^\infty (0,2\pi)$

2.5.47. Prove the following Fejer theorem. Assume that $f$ is $2\pi$ -periodic on $\mathbb{R}$ , $f \in L^{1}[-\pi, \pi]$ , and the limits $f(x^{-})$ and $f(x^{+})$ exist. Then

$$
\lim  _ {n \rightarrow \infty} \sigma_ {n} (x) = \frac {f \left(x ^ {-}\right) + f \left(x ^ {+}\right)}{2}.
$$

2.5.48. Prove the following Fejer-Lebesgue theorem. Assume that $f$ is $2\pi$ -periodic on $\mathbb{R}$ , $f \in L^{1}[-\pi, \pi]$ and $x$ is a Lebesgue point of $f$ . Then

$$
\lim  _ {n \rightarrow \infty} \sigma_ {n} (x) = f (x).
$$

2.5.49. Assume that $f$ is $2\pi$ -periodic on $\mathbb{R}$ and $f \in L^2[-\pi, \pi]$ . Show that the function

$$
g (x) = \int_ {- \pi} ^ {\pi} f (x + t) f (t) d t
$$

is continuous on $\mathbb{R}$ .

2.5.50. Assume that $f$ is $2\pi$ -periodic and continuous on $\mathbb{R}$ . Prove that the sequence of Cesàro means of the Fourier series for $f$ converges uniformly on $\mathbb{R}$ to $f$ .   
2.5.51. Prove that the Fourier series of a $2\pi$ -periodic function continuous on $\mathbb{R}$ with nonnegative Fourier coefficients converges uniformly on $\mathbb{R}$ .   
2.5.52. Prove the following Fatou theorem. If a $2\pi$ -periodic function $f$ is integrable on $[-\pi, \pi]$ and

$$
\lim  _ {n \rightarrow \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}} = 0,
$$

then $\lim_{n\to \infty}s_n(x) = f(x)$ almost everywhere. Moreover, if $f$ is continuous, then $\lim_{n\to \infty}s_n(x) = f(x)$ uniformly on $\mathbb{R}$ .

2.5.53. Prove the following Wiener theorem. A $2\pi$ -periodic function of bounded variation on $[0, 2\pi]$ is continuous if and only if

$$
\lim  _ {n \rightarrow \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}} = 0.
$$

Conclude that a $2\pi$ -periodic function of bounded variation on $[0, 2\pi]$ for which $a_n = o(n^{-1})$ is continuous.

2.5.54. Prove that if the Fourier series of $f \in L^{1}[-\pi, \pi]$ is lacunary, that is,

$$
f (x) \sim \sum_ {k = 1} ^ {\infty} \left(a _ {n _ {k}} \cos n _ {k} x + b _ {n _ {k}} \sin n _ {k} x\right),
$$

where $\frac{n_{k+1}}{n_k} \geq q > 1$ for $k = 1, 2, \ldots$ , then $\lim_{k \to \infty} s_{n_k}(x) = f(x)$ almost everywhere.

2.5.55. Assume that $f$ is $2\pi$ -periodic on $\mathbb{R}$ and $f \in L^{p}[-\pi, \pi]$ , $1 \leq p < \infty$ . Prove that the sequence of Cesàro means of the Fourier series for $f$ converges in the $L^{p}$ norm to $f$ , that is,

$$
\lim  _ {n \rightarrow \infty} \| \sigma_ {n} - f \| _ {p} = \lim  _ {n \rightarrow \infty} \left(\int_ {- \pi} ^ {\pi} | \sigma_ {n} (x) - f (x) | ^ {p} d x\right) ^ {\frac {1}{p}} = 0.
$$

2.5.56. Suppose that $\{b_n\}$ is a monotonically decreasing sequence converging to zero. Prove that $\sum_{n=1}^{\infty} b_n \sin nx$ is uniformly convergent on $[0, 2\pi]$ if and only if $\lim_{n \to \infty} nb_n = 0$ .   
2.5.57. Suppose that $\{b_n\}$ is a monotonically decreasing sequence converging to zero. Prove that $\sum_{n=1}^{\infty} b_n \sin nx$ is the Fourier series of a continuous function if and only if $\lim_{n \to \infty} nb_n = 0$ .   
2.5.58. Suppose that $\{b_n\}$ is a monotonically decreasing sequence converging to zero. Prove that $\sum_{n=1}^{\infty} b_n \sin nx$ is the Fourier series of a bounded function if and only if $nb_n = O(1)$ .   
2.5.59. Let $\{a_n\}$ be a monotonically decreasing sequence converging to zero and such that $a_{n+1} \leq \frac{a_n + a_{n+2}}{2}$ for $n \in \mathbb{N}$ . Prove that

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} a _ {n} \cos n x
$$

is the Fourier series of a function nonnegative and integrable on $[- \pi, \pi]$ . Deduce that the series

$$
\sum_ {n = 2} ^ {\infty} \frac {\cos n x}{\ln n}
$$

is the Fourier series of such a function. (Compare with the result in 2.5.23.)

# Part 2

# Solutions

# Chapter 1

# The Riemann-Stieltjes Integral

# 1.1. Properties of the Riemann-Stieltjes Integral

1.1.1. Let $\varepsilon > 0$ be given. By Theorem 1, to show that $f \in \mathcal{R}(\alpha)$ it suffices to find a partition $P$ such that

$$
U (P, f, \alpha) - L (P, f, \alpha) <   \varepsilon .
$$

Suppose first that $c \in (a, b)$ . Since $\alpha$ is continuous at $c$ , there is $\delta > 0$ such that $|\alpha(x) - \alpha(c)| < \varepsilon / 2$ if $|x - c| < \delta$ . If we take a partition $P$ whose mesh is less than $\delta$ and such that $x_{i-1} < c < x_i$ for some $i$ , then

$$
U (P, f, \alpha) - L (P, f, \alpha) = \alpha \left(x _ {i}\right) - \alpha \left(x _ {i - 1}\right) <   \varepsilon .
$$

The same reasoning can be applied to the cases $c = a$ and $c = b$ . Clearly, $\int_{a}^{b} f d\alpha = \sup L(P, f, \alpha) = 0$ .

1.1.2. Let $a = x_0 < \dots < x_n = b$ be a partition of $[a, b]$ , and let $i \in \{1, 2, \ldots, n\}$ be such that $x_{i-1} < c \leq x_i$ . Then

$$
U (P, f, \alpha) = \sup  _ {x \in [ x _ {i - 1}, x _ {i} ]} f (x) = M _ {i}
$$

and

$$
I. (P, f, \alpha) = \inf  _ {x \in \left[ x _ {i - 1}, x _ {i} \right]} f (x) = m _ {i}.
$$

Since $f$ is continuous on $[a, b]$ , taking partitions whose mesh tends to zero, we see that

$$
\inf  U (P, f, \alpha) = \sup  L (P, f, \alpha) = f (c).
$$

1.1.3. Since the sets $\mathbb{Q}$ and $\mathbb{R} \backslash \mathbb{Q}$ are dense in $\mathbb{R}$ , we see that $L(P, f) = 0$ for any partition $P$ of $[a, b]$ . Consequently,

$$
\underline {{\int_ {a} ^ {b}}} f d x = 0.
$$

On the other hand,

$$
U (P, f) = \sum_ {i = 1} ^ {n} x _ {i} \left(x _ {i} - x _ {i - 1}\right) = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \sum_ {i = 1} ^ {n} x _ {i} x _ {i - 1} \geq \frac {1}{2} \left(b ^ {2} - a ^ {2}\right),
$$

because $2x_{i}x_{i-1} \leq (x_{i}^{2} + x_{i-1}^{2})$ . It is worth noting here that

$$
\overline {{\int_ {a} ^ {b}}} f d x = \frac {1}{2} (b ^ {2} - a ^ {2}).
$$

Indeed, taking the sequence of partitions $P_{n}$ with $x_{i} = a + (b - a)i / n$ , $i = 0,1,\ldots ,n$ , we see that $\lim_{n\to \infty}U(P_n,f) = \frac{1}{2} (b^2 -a^2)$ .

1.1.4. Choose a partition $P$ of $[-a, a]$ such that

$$
- a = x _ {0} <   \dots <   x _ {j - 1} = 0 <   x _ {j} <   \dots <   x _ {n} = a.
$$

Then, as in the previous problem, we get

$$
U (P, f) = \sum_ {k - j - 1} ^ {n - 1} x _ {k + 1} \left(x _ {k + 1} - x _ {k}\right) \geq \frac {a ^ {2}}{2}
$$

and

$$
L (P, f) = \sum_ {k = 0} ^ {j - 2} x _ {k} \left(x _ {k + 1} - x _ {k}\right) \leq - \frac {a ^ {2}}{2}.
$$

Taking a suitable sequence of partitions (compare with the solution of the previous problem), one can show that

$$
\overline {{\int_ {- a} ^ {a}}} f (x) d x = \frac {a ^ {2}}{2} \quad \text {a n d} \quad \underline {{\int_ {- a} ^ {a}}} f (x) d x = - \frac {a ^ {2}}{2}.
$$

Finally, we remark that if

$$
f (x) = \left\{ \begin{array}{l l} x & \text {i f} x \in \mathbb {Q}, \\ 0 & \text {i f} x \in \mathbb {R} \backslash \mathbb {Q}, \end{array} \right.
$$

then $f$ is not Riemann integrable on any interval $[a, b]$ .

1.1.5. Let $[a, b]$ be arbitrarily fixed. Observe that, given a positive integer $N$ , there are only finitely many rationals $p/q$ (where $p$ and $q$ are co-prime) in $[a, b]$ such that $q \leq N$ . Let $k_N$ denote the number of such rationals. Consider a partition of $[a, b]$ of mesh $\delta > 0$ . Then there are at most $2k_N$ subintervals $[x_{i-1}, x_i]$ containing at least one of the rationals mentioned above. On the other subintervals $[x_{j-1}, x_j]$ we have $M_j - m_j < 1/N$ . Consequently,

$$
U (P, f) - L (P, f) <   2 k _ {N} \delta + \frac {b - a}{N}.
$$

Given $\varepsilon > 0$ , we take $N > 2(b - a) / \varepsilon$ . Then for any partition of mesh $\delta < \varepsilon / (4k_N)$ we get, in view of the above,

$$
U (P, f) - L (P, f) <   \varepsilon .
$$

1.1.6. Let $\varepsilon > 0$ be given. There is a positive integer $n_0$ such that $1 / n < \varepsilon / 2$ for $n > n_0$ . Choose a partition $P$ determined by

$$
0 = x _ {0} <   x _ {1} = \frac {1}{n _ {0} + 1} <   x _ {2} <   \dots <   x _ {k} = 1
$$

such that $x_{i} - x_{i-1} < \varepsilon / (4n_{0})$ for $i = 2, 3, \ldots, k$ . Then

$$
U (P, f) - L (P, f) = U (P, f) <   \frac {\varepsilon}{2} + 2 n _ {0} \frac {\varepsilon}{4 n _ {0}} = \varepsilon .
$$

1.1.7. Let $\varepsilon > 0$ be given. There is a positive integer $n_0$ such that $1 / n < \varepsilon / 2$ for $n > n_0$ . Choose a partition $P$ determined by

$$
\begin{array}{l} 0 = x _ {0} <   x _ {1} = \frac {1}{n _ {0} + 1} <   x _ {2} <   \dots <   x _ {n _ {0} ^ {\prime}} = \frac {1}{n _ {0}} \\ <   x _ {n _ {0} ^ {\prime} + 1} <   \dots <   x _ {n _ {1} ^ {\prime}} = \frac {1}{n _ {0} - 1} <   \dots <   x _ {n _ {n _ {0} - 1} ^ {\prime}} = 1 \\ \end{array}
$$

such that $x_{i} - x_{i-1} < \varepsilon / (4n_{0})$ , $i \geq 2$ . Then

$$
\begin{array}{l} U (P, f) - L (P, f) = \frac {1}{n _ {0} + 1} + \sum_ {i = 2} ^ {n _ {0} ^ {\prime}} \left(M _ {i} - m _ {i}\right) \left(x _ {i} - x _ {i - 1}\right) \\ + \sum_ {k = 0} ^ {n _ {0} - 2} \sum_ {i = n _ {k} ^ {\prime} + 1} ^ {n _ {k + 1} ^ {\prime}} (M _ {i} - m _ {i}) (x _ {i} - x _ {i - 1}) \\ <   \frac {\varepsilon}{2} + 2 n _ {0} \frac {\varepsilon}{4 n _ {0}} = \varepsilon . \\ \end{array}
$$

So, we have proved that $f$ is Riemann integrable on $[0,1]$ .

1.1.8. Since for every partition $P$ such that $x_{k} = 0$ for some $k$ we have $U(P, f, \alpha) = L(P, f, \alpha) = 0$ , we see that $\int_{a}^{b} f d\alpha = 0$ . Now to see that $\lim_{\mu(P) \to 0} S(P, f)$ does not exist, consider partitions with $\mu(P) \to 0$ and such that for some $k$ , $x_{k-1} < 0 < x_{k}$ . If we select $t_{k} = 0$ and $t_{k}' \in (0, x_{k}]$ , then we get $S(P, f) = 0$ and $S(P, f) = 1$ , respectively.

1.1.9. Suppose that $c, a < c < b$ , is a common point of discontinuity of $f$ and $\alpha$ . Then there is $\varepsilon > 0$ such that for any $\delta > 0$ there exist $x'$ and $x''$ such that $|x' - c| < \delta$ , $|x'' - c| < \delta$ , and

$$
| f \left(x ^ {\prime}\right) - f (c) | > \varepsilon , \quad | \alpha \left(x ^ {\prime \prime}\right) - \alpha (c) | > \varepsilon . \tag {1}
$$

Assume, contrary to our claim, that $\lim_{\mu(P) \to 0} S(P, f)$ exists. It then follows that there is $\delta' > 0$ such that $\mu(P) < \delta'$ implies that

$$
\left| S (P, f, \alpha) - S ^ {\prime} (P, f, \alpha) \right| <   \varepsilon^ {2}, \tag {2}
$$

where

$$
S (P, f, \alpha) = \sum_ {i = 1} ^ {n} f \left(t _ {i}\right) \Delta \alpha_ {i} \quad \text {a n d} \quad S ^ {\prime} (P, f, \alpha) = \sum_ {i = 1} ^ {n} f \left(t _ {i} ^ {\prime}\right) \Delta \alpha_ {i}
$$

for all admissible choices of $t_i$ and $t_i'$ . Our task is now to find a partition $P$ with points $t_i$ and $t_i'$ for which (2) does not hold. To this end we start with a partition $P_1$ of mesh less than $\delta'$ and such that $x_{k-1} < c < x_k$ . Then there are $x', x'' \in (x_{k-1}, x_k)$ satisfying (1). Assume first that $x' < c < x''$ , and construct the partition $P$ by adding the points $x'$ and $x''$ to $P_1$ . Next choose $t_i = t_i'$ in every subinterval except for $[x', x'']$ . Now if we take $t = x'$ and $t' = c$ in $[x', x'']$ , then

$$
\begin{array}{l} \left| S (P, f, \alpha) - S ^ {\prime} (P, f, \alpha) \right| = \left| f (c) - f \left(x ^ {\prime}\right) \right| \left(\alpha \left(x ^ {\prime \prime}\right) - \alpha \left(x ^ {\prime}\right)\right) \\ \geq | f (c) - f \left(x ^ {\prime}\right) \mid \left(\alpha \left(x ^ {\prime \prime}\right) - \alpha (c)\right) > \varepsilon^ {2}. \\ \end{array}
$$

In the case $x'' < c < x'$ similar reasoning can be applied. If $x_{k-1} < x'' < x' < c < x_k$ , then we add to the partition $P_1$ the points $x''$ and $c$ . As before, we choose $t_i = t_i'$ in every subinterval except for the interval $[x'', c]$ . In $[x'', c]$ we select $t = x'$ and $t' = c$ , and get

$$
\left| S (P, f, \alpha) - S ^ {\prime} (P, f, \alpha) \right| = \left| f (c) - f \left(x ^ {\prime}\right) \right| (\alpha (c) - \alpha \left(x ^ {\prime \prime}\right)) > \varepsilon^ {2}.
$$

If $x_{k-1} < x' \leq x'' < c < x_k$ , then we refine the partition $P_1$ by adding the points $x'$ and $c$ . Choosing $t_i = t_i'$ in every subinterval except for the interval $[x', c]$ , in which we take $t = x'$ and $t' = c$ , we arrive at

$$
\begin{array}{l} \left| S (P, f, \alpha) - S ^ {\prime} (P, f, \alpha) \right| = | f (c) - f \left(x ^ {\prime}\right) | (\alpha (c) - \alpha \left(x ^ {\prime}\right)) \\ \geq | f (c) - f \left(x ^ {\prime}\right) | (\alpha (c) - \alpha \left(x ^ {\prime \prime}\right)) > \varepsilon^ {2}. \\ \end{array}
$$

Similar arguments apply to the case $x', x'' \in (c, x_k)$ . Finally, if the common point of discontinuity is $a$ or $b$ , the proof runs as before.

1.1.10. We first show that, given a partition $P$ ,

$$
U (P, f, \alpha) = \sup  S (P, f, \alpha) \quad \text {a n d} \quad L (P, f, \alpha) = \inf  S (P, f, \alpha),
$$

where the supremum and the infimum are taken over all admissible choices of $t_i$ , $i = 1,2,\ldots,n$ . Indeed, for $\varepsilon > 0$ , there are $t_i'$ and $t_i''$ in the interval $[x_{i-1}, x_i]$ such that $f(t_i') < m_i + \varepsilon/(b - a)$ and $f(t_i'') > M_i - \varepsilon/(b - a)$ . Consequently, if $S'(P, f, \alpha)$ and $S''(P, f, \alpha)$ are the corresponding sums, then

$$
L (P, f, \alpha) \leq S ^ {\prime} (P, f, \alpha) <   \varepsilon + L (P, f, \alpha)
$$

and

$$
U (P, f, \alpha) \geq S ^ {\prime \prime} (P, f, \alpha) > U (P, f, \alpha) - \varepsilon .
$$

Now, if $\lim_{\mu(P) \to 0} S(P, f, \alpha) = A$ , then, given $\varepsilon > 0$ , there is $\delta > 0$ such that $\mu(P) < \delta$ implies that $|S(P, f, \alpha) - A| < \varepsilon$ for all admissible choices of $t_i$ . It follows from the above that

$$
S ^ {\prime} (P, f, \alpha) - \varepsilon <   L (P, f, \alpha) \leq U (P, f, \alpha) <   S ^ {\prime \prime} (P, f, \alpha) + \varepsilon
$$

and

$$
A - 2 \varepsilon <   L (P, f, \alpha) \leq U (P, f, \alpha) <   A + 2 \varepsilon ,
$$

which gives the desired result.

Suppose now that $f$ is continuous on $[a, b]$ . Then $f$ is uniformly continuous on that interval. So, given $\varepsilon > 0$ , there is $\delta > 0$ such that $|f(x) - f(x')| < \varepsilon / (\alpha(b) - \alpha(a))$ if $|x - x'| < \delta$ . Consequently, for every partition $P$ of mesh less than $\delta$ , we have $U(P, f, \alpha) - L(P, f, \alpha) < \varepsilon$ (which clearly shows that $f \in \mathcal{R}(\alpha)$ ). Now, since $S(P, f, \alpha)$ and $\int_{\alpha}^{b} f d\alpha$ lie between $U(P, f, \alpha)$ and $L(P, f, \alpha)$ , the claim follows.

1.1.11. By the previous problem, if $\lim_{\mu(P) \to 0} S(P, f, \alpha)$ exists, then $f \in \mathcal{R}(\alpha)$ on $[a, b]$ . To prove the other implication, suppose that $f \in \mathcal{R}(\alpha)$ . Then, given $\varepsilon > 0$ , there is a partition $P'$ such that

$$
U \left(P ^ {\prime}, f, \alpha\right) - \frac {\varepsilon}{2} <   \int_ {a} ^ {b} f (x) d \alpha (x) <   L \left(P ^ {\prime}, f, \alpha\right) + \frac {\varepsilon}{2}. \tag {1}
$$

Assume that the partition $P'$ is an array of $n$ points. Moreover, let $M = \sup \{|f(x)| : x \in [a, b]\}$ . By the uniform continuity of $\alpha$ there is $\delta > 0$ such that $|\alpha(x) - \alpha(x')| < \varepsilon / (4Mn)$ for $|x - x'| < \delta$ . If $P$ is a partition of mesh less than $\delta$ , then the partition $P \cup P'$ contains at most $n - 2$ points more than $P$ , and consequently,

$$
U (P, f, \alpha) - U (P \cup P ^ {\prime}, f, \alpha) <   (n - 2) \frac {\varepsilon}{4 M n} 2 M <   \frac {\varepsilon}{2}.
$$

Since (1) holds if we replace $P'$ by $P' \cup P$ , it then follows that

$$
U (P, f, \alpha) - \varepsilon <   \int_ {a} ^ {b} f (x) d \alpha (x).
$$

Likewise,

$$
\int_ {a} ^ {b} f (x) d \alpha (x) <   L (P, f, \alpha) + \varepsilon .
$$

Since $S(P, f, \alpha)$ lies between $L(P, f, \alpha)$ and $U(P, f, \alpha)$ , the claim follows.

1.1.12. Suppose that $\alpha$ is continuous from the left at $x^{*}$ . Then for a partition $P$ such that $a = x_0 < x_1 < \dots < x_{i-1} = x^* < x_i < \dots < x_n = b$ we have

$$
U (P, f, \alpha) = M _ {i} (d - c) \quad \text {a n d} \quad L (P, f, \alpha) = m _ {i} (d - c).
$$

Since in the case considered $f$ is continuous from the right at $x^*$ , the result follows. Similar reasoning can be applied to the other case.

1.1.13. Putting $c_0 = a$ and $c_{m+1} = b$ , wc gct

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = \sum_ {k = 0} ^ {m} \int_ {c _ {k}} ^ {c _ {k + 1}} f (x) d \alpha (x).
$$

Furthermore, since $\pmb{f}$ is continuous, by the result in 1.1.10, we see that

$$
\int_ {c _ {k}} ^ {c _ {k + 1}} f (x) d \alpha (x) = f \left(c _ {k}\right) \left(\alpha \left(c _ {k} ^ {+}\right) - \alpha \left(c _ {k}\right)\right) + f \left(c _ {k + 1}\right) \left(\alpha \left(c _ {k + 1}\right) - \alpha \left(c _ {k + 1} ^ {-}\right)\right).
$$

# 1.1.14. (a) We have

$$
\frac {1}{n + 1} + \frac {1}{n + 2} + \dots + \frac {1}{3 n} = \frac {1}{2 n} \left(\frac {1}{\frac {1}{2} + \frac {1}{2 n}} + \frac {1}{\frac {1}{2} + \frac {2}{2 n}} + \dots + \frac {1}{\frac {1}{2} + \frac {2 n}{2 n}}\right).
$$

Since $f(x) = 1 / (1 / 2 + x)$ is continuous on $[0,1]$ , by the result in 1.1.10, we get

$$
\lim  _ {n \rightarrow \infty} \left(\frac {1}{n + 1} + \frac {1}{n + 2} + \dots + \frac {1}{3 n}\right) = \int_ {0} ^ {1} \frac {2}{1 + 2 x} d x = \ln 3.
$$

(b) Since

$$
\begin{array}{l} n ^ {2} \left(\frac {1}{n ^ {3} + 1 ^ {3}} + \frac {1}{n ^ {3} + 2 ^ {3}} + \dots + \frac {1}{n ^ {3} + n ^ {3}}\right) \\ = \frac {1}{n} \left(\frac {1}{1 + \frac {1 ^ {3}}{n ^ {3}}} + \frac {1}{1 + \frac {2 ^ {3}}{n ^ {3}}} + \dots + \frac {1}{1 + \frac {n ^ {3}}{n ^ {3}}}\right), \\ \end{array}
$$

we see that

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} n ^ {2} \left(\frac {1}{n ^ {3} + 1 ^ {3}} + \frac {1}{n ^ {3} + 2 ^ {3}} + \dots + \frac {1}{n ^ {3} + n ^ {3}}\right) = \int_ {0} ^ {1} \frac {1}{1 + x ^ {3}} d x \\ = \frac {1}{3} \ln 2 + \frac {1}{9} \sqrt {3} \pi . \\ \end{array}
$$

(c) As in (a) and (b) we obtain

$$
\lim  _ {n \rightarrow \infty} \left(\frac {1 ^ {k} + 2 ^ {k} + \cdots + n ^ {k}}{n ^ {k + 1}}\right) = \int_ {0} ^ {1} x ^ {k} d x = \frac {1}{k + 1}.
$$

(d) Note that

$$
\begin{array}{l} a _ {n} = \frac {1}{n} \sqrt [ n ]{(n + 1) (n + 2) \cdots (n + n)} \\ = \sqrt {\left(1 + \frac {1}{n}\right) \left(1 + \frac {2}{n}\right) \cdots \left(1 + \frac {n}{n}\right)}. \\ \end{array}
$$

So,

$$
\ln a _ {n} = \frac {1}{n} \left(\ln \left(1 + \frac {1}{n}\right) + \ln \left(1 + \frac {2}{n}\right) + \dots + \ln \left(1 + \frac {n}{n}\right)\right).
$$

Consequently,

$$
\lim  _ {n \rightarrow \infty} \ln a _ {n} = \int_ {0} ^ {1} \ln (1 + x) d x = 2 \ln 2 - 1
$$

and

$$
\lim  _ {n \rightarrow \infty} a _ {n} = \frac {4}{e}.
$$

(e) We know that for positive $x$ ,

$$
x - \frac {x ^ {3}}{3 !} <   \sin x <   x.
$$

So,

$$
\sum_ {i = 1} ^ {n} \frac {n}{n ^ {2} + i ^ {2}} - \frac {1}{3 !} \sum_ {i = 1} ^ {n} \left(\frac {n}{n ^ {2} + i ^ {2}}\right) ^ {3} <   \sum_ {i = 1} ^ {n} \sin \frac {n}{n ^ {2} + i ^ {2}} <   \sum_ {i = 1} ^ {n} \frac {n}{n ^ {2} + i ^ {2}}.
$$

As in (b), one can show that

$$
\lim  _ {n \rightarrow \infty} \sum_ {i = 1} ^ {n} \frac {n}{n ^ {2} + i ^ {2}} = \int_ {0} ^ {1} \frac {1}{1 + x ^ {2}} d x = \frac {\pi}{4}.
$$

Clearly,

$$
0 \leq \sum_ {i = 1} ^ {n} \left(\frac {n}{n ^ {2} + i ^ {2}}\right) ^ {3} <   \sum_ {i = 1} ^ {n} \frac {n ^ {3}}{n ^ {6}} = \frac {1}{n ^ {2}}.
$$

Consequently, the limit is $\pi /4$

(f) We have

$$
\sum_ {i = 1} ^ {n} \frac {2 ^ {i / n}}{n + 1 / i} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {2 ^ {i / n}}{1 + 1 / (i n)}.
$$

Moreover, the inequality $e^x > 1 + x$ , $x > 0$ , implies

$$
2 ^ {i / n} > \frac {2 ^ {i / n}}{1 + 1 / (i n)} = 2 ^ {(i - 1) / n} \frac {2 ^ {1 / n}}{1 + 1 / (i n)} > 2 ^ {(i - 1) / n} \frac {1 + \frac {\ln 2}{n}}{1 + \frac {1}{i n}}.
$$

Hence for $i\geq 2$

$$
2 ^ {i / n} > \frac {2 ^ {i / n}}{1 + 1 / (i n)} > 2 ^ {(i - 1) / n}.
$$

By the intermediate value property there is $\zeta_i \in [(i - 1)/n, i/n]$ , $i \geq 2$ , such that

$$
\frac {2 ^ {i / n}}{1 + 1 / (i n)} = 2 ^ {\zeta_ {i}}.
$$

It then follows that the limit is equal to

$$
\int_ {0} ^ {1} 2 ^ {x} d x = \frac {1}{\ln 2}.
$$

(g) If $a_n = \sqrt[n]{f(1/n)f(2/n)\ldots f(n/n)}$ , then

$$
\ln a _ {n} = \frac {1}{n} (\ln f (1 / n) + \ln f (2 / n) + \dots + \ln f (n / n))
$$

and therefore

$$
\lim  _ {n \rightarrow \infty} a _ {n} = e ^ {\int_ {0} ^ {1} \ln f (x) d x}.
$$

1.1.15. The function

$$
f (x) = \left\{ \begin{array}{l l} \frac {\sin x}{x} & \text {i f} x \in (0, \pi ], \\ 1 & \text {i f} x = 0 \end{array} \right.
$$

is continuous on $[0, \pi]$ and positive on $[0, \pi)$ . Thus it is Riemann integrable, and $\int_0^\pi f(x) dx > 0$ . Moreover, since

$$
\begin{array}{l} S _ {n} = \frac {\sin \frac {\pi}{n + 1}}{1} + \frac {\sin \frac {2 x}{n + 1}}{2} + \dots + \frac {\sin \frac {n \pi}{n + 1}}{n} \\ = \frac {\pi}{n + 1} \left(\frac {\sin \frac {\pi}{n + 1}}{\frac {\pi}{n + 1}} + \frac {\sin \frac {2 \pi}{n + 1}}{\frac {2 \pi}{n + 1}} + \dots + \frac {\sin \frac {n \pi}{n + 1}}{\frac {n \pi}{n + 1}}\right), \\ \end{array}
$$

we see that

$$
\lim  _ {n \rightarrow \infty} S _ {n} = \int_ {0} ^ {\pi} f (x) d x > 0.
$$

1.1.16. Observe first that

$$
\begin{array}{l} n \left(\frac {1}{n} \sum_ {i = 1} ^ {n} f \left(\frac {i}{n}\right) - \int_ {0} ^ {1} f (x) d x\right) \\ = n \left(\frac {1}{n} \sum_ {i = 1} ^ {n} f \left(\frac {i}{n}\right) - \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} f (x) d x\right) \\ = n \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} \left(f \left(\frac {i}{n}\right) - f (x)\right) d x \\ = n \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} f ^ {\prime} (\xi_ {i} (x)) \left(\frac {i}{n} - x\right) d x, \\ \end{array}
$$

where the last equality follows from the mean value theorem. If we set

$$
m _ {i} = \inf  \left\{f ^ {\prime} (x): x \in [ (i - 1) / n, i / n ] \right\}
$$

and

$$
M _ {i} = \sup  \left\{f ^ {\prime} (x): x \in [ (i - 1) / n, i / n ] \right\},
$$

we get

$$
\begin{array}{l} m _ {i} \int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} \left(\frac {i}{n} - x\right) d x \leq \int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} f ^ {\prime} (\xi_ {i} (x)) \left(\frac {i}{n} - x\right) d x \\ \leq M _ {i} \int_ {\frac {1}{n}} ^ {\frac {1}{n}} \left(\frac {i}{n} - x\right) d x, \\ \end{array}
$$

and consequently,

$$
\frac {1}{2 n} \sum_ {i = 1} ^ {n} m _ {i} \leq n \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {1}{n}} f ^ {\prime} (\xi_ {i} (x)) \left(\frac {i}{n} - x\right) d x \leq \frac {1}{2 n} \sum_ {i = 1} ^ {n} M _ {i}.
$$

Finally, since $f'$ is continuous on $[0,1]$ , we obtain

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} n \left(\frac {1}{n} \sum_ {i = 1} ^ {n} f \left(\frac {i}{n}\right) - \int_ {0} ^ {1} f (x) d x\right) = \frac {1}{2} \int_ {0} ^ {1} f ^ {\prime} (x) d x \\ = \frac {f (1) - f (0)}{2}. \\ \end{array}
$$

Now applying the proved result to $f(x) = x^{k}$ , we get

$$
\lim  _ {n \rightarrow \infty} n \left(\frac {1 ^ {k} + 2 ^ {k} + \cdots + n ^ {k}}{n ^ {k + 1}} - \frac {1}{k + 1}\right) = \frac {1}{2}.
$$

1.1.17. Write

$$
\begin{array}{l} \frac {1 ^ {k} + 3 ^ {k} + \cdots + (2 n - 1) ^ {k}}{n ^ {k + 1}} \\ = \frac {1}{n} \left(\frac {1 ^ {k} + 3 ^ {k} + \cdots + (2 n - 1) ^ {k}}{n ^ {k}}\right) \\ = \frac {2 ^ {k}}{n} \left(\left(\frac {1}{2 n}\right) ^ {k} + \left(\frac {3}{2 n}\right) ^ {k} + \dots + \left(\frac {2 n - 1}{2 n}\right) ^ {k}\right) \\ \end{array}
$$

and observe that

$$
\frac {2 i - 1}{2 n} = \frac {1}{2} \left(\frac {i - 1}{n} + \frac {i}{n}\right)
$$

is the midpoint of $[(i - 1) / n, i / n]$ , $i = 1, 2, \ldots, n$ . So the last sum is an $S(P, f)$ , where $f(x) = 2^k x^k$ , and consequently, the limit is $2^k / (k + 1)$ .

1.1.18. By Taylor's formula we have

$$
\begin{array}{l} f (x) - f \left(\frac {2 i - 1}{2 n}\right) \\ = f ^ {\prime} \left(\frac {2 i - 1}{2 n}\right) \left(x - \frac {2 i - 1}{2 n}\right) + \frac {1}{2} f ^ {\prime \prime} \left(\xi_ {i} (x)\right) \left(x - \frac {2 i - 1}{2 n}\right) ^ {2}. \\ \end{array}
$$

Consequently,

$$
\begin{array}{l} n ^ {2} \left(\int_ {0} ^ {1} f (x) d x - \frac {1}{n} \sum_ {i = 1} ^ {n} f \left(\frac {2 i - 1}{2 n}\right)\right) \\ = n ^ {2} \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {1}{n}} \left(f (x) - f \left(\frac {2 i - 1}{2 n}\right)\right) d x \\ = n ^ {2} \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} f ^ {\prime} \left(\frac {2 i - 1}{2 n}\right) \left(x - \frac {2 i - 1}{2 n}\right) d x \\ + \frac {n ^ {2}}{2} \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {1}{n}} f ^ {\prime \prime} (\xi_ {i} (x)) \left(x - \frac {2 i - 1}{2 n}\right) ^ {2} d x. \\ \end{array}
$$

Now note that each of the integrals

$$
\int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} f ^ {\prime} \left(\frac {2 i - 1}{2 n}\right) \left(x - \frac {2 i - 1}{2 n}\right) d x
$$

vanishes and

$$
\frac {1}{2 4 n} \sum_ {i = 1} ^ {n} m _ {i} \leq \frac {n ^ {2}}{2} \sum_ {i = 1} ^ {n} \int_ {\frac {i - 1}{n}} ^ {\frac {i}{n}} f ^ {\prime \prime} (\xi_ {i} (x)) \left(x - \frac {2 i - 1}{2 n}\right) ^ {2} d x \leq \frac {1}{2 4 n} \sum_ {i = 1} ^ {n} M _ {i},
$$

where $m_i$ and $M_i$ denote the greatest lower and the least upper bound of $f''$ in the $i$ th subinterval. Since $f''$ is Riemann integrable on $[0,1]$ , the result follows.

1.1.19. Apply the results proved in 1.1.16 and 1.1.18 with $f(x) = 1 / (1 + x), x \in [0,1]$ .

1.1.20. It suffices to show that changing $f$ at one point, say $x' \in [a, b]$ , does not affect the integrability and the value of the integral. Let $\tilde{f}$ denote the changed function and let $m$ and $M$ be its greatest lower bound and least upper bound over $[a, b]$ , respectively. Suppose, e.g., that $x' \in (a, b)$ . Since $\tilde{f} = f$ is integrable on $[a, x' - \varepsilon]$ and on

$[x' + \varepsilon, b]$ , given $\varepsilon > 0$ , there are partitions $P_1$ of $[a, x' - \varepsilon]$ and $P_2$ of $[x' + \varepsilon, b]$ such that

$$
U (P _ {i}, \bar {f}) - L (P _ {i}, \bar {f}) <   \varepsilon , \quad i = 1, 2.
$$

So, if $P = P_{1} \cup P_{2}$ , then

$$
U (P, \tilde {f}) - L (P, \tilde {f}) <   2 \varepsilon + 2 (M - m) \varepsilon ,
$$

which shows that $\bar{f}$ is Riemann integrable on $[a,b]$ . Moreover,

$$
\left| \int_ {a} ^ {b} \bar {f} (x) d x - \int_ {a} ^ {b} f (x) d x \right| = \left| \int_ {x ^ {\prime} - e} ^ {x ^ {\prime} + \varepsilon} (\bar {f} (x) - f (x)) d x \right| \leq M ^ {*} 2 \varepsilon ,
$$

where $M^{*}$ is the sup of $|\bar{f} - f|$ over $[a, b]$ .

1.1.21. Suppose, for example, that $f$ is monotonically increasing on $[a, b]$ . By Theorem 1, it suffices to show that, given $\varepsilon > 0$ , there is a partition $P$ such that $U(P, f, \alpha) - L(P, f, \alpha) < \varepsilon$ . Consider the partition $a = x_0 < x_1 < \dots < x_n = b$ with

$$
x _ {i} - x _ {i - 1} = (\alpha (b) - \alpha (a)) / n.
$$

Then

$$
\begin{array}{l} U (P, f, \alpha) - L (P, f, \alpha) = \frac {\alpha (b) - \alpha (a)}{n} \sum_ {i = 1} ^ {n} \left(f \left(x _ {i}\right) - f \left(x _ {i - 1}\right)\right) \\ = \frac {(\alpha (b) - \alpha (a)) (f (b) - f (a))}{n} <   \varepsilon \\ \end{array}
$$

for sufficiently large $\pmb{n}$ .

The following corollary is worth noting here: every monotonic function on $[a, b]$ is Riemann integrable on that interval.

1.1.22. Suppose that $c \in (a, b)$ , $\alpha(c^-) \neq \alpha(c)$ and $\alpha(c) \neq \alpha(c^+)$ . Let $\varepsilon > 0$ be given. Since $f \in \mathcal{R}(\alpha)$ , there is a partition $P'$ such that

$$
U \left(P ^ {\prime}, f, \alpha\right) - L \left(P ^ {\prime}, f, \alpha\right) <   \varepsilon . \tag {1}
$$

Let $P$ : $a = x_0 < x_1 < \ldots < x_{k-1} < x_k = c < x_{k+1} < \ldots < x_n = b$ be the refinement of $P'$ obtained by adding the point $c$ . Then (1) also holds if we replace $P'$ by $P$ . Consequently,

$$
(M _ {k - 1} - m _ {k - 1}) (\alpha (c) - \alpha (x _ {k - 1})) <   \varepsilon \text {a n d} (M _ {k} - m _ {k}) (\alpha (x _ {k}) - \alpha (c)) <   \varepsilon .
$$

Since $\alpha$ is monotonically increasing,

$$
(M _ {k - 1} - m _ {k - 1}) (\alpha (c) - \alpha (c ^ {-})) \leq (M _ {k - 1} - m _ {k - 1}) (\alpha (c) - \alpha (x _ {k - 1})) <   \varepsilon .
$$

Therefore for $\pmb{x} \in [x_{k-1}, c]$ ,

$$
| f (x) - f (c) | \leq M _ {k - 1} - m _ {k - 1} <   \frac {\varepsilon}{\alpha (c) - \alpha (c ^ {-})}.
$$

This proves that $\lim_{x \to c^{-}} f(x) = f(c)$ . In much the same way one can show that $\lim_{x \to c^{+}} f(x) = f(c)$ . In the case $c = a$ or $c = b$ , similar reasoning can be applied.

1.1.23. If the points where $\alpha'$ does not exist are included in a partition $\{x_0, x_1, \ldots, x_n\}$ of $[a, b]$ , then by the mean value theorem,

$$
S (P, f, \alpha) = \sum_ {k = 1} ^ {n} f (t _ {k}) (\alpha (x _ {k}) - \alpha (x _ {k - 1})) = \sum_ {k = 1} ^ {n} f (t _ {k}) \alpha^ {\prime} (\tau_ {k}) (x _ {k} - x _ {k - 1}),
$$

with $\tau_{k} \in (x_{k-1}, x_{k})$ . In view of the result in 1.1.20 we can extend the function $\alpha'$ to the whole interval $[a, b]$ arbitrarily. Since $f\alpha'$ and $\alpha'$ are Riemann integrable, we know by 1.1.11 that, given $\varepsilon > 0$ , there are $\delta_{1} > 0$ and $\delta_{2} > 0$ such that

$$
\left| S \left(P, f \alpha^ {\prime}\right) - \int_ {a} ^ {b} f \alpha^ {\prime} d x \right| <   \varepsilon
$$

if $\mu(P) < \delta_1$ and

$$
\left| S (P, \alpha^ {\prime}) - \int_ {a} ^ {b} \alpha^ {\prime} d x \right| <   \varepsilon
$$

if $\mu(P) < \delta_2$ . Since the intermediate points $t_k$ can be chosen arbitrarily in $[x_{k-1}, x_k]$ , we see that

$$
\sum_ {k = 1} ^ {n} \left| \alpha^ {\prime} \left(t _ {k}\right) - \alpha^ {\prime} \left(\tau_ {k}\right) \right| \left(x _ {k} - x _ {k - 1}\right) <   2 \varepsilon
$$

if $\mu(P) < \delta_2$ and $t_k, \tau_k \in [x_{k-1}, x_k]$ . Consequently, if $P$ is a partition of mesh less than $\min\{\delta_1, \delta_2\}$ which contains points where $\alpha'$ does not

exist, then

$$
\begin{array}{l} \left| S (P, f, \alpha) - \int_ {a} ^ {b} f \alpha^ {\prime} d x \right| = \left| \sum_ {k = 1} ^ {n} f \left(t _ {k}\right) \alpha^ {\prime} \left(\tau_ {k}\right) \left(x _ {k} - x _ {k - 1}\right) - \int_ {a} ^ {b} f \alpha^ {\prime} d x \right| \\ \leq \left| \sum_ {k = 1} ^ {n} f \left(t _ {k}\right) \alpha^ {\prime} \left(t _ {k}\right) \left(x _ {k} - x _ {k - 1}\right) - \int_ {a} ^ {b} f \alpha^ {\prime} d x \right| \\ + \left| \sum_ {k = 1} ^ {n} f \left(t _ {k}\right) \left(\alpha^ {\prime} \left(t _ {k}\right) - \alpha^ {\prime} \left(\tau_ {k}\right)\right) \left(x _ {k} - x _ {k - 1}\right) \right| \\ \leq \varepsilon + M 2 \varepsilon , \\ \end{array}
$$

where $M$ is an upper bound of $|f|$ on $[a, b]$ . Since $\alpha$ is continuous, one can show that if $P_1$ is a partition (of sufficiently small mesh) that does not contain points where $\alpha'$ does not exist, then $|S(P, f, \alpha) - S(P_1, f, \alpha)| < \varepsilon$ .

# 1.1.24. Put

$$
\rho (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \leq 0, \\ 1 & \text {i f} x > 0. \end{array} \right.
$$

For $a = c_0 < c_1 < \dots < c_m < c_{m+1} = b$ , define

$$
\begin{array}{l} \alpha_ {1} (x) = \sum_ {k = 0} ^ {m} (\alpha \left(c _ {k} ^ {+}\right) - \alpha \left(c _ {k}\right)) \rho (x - c _ {k}) \\ - \sum_ {k = 1} ^ {m + 1} (\alpha (c _ {k}) - \alpha (c _ {k} ^ {-})) \rho (c _ {k} - x). \\ \end{array}
$$

Then $\alpha = (\alpha - \alpha_{1}) + \alpha_{1}$ , and $\alpha - \alpha_{1} = \alpha_{2}$ is continuous on $[a, b]$ . Moreover, except for finitely many points, $\alpha_{2}' = \alpha'$ . Thus, by 1.1.20, we get

$$
\int_ {a} ^ {b} f (x) \alpha_ {2} ^ {\prime} (x) d x = \int_ {a} ^ {b} f (x) \alpha^ {\prime} (x) d x.
$$

Consequently, using the result in the previous problem and in 1.1.13, we obtain

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \alpha (x) = \int_ {a} ^ {b} f (x) d \alpha_ {1} (x) + \int_ {a} ^ {b} f (x) d \alpha_ {2} (x) \\ = \int_ {a} ^ {b} f (x) d \alpha_ {1} (x) + \int_ {a} ^ {b} f (x) \alpha^ {\prime} (x) d x \\ = f (a) \left(\alpha \left(a ^ {+}\right) - \alpha (a)\right) + \sum_ {k = 1} ^ {m} f \left(c _ {k}\right) \left(\alpha \left(c _ {k} ^ {+}\right) - \alpha \left(c _ {k} ^ {-}\right)\right) \\ + f (b) (\alpha (b) - \alpha (b ^ {-})) + \int_ {a} ^ {b} f (x) \alpha^ {\prime} (x) d x. \\ \end{array}
$$

1.1.25. By the result in the previous problem we get

$$
\int_ {- 2} ^ {2} x ^ {2} d \alpha (x) = \int_ {- 2} ^ {- 1} x ^ {2} d x + \int_ {0} ^ {2} 2 x ^ {3} d x + (- 1) ^ {2} \cdot 1 + 0 \cdot 1 = \frac {3 4}{3}.
$$

1.1.26. Clearly,

$$
m (\alpha (b) - \alpha (a)) \leq \int_ {a} ^ {b} f (x) d \alpha (x) \leq M (\alpha (b) - \alpha (a)),
$$

where $m = \inf \{f(x):x\in [a,b]\}$ and $M = \sup \{f(x):x\in [a,b]\}$ . Thus

$$
m \leq \frac {\int_ {a} ^ {b} f (x) d \alpha (x)}{\alpha (b) - \alpha (a)} \leq M.
$$

Since $f$ is continuous on $[a, b]$ , the values $m$ and $M$ are assumed in $[a, b]$ , and by the intermediate value property,

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f (c) (\alpha (b) - \alpha (a))
$$

with some $c \in [a, b]$ .

1.1.27. If $f$ is constant on $[a, b]$ , the claim is obvious. If $f$ is nonconstant, set $m = \inf \{f(x): x \in [a, b]\} = f(x_1)$ and $M = \sup \{f(x): x \in [a, b]\} = f(x_2)$ . Then $m < M$ , and by the continuity of $f$ there are subintervals $[c_1, d_1]$ and $[c_2, d_2]$ such that $f(x) > m$ for $x \in [c_1, d_1]$ and $f(x) < M$ for $x \in [c_2, d_2]$ . Since $\alpha$ is strictly increasing, we see that

$$
m <   \frac {\int_ {a} ^ {b} f (x) d \alpha (x)}{\alpha (b) - \alpha (a)} <   M.
$$

By the intermediate value property, there is $c$ in an open interval with endpoints $x_1, x_2$ for which the desired equality holds.

Note that the assumption of strict monotonicity of $\alpha$ is essential. Indeed, if

$$
\alpha (x) = \left\{ \begin{array}{l l} 0 & \text {i f} \quad x = a, \\ 1 & \text {i f} \quad x \in (a, b ] \end{array} \right.
$$

and $f$ is continuous on $[a, b]$ , then

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f (a).
$$

1.1.28. (a) It is clear (see, e.g., 1.1.23) that

$$
\int_ {a \varepsilon} ^ {b \varepsilon} \frac {f (x)}{x} d x = \int_ {a \varepsilon} ^ {b \varepsilon} f (x) d (\ln x).
$$

Now by the first mean value theorem

$$
\int_ {a \varepsilon} ^ {b \varepsilon} f (x) d (\ln x) = f (c (\varepsilon)) (\ln (b \varepsilon) - \ln (a \varepsilon)) = f (c (\varepsilon)) \ln \frac {b}{a}.
$$

Thus the limit is $f(0) \ln (b / a)$ .

(b) As in (a), we have

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} \frac {x ^ {n}}{1 + x} d x = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} \frac {1}{1 + x} d \left(\frac {x ^ {n + 1}}{n + 1}\right) \\ = \lim  _ {n \rightarrow \infty} \frac {1}{(1 + c _ {n}) (n + 1)} = 0. \\ \end{array}
$$

1.1.29. By the first mean value theorem (see, e.g., 1.1.26),

$$
\lim  _ {h \rightarrow 0} \frac {F (x + h) - F (x)}{\alpha (x + h) - \alpha (x)} = \lim  _ {h \rightarrow 0} \frac {f (c (h)) (\alpha (x + h) - \alpha (x))}{\alpha (x + h) - \alpha (x)} = f (x),
$$

where the last equality follows from the continuity of $f$ .

1.1.30. Analysis similar to that in the proofs of mean value theorems can be used. We first note that if $c \in (a, b)$ is a point of local extremum of $f$ , then $\frac{df}{da}(c) = 0$ . Indeed, if, for example, $c$ is a point of local maximum, then for sufficiently small $h$ , $\frac{f(c + h) - f(c)}{\alpha(c + h) - \alpha(c)} \leq 0$ if $h > 0$ and $\frac{f(c + h) - f(c)}{\alpha(c + h) - \alpha(c)} \geq 0$ if $h < 0$ .

Now let $x$ and $h$ be fixed. Suppose, for example, that $h$ is positive. Define

$$
g (t) = \left(f (x + h) - f (x)\right) \alpha (t) - \left(\alpha (x + h) - \alpha (x)\right) f (t).
$$

Then $g$ is continuous on $[a, b]$ , and $g(x) = g(x + h)$ . If $g$ is constant on $[x, x + h]$ , then $\frac{dg}{dx}(t) = 0$ for all $t \in (x, x + h)$ . If, for example, $g(t) > g(x)$ for some $t \in (x, x + h)$ , then $g$ attains its maximum at some $c$ and $c \in (x, x + h)$ . Consequently, $\frac{dg}{dx}(c) = 0$ . On the other hand,

$$
\frac {d g}{d \alpha} (c) = (f (x + h) - f (x)) - (\alpha (x + h) - \alpha (x)) \frac {d f}{d \alpha} (c).
$$

It then follows that

$$
\frac {f (x + h) - f (x)}{\alpha (x + h) - \alpha (x)} = \frac {d f}{d \alpha} (c)
$$

with some $c$ between $x$ and $x + h$ .

Thus for any partition $\{x_0, x_1, \ldots, x_n\}$ of $[a, b]$ we have

$$
\begin{array}{l} f (b) - f (a) = \sum_ {k = 1} ^ {n} \frac {f \left(x _ {k}\right) - f \left(x _ {k - 1}\right)}{\alpha \left(x _ {k}\right) - \alpha \left(x _ {k - 1}\right)} (\alpha \left(x _ {k}\right) - \alpha \left(x _ {k - 1}\right)) \\ = \sum_ {k = 1} ^ {n} \frac {d f}{d \alpha} (t _ {k}) (\alpha (x _ {k}) - \alpha (x _ {k - 1})) \\ \end{array}
$$

with some $t_k \in (x_{k-1}, x_k)$ . On the other hand, by the first mean value theorem,

$$
\begin{array}{l} \int_ {a} ^ {b} \frac {d f}{d \alpha} (x) d \alpha (x) = \sum_ {k = 1} ^ {n} \int_ {x _ {k - 1}} ^ {x _ {k}} \frac {d f}{d \alpha} (x) d \alpha (x) \\ = \sum_ {k = 1} ^ {n} \frac {d f}{d \alpha} (\tau_ {k}) (\alpha (x _ {k}) - \alpha (x _ {k - 1})) \\ \end{array}
$$

with some $\tau_{k} \in [x_{k-1}, x_{k}]$ . Now, the uniform continuity of $\frac{df}{d\alpha}$ implies that, given $\varepsilon > 0$ ,

$$
\left| \frac {d f}{d \alpha} (\tau_ {k}) - \frac {d f}{d \alpha} (t _ {k}) \right| <   \frac {\varepsilon}{\alpha (b) - \alpha (a)}
$$

if the mesh of the partition is sufficiently small. Consequently,

$$
\left| \int_ {a} ^ {b} \frac {d f}{d \alpha} (x) d \alpha (x) - (f (b) - f (a)) \right| <   \varepsilon .
$$

# 1.2. Functions of Bounded Variation

1.2.1. It is clear that $f$ is differentiable on $[0, 1]$ . To show that it is of unbounded variation, consider the partition

$$
0 <   \sqrt {\frac {1}{n}} <   \sqrt {\frac {1}{n - 1 / 2}} <   \sqrt {\frac {1}{n - 1}} <   \dots <   \sqrt {\frac {1}{2}} <   \sqrt {\frac {1}{2 - 1 / 2}} <   1.
$$

Since on each of the intervals $[1 / \sqrt{i}, 1 / \sqrt{i - 1 / 2}]$ , $i = 2, 3, \ldots, n$ , and $[1 / \sqrt{i + 1 / 2}, 1 / \sqrt{i}]$ , $i = 1, 2, \ldots, n - 1$ , the function is monotonic, we see that

$$
V (f; 0, 1) \geq 1 + \sum_ {i = 2} ^ {n} \frac {2}{i} \xrightarrow [ n \rightarrow \infty ]{} \infty .
$$

1.2.2. By the mean value theorem, for any partition $a = x_0 < x_1 < \dots < x_n = b$ ,

$$
\sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) | = \sum_ {i = 1} ^ {n} | f ^ {\prime} (\xi_ {i}) | (x _ {i} - x _ {i - 1}) \leq M (b a),
$$

where $M = \sup_{\pmb {x}\in [a,b]}|f^{\prime}(\pmb {x})|$

1.2.3. Since $f'$ is bounded on $[0, 1]$ , by the result in the previous problem, $f$ is of bounded variation on $[0, 1]$ .

1.2.4. Clearly, if $f$ is monotonically increasing on $[a, b]$ , then

$$
V (f; a, b) = f (b) - f (a).
$$

To show the other implication, assume that $V(f; a, b) = f(b) - f(a)$ and take $a \leq x_1 \leq x_2 \leq b$ . Then

$$
f (b) - f (a) \leq | f (x _ {i}) - f (a) | + | f (b) - f (x _ {i}) | \leq V (f; a, b) = f (b) - f (a).
$$

Hence $f(a) \leq f(x_i) \leq f(b), i = 1,2$ . Consequently,

$$
\begin{array}{l} f (b) - f (a) \leq f \left(x _ {1}\right) - f (a) + \left| f \left(x _ {2}\right) - f \left(x _ {1}\right) \right| + f (b) - f \left(x _ {2}\right) \\ \leq V (f; a, b) = f (b) - f (a), \\ \end{array}
$$

which gives $f(x_{2}) - f(x_{1}) = |f(x_{2}) - f(x_{1})| \geq 0$ .

1.2.5. We first show that if $\alpha \leq \beta$ , then $V(f;0,1) = +\infty$ . Indeed, taking

$$
0 <   \frac {1}{n ^ {1 / \beta}} <   \frac {1}{(n - 1 / 2) ^ {1 / \beta}} <   \frac {1}{(n - 1) ^ {1 / \beta}} <   \dots <   \frac {1}{(2 - 1 / 2) ^ {1 / \beta}} <   1,
$$

we see that

$$
V (f; 0, 1) \geq 1 + \sum_ {i = 2} ^ {n} \frac {2}{i ^ {\alpha / \beta}} \xrightarrow [ n \to \infty ]{} \infty .
$$

Our task is now to show that if $\alpha > \beta$ , then $V(f; 0, 1) < +\infty$ . Let $P = \{x_0, x_1, \ldots, x_n\}$ be a partition of $[0, 1]$ . Take $n$ so large that $n^{-1/\beta} < x_1$ , and add to the partition $P$ points

$$
\frac {1}{n ^ {1 / \beta}}, \frac {1}{(n - 1 / 2) ^ {1 / \beta}}, \frac {1}{(n - 1) ^ {1 / \beta}}, \dots , \frac {1}{2 ^ {1 / \beta}}, \frac {1}{(2 - 1 / 2) ^ {1 / \beta}}.
$$

Note also that $f$ is monotonic on each interval $[i^{-1/\beta}, (i - 1/2)^{-1/\beta}]$ , $i = 2, 3, \ldots, n$ , and $[(i + 1/2)^{-1/\beta}, i^{-1/\beta}]$ , $i = 1, 2, \ldots, n - 1$ . Thus

$$
\sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) | \leq \sum_ {i = 1} ^ {n} \frac {2}{i ^ {\alpha / \beta}} \leq 2 \sum_ {i = 1} ^ {\infty} \frac {1}{i ^ {\alpha / \beta}} <   + \infty .
$$

1.2.6. It follows immediately from the definition of $V(f; a, b)$ that for $x \in [a, b]$ ,

$$
| f (x) | \leq | f (a) | + V (f; a, b).
$$

1.2.7. It follows from the preceding problem that the functions $f$ and $g$ are bounded on $[a, b]$ ; that is, there are positive constants $C$ and $D$ such that $|f(x)| < C$ and $|g(x)| < D$ on $[a, b]$ . If $h = fg$ , then for any partition of $[a, b]$ we have

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} \left| h \left(x _ {i}\right) - h \left(x _ {i - 1}\right) \right| \\ \leq C \sum_ {i = 1} ^ {n} | g (x _ {i}) - g (x _ {i - 1}) | + D \sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) | \\ \leq C V (g; a, b) + D V (f; a, b). \\ \end{array}
$$

Now to prove the second statement, it is enough to show that if $f$ is of bounded variation on $[a,b]$ and $\inf_{x\in [a,b]}|f(x)| = c > 0$ , then $1 / f$ is also of bounded variation on $[a,b]$ . For any partition of $[a,b]$ we get

$$
\sum_ {i = 1} ^ {n} \left| \frac {1}{f (x _ {i})} - \frac {1}{f (x _ {i - 1})} \right| = \sum_ {i = 1} ^ {n} \left| \frac {f (x _ {i}) - f (x _ {i - 1})}{f (x _ {i}) f (x _ {i - 1})} \right| \leq \frac {1}{c ^ {2}} V (f; a, b).
$$

1.2.8. No. Consider the functions

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} \cos^ {2} \frac {\pi}{x} & \text {i f} x \in (0, 1 ], \\ 0 & \text {i f} x = 0 \end{array} \right.
$$

and $g(y) = \sqrt{y}, y \in [0,1]$ . Both of them are of bounded variation on [0,1] (the derivative $f'$ is bounded on [0,1] and $g$ is monotonically increasing) and the composition $h(x) = g(f(x))$ is given by

$$
h (x) = \left\{ \begin{array}{l l} x \left| \cos \frac {\pi}{x} \right| & \text {i f} x \in (0, 1 ], \\ 0 & \text {i f} x = 0. \end{array} \right.
$$

To see that $h$ is not of bounded variation, take the partition

$$
0 <   \frac {1}{n} <   \frac {1}{n - 1 / 2} <   \frac {1}{n - 1} <   \dots <   \frac {1}{2} <   \frac {1}{2 - 1 / 2} <   1
$$

and note that

$$
V (f; a, b) \geq \frac {2}{n} + \frac {2}{n - 1} + \dots + \frac {2}{2} + 1.
$$

1.2.9. Let $g: [a, b] \to [c, d]$ and $f: [c, d] \to \mathbb{R}$ . If $f$ satisfies a Lipschitz condition, then there is a nonnegative $L$ , called the Lipschitz constant, such that $|f(x) - f(y)| \leq L|x - y|$ for all $x, y \in [c, d]$ . Thus for any partition of $[a, b]$ ,

$$
\sum_ {i = 1} ^ {n} | f (g (x _ {i})) - f (g (x _ {i - 1})) | \leq L \sum_ {i = 1} ^ {n} | g (x _ {i}) - g (x _ {i - 1}) | \leq L V (g; a, b).
$$

1.2.10. Clearly, if $f$ is of bounded variation on $[a, b]$ , then so is $|f|$ , and by 1.2.6, $f$ is bounded. Since $x \mapsto x^p$ satisfies a Lipschitz condition on any bounded interval in the domain, the assertion follows from the result in the preceding problem.

1.2.11. Observe first that if $a = x_0 < x_1 < \dots < x_n = b$ , then $|f(x_i) - f(x_{i-1})| = ||f(x_i)| - |f(x_{i-1})||$ in the case when $f(x_i)$ and $f(x_{i-1})$ are both nonnegative or nonpositive. In the other case, the continuity of $f$ implies that there is $\xi_i \in (x_{i-1}, x_i)$ such that $f(\xi_i) = 0$ . Then

$$
\begin{array}{l} | f (x _ {i}) - f (x _ {i - 1}) | = | f (x _ {i}) - f (\xi_ {i}) + f (\xi_ {i}) - f (x _ {i - 1}) | \\ \leq | f (x _ {i}) - f (\xi_ {i}) | + | f (\xi_ {i}) - f (x _ {i - 1}) | \\ = \left\| f \left(x _ {i}\right) \right| - \left| f \left(\xi_ {i}\right) \right| + \left\| f \left(\xi_ {i}\right) \right| - \left| f \left(x _ {i - 1}\right) \right|. \\ \end{array}
$$

Consequently,

$$
\sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) | \leq 2 V (| f |; a, b).
$$

The following example shows that continuity is an essential assumption:

$$
f (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x \in [ a, b ] \cap \mathbb {Q}, \\ - 1 & \text {i f} x \in [ a, b ] \backslash \mathbb {Q}. \end{array} \right.
$$

1.2.12. Since

$$
h (x) = \max  \{f (x), g (x) \} = \frac {\left| f (x) - g (x) \right| + f (x) + g (x)}{2},
$$

the result follows from the facts that a linear combination of two functions of bounded variation is also of bounded variation and that the absolute value of a function of bounded variation is of bounded variation (see 1.2.10).

1.2.13. (a) Since for $\alpha > 0$ ,

$$
\lim  _ {x \rightarrow 0 ^ {+}} \frac {f (x) - f (0)}{x ^ {\alpha}} = \lim  _ {x \rightarrow 0 ^ {+}} \frac {x ^ {- a}}{- \ln x} = + \infty ,
$$

we see that $f$ does not satisfy any Hölder condition. Clearly, $f$ is monotonically increasing on $[0, 1/2]$ , and so $V(f; 0, 1/2) = 1 / (\ln 2)$ .

(b) We show that $f$ satisfies the Hölder condition with every $0 < \alpha < 1$ . To this end, suppose first that $x, x' \in [x_{n+1}, x_n]$ , $x \neq x'$ , and put $g(x) = 2(\ln^2 n)(x - x_{n+1})$ on all of $[x_{n+1}, x_n]$ . Then,

$$
\begin{array}{l} \frac {\left| f (x) - f \left(x ^ {\prime}\right) \right|}{\left| x - x ^ {\prime} \right| ^ {\alpha}} \leq \frac {\left| g (x) - g \left(x ^ {\prime}\right) \right|}{\left| x - x ^ {\prime} \right| ^ {\alpha}} = \frac {2 \left(\ln^ {2} n\right) \left| x - x ^ {\prime} \right|}{\left| x - x ^ {\prime} \right| ^ {\alpha}} \\ \leq \frac {2 \ln^ {2} n}{n ^ {1 - \alpha} \ln^ {2 (1 - \alpha)} n} \xrightarrow [ n \to \infty ]{} 0. \\ \end{array}
$$

Consequently, there is a positive $C$ such that

$$
\frac {\left| f (x) - f \left(x ^ {\prime}\right) \right|}{\left| x - x ^ {\prime} \right| ^ {a}} \leq C.
$$

Assume now that $x < x'$ , $x \in [x_{n+1}, x_n]$ and $x' \in [x_{k+1}, x_k]$ , where $n > k$ . It then follows that

$$
\begin{array}{l} | f (x) - f \left(x ^ {\prime}\right) | \leq | f (x) - f \left(x _ {n}\right) | + | f \left(x _ {k + 1}\right) - f \left(x ^ {\prime}\right) | \\ \leq C | x - x _ {n} | ^ {\alpha} + C | x _ {k + 1} - x ^ {\prime} | ^ {\alpha} \\ \leq 2 C \max  \left\{\left| x - x _ {n} \right| ^ {\alpha}, \left| x _ {k + 1} - x ^ {\prime} \right| ^ {\alpha} \right\} \\ \leq 2 C | x - x ^ {\prime} | ^ {a}. \\ \end{array}
$$

To see that $f$ is not of bounded variation, take the partition

$$
0 <   x _ {n} <   \frac {x _ {n} + x _ {n - 1}}{2} <   x _ {n - 1} <   \dots <   x _ {3} <   \frac {x _ {3} + x _ {2}}{2} <   x _ {2}
$$

and note that

$$
V (f; 0, x _ {2}) \geq \frac {2}{n} + \frac {2}{n - 1} + \dots + \frac {2}{2} \xrightarrow [ n \to \infty ]{} \infty .
$$

1.2.14. Since $V(f; a, \infty) = \lim_{b \to \infty} V(f; a, b) < \infty$ , the Cauchy theorem (sec, c.g., II, 1.1.37) implies that, given $\epsilon > 0$ , there is $M > a$ such that

$$
V (f; a, x) - V (f; a, x ^ {\prime}) = V (f; x ^ {\prime}, x) <   \varepsilon
$$

whenever $x > x' > M$ . Thus

$$
| f (x ^ {\prime}) - f (x) | \leq V (f; x ^ {\prime}, x) <   \varepsilon ,
$$

which together with the Cauchy theorem shows that $\lim_{x\to \infty}f(x)$ exists and is finite.

To see that the other implication does not hold, consider the function $f(x) = \frac{|\sin x|}{x}$ , $x \geq 1$ . Clearly, $\lim_{x \to \infty} f(x) = 0$ and

$$
V (f; 1, n \pi) \geq \sin 1 + \frac {4}{\pi} \left(\frac {1}{3} + \frac {1}{5} + \dots + \frac {1}{2 n - 1}\right) \xrightarrow [ n \to \infty ]{} \infty .
$$

1.2.15. Let $\varepsilon > 0$ be arbitrarily chosen. It follows from the definition of the total variation $V(f; a, b)$ that there is a partition, say $P^{*} = \{x_{0}^{*}, x_{1}^{*}, \ldots, x_{m}^{*}\}$ , such that

$$
V (f, P ^ {*}) > V (f; a, b) - \frac {\varepsilon}{2}.
$$

Since $f$ is uniformly continuous on $[a, b]$ , we select $\delta > 0$ so small that if $|x - x'| < \delta$ , then

$$
| f (x) - f \left(x ^ {\prime}\right) | <   \frac {\varepsilon}{4 m}.
$$

From a partition $P$ of mesh less than $\delta$ we form a partition $P_{1}$ by adjoining all points of $P^{*}$ . Then

$$
V (f, P) \leq V (f, P _ {1}) \quad \text {a n d} \quad V (f, P ^ {*}) \leq V (f, P _ {1}).
$$

Moreover,

$$
V (f, P _ {1}) \leq V (f, P) + \frac {\varepsilon}{2},
$$

because $P_{1}$ is obtained from $P$ by adding at most $m$ new points and therefore $V(f, P)$ increases by at most $2m(\varepsilon/(4m))$ . Consequently,

$$
V (f, P) \geq V (f, P _ {1}) - \frac {\varepsilon}{2} \geq V (f, P ^ {*}) - \frac {\varepsilon}{2} > V (f; a, b) - \varepsilon .
$$

1.2.16. Since $f$ is continuous, there are points in $[x_{i-1}, x_i]$ at which $f$ assumes the values $M_i$ and $m_i$ . It is also clear that $|f(x_i) - f(x_{i-1})| \leq M_i - m_i$ . Thus for any partition $P$ ,

$$
V (f; a, b) \geq W (f, P) \geq V (f, P).
$$

It follows from the previous problem that, given $\varepsilon > 0$ , there is $\delta > 0$ such that $V(f; a, b) - V(f, P) < \varepsilon$ if $\mu(P) < \delta$ . Consequently,

$$
0 \leq V (f; a, b) - W (f, P) \leq V (f; a, b) - V (f, P) <   \varepsilon .
$$

1.2.17. It is clear that if $f = \alpha g_{1} + \beta g_{2}$ , and $g_{1}, g_{2}$ are of bounded variation, then $V(f; a, b) \leq |\alpha|V(g_{1}; a, b) + |\beta|V(g_{2}; a, b)$ . So, for $a \leq x < y \leq b$ ,

$$
\begin{array}{l} V (f; x, y) \leq V (p _ {1}; x, y) + V (q _ {1}; x, y) \\ = p _ {1} (y) - p _ {1} (x) + q _ {1} (y) - q _ {1} (x). \\ \end{array}
$$

By definition,

$$
\begin{array}{l} p (y) - p (x) = \frac {1}{2} \left(v _ {f} (y) + f (y) - v _ {f} (x) - f (x)\right) \\ = \frac {1}{2} (V (f; x, y) + f (y) - f (x)). \\ \end{array}
$$

Consequently,

$$
\begin{array}{l} p (y) - p (x) \\ \leq \frac {1}{2} (p _ {1} (y) - p _ {1} (x) + q _ {1} (y) - q _ {1} (x) + p _ {1} (y) - q _ {1} (y) - p _ {1} (x) + q _ {1} (x)) \\ = p _ {1} (y) \quad p _ {1} (x). \\ \end{array}
$$

This immediately implies that $V(p; a, b) \leq V(p_1; a, b)$ . The analogous conclusion can be drawn for $q$ and $q_1$ .

1.2.18. Since $f$ is of bounded variation, it is bounded above, say by $M > 0$ . Let $F(x) = \ln x$ , $x \in [m, M]$ . Then $F$ satisfies a Lipschitz condition, because $F'$ is bounded on $[m, M]$ . It follows from the result in 1.2.9 that $F \circ f = \ln f$ is of bounded variation on $[a, b]$ . By Theorem 1,

$$
\ln f = p - q,
$$

where $p$ and $q$ are monotonically increasing on $[a, b]$ . Hence one can take $g = e^p$ and $h = e^q$ .

1.2.19. (a) We have

$$
v _ {f} (x) = \left\{ \begin{array}{l l} f (x) + 2 & \text {i f} x \in [ - 1, 0 ], \\ 2 - f (x) & \text {i f} x \in [ 0, \sqrt {3} / 3 ], \\ f (x) + 2 + \frac {4 \sqrt {3}}{9} & \text {i f} x \in [ \sqrt {3} / 3, 1 ]. \end{array} \right.
$$

Thus

$$
p (x) = \left\{ \begin{array}{l l} f (x) + 2 & \text {i f} x \in [ - 1, 0 ], \\ 2 & \text {i f} x \in [ 0, \sqrt {3} / 3 ], \\ f (x) + 2 + \frac {2 \sqrt {3}}{9} & \text {i f} x \in [ \sqrt {3} / 3, 1 ], \end{array} \right.
$$

and

$$
q (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \in [ - 1, 0 ], \\ - f (x) & \text {i f} x \in [ 0, \sqrt {3} / 3 ], \\ \frac {2 \sqrt {3}}{9} & \text {i f} x \in [ \sqrt {3} / 3, 1 ]. \end{array} \right.
$$

(b) It easy to check that

$$
v _ {f} (x) = \left\{ \begin{array}{l l} 1 - \cos x & \text {i f} x \in [ 0, \pi ], \\ \cos x + 3 & \text {i f} x \in [ \pi , 2 \pi ], \end{array} \right.
$$

$$
p (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \in [ 0, \pi ], \\ \cos x + 1 & \text {i f} x \in [ \pi , 2 \pi ], \end{array} \right.
$$

and

$$
q (x) = \left\{ \begin{array}{l l} 1 - \cos x & \text {i f} x \in [ 0, \pi ], \\ 2 & \text {i f} x \in [ \pi , 2 \pi ]. \end{array} \right.
$$

(c) We have

$$
v _ {f} (x) = \left\{ \begin{array}{l l} x & \text {i f} x \in [ 0, 1), \\ 1 + x & \text {i f} x \in [ 1, 2), \\ 2 + x & \text {i f} x \in [ 2, 3), \\ 6 & \text {i f} x = 3, \end{array} \right.
$$

and

$$
p (x) = x \quad \text {a n d} \quad q (x) = [ x ].
$$

1.2.20. Let $x_0 \in [a, b)$ and $\lim_{x \to x_0^+} f(x) = f(x_0^+) = f(x_0)$ . It suffices to show that $\lim_{x \to x_0^+} V(f; x_0, x) = 0$ . Given $\varepsilon > 0$ , there is $\zeta > x_0$ such that $|f(x) - f(x_0)| < \varepsilon / 2$ if $x_0 < x < \zeta$ . It follows from the definition of the total variation that there is a partition $x_0 < x_1 < \dots < x_n = b$ such that

$$
V (f; x _ {0}, b) \leq | f (x _ {1}) \quad f (x _ {0}) | \mid \dots | | f (x _ {n}) \quad f (x _ {n - 1}) | \vdash_ {2} ^ {\varepsilon}.
$$

Hence for $x_0 < x < \min \{x_1, \zeta\}$ , we have

$$
\begin{array}{l} V (f; x _ {0}, b) \leq | f (x) - f (x _ {0}) | + | f (x _ {1}) - f (x) | \\ + \dots + | f (x _ {n}) - f (x _ {n} 1) | + \frac {\varepsilon}{2} \leq \varepsilon + V (f; x, b), \\ \end{array}
$$

which implies $\lim_{x \to x_0^+} V(f; x_0, x) = 0$ . The other part of the statement can be proved analogously.

It is worth noting here that a function $f$ of bounded variation is continuous at $x_0$ if and only if $v_f$ is continuous at $x_0$ . In view of what we have proved it is enough to show that if $v_f$ is continuous at $x_0$ , then so is $f$ . This follows immediately from $|f(x) - f(x_0)| \leq |v_f(x) - v_f(x_0)|$ .

1.2.21. By Theorem 1, the function $f$ can be represented as the difference of two monotonically increasing functions, that is, $f = p - q$ . Since the set of points of discontinuity of a monotonically increasing function is at most countably infinite (see, e.g., II, 1.2.29), the same is true for a function of bounded variation. Note also that at every point $x_{n}$ of discontinuity of $f$ the one-sided limits exist (see, e.g., II, 1.1.35), and so the function $s$ is well defined. It follows from the result in 1.2.20 that all points of continuity of $f$ are also points of continuity

of the functions $p$ and $q$ . Consequently, all points of discontinuity of $p$ and $q$ are contained in $\{x_n\}$ . It suffices to show that the functions $g_p = p - s_p$ and $g_q = q - s_q$ , where $s_p$ and $s_q$ are the saltus functions of $p$ and $q$ , respectively, are continuous. We will only show that $g_p$ is continuous. For $a \leq x < b$ , we have

$$
s _ {p} (x ^ {+}) = p (a ^ {+}) - p (a) + \sum_ {x _ {n} \leq x} (p (x _ {n} ^ {+}) - p (x _ {n} ^ {-}),
$$

because $\lim_{t\to x^{+}}p(x^{-}) = p(x^{+})$ (see, e.g., II 1.1.36(a)). It then follows that $p(x^{+}) - p(x) = s_{p}(x^{+}) - s_{p}(x)$ , showing $g_{p}(x^{+}) = g_{p}(x)$ . Moreover, for $a < x \leq b$ ,

$$
s _ {p} \left(x ^ {-}\right) = p \left(a ^ {+}\right) - p (a) + \sum_ {x _ {n} <   x} \left(p \left(x _ {n} ^ {+}\right) - p \left(x _ {n} ^ {-}\right), \right.
$$

which gives $g_{p}(x^{-}) = g_{p}(x)$

In this way we have proved that every function of bounded variation can be represented as the sum of its saltus function and a continuous function.

1.2.22. By Theorem 1, $f(x) - f(a) = p(x) - q(x)$ , where $p$ and $q$ are the positive and negative variation functions of $f$ . The functions $p$ and $q$ are Riemann integrable (see 1.1.21) on $[a,b]$ , and $\int_{a}^{b}f(x)dx = f(a)(b - a) + \int_{a}^{b}p(x)dx - \int_{a}^{b}q(x)dx$ . To prove the assertion it is enough to show that if $p$ is monotonically increasing on $[a,b]$ , then so is $g$ defined by

$$
g (a) = 0 \quad \text {a n d} \quad g (x) = \frac {1}{x - a} \int_ {a} ^ {x} p (t) d t, \quad x \in (a, b ].
$$

Indeed, if $a < x < y \leq b$ , then

$$
\begin{array}{l} g (y) - g (x) = \frac {1}{y - a} \int_ {a} ^ {y} p (t) d t - \frac {1}{x - a} \int_ {a} ^ {x} p (t) d t \\ = \frac {x - y}{(x - a) (y - a)} \int_ {a} ^ {x} p (t) d t + \frac {1}{y - a} \int_ {x} ^ {y} p (t) d t \\ \geq \frac {x - y}{(x - a) (y - a)} \int_ {a} ^ {x} p (t) d t + \frac {1}{y - a} \int_ {x} ^ {y} p (x) d t \\ = \frac {y - x}{(x - a) (y - a)} \int_ {a} ^ {x} (p (x) - p (t)) d t \geq 0. \\ \end{array}
$$

1.2.23. Indeed, suppose that $|f(x') - f(x'')| \leq L|x' - x''|$ for $x', x'' \in [a, b]$ . If $x' = x_0 < x_1 < \dots < x_n = x''$ , then

$$
\sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) | \leq \sum_ {i = 1} ^ {n} L (x _ {i} - x _ {i - 1}) = L \left(x ^ {\prime \prime} - x ^ {\prime}\right).
$$

Taking the supremum over all partitions of $[x', x'']$ yields

$$
v _ {f} \left(x ^ {\prime \prime}\right) - v _ {f} \left(x ^ {\prime}\right) = V \left(f; x ^ {\prime}, x ^ {\prime \prime}\right) \leq L \left(x ^ {\prime \prime} - x ^ {\prime}\right).
$$

1.2.24. By Theorem 1, $f = p - q$ , where $p$ and $q$ are monotone on $[a, b]$ . So, the one-sided limits of $f$ exist at every point of $[a, b]$ (see, e.g., II, 1.1.35). Suppose, contrary to our claim, that $x_0$ is a point of discontinuity of $f$ . If $f(x_0^+) - f(x_0^-) = d > 0$ , then by the definition of one-sided limits there is $\delta > 0$ such that

$$
f (x) <   f \left(x _ {0} ^ {-}\right) + \frac {d}{3} \quad \text {f o r} \quad x \in \left(x _ {0} - \delta , x _ {0}\right)
$$

and

$$
f (x) > f \left(x _ {0} ^ {+}\right) - \frac {d}{3} \quad \text {f o r} \quad x \in \left(x _ {0}, x _ {0} + \delta\right).
$$

Then, if $y \in [f(x_0^-) + d/3, f(x_0^+) - d/3] \setminus \{f(x_0)\} \subset [f(x_1), f(x_2)] \setminus \{f(x_0)\}$ with $x_1 \in (x_0 - \delta, x_0)$ and $x_2 \in (x_0, x_0 + \delta)$ , there is no $x \in (x_1, x_2)$ such that $f(x) = y$ , a contradiction. If $f(x_0^+) = f(x_0^-) \neq f(x_0)$ , analogous reasoning can be applied.

Since the derivative $f'$ enjoys the intermediate value property (see, e.g., II, 2.2.31), the other statement follows immediately.

1.2.25. For $x \in [a, b]$ , let $P = \{x_0, x_1, \ldots, x_n\}$ be a partition of $[a, x]$ . Since $f'$ is continuous on $[a, b]$ , the results in 1.2.15 and in 1.1.26 imply that

$$
\begin{array}{l} v _ {f} (x) = \lim  _ {\mu (P) \rightarrow 0} \sum_ {k = 1} ^ {n} | f (x _ {k}) - f (x _ {k - 1}) | \\ = \lim  _ {\mu (P) \rightarrow 0} \sum_ {k = 1} ^ {n} \left| \int_ {x _ {k - 1}} ^ {x _ {k}} f ^ {\prime} (t) d t \right| \\ = \lim  _ {\mu (P) \rightarrow 0} \sum_ {k = 1} ^ {n} | f ^ {\prime} (t _ {k}) | (x _ {k} - x _ {k - 1}) = \int_ {a} ^ {x} | f ^ {\prime} (t) | d t. \\ \end{array}
$$

1.2.26. Clearly, there is $M > 0$ such that $|f(x)| \leq M$ for $x \in [a, b]$ . Moreover, for $a = x_0 < x_1 < \dots < x_n = b$ , using the first mean value theorem (see, e.g., 1.1.26), we get

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} | F (x _ {i}) - F (x _ {i - 1}) | \\ = \sum_ {i = 1} ^ {n} \left| \int_ {a} ^ {x _ {1}} f (t) d \alpha (t) - \int_ {a} ^ {x _ {1} - 1} f (t) d \alpha (t) \right| \\ = \sum_ {i = 1} ^ {n} \left| \int_ {x _ {i - 1}} ^ {x _ {i}} f (t) d \alpha (t) \right| \\ = \sum_ {i = 1} ^ {n} | f (\xi_ {i}) (\alpha (x _ {i}) - \alpha (x _ {i - 1})) | \\ \leq M (\alpha (b) - \alpha (a)). \\ \end{array}
$$

It then follows that $V(F; a, b) \leq M(\alpha(b) - \alpha(a))$ .

1.2.27. If $\lim_{n\to \infty}V(f_n;a,b) = +\infty$ , the inequality is obvious. So, suppose that $\lim_{n\to \infty}V(f_n;a,b) = l < +\infty$ . Then, given $\varepsilon > 0$ , there is a subsequence $\{n_k\}$ such that $V(f_{n_k};a,b) < l + \varepsilon$ . Thus for any partition $a = x_0 < x_1 < \dots < x_n = b$ ,

$$
\sum_ {i = 1} ^ {n} \left| f _ {n _ {k}} \left(x _ {i}\right) - f _ {n _ {k}} \left(x _ {i - 1}\right) \right| <   l + \varepsilon .
$$

Letting $k$ tend to infinity, we get

$$
\sum_ {i = 1} ^ {n} | f (x _ {i}) - f (x _ {i - 1}) | \leq l + \varepsilon ,
$$

and the desired inequality follows.

1.2.28. Since the series $\sum_{n=1}^{\infty} a_n$ and $\sum_{n=1}^{\infty} b_n$ are absolutely convergent, given $\varepsilon > 0$ , there is $n_0$ such that

$$
\sum_ {n = n _ {0}} ^ {\infty} \left| a _ {n} \right| <   \varepsilon \quad \text {a n d} \quad \sum_ {n = n _ {0}} ^ {\infty} \left| b _ {n} \right| <   \varepsilon .
$$

If $x \neq x_k$ , $k = 1, 2, \ldots$ , then there exists a $\delta > 0$ such that there is no $x_n$ with $n < n_0$ in $(x - \delta, x + \delta)$ . Consequently, for $x - \delta < y < x$ ,

$$
| f (y) - f (x) | \leq \sum_ {y <   x _ {n} \leq x} | a _ {n} | + \sum_ {y \leq x _ {n} <   x} | b _ {n} | <   2 \varepsilon .
$$

Likewise, $|f(y) - f(x)| < 2\varepsilon$ for $x < y < x + \delta$ . So $f$ is continuous at every $x \neq x_k$ .

Now note that $f(x_{k}) = \sum_{x_{n} \leq x_{k}} a_{n} + \sum_{x_{n} < x_{k}} b_{n}$ and $f(x_{k}^{-}) = \sum_{x_{n} < x_{k}} a_{n} + \sum_{x_{n} < x_{k}} b_{n}$ . Indeed, if $\delta = \min \{|x_{n} - x_{k}| : n \leq n_{0}, n \neq k\}$ , then there is no $x_{n}$ with $n \leq n_{0}$ in $(x_{k} - \delta, x_{k})$ , and therefore, for $x_{k} - \delta < x < x_{k}$ ,

$$
\left| f (x) - \left(\sum_ {x _ {n} <   x _ {k}} a _ {n} + \sum_ {x _ {n} <   x _ {k}} b _ {n}\right) \right| = \left| \sum_ {x <   x _ {n} <   x _ {k}} a _ {n} + \sum_ {x \leq x _ {n} <   x _ {k}} b _ {n} \right| <   2 \varepsilon .
$$

Thus $f(x_{k}) - f(x_{k}^{-}) = a_{k}$ . In an entirely similar manner one can prove that $f(x_{k}^{+}) - f(x_{k}) = b_{k}$ .

Finally, we will show that

$$
V (f; 0, 1) = \sum_ {n = 1} ^ {\infty} (| a _ {n} | + | b _ {n} |).
$$

To this end, take a partition $0 = t_0 < t_1 < \dots < t_n = 1$ . Then

$$
\begin{array}{l} \sum_ {k = 1} ^ {n} | f (t _ {k}) - f (t _ {k - 1}) | - \sum_ {k = 1} ^ {n} \left| \sum_ {t _ {k - 1} <   x _ {n} \leq t _ {k}} a _ {n} + \sum_ {t _ {k - 1} \leq x _ {n} <   t _ {k}} b _ {n} \right| \\ \leq \sum_ {n = 1} ^ {\infty} | a _ {n} | + \sum_ {n = 1} ^ {\infty} | b _ {n} |. \\ \end{array}
$$

It then follows that

$$
V (f; 0, 1) \leq \sum_ {n = 1} ^ {\infty} \left(\left| a _ {n} \right| + \left| b _ {n} \right|\right).
$$

To prove the reverse inequality, fix $N$ arbitrarily and assume, without loss of generality, that $x_1 < x_2 < \dots < x_N$ . Since $f(x_k) - f(x_k^-) = a_k$ and $f(x_k^+) - f(x_k) = b_k$ , given $\varepsilon > 0$ , there are $x_{k+1}^{\prime}, x_{k}^{\prime \prime}$ such that $x_{k-1} < x_k' < x_k < x_{k+1}'' < x_{k+1}' < x_{k+1}$ , $k = 1, \ldots, N-1$ (where we

assume that $x_0 = 0$ ), and

$$
\left| f \left(x _ {k}\right) - f \left(x _ {k} ^ {\prime}\right) \right| > \left| a _ {k} \right| - \frac {\varepsilon}{2 N}, \quad \left| f \left(x _ {k} ^ {\prime \prime}\right) - f \left(x _ {k}\right) \right| > \left| b _ {k} \right| - \frac {\varepsilon}{2 N}.
$$

Taking the partition

$$
t _ {0} = 0 <   t _ {1} = x _ {1} ^ {\prime} <   t _ {2} = x _ {1} <   t _ {3} = x _ {1} ^ {\prime \prime} <   t _ {4} = x _ {2} ^ {\prime} <   \dots <   t _ {3 N + 2} = 1,
$$

we get

$$
\begin{array}{l} \sum_ {k = 1} ^ {3 N + 2} | f (t _ {k}) - f (t _ {k - 1}) | \geq \sum_ {k = 1} ^ {N} | f (x _ {k}) - f (x _ {k} ^ {\prime}) | + \sum_ {k = 1} ^ {N} | f (x _ {k} ^ {\prime \prime}) - f (x _ {k}) | \\ > \sum_ {k = 1} ^ {N} (| a _ {k} | + | b _ {k} |) - \varepsilon . \\ \end{array}
$$

The arbitrariness of $\varepsilon > 0$ yields

$$
V (f; 0, 1) \geq \sum_ {k = 1} ^ {N} (| a _ {k} | + | b _ {k} |).
$$

Letting $N \to \infty$ gives the desired inequality.

# 1.3. Further Properties of the Riemann-Stieltjes Integral

1.3.1. We have $\alpha(x) = \alpha_1(x) - \alpha_2(x)$ , where

$$
\alpha_ {1} (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x = - 1, \\ 1 & \text {i f} x \in (- 1, 3 ], \end{array} \right. \quad \text {a n d} \quad \alpha_ {2} (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \in [ - 1, 2), \\ 2 & \text {i f} x \in [ 2, 3 ] \end{array} \right.
$$

Thus, by the result in 1.1.24, we get

$$
\int_ {- 1} ^ {3} x d \alpha (x) = \int_ {- 1} ^ {3} x d \alpha_ {1} (x) - \int_ {- 1} ^ {3} x d \alpha_ {2} (x) = (- 1) \cdot 1 - 2 \cdot 2 = - 5.
$$

1.3.2. Integrating by parts and Theorem 3 give

$$
\begin{array}{l} \left| \int_ {0} ^ {2 \pi} f (x) \cos n x d x \right| = \left| \int_ {0} ^ {2 \pi} f (x) d \left(\frac {\sin n x}{n}\right) \right| \\ = \left| - \frac {1}{n} \int_ {0} ^ {2 \pi} \sin n x d f (x) \right| \\ \leq \frac {1}{n} \int_ {0} ^ {2 \pi} | \sin n x | d v _ {f} (x) \leq \frac {V (f ; 0 , 2 \pi)}{n}. \\ \end{array}
$$

1.3.3. Since $f$ is continuous on $[a, b]$ , there is $M > 0$ such that $|f(x)| \leq M$ , $x \in [a, b]$ . Assume first that $\alpha$ is monotonically increasing on $[a, b]$ . For a partition $P$ : $a = x_0 < x_1 < \dots < x_n = b$ , let $\xi_i$ be defined by the first mean value theorem, that is,

$$
\int_ {x _ {i - 1}} ^ {x _ {i}} f (x) d \alpha (x) = f \left(\xi_ {i}\right) \left(\alpha \left(x _ {i}\right) - \alpha \left(x _ {i - 1}\right)\right). \tag {1}
$$

It follows from 1.2.26 that $\beta$ is of bounded variation on $[a, b]$ . Let $\beta = \beta_{1} - \beta_{2}$ be a decomposition of $\beta$ into a difference of two increasing functions. Since $f$ and $g$ are continuous, we can apply the result in 1.1.10. It then follows that

$$
\int_ {a} ^ {b} f (x) g (x) d \alpha (x) = \lim  _ {\mu (P) \rightarrow 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}) g (\xi_ {i}) (\alpha (x _ {i}) - \alpha (x _ {i - 1})),
$$

where the $\xi_{i}$ are as in (1). Consequently,

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) g (x) d \alpha (x) = \lim  _ {\mu (P) \rightarrow 0} \sum_ {i = 1} ^ {n} g (\xi_ {i}) \int_ {x _ {i - 1}} ^ {x _ {i}} f (x) d \alpha (x) \\ = \lim  _ {\mu (P) \rightarrow 0} \sum_ {i = 1} ^ {n} g (\xi_ {i}) (\beta (x _ {i}) - \beta (x _ {i - 1})) \\ = \lim  _ {\mu (P) \rightarrow 0} \sum_ {i = 1} ^ {n} g (\xi_ {i}) \left(\beta_ {1} \left(x _ {i}\right) - \beta_ {1} \left(x _ {i - 1}\right)\right) \\ - \lim  _ {\mu (P) \rightarrow 0} \sum_ {i = 1} ^ {n} g (\xi_ {i}) \left(\beta_ {2} \left(x _ {i}\right) - \beta_ {2} \left(x _ {i - 1}\right)\right) \\ = \int_ {a} ^ {b} g (x) d \beta_ {1} (x) - \int_ {a} ^ {b} g (x) d \beta_ {2} (x) \\ = \int_ {a} ^ {b} g (x) d \beta (x). \\ \end{array}
$$

1.3.4. Since $\sum_{n=1}^{\infty} c_n$ is convergent, given $\varepsilon > 0$ , there is $N$ such that

$$
\sum_ {n = N + 1} ^ {\infty} c _ {n} <   \varepsilon .
$$

If we set

$$
\alpha_ {1} (x) = \sum_ {n = 1} ^ {N} c _ {n} \rho (x - x _ {n}) \quad \text {a n d} \quad \alpha_ {2} (x) = \alpha (x) - \alpha_ {1} (x),
$$

then by the result in 1.1.2,

$$
\int_ {0} ^ {1} f d \alpha_ {1} = \sum_ {n = 1} ^ {N} c _ {n} f (x _ {n}).
$$

Moreover,

$$
V (\alpha_ {2}; 0, 1) = \sum_ {n = N + 1} ^ {\infty} c _ {n} <   \varepsilon ,
$$

and consequently, by Theorem 3,

$$
\left| \int_ {0} ^ {1} f d \alpha - \int_ {0} ^ {1} f d \alpha_ {1} \right| = \left| \int_ {0} ^ {1} f d \alpha_ {2} \right| \leq M V (\alpha_ {2}; 0, 1) <   M \varepsilon ,
$$

where $M = \sup_{\pmb {x}\in [0,1]}|f(\pmb {x})|$

1.3.5. Taking $f(x) \equiv 1$ , we see that $\alpha(b) = \alpha(a)$ . Now, for $a < u < v < b$ , define $f$ by setting

$$
f (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x \in [ a, u ], \\ - 1 & \text {i f} x \in [ v, b ], \\ l (x) & \text {i f} x \in [ u, v ], \end{array} \right.
$$

where $l(x)$ is the linear function such that $l(u) = 1$ and $l(v) = -1$ . Then

$$
0 = \int_ {a} ^ {b} f (x) d \alpha (x) = \alpha (u) - \alpha (a) + \int_ {u} ^ {v} l (x) d \alpha (x) - \alpha (b) + \alpha (v),
$$

or equivalently,

$$
\alpha (u) + \alpha (v) - 2 \alpha (a) = - \int_ {u} ^ {v} l (x) d \alpha (x). \tag {1}
$$

Moreover,

$$
\int_ {u} ^ {v} l (x) d \alpha (x) = \int_ {u} ^ {v} l (x) d p (x) - \int_ {u} ^ {v} l (x) d q (x),
$$

where $p$ and $q$ are monotonically increasing and continuous on $[a, b]$ (see, e.g., 1.2.20). Using the first mean value theorem, we get, by the continuity of $p$ ,

$$
\lim  _ {v \rightarrow u ^ {+}} \int_ {u} ^ {v} l (x) d p (x) = \lim  _ {v \rightarrow u ^ {+}} l (c) (p (v) - p (u)) = 0.
$$

Consequently,

$$
\lim  _ {v \rightarrow u ^ {+}} \int_ {u} ^ {v} l (x) d \alpha (x) = 0.
$$

This combined with (1) shows that $2\alpha(u) = 2\alpha(a)$ .

1.3.6. For $0 < u < \pi / 2 < v < \pi$ ,

$$
\begin{array}{l} 0 = \int_ {0} ^ {\pi} (1 - \sin x) d \alpha (x) \\ = \int_ {0} ^ {u} (1 - \sin x) d \alpha (x) + \int_ {u} ^ {v} (1 - \sin x) d \alpha (x) \\ + \int_ {v} ^ {\pi} (1 - \sin x) d \alpha (x). \\ \end{array}
$$

Since $\alpha$ is monotonically increasing, each of the terms in the above equality is nonnegative, and consequently,

$$
\int_ {0} ^ {u} (1 - \sin x) d \alpha (x) = 0. \quad \text {a n d} \quad \int_ {v} ^ {\pi} (1 - \sin x) d \alpha (x) = 0.
$$

It then follows by the first mean value theorem that $\alpha(u) = \alpha(0)$ and $\alpha(v) = \alpha(\pi)$ .

1.3.7. Taking $f(x) \equiv 1$ , we see that $\alpha(1) - \alpha(0) = 1$ . For $0 < u < v < 1$ , define

$$
f _ {1} (x) = \left\{ \begin{array}{l l} \frac {1}{u} x & \text {i f} \quad x \in [ 0, u ], \\ 1 & \text {i f} \quad x \in [ u, v ], \\ \frac {- 1}{1 - v} (x - 1) & \text {i f} \quad x \in [ v, 1 ]. \end{array} \right.
$$

Then

$$
\begin{array}{l} \int_ {0} ^ {1} f _ {1} (x) d x (x) = \int_ {0} ^ {u} \frac {1}{u} x d x (x) + (\alpha (v) - \alpha (u)) \\ + \int_ {v} ^ {1} \frac {- 1}{1 - v} (x - 1) d \alpha (x) = 0. \\ \end{array}
$$

Hence each of the terms in the last equality vanishes. This gives $\alpha(u) = \alpha(v)$ for $u, v \in (0,1)$ . Now, for $0 < v < 1$ , consider the function $f_2$ given by

$$
f _ {2} (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x \in [ 0, v ], \\ \frac {- 1}{1 - v} (x - 1) & \text {i f} x \in [ v, 1 ]. \end{array} \right.
$$

By assumption,

$$
\alpha (v) - \alpha (0) + \int_ {v} ^ {1} f _ {2} (x) d \alpha (x) = \frac {1}{2}.
$$

Since $\alpha(u) = \alpha(v)$ for $u, v \in (0,1)$ , we get

$$
\int_ {v} ^ {1} f _ {2} (x) d \alpha (x) = f _ {2} (1) (\alpha (1) - \alpha (1 ^ {-})) = 0.
$$

It then follows that $\alpha(v) = \alpha(0) + 1/2$ for $0 < v < 1$ . Summing up,

$$
\alpha (x) = \left\{ \begin{array}{l l} \dot {\alpha} (0) & \text {i f} x = 0, \\ \alpha (0) + \frac {1}{2} & \text {i f} x \in (0, 1), \\ \alpha (0) + 1 & \text {i f} x = 1. \end{array} \right.
$$

1.3.8. Consider the function

$$
\alpha (x) = \left\{ \begin{array}{l l} \alpha (a) & \text {i f} x \in [ a, u), \\ \alpha (b) & \text {i f} x \in (u, b ], \end{array} \right.
$$

with $\alpha(a) < \alpha(b)$ . Then

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f (u) (\alpha (b) - \alpha (a)),
$$

which combined with our assumption gives $f(u) = 1$ for $u \in (a, b)$ . Since $f$ is continuous on $[a, b]$ , we see that $f(a) = f(b) = 1$ .

1.3.9. Since $\alpha = p - q$ , where $p, q$ are monotonically increasing, it is enough to show that $f \in \mathcal{R}(p)$ if $f_n \in \mathcal{R}(p)$ , $n = 1, 2, \ldots$ , and

$$
\int_ {a} ^ {b} f (x) d p (x) = \lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f _ {n} (x) d p (x).
$$

The uniform convergence of $\{f_n\}$ means that

$$
\sup  _ {x \in [ a, b ]} | f _ {n} (x) - f (x) | = d _ {n} \underset {n \rightarrow \infty} {\longrightarrow} 0.
$$

Thus, given $\varepsilon > 0$ , there is $n_0$ such that

$$
d _ {n} (p (b) - p (a)) <   \frac {\epsilon}{3} \quad \text {f o r} \quad n \geq n _ {0}.
$$

By Theorem 1 in Section 1.1, there is a partition $P$ such that

$$
U (P, f _ {n _ {0}}, p) - L (P, f _ {n _ {0}}, p) <   \frac {\varepsilon}{3}.
$$

Moreover, we have

$$
U (P, f, p) \leq U (P, f _ {n _ {0}}, p) + \frac {\varepsilon}{3}
$$

and

$$
L (P, f, p) \geq L (P, f _ {n _ {0}}, p) - \frac {\varepsilon}{3}.
$$

Thus we see that $f \in \mathcal{R}(p)$ . Now observe that for $n \geq n_0$ ,

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f _ {n} (x) d p (x) - \int_ {a} ^ {b} f (x) d p (x) \right| \leq \int_ {a} ^ {b} | f _ {n} (x) - f (x) | d p (x) \\ \leq \int_ {a} ^ {b} d _ {n} d p (x) <   \frac {\varepsilon}{3}. \\ \end{array}
$$

1.3.10. Observe that for $x \in [0, 1]$ we have $\lim_{n \to \infty} nx(1 - x^2)^n = 0$ , but the convergence is not uniform on $[0, 1]$ and the result in the previous problem cannot be applied. We have

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} n x (1 - x ^ {2}) ^ {n} d x = \lim  _ {n \rightarrow \infty} \frac {n}{2 (n + 1)} = \frac {1}{2}.
$$

1.3.11. As in the foregoing problem, we cannot apply the result in 1.3.9 because $\{x^n\}$ does not converge uniformly on $[0,1]$ .

Let $\alpha = p - q$ , where $p$ and $q$ are monotonically increasing on $[0,1]$ . For $\varepsilon \in (0,1)$ , we have

$$
0 \leq \int_ {0} ^ {\varepsilon} x ^ {n} d p (x) \leq \varepsilon^ {n} (p (\varepsilon) - p (0)) \underset {n \rightarrow \infty} {\longrightarrow} 0
$$

and

$$
\int_ {1 - \varepsilon} ^ {1} x ^ {n} d p (x) \leq p (1) - p (1 - \varepsilon).
$$

Moreover, if $1 / (n^2) < \varepsilon$ , then

$$
\begin{array}{l} \int_ {1 - \epsilon} ^ {1} x ^ {n} d p (x) \geq \int_ {1 - \frac {1}{n ^ {2}}} ^ {1} x ^ {n} d p (x) \\ \geq \left(1 - \frac {1}{n ^ {2}}\right) ^ {n} \left(p (1) - p \left(1 - \frac {1}{n ^ {2}}\right)\right). \\ \end{array}
$$

Consequently, letting $n \to \infty$ gives

$$
p (1) - p \left(1 ^ {-}\right) \leq \lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} x ^ {n} d p (x) \leq \varlimsup_ {n \rightarrow \infty} \int_ {0} ^ {1} x ^ {n} d p (x) \leq p (1) - p (1 - \varepsilon).
$$

Since $\varepsilon \in (0,1)$ can be arbitrarily small,

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} x ^ {n} d p (x) = p (1) - p \left(1 ^ {-}\right).
$$

The same reasoning can be applied to $q$ . Thus

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} x ^ {n} d \alpha (x) = \alpha (1) - \alpha (1 ^ {-}).
$$

1.3.12. By assumption, for any partition $a = x_0 < x_1 < \dots < x_m = b$ , we have

$$
\sum_ {k = 1} ^ {m} \left| \alpha_ {n} \left(x _ {k}\right) - \alpha_ {n} \left(x _ {k - 1}\right) \right| \leq M.
$$

Letting $n \to \infty$ , we see that

$$
\sum_ {k = 1} ^ {m} | \alpha (x _ {k}) - \alpha (x _ {k - 1}) | \leq M,
$$

which means that $\alpha$ is of bounded variation on $[a, b]$ . Moreover, we have

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f (x) d \alpha_ {n} (x) - \int_ {a} ^ {b} f (x) d \alpha (x) \right| \leq \sum_ {k = 1} ^ {m} \left| \int_ {x _ {k - 1}} ^ {x _ {k}} (f (x) - f (x _ {k})) d \alpha (x) \right| \\ + \sum_ {k = 1} ^ {m} | f (x _ {k}) | | \alpha (x _ {k}) - \alpha (x _ {k - 1}) - \alpha_ {n} (x _ {k}) + \alpha_ {n} (x _ {k - 1}) | \\ + \sum_ {k = 1} ^ {m} \left| \int_ {x _ {k - 1}} ^ {x _ {k}} (f (x _ {k}) - f (x)) d \alpha_ {n} (x) \right|. \\ \end{array}
$$

Now, by the continuity of $f$ , given $\varepsilon > 0$ , there is $\delta > 0$ such that if the mesh of the partition is less than $\delta$ , then $|f(x) - f(x_k)| < \varepsilon / (3M)$ for $x \in [x_{k-1}, x_k]$ . Consequently, by Theorem 3,

$$
\sum_ {k = 1} ^ {m} \left| \int_ {x _ {k - 1}} ^ {x _ {k}} (f (x) - f (x _ {k})) d \alpha (x) \right| <   \frac {\varepsilon}{3}
$$

and

$$
\sum_ {k = 1} ^ {m} \left| \int_ {x _ {k - 1}} ^ {x _ {k}} (f (x _ {k}) - f (x)) d \alpha_ {n} (x) \right| <   \frac {\varepsilon}{3}.
$$

Moreover, if $n$ is sufficiently large and the partition is fixed, we see that

$$
\sum_ {k = 1} ^ {m} | f (x _ {k}) | \left| \alpha (x _ {k}) - \alpha (x _ {k - 1}) - \alpha_ {n} (x _ {k}) + \alpha_ {n} (x _ {k - 1}) \right| <   \frac {\varepsilon}{3}.
$$

1.3.13. We have

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f _ {n} (x) d \alpha_ {n} (x) - \int_ {a} ^ {b} f (x) d \alpha (x) \right| \\ \leq \left| \int_ {a} ^ {b} f _ {n} (x) d \alpha_ {n} (x) - \int_ {a} ^ {b} f (x) d \alpha_ {n} (x) \right| \\ + \left| \int_ {a} ^ {b} f (x) d \alpha_ {n} (x) - \int_ {a} ^ {b} f (x) d \alpha (x) \right|. \\ \end{array}
$$

By the result in the previous problem, given $\varepsilon > 0$ , there is $n_0$ such that

$$
\left| \int_ {a} ^ {b} f (x) d \alpha_ {n} (x) - \int_ {a} ^ {b} f (x) d \alpha (x) \right| <   \frac {\varepsilon}{2}
$$

for $n \geq n_0$ . Moreover, by assumption there is a positive $M$ such that $V(\alpha_n; a, b) \leq M$ for all $n$ . Thus the uniform convergence of $\{f_n\}$ implies that, for sufficiently large $n$ ,

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f _ {n} (x) d \alpha_ {n} (x) - \int_ {a} ^ {b} f (x) d \alpha_ {n} (x) \right| \\ \leq \int_ {a} ^ {b} | f _ {n} (x) - f (x) | d v _ {\alpha_ {n}} (x) \\ \leq \sup  _ {x \in [ a, b ]} | f _ {n} (x) - f (x) | V (\alpha_ {n}; a, b) <   \frac {\varepsilon}{2 M} M. \\ \end{array}
$$

1.3.14. Observe first that the sequence $\{\alpha_{n}\}$ is uniformly bounded on $[a, b]$ . Indeed, for $x \in [a, b]$ and $n \in \mathbb{N}$ , we have

$$
\left| \alpha_ {n} (x) \right| \leq \left| \alpha_ {n} (x) - \alpha_ {n} (a) \right| + \left| \alpha_ {n} (a) \right| \leq V \left(\alpha_ {n}; a, b\right) + M \leq 2 M.
$$

By Theorem 1 in Section 1.2, we can write $\alpha_{n}(x) - \alpha_{n}(a) = p_{n}(x) - q_{n}(x)$ , where

$$
p _ {n} (x) = \frac {1}{2} \left(v _ {\alpha_ {n}} (x) + \alpha_ {n} (x) - \alpha_ {n} (a)\right)
$$

and

$$
q _ {n} (x) = \frac {1}{2} \left(v _ {\alpha_ {n}} (x) - \alpha_ {n} (x) + \alpha_ {n} (a)\right)
$$

are monotonically increasing on $[a, b]$ . It is easy to check that $\{p_n\}$ and $\{q_n\}$ are uniformly bounded. Therefore the sequence $\{p_n\}$ contains a subsequence $\{p_{n_\nu}\}$ pointwise convergent on $[a, b]$ (see, e.g., II, 3.1.23) and, in turn, $\{q_{n_\nu}\}$ contains a subsequence $\{q_{n_k}\}$ pointwise convergent on $[a, b]$ . Consequently, the sequence $\{\alpha_{n_k}\}$ , converges on $[a, b]$ , say to $\alpha$ . Clearly, $\alpha$ is of bounded variation. To get

$$
\lim  _ {k \rightarrow \infty} \int_ {a} ^ {b} f (x) d \alpha_ {n _ {k}} (x) = \int_ {a} ^ {b} f (x) d \alpha (x),
$$

it suffices to apply the result in 1.3.12.

1.3.15. Our aim is to show that

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (x) d \beta_ {n} (x) = 0, \quad \text {w h e r e} \quad \beta_ {n} = \alpha_ {n} - \alpha .
$$

Clearly, $V(\beta_{n}; a, b) \leq V(\alpha_{n}; a, b) + V(\alpha; a, b)$ . So, by assumption, there is a positive $M$ such that $V(\beta_{n}; a, b) \leq M$ for all $n$ . By the uniform continuity of $f$ , given $\varepsilon > 0$ , we can choose a partition $a = x_{0} < x_{1} < \dots < x_{m} = b$ , $x_{0}, x_{1}, \ldots, x_{m} \in \mathbf{A}$ , such that $|f(t) - f(s)| < \varepsilon / (2M)$ if $t, s \in [x_{k-1}, x_{k}]$ , $k = 1, 2, \ldots, m$ . Therefore

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f (x) d \beta_ {n} (x) - \sum_ {k = 1} ^ {m} f \left(t _ {k}\right) \left(\beta_ {n} \left(x _ {k}\right) - \beta_ {n} \left(x _ {k - 1}\right)\right) \right| \\ \leq \frac {\varepsilon}{2 M} V (\beta_ {n}; a, b) \leq \frac {\varepsilon}{2}. \\ \end{array}
$$

Since $\lim_{n\to \infty}\beta_n(x_k) = 0, k = 0,1,\ldots,m,$ beginning with some value of the index $n$

$$
\left| \sum_ {k = 1} ^ {m} f (t _ {k}) \left(\beta_ {n} \left(x _ {k}\right) - \beta_ {n} \left(x _ {k - 1}\right)\right) \right| \leq \frac {\varepsilon}{2}.
$$

This gives

$$
\left| \int_ {a} ^ {b} f (x) d \beta_ {n} (x) \right| \leq \varepsilon .
$$

1.3.16. The partial integration formula (Theorem 1) and the first mean value theorem (see, e.g., 1.1.26) imply that

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \alpha (x) = f (b) \alpha (b) - f (a) \alpha (a) - \int_ {a} ^ {b} \alpha (x) d f (x) \\ = f (b) \alpha (b) - f (a) \alpha (a) - \alpha (c) (f (b) - f (a)). \\ \end{array}
$$

1.3.17. (a) Set $m = \min \{\alpha(x): x \in [a, b]\}$ and $M = \max \{\alpha(x): x \in [a, b]\}$ . Using the partial integration formula, we get

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \alpha (x) = f (b) \alpha (b) - f (a) \alpha (a) - \int_ {a} ^ {b} \alpha (x) d f (x) \\ \leq f (b) \alpha (b) - f (a) \alpha (a) - m (f (b) - f (a)) \\ = (f (b) - f (a)) (\alpha (b) - m) + f (a) (\alpha (b) - \alpha (a)) \\ \leq (f (b) - f (a)) (\alpha (b) - m) + f (a) (\alpha (b) - m) \\ = f (b) (\alpha (b) - m). \\ \end{array}
$$

Likewise,

$$
\int_ {a} ^ {b} f (x) d \alpha (x) \geq f (b) (\alpha (b) - M).
$$

It then follows that

$$
\int_ {a} ^ {b} f (x) d \alpha (x) = f (b) (\alpha (b) - k), \quad \text {w h e r e} \quad m \leq k \leq M.
$$

Since $\alpha$ is continuous, there is $c\in [a,b]$ such that $\alpha (c) = k$

(b) The proof runs as in (a).

1.3.18. By the Bonnet form of the second mean value theorem,

$$
\begin{array}{l} \int_ {a} ^ {b} \frac {\sin (n x)}{x} d x = \int_ {a} ^ {b} \frac {- 1}{n x} d \cos (n x) \\ = \frac {- 1}{n a} (\cos (n c) - \cos (n a)). \\ \end{array}
$$

Thus

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} \frac {\sin (n x)}{x} d x = 0.
$$

1.3.19. (a) If we put $t^2 = u$ and use the Bonnet form of the second mean value theorem, we get

$$
\begin{array}{l} \int_ {x} ^ {x + 1} \sin (t ^ {2}) d t = \int_ {x ^ {2}} ^ {(x + 1) ^ {2}} \sin u \frac {1}{2 \sqrt {u}} d u = - \int_ {x ^ {2}} ^ {(x + 1) ^ {2}} \frac {1}{2 \sqrt {u}} d \cos u \\ = - \frac {1}{2 x} (\cos c - \cos (x ^ {2})). \\ \end{array}
$$

This implies the desired inequality.

(b) Likewise,

$$
\begin{array}{l} \int_ {x} ^ {x + 1} \sin (e ^ {t}) d t = \int_ {e ^ {x}} ^ {e ^ {x + 1}} \sin u \frac {1}{u} d u = \frac {1}{e ^ {x}} \int_ {e ^ {x}} ^ {c} \sin u d u \\ = \frac {\cos (e ^ {x}) - \cos c}{e ^ {x}}. \\ \end{array}
$$

1.3.20. By assumption, all three integrals exist and are limits of corresponding intermediate sums (see, e.g., 1.1.11). In particular, given $\varepsilon > 0$ , there is a $\delta > 0$ such that if $P = \{a = x_0, x_1, \ldots, x_n = b\}$ is a partition whose mesh is less than $\delta$ , then

$$
\left| \int_ {a} ^ {b} f (x) d \left(\alpha_ {1} (x) \alpha_ {2} (x)\right) - S \left(P, f, \alpha_ {1} \alpha_ {2}\right) \right| <   \varepsilon , \tag {1}
$$

where

$$
S (P, f, \alpha_ {1} \alpha_ {2}) = \sum_ {k = 1} ^ {n} f (x _ {k}) (\alpha_ {1} (x _ {k}) \alpha_ {2} (x _ {k}) - \alpha_ {1} (x _ {k - 1}) \alpha_ {2} (x _ {k - 1})).
$$

Put $M = \max \{|f(x)| : x \in [a, b]\}$ . The uniform continuity of $\alpha_{2}$ implies that $|\alpha_{2}(x_{k}) - \alpha_{2}(x_{k-1})| < \varepsilon / (MV(\alpha_{1}; a, b))$ for $k = 1, 2, \ldots, n$ ,

if the mesh of $P$ is sufficiently small. Thus

$$
\left| \sum_ {k = 1} ^ {n} f (x _ {k}) \left(\alpha_ {2} \left(x _ {k - 1}\right) - \alpha_ {2} \left(x _ {k}\right)\right) \left(\alpha_ {1} \left(x _ {k}\right) - \alpha_ {1} \left(x _ {k - 1}\right)\right) \right| <   \varepsilon .
$$

Moreover,

$$
\begin{array}{l} S (P, f, \alpha_ {1} \alpha_ {2}) = \sum_ {k = 1} ^ {n} f (x _ {k}) \alpha_ {1} (x _ {k}) (\alpha_ {2} (x _ {k}) - \alpha_ {2} (x _ {k - 1})) \\ + \sum_ {k = 1} ^ {n} f (x _ {k}) \alpha_ {2} (x _ {k}) (\alpha_ {1} (x _ {k}) - \alpha_ {1} (x _ {k - 1})) \\ + \sum_ {k = 1} ^ {n} f (x _ {k}) (\alpha_ {2} (x _ {k - 1}) - \alpha_ {2} (x _ {k})) (\alpha_ {1} (x _ {k}) - \alpha_ {1} (x _ {k - 1})). \\ \end{array}
$$

On the other hand,

$$
\left| \sum_ {k = 1} ^ {n} f (x _ {k}) \alpha_ {1} (x _ {k}) (\alpha_ {2} (x _ {k}) - \alpha_ {2} (x _ {k - 1})) - \int_ {a} ^ {b} f (x) \alpha_ {1} (x) d \alpha_ {2} (x) \right| <   \varepsilon
$$

and

$$
\left| \sum_ {k = 1} ^ {n} f (x _ {k}) \alpha_ {2} (x _ {k}) (\alpha_ {1} (x _ {k}) - \alpha_ {1} (x _ {k - 1})) - \int_ {a} ^ {b} f (x) \alpha_ {2} (x) d \alpha_ {1} (x) \right| <   \varepsilon
$$

if the mesh of $P$ is sufficiently small. Hence

$$
\left| S (P, f, \alpha_ {1} \alpha_ {2}) - \int_ {a} ^ {b} f (x) \alpha_ {1} (x) d \alpha_ {2} (x) - \int_ {a} ^ {b} f (x) \alpha_ {2} (x) d \alpha_ {1} (x) \right| <   3 \varepsilon ,
$$

which together with (1) gives the desired result.

1.3.21. We first show that

$$
\int_ {a} ^ {b} f (x) d \left(\left(f (x)\right) ^ {n}\right) = n \int_ {a} ^ {b} \left(f (x)\right) ^ {n} d f (x).
$$

For $n = 1$ , the equality is obvious. If $n > 1$ , then by the result in the preceding problem, we get

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d \left(\left(f (x)\right) ^ {n}\right) = \int_ {a} ^ {b} \left(f (x)\right) ^ {2} d \left(\left(f (x)\right) ^ {n - 1}\right) + \int_ {a} ^ {b} \left(f (x)\right) ^ {n} d f (x) \\ = \int_ {a} ^ {b} (f (x)) ^ {3} d ((f (x)) ^ {n - 2}) + 2 \int_ {a} ^ {b} (f (x)) ^ {n} d f (x) \\ = \dots = n \int_ {a} ^ {b} (f (x)) ^ {n} d f (x). \\ \end{array}
$$

Now the partial integration formula (Theorem 1) and the proved equality yield

$$
\begin{array}{l} \int_ {a} ^ {b} (f (x)) ^ {n} d f (x) = (f (b)) ^ {n + 1} - (f (a)) ^ {n + 1} - \int_ {a} ^ {b} f (x) d ((f (x)) ^ {n}) \\ = (f (b)) ^ {n + 1} - (f (a)) ^ {n + 1} - n \int_ {a} ^ {b} (f (x)) ^ {n} d f (x), \\ \end{array}
$$

which gives the other equality.

1.3.22. (a) We have

$$
n \int_ {0} ^ {1} x ^ {n} f (x) d x = \frac {n}{n + 1} \int_ {0} ^ {1} f (x) d \left(x ^ {n + 1}\right).
$$

Clearly,

$$
\lim  _ {n \rightarrow \infty} x ^ {n + 1} = \alpha (x) = \left\{\begin{array}{l l}0&\text {i f} \quad x \in [ 0, 1),\\1&\text {i f} \quad x - 1.\end{array}\right.
$$

So, by the results in 1.3.12 and 1.1.13, we get

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} f (x) d \left(x ^ {n + 1}\right) = \int_ {0} ^ {1} f (x) d (\alpha (x)) = f (1).
$$

(b) As in (a), we obtain

$$
\lim  _ {n \rightarrow \infty} \left(n \int_ {0} ^ {1} e ^ {- n x} f (x) d x\right) = - \lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} f (x) d \left(e ^ {- n x}\right) = f (0).
$$

(c) Using (a), we get

$$
\lim  _ {n \rightarrow \infty} \frac {\int_ {0} ^ {1} x ^ {n} f (x) d x}{\int_ {0} ^ {1} x ^ {n} e ^ {x ^ {2}} d x} = \lim  _ {n \rightarrow \infty} \frac {n \int_ {0} ^ {1} x ^ {n} f (x) d x}{n \int_ {0} ^ {1} x ^ {n} e ^ {x ^ {2}} d x} = \frac {f (1)}{e}.
$$

(d) Put

$$
F _ {n} (x) = 2 \pi \int_ {0} ^ {x} \sqrt {n} \sin^ {2 n} (2 \pi t) d t.
$$

Since $\sqrt{n}\sin^{2n}(2\pi t)$ tends to zero uniformly on $[0,x], 0 < x < 1/4,$ we see that $\lim_{n\to \infty}F_n(x) = 0$ for $0 \leq x < 1/4$ . Now note that

$$
F _ {n} \left(\frac {1}{4}\right) = \int_ {0} ^ {\pi / 2} \sqrt {n} \sin^ {2 n} (t) d t = \sqrt {n} \frac {(2 n - 1) ! !}{(2 n) ! !}.
$$

It follows from the Wallis formula (see, e.g., I, 3.8.38) that

$$
\lim  _ {n \rightarrow \infty} F _ {n} (1 / 4) = \frac {1}{\sqrt {\pi}}.
$$

Now if $1/4 < x < 1/2$ , then

$$
\begin{array}{l} F _ {n} (x) = \int_ {0} ^ {2 \pi x} \sqrt {n} \sin^ {2 n} t d t = \int_ {0} ^ {\pi} \sqrt {n} \sin^ {2 n} t d t - \int_ {2 \pi x} ^ {\pi} \sqrt {n} \sin^ {2 n} t d t \\ = 2 F _ {n} \left(\frac {1}{4}\right) - \int_ {2 \pi x.} ^ {\pi} \sqrt {n} \sin^ {2 n} t d t. \\ \end{array}
$$

As above,

$$
\lim  _ {n \rightarrow \infty} \int_ {2 \pi x} ^ {\pi} \sqrt {n} \sin^ {2 n} t d t = 0.
$$

Thus

$$
\lim  _ {n \rightarrow \infty} F _ {n} (x) = \frac {2}{\sqrt {\pi}} \quad \text {i f} \quad x \in (1 / 4, 3 / 4).
$$

Similar analysis yields

$$
\lim  _ {n \rightarrow \infty} F _ {n} (x) = \left\{\begin{array}{l l}0&\text {i f} x \in [ 0, 1 / 4),\\\frac {1}{\sqrt {\pi}}&\text {i f} x = 1 / 4,\\\frac {2}{\sqrt {\pi}}&\text {i f} x \in (1 / 4, 3 / 4),\\\frac {3}{\sqrt {\pi}}&\text {i f} x = 3 / 4,\\\frac {4}{\sqrt {\pi}}&\text {i f} x \in (3 / 4, 1 ].\end{array}\right.
$$

As in (a), we write

$$
2 \pi \sqrt {n} \int_ {0} ^ {1} f (x) \sin^ {2 n} (2 \pi x) d x = \int_ {0} ^ {1} f (x) d \left(F _ {n} (x)\right),
$$

and get

$$
\lim  _ {n \rightarrow \infty} \left(\sqrt {n} \int_ {0} ^ {1} f (x) \sin^ {2 n} (2 \pi x) d x\right) = \frac {1}{\pi \sqrt {\pi}} \left(f \left(\frac {1}{4}\right) + f \left(\frac {3}{4}\right)\right).
$$

(e) Using (d), we obtain

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} \frac {\int_ {0} ^ {1} f (x) \sin^ {2 n} (2 \pi x) d x}{\int_ {0} ^ {1} e ^ {x ^ {2}} \sin^ {2 n} (2 \pi x) d x} = \lim  _ {n \rightarrow \infty} \frac {\sqrt {n} \int_ {0} ^ {1} f (x) \sin^ {2 n} (2 \pi x) d x}{\sqrt {n} \int_ {0} ^ {1} e ^ {x ^ {2}} \sin^ {2 n} (2 \pi x) d x} \\ = \frac {f (1 / 4) + f (3 / 4)}{e ^ {1 / 1 6} + e ^ {9 / 1 6}}. \\ \end{array}
$$

1.3.23. [W. A. J. Luxemburg, Amer. Math. Monthly, 78(1971), 970-979]. Without loss of generality we may assume that $\lim_{n\to \infty}f_n(x) = 0$ for $x\in [a,b]$ . We first show that if $f$ is nonnegative and Riemann integrable on $[a,b]$ , then, given $\varepsilon >0$ , there is a continuous function $g$ such that $0\leq g(x)\leq f(x)$ and

$$
\int_ {a} ^ {b} f (x) d x \leq \int_ {a} ^ {b} g (x) d x + \varepsilon .
$$

There exists a partition $a = x_0 < x_1 < \dots < x_n = b$ such that

$$
\int_ {a} ^ {b} f (x) d x <   \sum_ {i = 1} ^ {n} m _ {i} \left(x _ {i} - x _ {i - 1}\right) + \varepsilon / 2,
$$

where $m_{i} = \inf_{x\in [x_{i - 1},x_{i}]}f(x)$ . This means that there is a step function $s$ such that

$$
\int_ {a} ^ {b} f (x) d x <   \int_ {a} ^ {b} s (x) d x + \varepsilon / 2.
$$

It is easy to see that $s$ can be transformed into a trapezoidal function $g$ such that $0 \leq g \leq s$ and $\int_{a}^{b} s(x) dx \leq \int_{a}^{b} g(x) dx + \varepsilon / 2$ . So, our claim is proved. Now we turn to the proof of the monotone convergence theorem. Let $\varepsilon > 0$ be given. Then for each $n$ there is a continuous function $g_{n}$ such that $0 \leq g_{n} \leq f_{n}$ and

$$
\int_ {a} ^ {b} f _ {n} (x) d x \leq \int_ {a} ^ {b} g _ {n} (x) d x + \frac {\varepsilon}{2 ^ {n}}. \tag {1}
$$

If we set $h_n = \min \{g_1, g_2, \ldots, g_n\}$ , then $0 \leq h_n \leq g_n \leq f_n$ , and the $h_n$ are continuous on $[a, b]$ . Since the sequence $\{f_n\}$ is decreasing,

$$
0 \leq f _ {n} - h _ {n} = \min  \left\{f _ {1}, f _ {2}, \dots , f _ {n} \right\} - \min  \left\{g _ {1}, g _ {2}, \dots , g _ {n} \right\} \leq \sum_ {i = 1} ^ {n} \left(f _ {i} - g _ {i}\right).
$$

Hence

$$
\begin{array}{l} 0 \leq \int_ {a} ^ {b} f _ {n} (x) d x - \int_ {a} ^ {b} h _ {n} (x) d x \leq \sum_ {i = 1} ^ {n} \int_ {a} ^ {b} \left(f _ {i} (x) - g _ {i} (x)\right) d x \\ \leq \sum_ {i = 1} ^ {n} \frac {\varepsilon}{2 ^ {i}} = \varepsilon \left(1 - \frac {1}{2 ^ {n}}\right). \tag {2} \\ \end{array}
$$

Since $\{h_n\}$ is a sequence of continuous functions on $[a, b]$ monotonically decreasing to zero, by Dini's theorem (see, e.g., II,3.1.16), it converges uniformly on $[a, b]$ to zero. Therefore $\lim_{n \to \infty} \int_{a}^{b} h_n(x) dx = 0$ (see, c.g., 1.3.9). Combined with (2), this implies the desired result.

1.3.24. [W. A. J. Luxemburg, Amer. Math. Monthly, 78(1971), 970-979]. The proof runs as in the previous problem where the integrals $\int_{a}^{b} f dx$ and $\int_{a}^{b} f_{n} dx$ should be replaced by $\int_{a}^{b} f dx$ and $\int_{a}^{b} f_{n} dx$ , respectively, except for the fact that the lower Riemann integral is not subadditive (as observed in the cited paper). So, the inequality

$$
0 \leq \int_ {\dot {a}} ^ {b} f _ {n} (x) d x \leq \int_ {a} ^ {b} h _ {n} (x) d x + \varepsilon \left(1 - \frac {1}{2 ^ {n}}\right)
$$

has to be proved in a different way. To this end we note that for each $i = 1,2,\ldots,n$ ,

$$
\begin{array}{l} 0 \leq g _ {n} = g _ {i} + (g _ {n} - g _ {i}) \leq g _ {i} + (\max  \{g _ {i}, \dots , g _ {n} \} - g _ {i}) \\ \leq g _ {i} + \sum_ {i = 1} ^ {n - 1} \left(\max  \left\{g _ {i _ {1}} \dots , g _ {n} \right\} - g _ {i}\right). \\ \end{array}
$$

Hence

$$
0 \leq g _ {n} \leq h _ {n} + \sum_ {i = 1} ^ {n - 1} (\max  \{g _ {i}, \dots , g _ {n} \} - g _ {i}).
$$

Moreover, using

$$
\max  \{g _ {i}, \dots , g _ {n} \} \leq \max  \{f _ {i}, \dots , f _ {n} \} = f _ {i}
$$

we gel

$$
\underline {{\int_ {a} ^ {b}}} f _ {i} (x) d x \geq \int_ {a} ^ {b} (\max  \{g _ {i} (x), \dots , g _ {n} (x) \} - g _ {i} (x)) d x + \int_ {a} ^ {b} g _ {i} (x) d x,
$$

and consequently,

$$
\begin{array}{l} \int_ {a} ^ {b} \left(\max  \left\{g _ {i} (x), \dots , g _ {n} (x) \right\} - g _ {i} (x)\right) d x \leq \int_ {a} ^ {b} f _ {i} (x) d x - \int_ {a} ^ {b} g _ {i} (x) d x \\ \leq \frac {\varepsilon}{2 ^ {i}}, \\ \end{array}
$$

where the last inequality follows from (1) in the solution to the previous problem. It then follows that

$$
\int_ {a} ^ {b} g _ {n} (x) d x \leq \int_ {a} ^ {b} h _ {n} (x) d x + \sum_ {i = 1} ^ {n - 1} \frac {\varepsilon}{2 ^ {i}},
$$

which gives the desired inequality.

1.3.25. [W. A. J. Luxemburg, Amer. Math. Monthly, 78(1971), 970-979]. Without loss of generality we can assume that $0 \leq f_n(x) \leq M$ and that $\lim_{n \to \infty} f_n(x) = 0$ , $x \in [a, b]$ . If we set $p_n(x) = \sup_{k \geq 0} f_{n + k}(x)$ , then we get $0 \leq f_n(x) \leq p_n(x)$ , and therefore,

$$
0 = \lim  _ {n \rightarrow \infty} f _ {n} (x) = \varlimsup_ {n \rightarrow \infty} f _ {n} (x) = \lim  _ {n \rightarrow \infty} p _ {n} (x),
$$

which shows that the sequence $\{p_n\}$ decreases to zero on $[a, b]$ . By the monotone convergence theorem for the lower Riemann integral stated in the last problem,

$$
0 \leq \lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f _ {n} (x) d x \leq \lim  _ {n \rightarrow \infty} \underline {{\int_ {a} ^ {b} p _ {n} (x) d x}} = 0.
$$

1.3.26. [W. A. J. Luxemburg, Amer. Math. Monthly, 78(1971), 970-979]. Since $f_n$ and $f$ are nonnegative, we have $f - f_n \leq f$ , and consequently, $(f - f_n)^+ \leq f$ , where $(f - f_n)^+ = \max \{f - f_n, 0\}$ . This shows that the sequence $\{(f - f_n)^+\}$ is uniformly bounded on $[a, b]$ . By Arzelà's theorem, $\lim_{n \to \infty} \int_a^b (f(x) - f_n(x))^+ dx = 0$ . Observe also that $f = (f - f_n) + f_n \leq (f - f_n)^+ + f_n$ . Hence

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d x \leq \lim  _ {n \rightarrow \infty} \left(\int_ {a} ^ {b} (f (x) - f _ {n} (x)) ^ {+} d x + \int_ {a} ^ {b} f _ {n} (x) d x\right) \\ = \lim  _ {n \rightarrow \infty} \int_ {a} ^ {h} f _ {n} (x) d x, \\ \end{array}
$$

where the last equality follows from I, 2.4.19.

# 1.4. Proper Integrals

1.4.1. (a) We have

$$
\begin{array}{l} \int_ {0} ^ {4} \frac {| x - 1 |}{| x - 2 | + | x - 3 |} d x = \int_ {0} ^ {1} \frac {x - 1}{2 x - 5} d x + \int_ {1} ^ {2} \frac {x - 1}{- 2 x + 5} d x \\ + \int_ {2} ^ {3} (x - 1) d x + \int_ {3} ^ {4} \frac {x - 1}{2 x - 5} d x \\ = 2 + \frac {9}{4} \ln 3 - \frac {3}{4} \ln 5. \\ \end{array}
$$

(b) Using the substitution $t = \pi / 2 - x$ , we see that

$$
\int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} x d x = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {n} x d x.
$$

Now we show by induction that

$$
\int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n} x d x = \frac {1 \cdot 3 \dots (2 n - 1)}{2 \cdot 4 \dots (2 n)} \cdot \frac {\pi}{2} = \frac {(2 n - 1) ! !}{(2 n) ! !} \cdot \frac {\pi}{2} \tag {1}
$$

and

$$
\int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n + 1} x d x = \frac {2 \cdot 4 \dots (2 n)}{1 \cdot 3 \dots (2 n + 1)} = \frac {(2 n) ! !}{(2 n + 1) ! !}. \tag {2}
$$

It is easy to check that both formulas are true for $n = 1$ . For $n > 1$ , integration by parts gives

$$
\begin{array}{l} I _ {n} = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n} x d x = - \int_ {0} ^ {\frac {\pi}{2}} \sin^ {n - 1} x d \cos x \\ = \int_ {0} ^ {\frac {\pi}{2}} \cos x d \sin^ {n - 1} x = (n - 1) \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} x \sin^ {n - 2} d x \\ = (n - 1) I _ {n - 2} - (n - 1) I _ {n}. \\ \end{array}
$$

Hence

$$
I _ {n} = \frac {n - 1}{n} I _ {n - 2}. \tag {3}
$$

So, if

$$
I _ {2 n} = \frac {(2 n - 1) ! !}{(2 n) ! !} \cdot \frac {\pi}{2},
$$

we get from (3) that

$$
I _ {2 n + 2} = \frac {2 n + 1}{2 n + 2} \cdot \frac {(2 n - 1) ! !}{(2 n) ! !} \cdot \frac {\pi}{2} = \frac {(2 n + 1) ! !}{(2 n + 2) ! !} \cdot \frac {\pi}{2}.
$$

This completes the proof of (1). Formula (2) can be proved analogously.

(c) We have

$$
\int_ {\frac {1}{e}} ^ {e} | \ln x | d x = - \int_ {\frac {1}{e}} ^ {1} \ln x d x + \int_ {1} ^ {e} \ln x d x.
$$

Integrating by parts, we get

$$
\int_ {\frac {1}{4}} ^ {e} | \ln x | d x = 2 - \frac {2}{e}.
$$

(d) Substituting $t = \pi - x$ gives

$$
\begin{array}{l} I = \int_ {0} ^ {\pi} \frac {x \sin x}{1 + \cos^ {2} x} d x = \int_ {0} ^ {\pi} \frac {(\pi - x) \sin x}{1 + \cos^ {2} x} d x \\ = \int_ {0} ^ {\pi} \frac {\pi \sin x}{1 + \cos^ {2} x} d x - \int_ {0} ^ {\pi} \frac {x \sin x}{1 + \cos^ {2} x} d x. \\ \end{array}
$$

So,

$$
I = \frac {1}{2} \int_ {0} ^ {\pi} \frac {\pi \sin x}{1 + \cos^ {2} x} d x = \frac {\pi^ {2}}{4}.
$$

(e) We have

$$
\begin{array}{l} I _ {2 n} = \int_ {0} ^ {\frac {\pi}{4}} \tan^ {2 n} x d x = \int_ {0} ^ {\frac {\pi}{4}} \left(\frac {1}{\cos^ {2} x} - 1\right) \tan^ {2 n - 2} x d x \\ = \int_ {0} ^ {\frac {\pi}{4}} \tan^ {2 n - 2} x d (\tan x) - I _ {2 n - 2} = \frac {1}{2 n - 1} - I _ {2 n - 2}. \\ \end{array}
$$

Consequently, one can show by induction that

$$
I _ {2 n} = (- 1) ^ {n} \left(\frac {\pi}{4} - \left(1 - \frac {1}{3} + \frac {1}{5} - \dots + (- 1) ^ {n - 1} \frac {1}{2 n - 1}\right)\right).
$$

(f) We have

$$
\begin{array}{l} \int_ {0} ^ {\frac {\pi}{4}} \frac {\sin x}{\sin x + \cos x} d x = \int_ {0} ^ {\frac {\pi}{4}} \frac {\sin \left(\frac {\pi}{4} - x\right)}{\sin \left(\frac {\pi}{4} - x\right) + \cos \left(\frac {\pi}{4} - x\right)} d x \\ = \int_ {0} ^ {\frac {\pi}{4}} \frac {\cos x - \sin x}{2 \cos x} d x = \frac {\pi}{8} + \frac {1}{2} \ln \frac {\sqrt {2}}{2}. \\ \end{array}
$$

(g) Observe that

$$
I = \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin^ {n} x}{\sin^ {n} x + \cos^ {n} x} d x = \int_ {0} ^ {\frac {\pi}{2}} \frac {\cos^ {n} x}{\sin^ {n} x + \cos^ {n} x} d x.
$$

It then follows that

$$
2 I = \int_ {0} ^ {\frac {\pi}{2}} d x = \frac {\pi}{2}.
$$

1.4.2. Using the substitution $x = \cos t$ and 1.4.1 (b), we get

$$
\int_ {0} ^ {1} (1 - x ^ {2}) ^ {n} d x = \int_ {0} ^ {\pi / 2} \sin^ {2 n + 1} t d t = \frac {(2 n) ! !}{(2 n + 1) ! !}.
$$

On the other hand,

$$
\int_ {0} ^ {1} (1 - x ^ {2}) ^ {n} d x = \sum_ {k = 0} ^ {n} \binom {n} {k} (- 1) ^ {k} \int_ {0} ^ {1} x ^ {2 k} d x = \sum_ {k = 0} ^ {n} \binom {n} {k} (- 1) ^ {k} \frac {1}{2 k + 1}.
$$

1.4.3. Assume, for example, that $f(x_0^+) = a$ . We have

$$
f (x _ {0}) = F ^ {\prime} (x _ {0}) = \lim  _ {x \rightarrow x _ {0}} \frac {F (x) - F (x _ {0})}{x - x _ {0}}.
$$

On the other hand, using l'Hospital's rule, we get

$$
\lim  _ {x \rightarrow x _ {0} ^ {+}} \frac {F (x) - F \left(x _ {0}\right)}{x - x _ {0}} = \lim  _ {x \rightarrow x _ {0} ^ {+}} \frac {F ^ {\prime} (x)}{1} = \lim  _ {x \rightarrow x _ {0} ^ {+}} f (x) = a.
$$

1.4.4. Define $F(x) = x^{2} \cos \frac{1}{x} - 2 \int_{0}^{x} t \cos \frac{1}{t} dt$ for $x \neq 0$ and $F(0) = 0$ . Then $F'(x) = f(x)$ for $x \in \mathbb{R}$ . Thus $F$ is an antiderivative of $f$ in the case when $c = 0$ . If $c \neq 0$ , then an antiderivative $G$ of $f$ would equal $F(x) + c_{1}$ for $x > 0$ and $F(x) + c_{2}$ for $x < 0$ , with some constants $c_{1}$ and $c_{2}$ . Moreover, since $G$ must be continuous at zero, $c_{1} = c_{2}$ . Consequently, $G'(0) = 0$ . This proves that an antiderivative of $f$ exists if and only if $c = 0$ .

1.4.5. We will show that

$$
f (x) = \left\{ \begin{array}{l l} - \frac {\pi}{k x ^ {3}} \sin \frac {\pi}{x ^ {2}} & \text {i f} x \in [ x _ {2 k + 1}, x _ {2 k - 1} ], \\ 0 & \text {i f} x = 0 \end{array} \right.
$$

has the desired properties. Indeed, since $\pmb{f}$ is continuous on $(0,1]$ ,

$$
\begin{array}{l} F \left(x _ {2 k - 1}\right) - F \left(x _ {2 k}\right) = - \frac {\pi}{k} \int_ {x _ {2 k}} ^ {x _ {2 k - 1}} \frac {1}{x ^ {3}} \sin \frac {\pi}{x ^ {2}} d x \\ = \frac {1}{2 k} \int_ {2 k \pi} ^ {(2 k - 1) \pi} \sin t d t = \frac {1}{k}. \\ \end{array}
$$

Similarly,

$$
F (x _ {2 k + 1}) - F (x _ {2 k}) = \frac {1}{k}.
$$

Now we put

$$
F (x) = \left\{ \begin{array}{l l} \int_ {1} ^ {x} f (t) d t & \text {i f} \quad x \in (0, 1 ], \\ 0 & \text {i f} \quad x = 0. \end{array} \right.
$$

Calculation shows that

$$
F (x) = \left\{ \begin{array}{l l} - \frac {1}{2 k} \left(\cos \frac {\pi}{x ^ {2}} + 1\right) & \text {i f} x \in [ x _ {2 k + 1}, x _ {2 k - 1} ], \\ 0 & \text {i f} x = 0. \end{array} \right.
$$

Then $F'(x) = f(x)$ for $x \in (0,1]$ . Moreover, for $x \in [x_{2k+1}, x_{2k-1}]$ ,

$$
- \frac {\sqrt {2 k - 1}}{k} \leq \frac {F (x)}{x} \leq 0,
$$

which implies

$$
F ^ {\prime} (0) - \lim  _ {x \rightarrow 0 ^ {+}} \frac {F (x)}{x} - 0 - f (0).
$$

Having established that $f$ has an antiderivative on $[0,1]$ , we turn to the proof of the other claim. To this end we define

$$
G (x) = \int_ {1} ^ {x} | f (t) | d t, \quad x \in (0, 1 ],
$$

and get

$$
G (x) = - 2 \left(1 + \dots + \frac {1}{k - 1}\right) - \frac {1}{2 k} \left(\cos \frac {\pi}{x ^ {2}} + 1\right)
$$

if $x\in [x_{2k},x_{2k - 1}],k > 1$ , and

$$
G (x) = - 2 \left(1 + \dots + \frac {1}{k - 1}\right) - \frac {1}{k} + \frac {1}{2 k} \left(\cos \frac {\pi}{x ^ {2}} - 1\right)
$$

if $x \in [x_{2k+1}, x_{2k}]$ . Since $\lim_{x \to 0^+} G(x) = -\infty$ , there is no function $G$ such that $G'(x) = |f(x)|$ on the closed interval $[0,1]$ .

1.4.6. The substitution $t - \pi - x$ gives

$$
I = \int_ {0} ^ {\pi} x f (\sin x) d x = \int_ {0} ^ {\pi} (\pi - t) f (\sin t) d t = \pi \int_ {0} ^ {\pi} f (\sin t) d t - I.
$$

So

$$
\begin{array}{l} \int_ {0} ^ {\pi} \frac {x \sin^ {2 n} x}{\sin^ {2 n} x + \cos^ {2 n} x} d x = \frac {\pi}{2} \int_ {0} ^ {\pi} \frac {\sin^ {2 n} x}{\sin^ {2 n} x + \cos^ {2 n} x} d x \\ = \frac {\pi}{2} \int_ {0} ^ {\pi / 2} \frac {\sin^ {2 n} x}{\sin^ {2 n} x + \cos^ {2 n} x} d x \\ + \frac {\pi}{2} \int_ {\pi / 2} ^ {\pi} \frac {\sin^ {2 n} x}{\sin^ {2 n} x + \cos^ {2 n} x} d x \\ = \frac {\pi}{2} \int_ {0} ^ {\pi / 2} \frac {\sin^ {2 n} x + \cos^ {2 n} x}{\sin^ {2 n} x + \cos^ {2 n} x} d x = \frac {\pi^ {2}}{4}. \\ \end{array}
$$

1.4.7. (a) We have

$$
\int_ {- a} ^ {a} f (x) d x = \int_ {- a} ^ {0} f (- x) d x + \int_ {0} ^ {a} f (x) d x = 2 \int_ {0} ^ {a} f (x) d x.
$$

(b) We have

$$
\int_ {- a} ^ {a} f (x) d x = \int_ {- a} ^ {0} - f (- x) d x + \int_ {0} ^ {n} f (x) d x = 0.
$$

1.4.8. Since $f$ is a periodic function, we obtain

$$
\begin{array}{l} \int_ {a} ^ {a + T} f (x) d x = \int_ {a} ^ {0} f (x) d x + \int_ {0} ^ {T} f (x) d x + \int_ {T} ^ {a + T} f (x - T) d x \\ = \int_ {a} ^ {0} f (x) d x + \int_ {0} ^ {T} f (x) d x - \int_ {a} ^ {0} f (x) d x. \\ \end{array}
$$

1.4.9. We have

$$
\begin{array}{l} \int_ {a} ^ {b} f (n x) d x = \frac {1}{n} \int_ {n a} ^ {n b} f (x) d x \\ = \frac {1}{n} \left(\int_ {n a} ^ {n a + T} f (x) d x + \dots + \int_ {n a + k (n) T} ^ {n b} f (x) d x\right), \\ \end{array}
$$

where $k(n) = [n(b - a) / T]$ . By the result in the previous problem,

$$
\int_ {a} ^ {b} f (n x) d x = \frac {1}{n} k (n) \int_ {0} ^ {T} f (x) d x + \frac {1}{n} \int_ {n a + k (n) T} ^ {n b} f (x) d x.
$$

It is clear that $\lim_{n\to \infty}k(n) / n = (b - a) / T$ and

$$
\left| \frac {1}{n} \int_ {n a + k (n) T} ^ {n b} f (x) d x \right| \leq \frac {T}{n} \sup  _ {x \in [ 0, T ]} | f (x) | \xrightarrow [ n \to \infty ]{} 0.
$$

1.4.10. (a) We have

$$
\lim  _ {n \rightarrow \infty} \frac {1}{n} \int_ {0} ^ {n} f (\sin x) d x = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} f (\sin (n x)) d x = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} f (\sin x) d x,
$$

where the last equality follows from 1.4.9.

(b) As in (a), we get

$$
\lim  _ {n \rightarrow \infty} \frac {1}{n} \int_ {0} ^ {n} f (| \sin x |) d x = \frac {1}{\pi} \int_ {0} ^ {\pi} f (\sin x) d x.
$$

(c) Note that

$$
\int_ {0} ^ {1} x f (\sin (2 \pi n x)) d x = \frac {1}{4 \pi^ {2} n ^ {2}} \int_ {0} ^ {2 \pi n} x f (\sin x) d x
$$

and

$$
\int_ {0} ^ {2 n \pi} x f (\sin x) d x = \int_ {0} ^ {2 \pi} x f (\sin x) d x + \dots + \int_ {2 (n - 1) \pi} ^ {2 n \pi} x f (\sin x) d x.
$$

Since

$$
\int_ {k 2 \pi} ^ {(k + 1) 2 \pi} x f (\sin x) d x = 2 k \pi \int_ {0} ^ {2 \pi} f (\sin x) d x + \int_ {0} ^ {2 \pi} x f (\sin x) d x,
$$

we see that

$$
\begin{array}{l} \int_ {0} ^ {2 n \pi} x f (\sin x) d x \\ = (1 + 2 + \dots + (n - 1)) 2 \pi \int_ {0} ^ {2 \pi} f (\sin x) d x + n \int_ {0} ^ {2 \pi} x f (\sin x) d x, \\ \end{array}
$$

and consequently,

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} x f (\sin (2 \pi n x)) d x = \frac {1}{4 \pi} \int_ {0} ^ {2 \pi} f (\sin x) d x.
$$

1.4.11. (a) We will show that

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (x) \cos (n x) d x = \lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (x) \sin (n x) d x = 0.
$$

Since $f$ is uniformly continuous on $[a, b]$ , given $\varepsilon > 0$ , there is $\delta > 0$ such that $|f(t) - f(s)| < \varepsilon$ if $|t - s| < \delta$ . Taking a partition $a = x_0 <$

$x_{1} < \dots < x_{m} = b$ of mesh less than $\delta$ , we get

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) \cos (n x) d x = \sum_ {k = 1} ^ {m} \int_ {x _ {k - 1}} ^ {x _ {k}} f (x) \cos (n x) d x \\ = \sum_ {k = 1} ^ {m} \left(f (x _ {k}) \int_ {x _ {k - 1}} ^ {x _ {k}} \cos (n x) d x + \int_ {x _ {k - 1}} ^ {x _ {k}} (f (x) - f (x _ {k})) \cos (n x) d x\right) \\ \end{array}
$$

and

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f (x) \cos (n x) d x \right| \leq \sum_ {k = 1} ^ {m} | f (x _ {k}) | \left| \int_ {x _ {k - 1}} ^ {x _ {k}} \cos (n x) d x \right| + \varepsilon (b - a) \\ \leq \frac {2}{n} M m + \varepsilon (b - a), \\ \end{array}
$$

where $M = \max \{|f(x)| : x \in [a, b]\}$ . So, $\lim_{n \to \infty} \int_{a}^{b} f(x) \cos(nx) dx = 0$ . The proof of the other equality is analogous.

(b) By (a) we have

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (x) \sin^ {2} (n x) d x = \lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} f (x) \frac {1 - \cos (2 n x)}{2} d x \\ = \frac {1}{2} \int_ {a} ^ {b} f (x) d x. \\ \end{array}
$$

1.4.12. We have

$$
\begin{array}{l} \int_ {0} ^ {1} f (n x) d x = \frac {1}{n} \int_ {0} ^ {n} f (x) d x = \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \int_ {k} ^ {k + 1} f (x) d x \\ = \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {1} f (x + k) d x \\ = \frac {a _ {0} + a _ {1} + \cdots + a _ {n - 1}}{n}. \\ \end{array}
$$

Thus

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} f (n x) d x = a
$$

(see, c.g., I, 2.3.2).

1.4.13. We have

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {f (x)}{f (x) + f (1 - x)} d x = \int_ {0} ^ {1 / 2} \frac {f (x)}{f (x) + f (1 - x)} d x \\ + \int_ {1 / 2} ^ {1} \frac {f (x)}{f (x) + f (1 - x)} d x \\ = \int_ {0} ^ {1 / 2} \frac {f (x)}{f (x) + f (1 - x)} d x \\ + \int_ {0} ^ {1 / 2} \frac {f (1 - x)}{f (x) + f (1 - x)} d x \\ = \frac {1}{2}. \\ \end{array}
$$

1.4.14. We have

$$
\begin{array}{l} \int_ {- a} ^ {a} \frac {f (x)}{1 + e ^ {x}} d x = \int_ {- a} ^ {0} \frac {f (- x)}{1 + e ^ {x}} d x + \int_ {0} ^ {a} \frac {f (x)}{1 + e ^ {x}} d x \\ = \int_ {0} ^ {a} \frac {e ^ {t} f (t)}{1 + e ^ {t}} d t + \int_ {0} ^ {a} \frac {f (x)}{1 + e ^ {x}} d x \\ = \int_ {0} ^ {a} f (x) d x. \\ \end{array}
$$

1.4.15. If there is $x_0 \in [a, b]$ such that $f(x_0) > 0$ , then by the continuity of $f$ , $f(x) > 0$ on some interval $[\alpha, \beta] \subset [a, b]$ . Consequently,

$$
\int_ {a} ^ {b} f (x) d x \geq \int_ {\alpha} ^ {\beta} f (x) d x > 0,
$$

a contradiction.

1.4.16. Let $a \leq x_0 < x_0 + h \leq b$ . By assumption and by the first mean value theorem,

$$
0 = \int_ {x _ {0}} ^ {x _ {0} + h} f (x) d x = f (x _ {0} + \theta h) h,
$$

with some $\theta \in [0,1]$ . Thus $f(x_0 + \theta h) = 0$ . Since $h > 0$ can be arbitrarily chosen, we see that $f(x_0) = 0$ .

1.4.17. Taking $g = f$ , we get $\int_{a}^{b}(f(x))^{2}dx = 0$ , and by the result in 1.4.15, $f(x) \equiv 0$ .

1.4.18. Observe first that if $f$ is Riemann integrable over $[a, b]$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {a + \frac {1}{n}} ^ {b} f (x) d x = \int_ {a} ^ {b} f (x) d x.
$$

Indeed,

$$
\left| \int_ {a} ^ {b} f (x) d x - \int_ {a + \frac {1}{n}} ^ {b} f (x) d x \right| \leq M \frac {1}{n},
$$

where $M = \sup \{|f(x)| : x \in [a, b]\}$ . For a sufficiently large positive integer $n$ , define

$$
g (x) = \left\{ \begin{array}{l l} n f \left(a + \frac {1}{n}\right) (x - a) & \text {i f} x \in [ a, a + 1 / n ], \\ f (x) & \text {i f} x \in [ a + 1 / n, b - 1 / n ], \\ - n f \left(b - \frac {1}{n}\right) (x - b) & \text {i f} x \in [ b - 1 / n, b ]. \end{array} \right.
$$

Then by assumption,

$$
\begin{array}{l} 0 = \int_ {a} ^ {b} f (x) g (x) d x \\ = \int_ {a} ^ {a + \frac {1}{n}} n f \left(a + \frac {1}{n}\right) (x - a) f (x) d x + \int_ {a + \frac {1}{n}} ^ {b - \frac {1}{n}} (f (x)) ^ {2} d x \\ - \int_ {b - \frac {1}{n}} ^ {b} n f \left(b - \frac {1}{n}\right) (x - b) f (x) d x. \\ \end{array}
$$

Now note that

$$
\left| \int_ {a} ^ {a + \frac {1}{n}} n f \left(a + \frac {1}{n}\right) (x - a) f (x) d x \right| \leq M ^ {2} \frac {1}{2 n},
$$

which shows that

$$
\lim  _ {n \rightarrow \infty} \int_ {a} ^ {\alpha + \frac {1}{n}} n f \left(a + \frac {1}{n}\right) (x - a) f (x) d x = 0.
$$

Summing up, we obtain

$$
\lim  _ {n \rightarrow \infty} \int_ {a + \frac {1}{n}} ^ {b - \frac {1}{n}} (f (x)) ^ {2} d x = \int_ {a} ^ {b} (f (x)) ^ {2} d x = 0,
$$

which together with the result in 1.4.15 gives $f(x) \equiv 0$ .

1.4.19. We will use the result in 1.4.16.

(a) Note that for every $x$ ,

$$
\int_ {- x} ^ {x} f (t) d t = \int_ {0} ^ {x} (f (- t) + f (t)) d t = 0.
$$

This clearly implies that

$$
\int_ {x} ^ {y} (f (- t) + f (t)) d t = 0
$$

for every $x$ and $y$ , which combined with the result in 1.4.16 gives $f(-t) + f(t) \equiv 0$ .

(b) The proof is analogous.

(c) We have

$$
\int_ {x} ^ {x + T} f (t) d t = \int_ {x} ^ {0} f (t) d t + \int_ {0} ^ {T} f (t) d t + \int_ {0} ^ {x} f (t + T) d t,
$$

which combined with the assumption shows that

$$
\int_ {0} ^ {x} (f (t + T) - f (t)) = 0 \quad \text {f o r e v e r y} \quad x \in \mathbb {R}.
$$

As in (a) we therefore get $f(t + T) - f(t) \equiv 0$ .

1.4.20. (a) By the first mean value theorem (see, e.g., 1.1.26) there are $x_{n} \in [n, n + 1]$ such that

$$
n ^ {4} \int_ {n} ^ {n + 1} \frac {x d x}{x ^ {5} + 1} = \frac {n ^ {4} x _ {n}}{x _ {n} ^ {5} + 1} \xrightarrow [ n \to \infty ]{} 1,
$$

(b) We have

$$
n ^ {3} \int_ {n} ^ {2 n} \frac {d x}{(x + 1) ^ {4}} <   n ^ {3} \int_ {n} ^ {2 n} \frac {x d x}{x ^ {5} + 1} <   n ^ {3} \int_ {n} ^ {2 n} \frac {d x}{x ^ {4}}.
$$

Thus

$$
\lim  _ {n \rightarrow \infty} n ^ {3} \int_ {n} ^ {2 n} \frac {x d x}{x ^ {5} + 1} = \frac {7}{2 4}.
$$

(c) Since $\ln \left(x + \frac{x^5}{n}\right) \xrightarrow[n\to\infty]{} \ln x$ uniformly on $[1,2]$ , by the result in 1.3.9 we have

$$
\lim  _ {n \rightarrow \infty} \int_ {1} ^ {2} \ln \left(x + \frac {x ^ {5}}{n}\right) d x = \int_ {1} ^ {2} \ln x d x = 2 \ln 2 - 1.
$$

(d) We have

$$
\int_ {\pi} ^ {2 \pi} \frac {x d x}{\arctan (n x)} = \frac {1}{n ^ {2}} \int_ {n \pi} ^ {2 n \pi} \frac {x d x}{\arctan x}.
$$

Since

$$
\lim  _ {x \rightarrow \infty} \left(\frac {x}{\arctan x} - \frac {x}{\pi / 2}\right) = \frac {4}{\pi^ {2}},
$$

given $\varepsilon > 0$ , there is $x_0$ such that

$$
\frac {4}{\pi^ {2}} + \frac {2 x}{\pi} - \varepsilon <   \frac {x}{\arctan x} <   \frac {4}{\pi^ {2}} + \frac {2 x}{\pi} + \varepsilon
$$

if $x > x_0$ . Consequently, for sufficiently large $n$ ,

$$
3 \pi \left(1 + \frac {4 / (\pi) ^ {2} - \varepsilon}{3 n}\right) <   \frac {1}{n ^ {2}} \int_ {n \pi} ^ {2 n \pi} \frac {x d x}{\arctan x} <   3 \pi \left(1 + \frac {4 / (\pi) ^ {2} + \varepsilon}{3 n}\right).
$$

Thus

$$
\begin{array}{l} e ^ {\frac {1}{3} \left(\frac {4}{\pi^ {2}} - \varepsilon\right)} \leq \lim  _ {n \rightarrow \infty} \left(\frac {1}{3 \pi} \int_ {\pi} ^ {2 \pi} \frac {x d x}{\arctan (n x)}\right) ^ {n} \\ \leq \varlimsup_ {n \rightarrow \infty} \left(\frac {1}{3 \pi} \int_ {\pi} ^ {2 \pi} \frac {x d x}{\arctan (n x)}\right) ^ {n} \leq e _ {i} ^ {\frac {1}{3} \left(\frac {4}{\pi^ {2}} + \varepsilon\right)}. \\ \end{array}
$$

Letting $\varepsilon \to 0$ gives

$$
\lim  _ {n \rightarrow \infty} \left(\frac {1}{3 \pi} \int_ {\pi} ^ {2 \pi} \frac {x d x}{\arctan (n x)}\right) ^ {n} = e ^ {\frac {4}{3 \pi^ {2}}}.
$$

1.4.21. (a) We know that $\sin t \geq \frac{2}{\pi} t$ for $t \in [0, \pi/2]$ . Hence

$$
0 \leq \int_ {0} ^ {\pi / 2} e ^ {- R \sin t} d t \leq \int_ {0} ^ {\pi / 2} e ^ {- \frac {2}{\pi} R t} d t = \frac {\pi}{2 R} (1 - e ^ {- R}),
$$

and consequently,

$$
\lim  _ {R \rightarrow \infty} \int_ {0} ^ {\pi / 2} e ^ {- R \sin t} d t = 0.
$$

(b) Fix a sufficiently small $\varepsilon > 0$ . Then $\{\sqrt{x}\}$ is uniformly convergent to 1 on $[\varepsilon, \pi]$ . So, by the result in 1.3.9,

$$
\lim  _ {n \rightarrow \infty} \int_ {\varepsilon} ^ {\pi} \sqrt {x} \sin x d x = \int_ {\varepsilon} ^ {\pi} \sin x d x = 1 + \cos \varepsilon .
$$

Moreover,

$$
\int_ {0} ^ {\varepsilon} \sqrt [ n ]{x} \sin x d x <   \varepsilon \sqrt [ n ]{\varepsilon} <   \varepsilon
$$

for $0 < \varepsilon < 1$ . Letting $\varepsilon \to 0^{+}$ , we see that

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {\pi} \sqrt {x} \sin x d x = 2.
$$

(c) Fix a sufficiently small $\varepsilon > 0$ , and write

$$
\int_ {0} ^ {\pi / 2} \frac {\sin^ {n} x}{\sqrt {1 + x}} d x = \int_ {0} ^ {\pi / 2 - \varepsilon} \frac {\sin^ {n} x}{\sqrt {1 + x}} d x + \int_ {\pi / 2 - \varepsilon} ^ {\pi / 2} \frac {\sin^ {n} x}{\sqrt {1 + x}} d x.
$$

Since $\{\sin^n x\}$ converges to zero uniformly on $[0,\pi /2 - \varepsilon ]$ , we get

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {\pi / 2 - \varepsilon} \frac {\sin^ {n} x}{\sqrt {1 + x}} d x = 0.
$$

Moreover, for $n \in \mathbb{N}$ ,

$$
0 <   \int_ {\pi / 2 - \varepsilon} ^ {\pi / 2} \frac {\sin^ {n} x}{\sqrt {1 + x}} d x <   \frac {\varepsilon}{\sqrt {1 + \pi / 2 - \varepsilon}}.
$$

Passage to the limit as $\varepsilon$ tends to zero yields

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {\pi / 2} \frac {\sin^ {n} x}{\sqrt {1 + x}} d x = 0.
$$

1.4.22. Let $0 < \varepsilon < 1$ . Then

$$
\int_ {0} ^ {1} f (x ^ {n}) d x = \int_ {0} ^ {1 - \varepsilon} f (x ^ {n}) d x + \int_ {1 - \varepsilon} ^ {1} f (x ^ {n}) d x
$$

and, by the first mean value theorem,

$$
\int_ {0} ^ {1 - \varepsilon} f (x ^ {n}) d x = f (\xi^ {n}) (1 - \varepsilon), \quad \text {w h e r e} \quad 0 \leq \xi \leq (1 - \varepsilon).
$$

Thus

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1 - \epsilon} f (x ^ {n}) d x = f (0) (1 - \varepsilon).
$$

Moreover,

$$
\left| \int_ {1 - \varepsilon} ^ {1} f (x ^ {n}) d x \right| \leq M \varepsilon , \quad \text {w h e r e} \quad M = \sup  \{| f (x) |: x \in [ 0, 1 ] \}.
$$

Consequently,

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {1} f (x ^ {n}) d x = f (0).
$$

1.4.23. Problems 1.4.23 - 1.4.30 have been borrowed from [7]. Since

$$
F (x) = \int_ {a} ^ {x} f (t) d t - \int_ {x} ^ {b} f (t) d t
$$

is continuous on $[a, b]$ and $F(a) = -F(b)$ , by the intermediate value property, there is $\theta \in [a, b]$ such that $F(\theta) = 0$ .

1.4.24. Put

$$
F (x) = e ^ {- x} \int_ {a} ^ {x} f (t) d t.
$$

By assumption, $F(a) = F(b) = 0$ . It follows from the mean value theorem that there is $\theta \in (a,b)$ such that

$$
F ^ {\prime} (\theta) = e ^ {- \theta} f (\theta) - e ^ {- \theta} \int_ {a} ^ {\theta} f (t) d t = 0.
$$

1.4.25. Consider

$$
F (x) = \frac {1}{x} \int_ {a} ^ {x} f (t) d t.
$$

By assumption, $F(a) = F(b) = 0$ . It then follows, by the mean value theorem, that there is $\theta \in (a,b)$ such that

$$
F ^ {\prime} (\theta) = - \frac {1}{\theta^ {2}} \int_ {a} ^ {\theta} f (t) d t + \frac {1}{\theta} f (\theta) = 0.
$$

1.4.26. It is enough to apply the generalized mean value theorem to the functions

$$
F (x) = \int_ {a} ^ {x} f (t) d t \quad \text {a n d} \quad G (x) = \int_ {a} ^ {x} g (t) d t.
$$

1.4.27. Define

$$
F (x) - \int_ {a} ^ {x} f (t) d t \int_ {x} ^ {b} g (t) d t.
$$

Since $F(a) = F(b) = 0$ , there is $\theta \in (a, b)$ such that $F'(\theta) = 0$ .

1.4.28: Consider

$$
F (x) = e ^ {- x} \int_ {a} ^ {x} f (t) d t \int_ {x} ^ {b} g (t) d t
$$

and apply the mean value theorem.

1.4.29. Set

$$
F (x) = \int_ {0} ^ {x} f (t) d t + \int_ {1 - x} ^ {1} f (t) d t
$$

and observe that

$$
F (0) = 0 \quad \text {a n d} \quad F (1) = 2 \int_ {0} ^ {1} f (t) d t.
$$

Since $F$ is continuous on $[0,1]$ , there is $\theta(n)$ such that

$$
\frac {1}{n} \int_ {0} ^ {1} f (x) d x = \int_ {0} ^ {\theta (n)} f (x) d x + \int_ {1 - \theta (n)} ^ {1} f (x) d x.
$$

Moreover, by the first mean value theorem,

$$
\frac {1}{n} \int_ {0} ^ {1} f (x) d x = \theta (n) \left(f \left(\xi_ {1} (n)\right) + f \left(\xi_ {2} (n)\right)\right),
$$

where $0 \leq \xi_{1}(n) \leq \theta(n)$ and $1 - \theta(n) \leq \xi_{2}(n)) \leq 1$ . Finally,

$$
n \theta (n) = \frac {\int_ {0} ^ {1} f (x) d x}{f (\xi_ {1} (n)) + f (\xi_ {2} (n))} \xrightarrow [ n \to \infty ]{\int_ {0} ^ {1} f (x) d x} \frac {\int_ {0} ^ {1} f (x) d x}{f (0) + f (1)}.
$$

1.4.30. We have

$$
\int_ {0} ^ {1} f (x) d x = (x - 1) f (x) \big | _ {0} ^ {1} - \int_ {0} ^ {1} (x - 1) f ^ {\prime} (x) d x.
$$

Hence, by the first mean value theorem,

$$
\int_ {0} ^ {1} f (x) d x = f (0) - f ^ {\prime} (\theta) \int_ {0} ^ {1} (x - 1) d x.
$$

1.4.31. As in the proof of the previous problem, we have.

$$
\begin{array}{l} \int_ {0} ^ {1} f (x) d x = f (0) - \int_ {0} ^ {1} (x - 1) f ^ {\prime} (x) d x \\ = f (0) - \frac {(x - 1) ^ {2}}{2} f ^ {\prime} (x) \Big | _ {0} ^ {1} + \int_ {0} ^ {1} \frac {(x - 1) ^ {2}}{2} f ^ {\prime \prime} (x), \\ \end{array}
$$

which combined with the first mean value theorem gives the desired result.

1.4.32. Setting

$$
F (x) = \int_ {0} ^ {x} f (t) d t,
$$

we get $F''(0) = f'(0) \neq 0$ , and by Taylor's formula with the Peano form for the remainder (see, e.g., II, 2.3.1),

$$
F (x) = F (0) + F ^ {\prime} (0) x + \frac {1}{2} F ^ {\prime \prime} (0) x ^ {2} + o \left(x ^ {2}\right).
$$

Likewise,

$$
f (\theta) x = F ^ {\prime} (\theta) x = x \left(F ^ {\prime} (0) + F ^ {\prime \prime} (0) \theta + o (\theta)\right).
$$

By assumption,

$$
F ^ {\prime} (0) x + \frac {1}{2} F ^ {\prime \prime} (0) x ^ {2} + o \left(x ^ {2}\right) = x \left(F ^ {\prime} (0) + F ^ {\prime \prime} (0) \theta + o (\theta)\right),
$$

which yields

$$
\lim  _ {x \rightarrow 0 ^ {+}} \frac {\theta (x)}{x} = \frac {1}{2}.
$$

1.4.33. Let $\varepsilon$ be a given number such that $0 < \varepsilon < (b - a) / 2$ . Since $f$ is strictly increasing, $f(b - \varepsilon) / f(b - 2\varepsilon) > 1$ . Hence there is a positive integer $p_0$ such that for $p > p_0$ ,

$$
\left(\frac {f (b - \varepsilon)}{f (b - 2 \varepsilon)}\right) ^ {p} > \frac {b - a}{\varepsilon},
$$

or, equivalently,

$$
(f (b - \varepsilon)) ^ {p} > \frac {b - a}{\varepsilon} (f (b - 2 \varepsilon)) ^ {p}.
$$

Since

$$
\int_ {a} ^ {b} (f (x)) ^ {p} d x > \int_ {b - \varepsilon} ^ {b} (f (b - \varepsilon)) ^ {p} d x,
$$

we see that

$$
\begin{array}{l} \frac {1}{b - a} \int_ {a} ^ {b} (f (x)) ^ {p} d x > \frac {1}{b - a} \int_ {b - \varepsilon} ^ {b} (f (b - \varepsilon)) ^ {p} d x \\ = \frac {\varepsilon (f (b - \varepsilon)) ^ {p}}{b - a} > (f (b - 2 \varepsilon)) ^ {p}. \\ \end{array}
$$

Hence $\theta(p)$ must satisfy $\theta(p) > b - 2\varepsilon$ , for $p > p_0$ , which means that $\lim_{p \to \infty} \theta(p) = b$ .

1.4.34. Clearly,

$$
\int_ {a} ^ {b} P (x) f (x) d x = 0
$$

for every polynomial $P$ . By the approximation theorem of Weierstrass (see, e.g., II, 3.1.33), there is a sequence of polynomials $\{P_n\}$ uniformly convergent on $[a,b]$ to $f$ . Thus by the result in 1.3.9,

$$
\int_ {a} ^ {b} f ^ {2} (x) d x = \lim  _ {n \rightarrow \infty} \int_ {a} ^ {b} P _ {n} (x) f (x) d x = 0,
$$

which gives $f(x) \equiv 0$ in $[a, b]$ .

1.4.35. By assumption,

$$
\int_ {a} ^ {b} P (x) f (x) d x = 0
$$

for any polynomial $\pmb{F}$ of degree less than or equal to $N$ . Suppose, contrary to our claim, that $a \leq x_1 < x_2 < \dots < x_m \leq b$ , $m \leq N$ , are all zeros of $f$ . Now choose those points $x_{i_1}, \ldots, x_{i_r}$ where $f$ changes its sign. Without loss of generality we can assume that $f(x) \geq 0$ in $[a, x_{i_1}]$ , $f(x) \leq 0$ in $[x_{i_1}, x_{i_2}]$ , and so on. Put

$$
P (x) = \prod_ {k = 1} ^ {r} \left(x _ {i _ {k}} - x\right).
$$

Then $P(x)f(x) \geq 0$ in $[a, b]$ and $P(x)f(x) > 0$ in each of the intervals $(a, x_1), (x_1, x_2), \ldots, (x_m, b)$ . Therefore

$$
\int_ {a} ^ {b} P (x) f (x) d x > 0,
$$

although $P$ is a polynomial of degree less than or equal to $N$ , a contradiction.

1.4.36. Suppose that $f \in C([-a, a])$ .

(a) Note first that, by assumption,

$$
\begin{array}{l} \int_ {- a} ^ {a} (f (x) + f (- x)) x ^ {2 n} d x = \int_ {- a} ^ {a} f (x) x ^ {2 n} d x + \int_ {- a} ^ {a} f (- x) (- x) ^ {2 n} d x \\ = 2 \int_ {- a} ^ {a} f (x) x ^ {2 n} d x = 0. \\ \end{array}
$$

Moreover,

$$
\begin{array}{l} \int_ {- a} ^ {a} (f (x) + f (- x)) x ^ {2 n + 1} d x = \int_ {- a} ^ {a} f (x) x ^ {2 n + 1} d x \\ - \int_ {- a} ^ {a} f (- x) (- x) ^ {2 n + 1} d x = 0. \\ \end{array}
$$

Thus, we see that

$$
\int_ {- a} ^ {a} (f (x) + f (- x)) x ^ {n} d x = 0 \quad \text {f o r} \quad n = 0, 1, 2, \dots ,
$$

and the desired result follows from 1.4.34.

(b) The proof runs as in (a).

1.4.37. By the first mean value theorem we get

$$
\begin{array}{l} \int_ {a} ^ {b} (f (x + h) - f (x)) d x = \int_ {a + h} ^ {b + h} f (x) d x - \int_ {a} ^ {b} f (x) d x \\ - \int_ {a + h} ^ {a} f (x) d x + \int_ {b} ^ {b + h} f (x) d x \\ = - h f (a + \theta h) + h f (b + \theta^ {\prime} h), \\ \end{array}
$$

where $\theta, \theta' \in [0,1]$ . It then follows from the continuity of $f$ that

$$
\lim  _ {h \rightarrow 0} \frac {1}{h} \int_ {a} ^ {b} (f (x + h) - f (x)) d x = f (b) - f (a).
$$

1.4.38. We have

$$
g (x) = \int_ {a + x} ^ {b + x} f (u) d u.
$$

Thus

$$
g ^ {\prime} (x) = f (b + x) - f (a + x).
$$

1.4.39. Using l'Hospital's rule, we obtain

(a)

$$
\lim  _ {x \rightarrow \infty} \frac {\int_ {1} ^ {x} \ln \left(1 + \frac {1}{\sqrt {t}}\right) d t}{\sqrt {x}} = \lim  _ {x \rightarrow \infty} \frac {\ln \left(1 + \frac {1}{\sqrt {x}}\right)}{\frac {1}{2 \sqrt {x}}} = 2.
$$

(b)

$$
\lim  _ {x \rightarrow 0} \frac {\int_ {x} ^ {1} \frac {\cos t}{t ^ {2}} d t}{\frac {1}{x}} = \lim  _ {x \rightarrow 0} \cos x = 1.
$$

(c)

$$
\lim  _ {x \rightarrow 0 ^ {+}} \frac {\int_ {0} ^ {x ^ {2}} \sin \sqrt {t} d t}{x ^ {3}} = \lim  _ {x \rightarrow 0 ^ {+}} \frac {2 x \sin x}{3 x ^ {2}} = \frac {2}{3}.
$$

(d)

$$
\lim  _ {x \rightarrow \infty} \left(\frac {1}{x ^ {a}} \int_ {0} ^ {x} \ln \frac {P (t)}{Q (t)} d t\right) = \lim  _ {x \rightarrow \infty} \frac {\ln P (x) - \ln Q (x)}{a x ^ {a - 1}} = 0.
$$

1.4.40. Using l'Hospital's rule, we get

(a)

$$
\lim  _ {x \rightarrow \infty} \left(\frac {1}{\ln x} \int_ {0} ^ {x} \frac {1}{\sqrt [ 5 ]{1 + t ^ {5}}} d t\right) = \lim  _ {x \rightarrow \infty} \frac {x}{\sqrt [ 6 ]{1 + x ^ {5}}} = 1.
$$

(b)

$$
\lim  _ {x \rightarrow 0} \left(\frac {1}{x} \int_ {0} ^ {x} (1 + \sin t) ^ {\frac {1}{i}} d t\right) = \lim  _ {x \rightarrow 0} (1 + \sin x) ^ {1 / x} = e,
$$

because

$$
\lim  _ {x \rightarrow 0} \frac {\ln (1 + \sin x)}{x} = \lim  _ {x \rightarrow 0} \frac {\cos x}{1 + \sin x} = 1.
$$

(c)

$$
\lim  _ {x \rightarrow 0 ^ {+}} \left(\frac {1}{x ^ {2}} \int_ {0} ^ {x} t ^ {1 + t} d t\right) = \lim  _ {x \rightarrow 0 ^ {+}} \frac {x ^ {x}}{2} = \frac {1}{2}.
$$

(d)

$$
\begin{array}{l} \lim  _ {x \rightarrow \infty} \frac {1}{x ^ {2}} \ln \int_ {0} ^ {x} e ^ {t ^ {2}} d t = \lim  _ {x \rightarrow \infty} \frac {e ^ {x ^ {2}}}{2 x \int_ {0} ^ {x} e ^ {t ^ {2}} d t} \\ = \lim  _ {x \rightarrow \infty} \frac {2 x e ^ {x ^ {2}}}{2 \int_ {0} ^ {x} e ^ {t ^ {2}} d t + 2 x e ^ {x ^ {2}}} \\ = \lim  _ {x \rightarrow \infty} \frac {e ^ {x ^ {2}} + 2 x ^ {2} e ^ {x ^ {2}}}{2 e ^ {x ^ {2}} + 2 x ^ {2} e ^ {x ^ {2}}} = 1. \\ \end{array}
$$

So $\lim_{x\to \infty}\left(\int_0^x e^{t^2}dt\right)^{1 / (x^2)} = e.$

1.4.41. If $A = |f(x_0)| = \max \{|f(x)| : x \in [0, 1]\}$ , then for $p > 0$

$$
\left(\int_ {0} ^ {1} | f (x) | ^ {p}\right) ^ {1 / p} \leq \left(\int_ {0} ^ {1} A ^ {p}\right) ^ {1 / p} = A.
$$

On the other hand, the continuity of $f$ implies that, given $\varepsilon > 0$ , there is an interval $[\alpha, \beta] \subset [0,1]$ such that $|f(x)| \geq A - \varepsilon / 2$ for $x \in [\alpha, \beta]$ . Consequently,

$$
\begin{array}{l} \left(\int_ {0} ^ {1} | f (x) | ^ {p}\right) ^ {1 / p} \geq \left(\int_ {\alpha} ^ {\beta} | f (x) | ^ {p}\right) ^ {1 / p} \geq \left(\int_ {\alpha} ^ {\beta} (A - \varepsilon / 2) ^ {p}\right) ^ {1 / p} \\ = (A - \varepsilon / 2) (\beta - \alpha) ^ {1 / p} \geq A - \varepsilon \\ \end{array}
$$

for sufficiently large $\pmb{p}$ .

1.4.42. Let $y_0 \in [c, d]$ and $\varepsilon > 0$ be chosen arbitrarily. Since $f$ is uniformly continuous on $\mathbb{R}$ , there is $\delta > 0$ such that

$$
\left| f \left(x _ {1}, y _ {1}\right) - f \left(x _ {2}, y _ {2}\right) \right| <   \frac {\varepsilon}{b - a}
$$

if $(x_{1},y_{1}),(x_{2},y_{2})\in \mathbf{R}$ and $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} < \delta$ . So, for $|y - y_0| < \delta$ ,

$$
| I (y) - I (y _ {0}) | \leq \int_ {a} ^ {b} | f (x, y) - f (x, y _ {0}) | d x <   \varepsilon .
$$

1.4.43. By definition,

$$
\frac {d}{d y} \int_ {a} ^ {b} f (x, y) d x = \lim  _ {h \rightarrow 0} \int_ {a} ^ {b} \frac {f (x , y + h) - f (x , y)}{h} d x.
$$

Since the partial derivative $\frac{\partial f}{\partial y}$ is continuous on $\mathbf{R}$ , it is also uniformly continuous on $\mathbf{R}$ . Thus, given $\varepsilon > 0$ , there is $\delta > 0$ such that for $x \in [a, b]$ and $|h| < \delta$ ,

$$
\left| \frac {\partial f}{\partial y} (x, y + h) - \frac {\partial f}{\partial y} (x, y) \right| <   \frac {\varepsilon}{b - a}.
$$

Hence by the mean value theorem we get

$$
\begin{array}{l} \left| \int_ {a} ^ {b} \frac {f (x , y + h) - f (x , y)}{h} d x - \int_ {a} ^ {b} \frac {\partial f}{\partial y} (x, y) d x \right| \\ \leq \int_ {a} ^ {b} \left| \frac {\partial f}{\partial y} (x, y + \theta h) - \frac {\partial f}{\partial y} (x, y) \right| d x <   \varepsilon , \\ \end{array}
$$

which proves that

$$
\frac {d}{d y} \int_ {a} ^ {b} f (x, y) d x = \int_ {a} ^ {b} \frac {\partial f}{\partial y} (x, y) d x.
$$

1.4.44. Applying l'Hospital's rule and the result in the previous problem, we obtain

$$
\begin{array}{l} \lim  _ {p \rightarrow 0} \ln \left(\int_ {0} ^ {1} (f (x)) ^ {p} d x\right) ^ {1 / p} = \lim  _ {p \rightarrow 0} \frac {\ln \int_ {0} ^ {1} (f (x)) ^ {p} d x}{p} \\ = \lim  _ {p \rightarrow 0} \frac {\int_ {0} ^ {1} (f (x)) ^ {p} \ln (f (x)) d x}{\int_ {0} ^ {1} (f (x)) ^ {p} d x} \\ = \int_ {0} ^ {1} \ln f (x) d x, \\ \end{array}
$$

because

$$
(f (x)) ^ {p} \ln f (x) \underset {p \rightarrow 0} {\longrightarrow} \ln f (x) \quad \text {a n d} \quad (f (x)) ^ {p} \underset {p \rightarrow 0} {\longrightarrow} 1
$$

uniformly on [0, 1].

1.4.45. Using the result in 1.4.41, we get

$$
\begin{array}{l} \lim  _ {p \rightarrow - \infty} \left(\int_ {0} ^ {1} (f (x)) ^ {p} d x\right) ^ {1 / p} = \lim  _ {p \rightarrow \infty} \left(\int_ {0} ^ {1} (f (x)) ^ {- p} d x\right) ^ {- 1 / p} \\ = \lim  _ {p \rightarrow \infty} \frac {1}{\left(\int_ {0} ^ {1} \frac {1}{(f (x)) ^ {p}} d x\right) ^ {1 / p}} \\ = \frac {1}{\max  \{1 / (f (x)): x \in [ 0 , 1 ] \}} \\ = \min  \{f (x): x \in [ 0, 1 ] \}. \\ \end{array}
$$

1.4.46. We will use the following inequality (see, e.g., II, 2.5.30):

$$
\sum_ {k = 0} ^ {N} \frac {x ^ {k}}{k !} > e ^ {x} - \frac {x}{N} e ^ {x} + \frac {x}{N} \quad \text {f o r} \quad x > 0.
$$

If we set

$$
F (x) = \int_ {0} ^ {x} e ^ {- t} \left(1 + \frac {t}{1 !} + \frac {t ^ {2}}{2 !} + \dots + \frac {t ^ {2 N}}{(2 N) !}\right) d t,
$$

then, by the above inequality,

$$
\begin{array}{l} F (2 N) = \int_ {0} ^ {2 N} c ^ {- t} \left(1 + \frac {t}{1 !} + \frac {t ^ {2}}{2 !} \mid \dots \mid \frac {t ^ {2 N}}{(2 N) !}\right) d t \\ > \int_ {0} ^ {2 N} \left(1 - \frac {t}{2 N} + e ^ {- t} \frac {t}{2 N}\right) d t > N. \\ \end{array}
$$

On the other hand,

$$
F (N) = \int_ {0} ^ {N} e ^ {- t} \left(1 + \frac {t}{1 !} + \frac {t ^ {2}}{2 !} + \dots + \frac {t ^ {2 N}}{(2 N) !}\right) d t <   \int_ {0} ^ {N} 1 d t = N.
$$

Since $\pmb{F}$ is continuous, the desired result follows from the intermediate value property.

1.4.47. Put

$$
P (x) = a _ {n} x ^ {n} + a _ {n - 1} x ^ {n - 1} + \dots + a _ {0}.
$$

By assumption,

$$
\int_ {0} ^ {1} (P (x)) ^ {2} d x = a _ {0} \int_ {0} ^ {1} P (x) d x.
$$

On the other hand,

$$
\int_ {0} ^ {1} x ^ {k} P (x) d x = \frac {a _ {n}}{n + k + 1} + \frac {a _ {n - 1}}{n + k} + \dots + \frac {a _ {0}}{k + 1}, \quad k = 0, 1, \dots ,
$$

and, by assumption,

$$
\frac {a _ {n}}{n + k + 1} + \frac {a _ {n - 1}}{n + k} + \dots + \frac {a _ {0}}{k + 1} = 0 \quad \text {f o r} \quad k = 1, \dots , n.
$$

Observe now that

$$
\frac {a _ {n}}{n + k + 1} + \frac {a _ {n - 1}}{n + k} + \dots + \frac {a _ {0}}{k + 1} = \frac {Q (k)}{(k + 1) \dots (n + k + 1)}, \tag {1}
$$

where $Q$ is a polynomial of degree at most $n$ . Since $Q(k) = 0$ for $k = 1, 2, \ldots, n$ , there is a constant $C$ such that

$$
Q (k) = C (k - 1) (k - 2) \dots (k - n).
$$

Putting $k = 0$ in (1) we see that

$$
\int_ {0} ^ {1} P (x) d x = \frac {a _ {n}}{n + 1} + \frac {a _ {n - 1}}{n} + \dots + \frac {a _ {0}}{1} = (- 1) ^ {n} \frac {C}{n + 1}.
$$

Now, multiplying (1) by $k + 1$ and next setting $k = -1$ , we obtain $a_0 = (-1)^n (n + 1)C$ . So,

$$
a _ {0} = (n + 1) ^ {2} \int_ {0} ^ {1} P (x) d x,
$$

which implies the desired equality.

1.4.48. If $I(y) = \int_{a}^{b} f(x, y) dx$ , then by 1.4.42, $I(y)$ is continuous on $[c, d]$ . Thus the integral on the left-hand side of the equality to be proved exists. Moreover, if

$$
g (z) = \int_ {c} ^ {z} I (y) d y \quad \text {a n d} \quad h (z) = \int_ {a} ^ {b} \left(\int_ {c} ^ {z} f (x, y) d y\right) d x,
$$

then $g'(z) = I(z)$ for $z \in [c, d]$ , and by 1.4.42, the function

$$
F (x, z) = \int_ {c} ^ {z} f (x, y) d y
$$

is continuous with respect to $x$ . It is clear that $\frac{\partial F}{\partial z}(x, z) = f(x, z)$ is continuous on $\mathbb{R}$ . Hence by 1.4.43, $h'(z) = I(z)$ . So $h'(z) = g'(z) =$

$I(z)$ for $z \in [c, d]$ , and therefore $h(z) = g(z) + C$ . Since $h(c) = g(c) = 0$ , we see that $C = 0$ , which ends the proof.

1.4.49. Since $\lim_{x\to 0^{+}}\frac{x^b - x^a}{\ln x} = 0$ and $\lim_{x\to 1^{-}}\frac{x^b - x^a}{\ln x} = b - a$ , the proper integral exists. By 1.4.48,

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {x ^ {b} - x ^ {a}}{\ln x} d x = \int_ {0} ^ {1} \left(\int_ {a} ^ {b} x ^ {y} d y\right) d x = \int_ {a} ^ {b} \left(\int_ {0} ^ {1} x ^ {y} d x\right) d y \\ = \int_ {a} ^ {b} \frac {x ^ {y + 1}}{y + 1} \Bigg | _ {x = 0} ^ {x = 1} d y = \ln \frac {1 + b}{1 + a}. \\ \end{array}
$$

# 1.5. Improper Integrals

1.5.1. (a) We have

$$
\begin{array}{l} \int_ {0} ^ {2 \pi} \sin^ {4} x + \cos^ {4} x d x = 8 \int_ {0} ^ {\pi / 4} \frac {1}{\sin^ {4} x + \cos^ {4} x} d x \\ = 8 \int_ {0} ^ {\pi / 4} \frac {1}{\cos^ {2} (2 x) + \frac {1}{2} \sin^ {2} (2 x)} d x \\ = 8 \int_ {0} ^ {\pi / 4} \frac {1}{\cos^ {2} (2 x)} \left(\frac {d x}{1 + \frac {1}{2} \tan^ {2} (2 x)}\right). \\ = 4 \int_ {0} ^ {\pi / 4} \frac {1}{1 + \frac {1}{2} \tan^ {2} (2 x)} d (\tan (2 x)) \\ = 4 \int_ {0} ^ {\infty} \frac {d t}{1 + \frac {1}{2} t ^ {2}} \\ = 2 \pi \sqrt {2} \\ \end{array}
$$

(b) Observe first that

$$
\int_ {0} ^ {\pi / 2} \ln (\sin x) d x = \int_ {0} ^ {\pi / 2} \ln (\cos (\pi / 2 - x)) d x = \int_ {0} ^ {\pi / 2} \ln (\cos x) d x.
$$

Thus

$$
\begin{array}{l} \int_ {0} ^ {\pi / 2} \ln (\sin x) d x = \frac {1}{2} \int_ {0} ^ {\pi / 2} \ln \frac {\sin 2 x}{2} d x = \frac {1}{4} \int_ {0} ^ {\pi} \ln \frac {\sin x}{2} d x \\ = \frac {1}{2} \int_ {0} ^ {\pi / 2} (\ln (\sin x) - \ln 2) d x. \\ \end{array}
$$

Consequently,

$$
\int_ {0} ^ {\pi / 2} \ln (\sin x) d x = - \frac {\pi}{2} \ln 2.
$$

(c) We prove by induction that

$$
\int_ {0} ^ {1} x ^ {n} (1 - x) ^ {\alpha} d x = \frac {n !}{(\alpha + 1) (\alpha + 2) \cdots (\alpha + n + 1)}.
$$

For $n = 0$ and $\alpha > -1$ we have

$$
\int_ {0} ^ {1} (1 - x) ^ {\alpha} d x = \frac {1}{\alpha + 1} = \frac {0 !}{\alpha + 1}.
$$

Assuming the equality to hold for $n$ , we integrate by parts and get

$$
\begin{array}{l} \int_ {0} ^ {1} x ^ {n + 1} (1 - x) ^ {\alpha} d x = \int_ {0} ^ {1} x ^ {n + 1} \left(\frac {- (1 - x) ^ {\alpha + 1}}{\alpha + 1}\right) ^ {\prime} d x \\ = \frac {n + 1}{\alpha + 1} \int_ {0} ^ {1} x ^ {n} (1 - x) ^ {\alpha + 1} d x \\ = \frac {(n + 1) !}{(\alpha + 1) (\alpha + 2) \dots (\alpha + n + 1) (\alpha + n + 2)}. \\ \end{array}
$$

(d) Integrating by parts gives

$$
I _ {n} = \int_ {0} ^ {1} (- \ln x) ^ {n} d x = n \int_ {0} ^ {1} (- \ln x) ^ {n - 1} d x = n I _ {n - 1}.
$$

Since $I_{1} = 1$ , we see that $I_{n} = n!$ .

(e) The substitution $t = 1 - \frac{x}{n}$ gives

$$
\begin{array}{l} \int_ {0} ^ {n} \frac {1 - (1 - x / n) ^ {n}}{x} d x = \int_ {0} ^ {1} \frac {1 - t ^ {n}}{1 - t} d t \\ = \int_ {0} ^ {1} (1 + t + t ^ {2} + \dots + t ^ {n - 1}) d t \\ = 1 + \frac {1}{2} + \frac {1}{3} + \dots + \frac {1}{n}. \\ \end{array}
$$

(f) Integrating by parts $n$ times, we get

$$
\begin{array}{l} \int_ {0} ^ {1} x ^ {n} \ln^ {n} x d x = - \frac {n}{n + 1} \int_ {0} ^ {1} x ^ {n} \ln^ {n - 1} x d x \\ = \frac {n (n - 1)}{(n + 1) ^ {2}} \int_ {0} ^ {1} x ^ {n} \ln^ {n - 2} x d x \\ = \dots = (- 1) ^ {n} \frac {n !}{(n + 1) ^ {n + 1}}. \\ \end{array}
$$

(g) If $n = 1$ , then $\int_0^\infty \frac{dx}{(1 + x^2)^n} = \pi / 2$ . If $n > 1$ , then the substitution $x = \tan t$ gives

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {d x}{(1 + x ^ {2}) ^ {n}} = \int_ {0} ^ {\pi / 2} \cos^ {2 n} t \cos^ {- 2} t d t = \int_ {0} ^ {\pi / 2} \cos^ {2 n - 2} t d t \\ = \frac {1 \cdot 3 \dots (2 n - 3)}{2 \cdot 4 \dots (2 n - 2)} \cdot \frac {\pi}{2}, \\ \end{array}
$$

where the last equality follows from 1.4.1(b).

(h) The substitution $t = x - \sqrt{x^2 - 1}$ yields

$$
\int_ {1} ^ {\infty} \frac {d x}{x ^ {2} \sqrt {x ^ {2} - 1}} = \int_ {0} ^ {1} \frac {4 t}{(1 + t ^ {2}) ^ {2}} d t = 1.
$$

(i) Observe first that

$$
\int_ {0} ^ {\infty} \frac {\ln x}{x ^ {2} + a ^ {2}} d x = \int_ {0} ^ {1} \frac {\ln x}{x ^ {2} + a ^ {2}} d x + \int_ {1} ^ {\infty} \frac {\ln x}{x ^ {2} + a ^ {2}} d x
$$

and that both integrals on the right side of the equality converge. Furthermore,

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {\ln x}{x ^ {2} + a ^ {2}} d x = \int_ {0} ^ {a} \frac {\ln x}{x ^ {2} + a ^ {2}} d x + \int_ {0} ^ {\infty} \frac {\ln x}{x ^ {2} + a ^ {2}} d x \\ = \int_ {0} ^ {a} \frac {\ln x}{x ^ {2} + a ^ {2}} d x + \int_ {a} ^ {0} \frac {\ln \left(a ^ {2} / t\right)}{\left(a ^ {2} / t\right) ^ {2} + a ^ {2}} \left(- \frac {a ^ {2}}{t ^ {2}}\right) d t \\ - \int_ {0} ^ {a} \frac {\ln x}{x ^ {2} + a ^ {2}} d x + \int_ {0} ^ {a} \frac {2 \ln a - \ln t}{t ^ {2} + a ^ {2}} d t \\ = \int_ {0} ^ {a} \frac {2 \ln a}{t ^ {2} + a ^ {2}} d t = \frac {\pi \ln a}{2 a}. \\ \end{array}
$$

(j) We have

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {\ln x}{(x ^ {2} + a ^ {2}) ^ {2}} d x = \frac {1}{a ^ {3}} \int_ {0} ^ {\infty} \frac {\ln a + \ln t}{(1 + t ^ {2}) ^ {2}} d t \\ = \frac {1}{a ^ {3}} \int_ {0} ^ {\infty} \frac {\ln a}{(1 + t ^ {2}) ^ {2}} d t + \frac {1}{a ^ {3}} \int_ {0} ^ {\infty} \frac {\ln t}{(1 + t ^ {2}) ^ {2}} d t \\ = \frac {\pi \ln a}{4 a ^ {3}} + \frac {1}{a ^ {3}} \int_ {0} ^ {\infty} \frac {\ln t}{(1 + t ^ {2}) ^ {2}} d t, \\ \end{array}
$$

where the last equality follows from (g). Substituting $t = \tan x$ gives

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {\ln t}{(1 + t ^ {2}) ^ {2}} d t = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} x \ln (\tan x) d x \\ = \int_ {0} ^ {\frac {\pi}{2}} \frac {1 + \cos 2 x}{2} \ln (\tan x) d x \\ = \frac {1}{2} \int_ {0} ^ {\frac {\pi}{2}} \cos 2 x \ln (\tan x) d x, \\ \end{array}
$$

because $\int_0^{\pi /2}\ln (\tan x)dx = 0$ (see the solution to (b)). Finally, integration by parts gives

$$
\int_ {0} ^ {\frac {\pi}{2}} \cos 2 x \ln (\tan x) d x = 0 - \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin 2 x}{2} \cdot \frac {1}{\tan x} \cdot \frac {1}{\cos^ {2} x} d x = - \frac {\pi}{2}.
$$

(k) Using the substitution $t = \pi - x$ , we see that

$$
I = \int_ {0} ^ {\pi} \ln (1 + \cos x) d x = \int_ {0} ^ {\pi} \ln (1 - \cos t) d t.
$$

So, by the symmetry of $\sin x$ and by (b),

$$
\begin{array}{l} 2 I = \int_ {0} ^ {\pi} \ln (1 - \cos^ {2} x) d x = 2 \int_ {0} ^ {\pi} \ln (\sin x) d x \\ = 4 \int_ {0} ^ {\pi / 2} \ln (\sin x) d x = - 2 \pi \ln 2. \\ \end{array}
$$

(1) Substituting $x = \tan t$ and (b) give

$$
\int_ {0} ^ {\infty} \ln \left(x + \frac {1}{x}\right) \frac {d x}{1 + x ^ {2}} = \int_ {0} ^ {\pi / 2} \ln \frac {1}{\sin t \cos t} d t = \pi \ln 2.
$$

1.5.2. Observe that

$$
f _ {\alpha} (x) = - \left(\frac {\alpha}{x} - \left[ \frac {\alpha}{x} \right]\right) + \alpha \left(\frac {1}{x} - \left[ \frac {1}{x} \right]\right).
$$

Since for $j = 1,2,\ldots$

$$
\int_ {\alpha / (j + 1)} ^ {\alpha / j} \left(\frac {\alpha}{x} - \left[ \frac {\alpha}{x} \right]\right) d x = \alpha \int_ {1 / (j + 1)} ^ {1 / j} \left(\frac {1}{x} - \left[ \frac {1}{x} \right]\right) d x,
$$

we have

$$
\begin{array}{l} \int_ {0} ^ {1} f _ {\alpha} (x) d x = - \int_ {0} ^ {\alpha} \left(\frac {\alpha}{x} - \left[ \frac {\alpha}{x} \right]\right) d x - \int_ {\alpha} ^ {1} \left(\frac {\alpha}{x} - \left[ \frac {\alpha}{x} \right]\right) d x \\ + \alpha \int_ {0} ^ {1} \left(\frac {1}{x} - \left[ \frac {1}{x} \right]\right) d x = - \int_ {\alpha} ^ {1} \left(\frac {\alpha}{x} - \left[ \frac {\alpha}{x} \right]\right) d x \\ = \alpha \ln \alpha . \\ \end{array}
$$

1.5.3. Suppose, for example, that $f$ is monotonically increasing on (0,1). Then

$$
\int_ {0} ^ {1 - \frac {1}{n}} f (x) d x \leq \frac {f \left(\frac {1}{n}\right) + f \left(\frac {2}{n}\right) + \cdots + f \left(\frac {n - 1}{n}\right)}{n} \leq \int_ {\frac {1}{n}} ^ {1} f (x) d x,
$$

which implies the desired result.

1.5.4. Without loss of generality we can assume that $f$ is monotonically decreasing and $\lim_{x \to 1^-} f(x)$ is finite. Then

$$
\int_ {\frac {1}{n}} ^ {1} f (x) d x \leq \frac {f \left(\frac {1}{n}\right) + f \left(\frac {2}{n}\right) + \cdots + f \left(\frac {n - 1}{n}\right)}{n}.
$$

Thus $\lim_{\varepsilon \to 0^{+}}\int_{\varepsilon}^{1}f(x)dx$ exists as a finite limit.

1.5.5. Consider

$$
f (x) = \frac {1}{x} - \frac {1}{1 - x}.
$$

Then $f$ is monotonically decreasing on $(0,1)$ , the limit

$$
\lim  _ {n \rightarrow \infty} \frac {f \left(\frac {1}{n}\right) + f \left(\frac {2}{n}\right) + \cdots + f \left(\frac {n - 1}{n}\right)}{n} = 0,
$$

but the improper integral $\int_0^1 f(x)dx$ does not exist.

1.5.6. (a) Taking $f(x) = \ln x$ , we see that

$$
\lim  _ {n \rightarrow \infty} \frac {\ln \frac {1}{n} + \ln \frac {2}{n} + \cdots + \ln \frac {n - 1}{n}}{n} = - 1.
$$

So,

$$
\lim  _ {n \rightarrow \infty} \frac {\sqrt [ n ]{n !}}{n} = \frac {1}{e}.
$$

(b) Taking $f(x) = \ln \sin \left(\frac{\pi x}{2}\right), x \in (0,1]$ , and using 1.5.1 (b), we get

$$
\lim  _ {n \rightarrow \infty} \sqrt [ n ]{\sin \frac {\pi}{2 n} \sin \frac {2 \pi}{2 n} \dots \sin \frac {(n - 1) \pi}{2 n}} = \frac {1}{2}.
$$

(c) Set

$$
a _ {n} - \frac {1}{n} \sum_ {k = 1} ^ {n} (\ln k) ^ {2} - \left(\frac {1}{n} \sum_ {k = 1} ^ {n} \ln k\right) ^ {2}.
$$

Then

$$
\begin{array}{l} a _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} \left(\ln \frac {k}{n} + \ln n\right) ^ {2} - \left(\frac {1}{n} \sum_ {k = 1} ^ {n} \left(\ln \frac {k}{n} + \ln n\right)\right) ^ {2} \\ = \frac {1}{n} \sum_ {k = 1} ^ {n - 1} \left(\ln \frac {k}{n}\right) ^ {2} - \left(\frac {1}{n} \sum_ {k = 1} ^ {n - 1} \ln \frac {k}{n}\right) ^ {2}. \\ \end{array}
$$

Hence by 1.5.3 and 1.5.1(d),

$$
\lim  _ {n \rightarrow \infty} a _ {n} = \int_ {0} ^ {1} (\ln x) ^ {2} d x - \left(\int_ {0} ^ {1} \ln x d x\right) ^ {2} = 2 - 1 = 1.
$$

1.5.7. We first observe that the Cauchy theorem (see, II, 1.1.37) implies the following criterion for convergence of improper integrals: For $g:(a,b]\to \mathbb{R}$ , the improper integral $\int_{a}^{b}g(x)dx$ converges if and only if, given $\varepsilon >0$ , there is $\delta >0$ such that $\left|\int_{a_1}^{a_2}g(x)dx\right| < \varepsilon$ whenever $a < a_1 < a + \delta$ and $a < a_2 < a + \delta$ .

Consequently, by assumption,

$$
\lim  _ {x \rightarrow 0 ^ {+}} \int_ {x} ^ {2 x} t ^ {\alpha} f (t) d t = 0.
$$

Clearly, we can assume that there is a positive $x_0$ such that $f$ is either positive or negative on $(0, x_0)$ . If $f$ is positive on $(0, x_0)$ and decreasing, then

$$
\int_ {x} ^ {2 x} t ^ {\alpha} f (t) d t > \left\{ \begin{array}{l l} f (2 x) x ^ {\alpha} x & \text {i f} \quad \alpha \geq 0, \\ f (2 x) (2 x) ^ {\alpha} x & \text {i f} \quad \alpha <   0. \end{array} \right.
$$

Likewise, if $f$ is positive on $(0, x_0)$ and increasing, then

$$
\int_ {x} ^ {2 x} t ^ {\alpha} f (t) d t > \left\{ \begin{array}{l l} f (x) x ^ {\alpha} x & \text {i f} \quad \alpha \geq 0, \\ f (x) (2 x) ^ {\alpha} x & \text {i f} \quad \alpha <   0. \end{array} \right.
$$

It follows from the above inequalities that $\lim_{x \to 0^{+}} f(x) x^{\alpha + 1} = 0$ . Analogous reasoning can be applied in the case when $f$ is negative on $(0, x_0)$ .

1.5.8. (a) We have

$$
\int_ {2} ^ {\infty} \frac {d x}{x \ln x} = \lim  _ {x \rightarrow \infty} \ln \ln x - \ln \ln 2 = + \infty .
$$

(b) Since

$$
\frac {\sin^ {2} x}{1 + x ^ {2}} \leq \frac {1}{1 + x ^ {2}},
$$

the integral converges.

(c) The substitution $-\ln x = t$ gives

$$
\int_ {0} ^ {1} (- \ln x) ^ {a} d x = \int_ {0} ^ {\infty} t ^ {a} e ^ {- t} d t = \int_ {0} ^ {1} t ^ {a} e ^ {- t} d t + \int_ {1} ^ {\infty} t ^ {a} e ^ {- t} d t.
$$

Since

$$
\lim  _ {t \rightarrow \infty} \frac {t ^ {a} e ^ {- t}}{t ^ {- 2}} = 0,
$$

the last integral converges for all real $a$ . Moreover, since

$$
\lim  _ {t \rightarrow 0 ^ {+}} \frac {t ^ {a} e ^ {- t}}{t ^ {a}} = 1,
$$

the integral $\int_0^1 t^a e^{-t}dt$ converges if and only if the integral $\int_0^1 t^a dt$ converges, that is, if and only if $a > -1$ .

(d) As in (c),

$$
\int_ {0} ^ {1} \frac {d x}{x ^ {a} (- \ln x) ^ {b}} = \int_ {0} ^ {\infty} t ^ {- b} e ^ {- (1 - a) t} d t.
$$

It is easy to check that if $a \geq 1$ , then the last integral diverges to infinity for any $b$ . Since for $a < 1$

$$
\int_ {0} ^ {\infty} t ^ {- b} e ^ {- (1 - a) t} d t = (1 - a) ^ {b - 1} \int_ {0} ^ {\infty} t ^ {- b} e ^ {- t} d t,
$$

it follows from the solution to (c) that our integral converges if and only if $a < 1$ and $b < 1$ .

(c) The divergence of the integral follows from the inequality

$$
\int_ {0} ^ {\infty} \frac {x}{1 + x ^ {2} \sin^ {2} x} d x \geq \int_ {0} ^ {\infty} \frac {x}{1 + x ^ {2}} d x.
$$

1.5.9. Since $f(t) + 1 / (f(t)) \geq 2$ , we see that

$$
\int_ {a} ^ {\infty} f (t) g (t) d t + \int_ {a} ^ {\infty} \frac {g (t)}{f (t)} d t \geq 2 \int_ {a} ^ {\infty} g (t) d t.
$$

Letting $x \to \infty$ , we get the desired result.

1.5.10. The assertion follows immediately from the definition of an improper integral and the Cauchy theorem given in II, 1.1.37.

1.5.11. Suppose that the integral $\int_{a}^{\infty} f(x) dx$ converges and $\{a_n\}$ , $a_n > a$ , is an increasing sequence diverging to infinity. Then

$$
\begin{array}{l} \int_ {a} ^ {\infty} f (x) d x = \lim  _ {n \rightarrow \infty} \int_ {a} ^ {a _ {n}} f (x) d x = \lim  _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} \int_ {a _ {k - 1}} ^ {a _ {k}} f (x) d x \\ = \sum_ {n = 1} ^ {\infty} \int_ {a _ {n - 1}} ^ {a _ {n}} f (x) d x. \\ \end{array}
$$

On the other hand, if the last series converges for every increasing sequence $\{a_n\}$ diverging to infinity, then the limit $\lim_{x \to \infty} \int_{a}^{x} f(t) dt$ exists and is equal to the sum of this series.

If $f$ is nonnegative, then the function $F(x) = \int_{a}^{x} f(t) dt$ is monotonically increasing. Moreover, if there is an increasing sequence $\{a_n\}$ , $a_n > a$ , diverging to infinity for which the series (1) converges, then $F$ is bounded above by the sum of this series. So, the limit $\lim_{x \to \infty} F(x)$ exists.

1.5.12. By the result in the previous problem, the integral converges if and only if

$$
\sum_ {n = 0} ^ {\infty} \int_ {n \pi} ^ {(n + 1) \pi} \frac {d x}{1 + x ^ {a} \sin^ {2} x} = \sum_ {n = 0} ^ {\infty} \int_ {0} ^ {\pi} \frac {d x}{1 + (x + n \pi) ^ {a} \sin^ {2} x} <   + \infty .
$$

Now observe that

$$
\begin{array}{l} \int_ {0} ^ {\pi} \frac {d x}{1 + ((n + 1) \pi) ^ {a} \sin^ {2} x} \leq \int_ {0} ^ {\pi} \frac {d x}{1 + (x + n \pi) ^ {a} \sin^ {2} x} \\ \leq \int_ {0} ^ {\pi} \frac {d x}{1 + (n \pi) ^ {a} \sin^ {2} x}. \\ \end{array}
$$

Moreover, we have

$$
\int_ {0} ^ {\pi} \frac {d x}{1 + b ^ {2} \sin^ {2} x} = 2 \int_ {0} ^ {\pi / 2} \frac {d x}{1 + b ^ {2} \sin^ {2} x}.
$$

Substituting $y = \tan x$ , we see that

$$
\int_ {0} ^ {\pi / 2} \frac {d x}{1 + b ^ {2} \sin^ {2} x} = \int_ {0} ^ {\infty} \frac {d y}{1 + (b ^ {2} + 1) y ^ {2}} = \frac {\pi}{2 \sqrt {b ^ {2} + 1}}.
$$

It then follows that the integral converges for $a > 2$ and diverges for $0 < a \leq 2$ .

1.5.13. No. Take $f(x) = e^{-x} + g(x), x \in [0, \infty)$ , where

$$
g (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \in [ 0, 7 / 4 ], \\ 1 & \text {i f} x = 2, 3, \dots , \\ n ^ {2} (x - n) + 1 & \text {i f} x \in [ n - n ^ {- 2}, n ], \quad n = 2, 3, \dots , \\ - n ^ {2} (x - n) + 1 & \text {i f} x \in [ n, n + n ^ {- 2} ], \quad n = 2, 3, \dots , \\ 0 & \text {o t h e r w i s e .} \end{array} \right.
$$

1.5.14. Yes, it does. Indeed, if it is not true that $\lim_{x\to \infty}f(x) - 0$ then there exist $\varepsilon >0$ and a sequence $\{x_{n}\}$ diverging to infinity, $x_{n + 1} - x_n > 2\varepsilon$ , and such that $f(x_{n})\geq \varepsilon$ . By the mean value theorem,

$$
f (x) = f \left(x _ {n}\right) + f ^ {\prime} \left(\xi_ {n}\right) \left(x - x _ {n}\right), \quad x _ {n} <   \xi_ {n} <   x <   x _ {n} + \varepsilon / 4.
$$

Consequently,

$$
f (x) > \varepsilon - 2 \frac {\varepsilon}{4} = \frac {\varepsilon}{2}, \quad x \in [ x _ {n}, x _ {n} + \varepsilon / 4 ],
$$

and

$$
\begin{array}{l} \int_ {a} ^ {\infty} f (x) d x \geq \sum_ {n = 1} ^ {\infty} \int_ {x _ {n}} ^ {x _ {n + 1}} f (x) d x > \sum_ {n = 1} ^ {\infty} \int_ {x _ {n}} ^ {x _ {n} + \varepsilon / 4} f (x) d x \\ \geq \sum_ {n = 1} ^ {\infty} \frac {\varepsilon^ {2}}{8} = + \infty , \\ \end{array}
$$

a contradiction.

1.5.15. Assume, contrary to our claim, that $\lim_{x\to \infty}f(x) = 0$ does not hold. Then there exist a positive number $\varepsilon$ and an increasing sequence $\{x_n\}$ diverging to infinity such that either $f(x_{n})\geq \varepsilon$ for all $n$ or $f(x_{n})\leq -\varepsilon$ for all $n$ . Suppose, for example, that $f(x_{n})\geq \varepsilon$ for all $n$ . By the uniform continuity of $f$ , there is $\delta >0$ such that if $|t - s| < \delta$ ,

then $|f(t) - f(s)| < \varepsilon / 2$ . Consequently, for $t \in [x_n - \delta, x_n + \delta]$ , we get $f(t) > \varepsilon / 2$ , and therefore

$$
\int_ {x _ {n} - \delta} ^ {x _ {n} + \delta} f (x) d x > \varepsilon \delta . \tag {1}
$$

On the other hand, since the improper integral $\int_{a}^{\infty} f(x) dx$ converges, by the Cauchy theorem (see 1.5.10), there is $a_0 > a$ such that for $a_2 > a_1 > a_0$ ,

$$
\left| \int_ {a _ {1}} ^ {a _ {2}} f (x) d x \right| <   \varepsilon \delta ,
$$

which contradicts (1).

Additionally, we observe that if $f$ is continuous on $[a, \infty)$ and $\lim_{x \to \infty} f(x) = 0$ , then $f$ is uniformly continuous on $[a, \infty)$ (see, e.g., II, 1.5.7(b)).

It is also worth noting here that the result in 1.5.14 is contained as a special case in this problem.

1.5.16. Let $\{x_{n}\}$ be an increasing sequence diverging to infinity. Then, given $\varepsilon > 0$ , there is $n_{0}$ such that

$$
\int_ {x _ {n _ {0}}} ^ {\infty} f (x) d x <   \varepsilon .
$$

So, by the monotonicity of $f$ , for $n > n_0$

$$
(x _ {n} - x _ {n _ {0}}) f (x _ {n}) \leq \int_ {x _ {n _ {0}}} ^ {x _ {n}} f (x) d x \leq \int_ {x _ {n _ {0}}} ^ {\infty} f (x) d x <   \varepsilon .
$$

Consequently,

$$
0 \leq x _ {n} f (x _ {n}) \leq \frac {x _ {n}}{x _ {n} - x _ {n _ {0}}} \varepsilon .
$$

Letting $n \to \infty$ gives $0 \leq \varlimsup_{n \to \infty} x_n f(x_n) \leq \varepsilon$ . Since $\varepsilon$ can be arbitrarily chosen, we see that $\lim_{n \to \infty} x_n f(x_n) = 0$ .

To see that the converse does not hold, consider, for example, $f(x) = \frac{1}{x \ln x}, x \geq 2$ .

1.5.17. (a) Suppose, contrary to our claim, that $\int_{1}^{\infty}\frac{dx}{x\ln f(x)} < \infty$ . Then, using the substitution $x = e^{t}$ , we see that $\int_{0}^{\infty}\frac{dt}{\ln f(e^{t})} < \infty$ . It

follows from the previous result that $\lim_{x\to \infty}\frac{x}{\ln f(e^x)} = 0$ . Thus, for sufficiently large $x$ , $\frac{x}{\ln f(e^x)} < \frac{1}{2}$ , which implies $\frac{e^x}{f(e^x)} < e^{-x}$ . Consequently, $\int_1^\infty \frac{dx}{f(x)}$ converges, a contradiction.

(b) Let

$$
a _ {n} = e ^ {e ^ {e ^ {n}}}, \quad n = 0, 1, 2, \dots .
$$

We define $f$ by setting $f(x) = a_{n}$ for $a_{n-1} \leq x < a_{n}, n = 1, 2, \ldots$ . Then, by 1.5.11,

$$
\int_ {e ^ {\circ}} ^ {\infty} \frac {d x}{f (x)} = \sum_ {n - 1} ^ {\infty} \frac {a _ {n} - a _ {n - 1}}{a _ {n}} = \infty ,
$$

because $\lim_{n\to \infty}\frac{a_{n - 1}}{a_n} = 0$ .On the other hand,

$$
\begin{array}{l} \int_ {e ^ {n}} ^ {\infty} \frac {d x}{x \ln f (x) \ln (\ln f (x))} = \sum_ {n = 1} ^ {\infty} \int_ {a _ {n - 1}} ^ {a _ {n}} \frac {d x}{x e ^ {e ^ {n}} e ^ {n}} \\ = \sum_ {n = 1} ^ {\infty} \frac {e ^ {e ^ {n}} - e ^ {e ^ {n - 1}}}{e ^ {e ^ {n}} e ^ {n}} <   \sum_ {n = 1} ^ {\infty} \frac {1}{e ^ {n}}. \\ \end{array}
$$

1.5.18. Set $F(x) = \int_0^x f(t)dt$ . Then $F'(x) = f(x)$ , and by assumption,

$$
\lim  _ {x \rightarrow \infty} \left(F ^ {\prime} (x) + F (x)\right) = l, \quad l \in \mathbb {R}.
$$

It follows from II, 2.2.32 that $\lim_{x\to \infty}F(x) = l,$ and therefore,

$$
\lim  _ {x \rightarrow \infty} f (x) = \lim  _ {x \rightarrow \infty} F ^ {\prime} (x) = 0.
$$

1.5.19. Put $F(x) = \int_{0}^{x} f(t) dt$ . Then, by assumption, $F$ is increasing, and integration by parts gives

$$
\frac {1}{n} \int_ {0} ^ {n} x f (x) d x = \frac {1}{n} \int_ {0} ^ {n} x d F (x) = F (n) - \frac {1}{n} \int_ {0} ^ {n} F (x) d x.
$$

We know that $\lim_{n\to \infty}F(n) = \int_0^\infty f(x)dx < \infty$ . Now we show that $\lim_{n\to \infty}\frac{1}{n}\int_0^n F(x)dx = \lim_{n\to \infty}F(n)$ . By the monotonicity of $F$ ,

$$
\frac {F (0) + \cdots + F (n - 1)}{n} \leq \frac {1}{n} \int_ {0} ^ {n} F (x) d x \leq \frac {F (1) + \cdots + F (n)}{n},
$$

and our claim follows from I, 2.3.2.

1.5.20. Since $f$ is uniformly continuous on $[a, \infty)$ , there is $\delta > 0$ such that $|f(s) - f(t)| < 1$ if $|t - s| < \delta$ . Now suppose, contrary to our claim, that $f$ is not bounded. Then there is a sequence $\{a_n\}$ such that $a_{n+1} > a_n + \delta$ and $|f(a_n)| \geq n$ . By assumption,

$$
\begin{array}{l} \left| \int_ {a} ^ {a _ {n}} f (t) d t \right| \geq \left| \int_ {a _ {n} - \frac {\varepsilon}{2}} ^ {a _ {n}} f (t) d t \right| - \left| \int_ {a} ^ {a _ {n} - \frac {\varepsilon}{2}} f (t) d t \right| \\ \geq \left| \int_ {a _ {n} - \frac {6}{2}} ^ {a _ {n}} f (t) d t \right| - M. \\ \end{array}
$$

Moreover, we have $|f(t) - f(a_n)| < 1$ for $t \in [a_n - \delta / 2, a_n]$ . Consequently,

$$
\left| \int_ {a _ {n} - \frac {\delta}{2}} ^ {a _ {n}} f (t) d t \right| \geq \left(| f (a _ {n}) | - 1\right) \frac {\delta}{2} \geq (n - 1) \frac {\delta}{2}
$$

and

$$
\left| \int_ {a} ^ {a _ {n}} f (t) d t \right| \geq (n - 1) \frac {\delta}{2} - M,
$$

a contradiction.

1.5.21. Integration by parts gives

$$
\int_ {a} ^ {x} f (t) f ^ {\prime \prime} (t) d t = f (x) f ^ {\prime} (x) - f (a) f ^ {\prime} (a) - \int_ {a} ^ {x} \left(f ^ {\prime} (t)\right) ^ {2} d t. \tag {1}
$$

By the inequality $(f(x))^2 + (f''(x))^2 \geq 2|f(x)f''(x)|$ and by assumption, the integral $\int_{a}^{\infty} f(t) f''(t) dt$ converges. Clearly, $\int_{a}^{x} (f'(t))^2 dt$ either converges or diverges to infinity as $x \to \infty$ . In the latter case, by (1), $\lim_{x \to \infty} f(x) f'(x) = +\infty$ , and since

$$
f ^ {2} (x) - f ^ {2} (a) = \frac {1}{2} \int_ {a} ^ {x} f (t) f ^ {\prime} (t) d t,
$$

we see that $\lim_{x\to \infty}f^2 (x) = +\infty$ , which contradicts the convergence of $\int_{a}^{\infty}(f(x))^{2}dx$ . So the convergence of $\int_{a}^{\infty}(f'(t))^{2}dt$ is proved.

1.5.22. It follows from the Cauchy theorem (see 1.5.10) that the improper integral $\int_{a}^{\infty} f(x) g(x) dx$ converges if and only if, given $\varepsilon > 0$ , there is $a_0 > a$ such that for $a_2 > a_1 > a_0$ ,

$$
\left| \int_ {a _ {1}} ^ {a _ {2}} f (x) g (x) d x \right| <   \varepsilon .
$$

By the second mean value theorem (see 1.3.16),

$$
\int_ {a _ {1}} ^ {a _ {2}} f (x) g (x) d x = g \left(a _ {1}\right) \int_ {a _ {1}} ^ {c} f (x) d x + g \left(a _ {2}\right) \int_ {c} ^ {u _ {2}} f (x) d x
$$

with some $c$ in $[a_1, a_2]$ . Since $g$ is bounded, there is $C > 0$ such that $|g(x)| \leq C$ for all $x \in [a, \infty)$ . By (1), the improper integral $\int_{a}^{\infty} f(x) dx$ exists, so the Cauchy theorem implies that there is $u_0 > u$ such that

$$
\left| \int_ {a _ {1}} ^ {c} f (x) d x \right| <   \frac {\varepsilon}{2 C} \quad \text {a n d} \quad \left| \int_ {c} ^ {a _ {2}} f (x) d x \right| <   \frac {\varepsilon}{2 C}
$$

for $a_1 > a_0$ . Thus

$$
\begin{array}{l} \left| \int_ {a _ {1}} ^ {a _ {2}} f (x) g (x) d x \right| \leq | g (a _ {1}) | \left| \int_ {a _ {1}} ^ {c} f (x) d x \right| + | g (a _ {2}) | \left| \int_ {c} ^ {a _ {2}} f (x) d x \right| \\ <   C \frac {\varepsilon}{2 C} + C \frac {\varepsilon}{2 C} = \varepsilon . \\ \end{array}
$$

1.5.23. As in the proof of Abel's test, we show that, given $\varepsilon > 0$ , there is $a_0 > a$ such that for $a_2 > a_1 > a_0$ ,

$$
\left| \int_ {a _ {1}} ^ {a _ {2}} f (x) g (x) d x \right| <   \varepsilon .
$$

Since $\lim_{x\to \infty}g(x) = 0$ , there is $a_0 > a$ such that $|g(x)| < \varepsilon / (4C)$ whenever $x > a_0$ . By the second mean value theorem and by (1),

$$
\begin{array}{l} \left| \int_ {a _ {1}} ^ {a _ {2}} f (x) g (x) d x \right| \leq | g (a _ {1}) | \left| \int_ {a _ {1}} ^ {c} f (x) d x \right| + | g (a _ {2}) | \left| \int_ {c} ^ {a _ {2}} f (x) d x \right| \\ <   \frac {\varepsilon}{4 C} 2 C + \frac {\varepsilon}{4 C} 2 C = t. \\ \end{array}
$$

1.5.24. (a) Since

$$
\left| \int_ {1} ^ {b} \sin x d x \right| \leq 2 \quad \text {f o r a l l} \quad b > 1,
$$

and the function $x \mapsto 1 / (x^{\alpha})$ monotonically tends to zero as $x \to \infty$ , the convergence of $\int_{1}^{\infty} \frac{\sin x}{x^{\alpha}} dx$ follows from the Dirichlet test.

(b) If the improper integral $\int_{1}^{\infty}\frac{|\sin x|}{x} dx$ converged, then $\int_{1}^{\infty}\frac{\sin^2x}{x} dx$ would also converge (because $\sin^2 x\leq |\sin x|$ ). This would give

$$
\frac {1}{2} \int_ {1} ^ {\infty} \frac {1 - \cos 2 x}{x} d x <   \infty . \tag {1}
$$

As in (a), one can show that $\int_{1}^{\infty}\frac{\cos 2x}{x} dx$ converges. This combined with (1) would imply the convergence of $\int_{1}^{\infty}\frac{dx}{x}$ , a contradiction.

(c) The substitution $x = \sqrt{t}$ gives

$$
\int_ {1} ^ {\infty} \sin (x ^ {2}) d x = \int_ {1} ^ {\infty} \frac {\sin t}{2 \sqrt {t}} d t.
$$

Thus, by (a), the integral converges.

(d) One can apply the Dirichlet test with $g(x) = 1 / (x^{\alpha})$ and $f(x) = e^{\sin x} \sin 2x$ , because

$$
\left| \int_ {1} ^ {b} e ^ {\sin x} \sin (2 x) d x \right| = \left| 2 e ^ {\sin x} (\sin x - 1) \right| _ {1} ^ {b} \mid \leq 8 e
$$

for all $b > 1$ .

(e) Put

$$
g (x) = \frac {\ln^ {\alpha} x}{x} \quad \text {a n d} \quad f (x) = \sin x.
$$

Then

$$
g ^ {\prime} (x) = \frac {\ln^ {\alpha - 1} x}{x ^ {2}} (\alpha - \ln x) <   0
$$

for sufficiently large $\pmb{x}$ . Thus $g$ is monotonically decreasing to zero, and the Dirichlet test for convergence can be applied.

1.5.25. If $\int_{a}^{a + T} f(x) dx = 0$ , then also $\int_{a}^{a + kT} f(x) dx = 0$ for $k \in \mathbb{N}$ . For $b > a$ put $k = \left[\frac{b - a}{T}\right]$ . Then, by the result in 1.4.8,

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f (x) d x \right| = \left| \int_ {a + k T} ^ {b} f (x) d x \right| = \left| \int_ {a} ^ {b - k T} f (x) d x \right| \\ \leq \int_ {a} ^ {b - k T} | f (x) | d x \leq \int_ {a} ^ {a + T} | f (x) | d x = C. \\ \end{array}
$$

Now the first statement is an immediate consequence of the Dirichlet test.

To prove the second statement, set $\int_{a}^{a + T}f(x)dx = I\neq 0$ and consider the integral

$$
\int_ {a} ^ {\infty} \left(f (x) - \frac {I}{T}\right) g (x) d x.
$$

It follows from what we have already proved that this integral converges. Consequently, $\int_{a}^{\infty} f(x) g(x) dx$ converges if and only if the integral $\int_{a}^{\infty} g(x) dx$ converges.

1.5.26. (a) Since

$$
\begin{array}{l} \int_ {0} ^ {2 \pi} \sin (\sin x) e ^ {\cos x} d x \\ = \int_ {0} ^ {\pi} \sin (\sin x) e ^ {\cos x} d x + \int_ {\pi} ^ {2 \pi} \sin (\sin x) e ^ {\cos x} d x = 0, \\ \end{array}
$$

the given integral converges.

(b) We have

$$
\begin{array}{l} \int_ {0} ^ {2 \pi} \sin (\sin x) e ^ {\sin x} d x = \int_ {0} ^ {\pi} \sin (\sin x) e ^ {\sin x} d x + \int_ {\pi} ^ {2 \pi} \sin (\sin x) e ^ {\sin x} d x \\ = \int_ {0} ^ {\pi} \left(e ^ {\sin x} - e ^ {- \sin x}\right) \sin (\sin x) d x > 0. \\ \end{array}
$$

Thus the integral diverges.

1.5.27. Observe first that $\lim_{x\to 0^{+}}\frac{\sin x}{x^{\alpha} + \sin x}$ exists as a finite limit for all positive $\alpha$ . So we can confine ourselves to studying the convergence of

$$
\int_ {2} ^ {\infty} \frac {\sin x}{x ^ {a} + \sin x} d x.
$$

We have

$$
\frac {\sin x}{x ^ {\alpha} + \sin x} = \frac {\sin x}{x ^ {\alpha}} - \frac {\sin^ {2} x}{x ^ {\alpha} (x ^ {\alpha} + \sin x)}.
$$

We know (see 1.5.24(a)) that for $\alpha > 0$ the integral $\int_{2}^{\infty} \frac{\sin x}{x^{\alpha}} dx$ converges. So, it is enough to study the integral

$$
\int_ {2} ^ {\infty} \frac {\sin^ {2} x}{x ^ {\alpha} \left(x ^ {\alpha} + \sin x\right)} d x. \tag {1}
$$

Since

$$
\frac {\sin^ {2} x}{x ^ {\alpha} \left(x ^ {\alpha} + 1\right)} \leq \frac {\sin^ {2} x}{x ^ {\alpha} \left(x ^ {\alpha} + \sin x\right)} \leq \frac {1}{x ^ {\alpha} \left(x ^ {\alpha} - 1\right)}, \tag {2}
$$

we see that integral (1) converges for $\alpha > 1/2$ . Applying the result in 1.5.25, we find that the integral $\int_{2}^{\infty} \frac{\sin^{2} x}{x^{\alpha}(x^{\alpha} + 1)} dx$ diverges for $\alpha \leq 1/2$ . So, it follows from (2) that the integral (1) also diverges if $\alpha \leq 1/2$ . For $\alpha > 1/2$ the integral converges.

# 1.5.28. Since

$$
\int_ {a} ^ {\infty} f (x) d x = \int_ {a} ^ {\infty} (x f (x)) \frac {1}{x} d x,
$$

the assertion follows from the Abel test for convergence of improper integrals (see 1.5.22).

1.5.29. Assume, for example, that $f$ is decreasing on $[0,\infty)$ . Then, since $\int_0^\infty f(x)dx$ exists, we see that $\lim_{x\to \infty}f(x) = 0$ . Hence, by 1.5.11,

$$
\int_ {0} ^ {\infty} f (x) d x = \sum_ {n = 0} ^ {\infty} \int_ {n h} ^ {(n + 1) h} f (x) d x \leq h \sum_ {n = 0} ^ {\infty} f (n h).
$$

Likewise,

$$
\int_ {0} ^ {\infty} f (x) d x \geq h \sum_ {n = 1} ^ {\infty} f (n h) = h \sum_ {n = 0} ^ {\infty} f (n h) - h f (0).
$$

So,

$$
0 \leq h \sum_ {n = 0} ^ {\infty} f (n h) - \int_ {0} ^ {\infty} f (x) d x \leq h f (0),
$$

which gives the desired equality.

Taking $f(x) = 1 / (1 + x^2)$ , we get

$$
\lim  _ {h \rightarrow 0 ^ {+}} \sum_ {n = 1} ^ {\infty} \frac {h}{1 + h ^ {2} n ^ {2}} = \int_ {0} ^ {\infty} \frac {1}{1 + x ^ {2}} d x = \frac {\pi}{2}.
$$

1.5.30. It is clear that

$$
\Gamma (1) = \int_ {0} ^ {\infty} e ^ {- x} d x = 1.
$$

Assume first that $0 < \alpha < 1$ , and write

$$
\int_ {0} ^ {\infty} e ^ {- x} x ^ {\alpha - 1} d x = \int_ {0} ^ {1} e ^ {- x} x ^ {\alpha - 1} d x + \int_ {1} ^ {\infty} e ^ {- x} x ^ {\alpha - 1} d x = I _ {1} + I _ {2}.
$$

We have

$$
I _ {1} = \int_ {0} ^ {1} e ^ {- x} x ^ {\alpha - 1} d x \leq \int_ {0} ^ {1} x ^ {\alpha - 1} d x = \frac {1}{\alpha}.
$$

Moreover,

$$
I _ {2} = \int_ {1} ^ {\infty} e ^ {- x} x ^ {\alpha - 1} d x \leq \int_ {1} ^ {\infty} e ^ {- x} d x = e ^ {- 1}.
$$

If $\alpha > 1$ , then $\lim_{x \to 0^+} e^{-x} x^{\alpha - 1} = 0$ , so it suffices to show the convergence of

$$
\int_ {x _ {0}} ^ {\infty} e ^ {- x} x ^ {a - 1} d x
$$

with some $x_0 > 0$ . Since $\lim_{x \to \infty} e^{-x/2} x^{\alpha - 1} = 0$ , there is $x_0$ such that $x^{\alpha - 1} e^{-x/2} < 1$ for $x > x_0$ . Hence

$$
\int_ {x _ {0}} ^ {\infty} e ^ {- x} x ^ {a - 1} d x \leq \int_ {x _ {0}} ^ {\infty} e ^ {- x / 2} d x = 2 e ^ {- \frac {- x _ {0}}{2}}.
$$

1.5.31. Set $f(x) = e^{-x} x^{\alpha - 1}$ and take $h = -\ln t$ . Then

$$
\Gamma (\alpha) = \lim  _ {t \rightarrow 1 ^ {-}} (- \ln t) \sum_ {n = 1} ^ {\infty} t ^ {n} (- n \ln t) ^ {\alpha - 1} = \lim  _ {t \rightarrow 1 ^ {-}} (- \ln t) ^ {\alpha} \sum_ {n = 1} ^ {\infty} n ^ {\alpha - 1} t ^ {n}.
$$

Since $\lim_{\ell \to 1^{-}}\frac{-\ln\ell}{1 - \ell} = 1$ we get

$$
\Gamma (\alpha) = \lim  _ {t \rightarrow 1 ^ {-}} (1 - t) ^ {\alpha} \sum_ {n = 1} ^ {\infty} n ^ {\alpha - 1} t ^ {n}.
$$

Now, note that for $0 < t < 1$ ,

$$
\frac {1}{(1 - t) ^ {\alpha}} = 1 + \sum_ {n = 1} ^ {\infty} \frac {\alpha (\alpha + 1) . . . (\alpha + n - 1)}{n !} t ^ {n}
$$

and observe that the sequence

$$
c _ {n} = \frac {n ^ {\alpha - 1} n !}{\alpha (\alpha + 1) . . . (\alpha + n - 1)}
$$

is monotone. Indeed, if $\alpha \geq 1$ , then

$$
\frac {c _ {n + 1}}{c _ {n}} = \frac {n}{\alpha + n} \left(1 + \frac {1}{n}\right) ^ {\alpha} \geq 1,
$$

because $\left(1 + \frac{1}{n}\right)^{\alpha} \geq 1 + \frac{\alpha}{n}$ (see, e.g., II, 2.3.7(a)). Thus in this case the sequence $\{c_{n}\}$ either converges or diverges to infinity. If $0 < \alpha < 1$ , then $\left(1 + \frac{1}{n}\right)^{\alpha} < 1 + \frac{\alpha}{n}$ , (see, e.g., II, 2.3.7(b)), and consequently, the sequence $\{c_{n}\}$ is monotonically decreasing. To end the proof it is enough to apply the result given in II, 3.3.21 (which can also be extended to the case when $A = +\infty$ ).

1.5.32. We have

$$
\begin{array}{l} \Gamma (\alpha) = \lim  _ {n \rightarrow \infty} \frac {n ^ {\alpha - 1} n !}{\alpha (\alpha + 1) . . . (\alpha + n - 1)} \\ = \lim  _ {n \rightarrow \infty} \frac {n ^ {\alpha - 1} n}{\alpha (\alpha + 1) \left(\frac {\alpha}{2} + 1\right) \dots \left(\frac {\alpha}{n - 1} + 1\right)} \\ = \lim  _ {n \rightarrow \infty} n ^ {\alpha} \frac {1}{\alpha} e ^ {- \sum_ {k = 1} ^ {n - 1} k} \prod_ {k = 1} ^ {n - 1} \frac {e ^ {\alpha / k}}{1 + \frac {\alpha}{k}} \\ = \lim  _ {n \rightarrow \infty} e ^ {\alpha (\ln n - (1 + \frac {1}{2} + \dots + \frac {1}{n - 1}))} \frac {1}{\alpha} \prod_ {k = 1} ^ {n - 1} \frac {e ^ {\alpha / k}}{1 + \frac {\alpha}{k}} \\ = \frac {e ^ {- \gamma a}}{a} \prod_ {k = 1} ^ {\infty} e ^ {\alpha / k} \left(1 + \frac {\alpha}{k}\right) ^ {- 1}. \\ \end{array}
$$

1.5.33. By 1.5.24(a) we know that the integral $\int_0^\infty \frac{\sin x}{x} dx$ converges. Therefore

$$
\int_ {0} ^ {\infty} \frac {\sin x}{x} d x = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {n \pi / 2} \frac {\sin x}{x} d x = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {\pi / 2} \frac {\sin n x}{x} d x.
$$

Hence

$$
\int_ {0} ^ {\infty} \frac {\sin x}{x} d x = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{x} d x.
$$

We will show that

$$
\int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{\sin x} d x = \frac {\pi}{2}, \quad n = 1, 2, \dots , \tag {1}
$$

and

$$
\lim  _ {n \rightarrow \infty} \left(\int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{x} d x - \int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{\sin x} d x\right) = 0. \tag {2}
$$

To show (1), recall that for $x \in (0, 2\pi)$ ,

$$
\frac {1}{2} + \cos x + \cos 2 x + \dots + \cos n x = \frac {\sin \left(\frac {1}{2} (2 n + 1) x\right)}{2 \sin \frac {x}{2}}.
$$

Hence

$$
\frac {\sin (2 n + 1) x}{\sin x} = 1 + 2 \cos 2 x + 2 \cos 4 x + \dots + 2 \cos 2 n x, \quad x \in (0, \pi).
$$

This gives

$$
\int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{\sin x} d x = \frac {\pi}{2}.
$$

To prove (2), observe that by 1.4.11(a),

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} \left(\int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{x} d x - \int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{\sin x} d x\right) \\ = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {\pi / 2} \frac {\sin x - x}{x \sin x} \sin (2 n + 1) x d x = 0. \\ \end{array}
$$

1.5.34. It follows from the inequality

$$
1 - x ^ {2} \leq e ^ {- x ^ {2}} \leq \frac {1}{1 + x ^ {2}}
$$

that

$$
(1 - x ^ {2}) ^ {n} \leq e ^ {- n x ^ {2}} \quad \text {f o r} \quad | x | \leq 1, n \in \mathbb {N},
$$

and

$$
e ^ {- n x ^ {2}} \leq \frac {1}{(1 + x ^ {2}) ^ {n}} \quad \text {f o r} \quad x \in \mathbb {R}, n \in \mathbb {N}.
$$

Thus

$$
\int_ {0} ^ {1} (1 - x ^ {2}) ^ {n} d x \leq \int_ {0} ^ {1} e ^ {- n x ^ {3}} d x \leq \int_ {0} ^ {\infty} e ^ {- n x ^ {2}} d x \leq \int_ {0} ^ {\infty} \frac {1}{(1 + x ^ {2}) ^ {n}} d x.
$$

Now by the solution to 1.4.2 and by 1.5.1(g) we get

$$
\frac {2 \cdot 4 \dots (2 n)}{3 \cdot 5 \dots (2 n + 1)} \leq \int_ {0} ^ {\infty} e ^ {- n x ^ {2}} d x \leq \frac {3 \cdot 5 \dots (2 n - 3)}{2 \cdot 4 \dots (2 n - 2)} \cdot \frac {\pi}{2}.
$$

Moreover, the substitution $t = x\sqrt{n}$ gives

$$
\sqrt {n} \frac {2 \cdot 4 \dots (2 n)}{3 \cdot 5 \dots (2 n + 1)} \leq \int_ {0} ^ {\infty} e ^ {- t ^ {2}} d t \leq \frac {3 \cdot 5 \dots (2 n - 3)}{2 \cdot 4 \dots (2 n - 2)} \cdot \frac {\pi}{2} \sqrt {n},
$$

which combined with the Wallis formula (see, e.g., I, 3.8.38) yields the desired equality.

1.5.35. It follows from the Cauchy theorem (see 1.5.10) that, given $\varepsilon > 0$ , there is $a_0 > a$ such that for $b > a_0$ and $y \in A$ ,

$$
\left| \int_ {a} ^ {b} f (x, y) d x - \int_ {a} ^ {a _ {0}} f (x, y) d x \right| \leq \int_ {a _ {0}} ^ {b} | f (x, y) | d x \leq \int_ {a _ {0}} ^ {b} \varphi (x) d x <   \varepsilon .
$$

This implies the desired result.

1.5.36. It is enough to show that, given $\varepsilon > 0$ , there is $a_0 > a$ such that for $a_2 > a_1 > a_0$ , and for $y \in \mathbf{A}$ ,

$$
\left| \int_ {a _ {1}} ^ {a _ {2}} f (x, y) g (x, y) d x \right| <   \varepsilon .
$$

By the second mean value theorem (see 1.3.16),

$$
\int_ {a _ {1}} ^ {a _ {2}} f (x, y) g (x, y) d x = g \left(a _ {1}, y\right) \int_ {a _ {1}} ^ {c} f (x, y) d x + g \left(a _ {2}, y\right) \int_ {c} ^ {a _ {2}} f (x, y) d x
$$

with some $c$ in $[a_1, a_2]$ . Since $g$ is bounded, there is $C > 0$ such that $|g(x, y)| \leq C$ for $x \in [a, \infty)$ and $y \in \mathbf{A}$ . The uniform convergence of $\int_{a}^{\infty} f(x, y) dx$ implies that there is $a_0 > a$ such that

$$
\left| \int_ {a _ {1}} ^ {c} f (x, y) d x \right| <   \frac {\varepsilon}{2 C} \quad \text {a n d} \quad \left| \int_ {c} ^ {a _ {2}} f (x, y) d x \right| <   \frac {\varepsilon}{2 C}
$$

for $a_1 > a_0$ and $y \in \mathbf{A}$ . Thus for $y \in \mathbf{A}$ ,

$$
\begin{array}{l} \left| \int_ {a _ {1}} ^ {a _ {2}} f (x, y) g (x, y) d x \right| \\ \leq | g (a _ {1}, y) | \left| \int_ {a _ {1}} ^ {c} f (x, y) d x \right| + | g (a _ {2}, y) | \left| \int_ {c} ^ {a _ {2}} f (x, y) d x \right| \\ <   C \frac {\varepsilon}{2 C} + C \frac {\varepsilon}{2 C} = \varepsilon . \\ \end{array}
$$

1.5.37. Apply the above test with $f(x, y) = f(x)$ for $y \in \mathbf{A}$ .

1.5.38. The proof is analogous to that in 1.5.36.

1.5.39. (a) The uniform convergence of $\int_0^\infty \frac{\sin ax}{x} dx$ on $[a_0, \infty)$ follows from the test given in the previous problem.

(b) The integral $\int_0^\infty \frac{\sin ax}{x} dx$ is not uniformly convergent on $[0,\infty)$ . Indeed, for any $b > 0$ ,

$$
\int_ {b} ^ {\infty} \frac {\sin a x}{x} d x = \int_ {b a} ^ {\infty} \frac {\sin x}{x} d x,
$$

and consequently,

$$
\lim  _ {a \rightarrow 0 ^ {+}} \int_ {b} ^ {\infty} \frac {\sin a x}{x} d x = \int_ {0} ^ {\infty} \frac {\sin x}{x} d x = \frac {\pi}{2},
$$

where the last equality follows from 1.5.33.

(c) Since

$$
\left| \frac {\cos a (x ^ {2} + 1)}{x ^ {2} + 1} \right| \leq \frac {1}{x ^ {2} + 1}, \quad a \in \mathbb {R},
$$

the uniform convergence of the integral follows from 1.5.35.

(d) We know (compare with 1.5.24(c)) that $\int_0^\infty \cos x^2 dx$ converges. Thus the uniform convergence of the given integral follows from 1.5.37.

1.5.40. Since $f(x, y)$ converges to $\varphi(x)$ as $y \to y_0$ uniformly on an interval $[a, b]$ ,

$$
\lim  _ {y \cdot y _ {0}} \int_ {a} ^ {b} f (x, y) d x = \int_ {a} ^ {b} \varphi (x) d x \quad (\text {s e e} 1. 3. 9). \tag {1}
$$

Furthermore, the uniform convergence of $\int_{a}^{\infty} f(x, y) dx$ implies that, given $\varepsilon > 0$ , there is $a_0 > a$ such that for $b, b' > a_0$

$$
\left| \int_ {a} ^ {b} f (x, y) d x - \int_ {a} ^ {b ^ {\prime}} f (x, y) d x \right| <   \varepsilon
$$

for all $y \in \mathbf{A}$ . Taking $y \to y_0$ , we get by (1)

$$
\left| \int_ {a} ^ {b} \varphi (x) d x - \int_ {a} ^ {b ^ {\prime}} \varphi (x) d x \right| \leq \varepsilon .
$$

This means that the integral $\int_{a}^{\infty}\varphi (x)dx$ converges. Now we show that the given equality holds. Let $\varepsilon >0$ be chosen arbitrarily. Then there exists $a_0 > a$ such that for a $b > a_0$ ,

$$
\left| \int_ {b} ^ {\infty} f (x, y) d x \right| <   \varepsilon , \quad y \in A,
$$

and

$$
\left| \int_ {b} ^ {\infty} \varphi (x) d x \right| <   \varepsilon .
$$

Moreover, by (1), there is $\delta = \delta(b, \varepsilon)$ such that

$$
\left| \int_ {a} ^ {b} f (x, y) d x - \int_ {a} ^ {b} \varphi (x) d x \right| <   \varepsilon ,
$$

if $|y - y_0| < \delta$ . Consequently,

$$
\left| \int_ {a} ^ {\infty} f (x, y) d x - \int_ {a} ^ {\infty} \varphi (x) d x \right| <   3 \varepsilon ,
$$

whenever $|y - y_0| < \delta$ .

# 1.5. Improper Integrals

It is clear that we assume that $y_0$ is a limit point of $A$ . Moreover, the above reasoning can be applied when $y$ approaches infinity. In particular, the theorem applies to sequences of functions.

1.5.41. Here $\mathbf{A} = \mathbb{N}$ and, for each $n\in \mathbb{N}$

$$
\int_ {0} ^ {\infty} f _ {n} (x) d x = e ^ {- \frac {n}{2 x ^ {2}}} \left| _ {0} ^ {\infty} = 1. \right.
$$

Moreover, since

$$
\sup  _ {x \geq 0} f _ {n} (x) = f _ {n} (\sqrt {n / 3}) = \frac {3 \sqrt {3}}{\sqrt {n}} e ^ {- 3 / 2},
$$

$\{f_n\}$ converges to zero uniformly on $[0,\infty)$ , but

$$
1 = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {\infty} f _ {n} (x) d x \neq \int_ {0} ^ {\infty} 0 d x = 0.
$$

Note that the integral $\int_0^\infty f_n(x)dx$ fails to converge uniformly on $\mathbb{N}$ , because

$$
\int_ {a} ^ {\infty} f _ {n} (x) d x = 1 - e ^ {- \frac {n}{2 a ^ {2}}} > 1 - e ^ {- 1} \quad \text {f o r} \quad n > 2 a ^ {2}.
$$

1.5.42. (a) It follows from 1.5.37 that $\int_0^\infty \frac{\sin x}{x} e^{-yx} dx$ converges uniformly on $(0, \infty)$ . Moreover,

$$
\sup  _ {x \in [ 0, b ]} \left| \frac {\sin x}{x} e ^ {- y x} - \frac {\sin x}{x} \right| \leq 1 - e ^ {- y b}.
$$

So, the result follows from 1.5.33 and 1.5.40.

(b) We first show that

$$
\sin x ^ {2} \arctan (y x) \xrightarrow [ y \to \infty ]{\pi} \frac {\pi}{2} \sin x ^ {2}
$$

uniformly on $[0,\infty)$ . Indeed, given $\varepsilon > 0$ ,

$$
\begin{array}{l} \sup  _ {x \in [ 0, \infty)} \left| \sin x ^ {2} \left(\frac {\pi}{2} - \arctan (y x)\right) \right| \\ \leq \sup  _ {x \in [ 0, \sqrt {\varepsilon / \pi} ]} \left| \sin x ^ {2} \left(\frac {\pi}{2} - \arctan (y x)\right) \right| \\ + \sup  _ {x \in \left[ \sqrt {\varepsilon / \pi}, \infty\right)} \left| \sin x ^ {2} \left(\frac {\pi}{2} - \arctan (y x)\right) \right| \\ \leq \frac {\varepsilon}{2} + \frac {\pi}{2} - \arctan (y \sqrt {\varepsilon / \pi}) <   \varepsilon \\ \end{array}
$$

for sufficiently large $y$ . Moreover, the uniform convergence of the integral $\int_0^\infty \sin x^2 \arctan(yx) dx$ follows from 1.5.24(c) and 1.5.37. Thus one can apply 1.5.40.

(c) To show that $\int_0^\infty \frac{\sin x}{x} \left(1 + \frac{x}{n}\right)^{-n} dx$ converges uniformly on $N$ we apply 1.5.37 with $g(x, n) = \left(1 + \frac{x}{n}\right)^{-n}$ and $f(x) = \frac{\sin x}{x}$ . Thus the desired result follows from 1.5.40.

(d) As above, we apply 1.5.37, 1.5.1(h) and 1.5.40.

(e) Substituting $u = yx$ , we get

$$
\int_ {0} ^ {\infty} y ^ {2} \sin x e ^ {- y ^ {2} x ^ {2}} d x = \int_ {0} ^ {\infty} y \sin \frac {u}{y} e ^ {- u ^ {2}} d u.
$$

The uniform convergence of the last integral on $(0,\infty)$ follows from 1.5.35. It is also clear that $y\sin \frac{u}{y} e^{-u^2}\xrightarrow[y\to 0^+]{y\to 0^+}0$ uniformly on $[0,\infty)$ . Thus one can apply 1.5.40.

1.5.43. Since the improper integral $\int_{a}^{\infty} f(x, y) dx$ converges uniformly on $[c, d]$ , given $\varepsilon > 0$ , there is $b > a$ such that

$$
\left| \int_ {b} ^ {\infty} f (x, y) d x \right| <   \frac {\epsilon}{3}
$$

for all $y \in [c, d]$ . Moreover, the uniform continuity of $f$ on $[a, b] \times [c, d]$ implies that there is $\delta > 0$ such that if $|y_1 - y_2| < \delta$ , then

$$
| f (x, y _ {1}) - f (x, y _ {2}) | <   \frac {\varepsilon}{3 (b - a)}
$$

for $(x,y_1),(x,y_2)\in [a,b]\times [c,d]$ . Consequently,

$$
\begin{array}{l} \left| I \left(y _ {1}\right) - I \left(y _ {2}\right) \right| \\ = \left| \int_ {a} ^ {b} f (x, y _ {1}) d x - \int_ {a} ^ {b} f (x, y _ {2}) d x + \int_ {b} ^ {\infty} f (x, y _ {1}) d x - \int_ {b} ^ {\infty} f (x, y _ {2}) d x \right| \\ \leq \int_ {a} ^ {b} | f (x, y _ {1}) - f (x, y _ {2}) | d x + \left| \int_ {b} ^ {\infty} f (x, y _ {1}) d x \right| + \left| \int_ {b} ^ {\infty} f (x, y _ {2}) d x \right| \\ <   \frac {\varepsilon}{3} + \frac {\varepsilon}{3} + \frac {\varepsilon}{3} = \varepsilon . \\ \end{array}
$$

1.5.44. Since $\int_{a}^{\infty} f(x, y) dx$ converges for every $y \in [c, d]$ , we can write

$$
I (y) = \int_ {a} ^ {\infty} f (x, y) d x = \sum_ {n = 1} ^ {\infty} \int_ {a _ {n - 1}} ^ {a _ {n}} f (x, y) d x,
$$

where $a_0 = a$ and $\{a_n\}$ is an increasing sequence diverging to infinity (see 1.5.11). By 1.4.43,

$$
\frac {d}{d y} \int_ {a _ {n - 1}} ^ {a _ {n}} f (x, y) d x = \int_ {a _ {n - 1}} ^ {a _ {n}} \frac {\partial f}{\partial y} (x, y) d x.
$$

Moreover, the uniform convergence of the integral $\int_{a}^{\infty}\frac{\partial f}{\partial y} (x,y)dx$ implies the uniform convergence on $[c,d]$ of the series

$$
\sum_ {n = 1} ^ {\infty} \int_ {a _ {n - 1}} ^ {a _ {n}} \frac {\partial f}{\partial y} (x, y) d x.
$$

Using the result in II, 3.2.28, we see that

$$
\frac {d}{d y} I (y) = \sum_ {n = 1} ^ {\infty} \int_ {a _ {n - 1}} ^ {a _ {n}} \frac {\partial f}{\partial y} (x, y) d x = \int_ {0} ^ {\infty} \frac {\partial f}{\partial y} (x, y) d x.
$$

1.5.45. (a) It follows from 1.5.34 that

$$
\int_ {0} ^ {\infty} e ^ {- a x ^ {2}} d x = \frac {1}{2} \sqrt {\frac {\pi}{a}}, \quad a > 0. \tag {1}
$$

Note also that each of the improper integrals

$$
\int_ {0} ^ {\infty} e ^ {- a x ^ {2}} x ^ {2 n} d x, \quad n \in \mathbb {N},
$$

converges uniformly on $[c,d]$ , $0 < c < d$ . Thus, differentiating (1) under the integral sign, we get

$$
\int_ {0} ^ {\infty} e ^ {- a x ^ {2}} x ^ {2 n} d x = \frac {1 \cdot 3 \cdot 5 \dots (2 n - 1)}{2 ^ {n + 1} a ^ {n}} \sqrt {\frac {\pi}{a}}.
$$

(b) Since

$$
\int_ {0} ^ {\infty} \frac {d x}{a + x ^ {2}} = \frac {\pi}{2 \sqrt {a}},
$$

as above, we get

$$
\int_ {0} ^ {\infty} \frac {d x}{(a + x ^ {2}) ^ {n + 1}} = \frac {1 \cdot 3 \cdot 5 \dots (2 n - 1)}{2 \cdot 4 \dots (2 n)} \cdot \frac {1}{a ^ {n}} \cdot \frac {\pi}{2 \sqrt {a}}.
$$

(c) Put

$$
I (a) = \int_ {0} ^ {\infty} \frac {\sin (a x)}{x} e ^ {- x} d x.
$$

Differentiating under the integral sign, we obtain

$$
I ^ {\prime} (a) = \int_ {0} ^ {\infty} \cos (a x) e ^ {- x} d x.
$$

Now integration by parts yields

$$
I ^ {\prime} (a) = 1 - a ^ {2} I ^ {\prime} (a).
$$

Thus $I'(a) = \frac{1}{1 + a^2}$ , and consequently, $I(a) = \arctan a + C$ . Since $I(0) = 0$ , we get $I(a) = \arctan a$ .

(d) We set

$$
I (a) = \int_ {0} ^ {\infty} \frac {1 - \cos (a x)}{x} e ^ {- x} d x.
$$

Differentiating under the integral sign and then integrating by parts give

$$
I ^ {\prime} (a) = \int_ {0} ^ {\infty} \sin (a x) e ^ {- x} d x = a \int_ {0} ^ {\infty} \cos (a x) e ^ {- x} d x = \frac {a}{1 + a ^ {2}},
$$

where the last equality follows from the solution of (c). Since $I(0) = 0$ , it then follows that $I(a) = \frac{1}{2} \ln (1 + a^2)$ .

1.5.46. (a) Set

$$
I (y) = \int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2} \cos (y x) d x = 2 \int_ {0} ^ {\infty} e ^ {- x ^ {2} / 2} \cos (y x) d x.
$$

By the result in 1.5.44,

$$
I ^ {\prime} (y) = - 2 \int_ {0} ^ {\infty} e ^ {- x ^ {2} / 2} x \sin (y x) d x.
$$

Integrating by parts yields

$$
I ^ {\prime} (y) = - 2 y \int_ {0} ^ {\infty} e ^ {- x ^ {2} / 2} \cos (y x) d x = - y I (y).
$$

Consequently,

$$
I (y) = C e ^ {- v ^ {2} / 2},
$$

and, since $I(0) = \sqrt{2\pi}$ (see, e.g., 1.5.34), the desired result follows. (b) Put

$$
I (y) = \int_ {0} ^ {\infty} e ^ {- x - y / x} \frac {d x}{\sqrt {x}}.
$$

Differentiating under the integral sign (see 1.5.44) gives

$$
I ^ {\prime} (y) = - \int_ {0} ^ {\infty} e ^ {- x - y / x} \frac {d x}{x \sqrt {x}}.
$$

Now, substituting $t = y / x$ , we get

$$
I ^ {\prime} (y) = - \frac {1}{\sqrt {y}} I (y).
$$

Consequently,

$$
I (y) = C e ^ {- 2 \sqrt {y}},
$$

and, since

$$
I (0) = \int_ {0} ^ {\infty} e ^ {- x} \frac {d x}{\sqrt {x}} = 2 \int_ {0} ^ {\infty} e ^ {- x ^ {2}} d x = \sqrt {\pi},
$$

the desired equality follows.

1.5.47. By 1.5.43, $I(y) = \int_{a}^{\infty} f(x,y) dx$ is continuous on $[c,d]$ , and therefore Riemann integrable on that interval. We have

$$
\int_ {c} ^ {d} I (y) d y = \int_ {c} ^ {d} \left(\int_ {a} ^ {b} f (x, y) d x\right) d y + \int_ {c} ^ {d} \left(\int_ {b} ^ {\infty} f (x, y) d x\right) d y.
$$

By the uniform convergence of $\int_{a}^{\infty}f(x,y)dx$ on $[c,d]$ ,

$$
\left| \int_ {c} ^ {d} \left(\int_ {b} ^ {\infty} f (x, y) d x\right) d y \right| \xrightarrow [ b \to \infty ]{} 0.
$$

Thus by 1.4.48,

$$
\int_ {c} ^ {d} I (y) d y = \int_ {a} ^ {b} \left(\int_ {c} ^ {d} f (x, y) d y\right) d x + o (1) \quad a s \quad b \rightarrow \infty .
$$

Letting $b \to \infty$ gives the desired equality.

1.5.48. (a) We have

$$
\int_ {0} ^ {\infty} \frac {e ^ {- b x} - e ^ {- a x}}{x} d x = \int_ {0} ^ {\infty} \left(\int_ {b} ^ {a} e ^ {- y x} d y\right) d x.
$$

Since $\int_0^\infty e^{-yx}dx$ converges uniformly on the closed interval with endpoints $a$ and $b$ ,

$$
\int_ {0} ^ {\infty} \frac {e ^ {- b x} - e ^ {- a x}}{x} d x = \int_ {b} ^ {a} \left(\int_ {0} ^ {\infty} e ^ {- y x} d x\right) d y = \int_ {b} ^ {a} \frac {1}{y} d y = \ln \frac {a}{b}.
$$

(b) As in (a),

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {\cos (b x) - \cos (a x)}{x ^ {2}} d x = \int_ {0} ^ {\infty} \left(\int_ {a} ^ {b} - \frac {\sin (y x)}{x} d y\right) d x \\ = \int_ {a} ^ {b} \left(\int_ {0} ^ {\infty} - \frac {\sin (y x)}{x} d x\right) d y = - \frac {\pi}{2} (b - a), \\ \end{array}
$$

where the last equality follows from 1.5.39(a).

1.5.49. We have

$$
\int_ {0} ^ {\infty} \frac {f (b x) - f (a x)}{x} d x = \int_ {0} ^ {\infty} \left(\int_ {a} ^ {b} f ^ {\prime} (y x) d y\right) d x.
$$

It is clear that

$$
\int_ {0} ^ {\infty} f ^ {\prime} (y x) d x = \frac {l - f (0)}{y}.
$$

So in view of the monotonicity of $f'$ , $\lim_{x \to \infty} f'(x) = 0$ , and $f'$ is either nonnegative and decreasing or nonpositive and increasing. To show that the improper integral $\int_0^\infty f'(yx) dx$ converges uniformly on $[a, b]$ , assume, for example, that $f'$ is nonnegative and decreasing. Then

$$
f ^ {\prime} (y x) \leq f ^ {\prime} (a x), \quad x \geq 0, y \in [ a, b ],
$$

and the uniform convergence follows from 1.5.35. By the result in 1.5.47,

$$
\int_ {0} ^ {\infty} \frac {f (b x) - f (a x)}{x} d x = \int_ {a} ^ {b} \left(\int_ {0} ^ {\infty} f ^ {\prime} (y x) d x\right) d y = (l - f (0)) \ln \frac {b}{a}.
$$

1.5.50. Assume, for example, that the first integral in (4) converges, and set

$$
F (x, d) = \int_ {c} ^ {d} f (x, y) d y, \quad x \geq a.
$$

Then by 1.5.47,

$$
\int_ {c} ^ {d} \left(\int_ {a} ^ {\infty} f (x, y) d x\right) d y = \int_ {a} ^ {\infty} F (x, d) d x.
$$

Since

$$
| F (x, d) | \leq \varphi (x) = \int_ {c} ^ {\infty} | f (x, y) | d y
$$

and the integral $\int_{a}^{\infty}\varphi (x)dx$ converges, by the result in 1.5.35, the improper integral $\int_{a}^{\infty}F(x,d)dx$ converges uniformly on $[c,\infty)$ . We

now show that $F(x, d)$ converges to $\int_{c}^{\infty} f(x, y) dy$ as $d \to \infty$ uniformly on each interval $[a, b]$ . Indeed, by (2), given $\varepsilon > 0$ , there is $d_0$ such that for $d > d_0$ ,

$$
\sup  _ {x \in [ a, b ]} \left| F (x, d) - \int_ {c} ^ {\infty} f (x, y) d y \right| = \sup  _ {x \in [ a, b ]} \left| \int_ {d} ^ {\infty} f (x, y) d y \right| <   \varepsilon .
$$

Using the result in 1.5.40, we get

$$
\begin{array}{l} \lim  _ {d \rightarrow \infty} \int_ {a} ^ {\infty} F (x, d) d x = \int_ {a} ^ {\infty} \left(\lim  _ {d \rightarrow \infty} F (x, d)\right) d x \\ = \int_ {a} ^ {\infty} \left(\int_ {c} ^ {\infty} f (x, y) d y\right) d x. \\ \end{array}
$$

1.5.51. Substituting $x = \sqrt{u}$ , we get

$$
\int_ {0} ^ {\infty} \cos x ^ {2} d x = \frac {1}{2} \int_ {0} ^ {\infty} \frac {\cos u}{\sqrt {u}} d u
$$

and

$$
\int_ {0} ^ {\infty} \sin x ^ {2} d x = \frac {1}{2} \int_ {0} ^ {\infty} \frac {\sin u}{\sqrt {u}} d u.
$$

We will calculate the latter integral. The first can be calculated analogously. By the result in 1.5.34 we have

$$
\frac {1}{\sqrt {u}} = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {\infty} e ^ {- u y ^ {2}} d y.
$$

For $k > 0$ we consider

$$
\int_ {0} ^ {\infty} \frac {\sin u}{\sqrt {u}} e ^ {- k u} d u.
$$

It follows from the above that

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {\sin u}{\sqrt {u}} e ^ {- k u} d u = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {\infty} \sin u e ^ {- k u} \left(\int_ {0} ^ {\infty} e ^ {- u y ^ {2}} d y\right) d u \\ = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {\infty} \left(\int_ {0} ^ {\infty} \sin u e ^ {- (k + y ^ {2}) u} d y\right) d u \\ = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {\infty} \left(\int_ {0} ^ {\infty} \sin u e ^ {- (k + y ^ {2}) u} d u\right) d y, \\ \end{array}
$$

where the last equality follows from 1.5.50. An easy calculation shows that

$$
\int_ {0} ^ {\infty} \sin u e ^ {- (k + y ^ {2}) u} d u = \frac {1}{1 + (k + y ^ {2}) ^ {2}}.
$$

Consequently,

$$
\int_ {0} ^ {\infty} \frac {\sin u}{\sqrt {u}} e ^ {- k u} d u = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {\infty} \frac {1}{1 + (k + y ^ {2}) ^ {2}} d y.
$$

Finally, by the result stated in 1.5.40, we can switch the limit and the integral, and get

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {\sin u}{\sqrt {u}} d u = \lim  _ {k \rightarrow 0 ^ {+}} \int_ {0} ^ {\infty} \frac {\sin u}{\sqrt {u}} e ^ {- k u} d u = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {\infty} \frac {1}{1 + y ^ {4}} d y \\ = \frac {2}{\sqrt {\pi}} \cdot \frac {\pi \sqrt {2}}{4} = \sqrt {\frac {\pi}{2}}. \\ \end{array}
$$

1.5.52. Since $f(x, y)$ converges to $\varphi(x)$ as $y \to y_0$ uniformly on an interval $[a, b - \eta]$ ,

$$
\lim  _ {y \rightarrow y _ {0}} \int_ {a} ^ {b - \eta} f (x, y) d x = \int_ {a} ^ {b - \eta} \varphi (x) d x \quad (\text {s e e 1 . 3 . 9}). \tag {1}
$$

Furthermore, by assumption, given $\varepsilon > 0$ , there is $\eta_0 > 0$ such that for $0 < \eta, \eta' < \eta_0$

$$
\left| \int_ {a} ^ {b - \eta} f (x, y) d x - \int_ {a} ^ {b - \eta^ {\prime}} f (x, y) d x \right| <   \varepsilon
$$

for all $y \in \mathbf{A}$ . Taking $y \to y_0$ , we get by (1)

$$
\left| \int_ {a} ^ {b - \eta} \varphi (x) d x - \int_ {a} ^ {b - \eta^ {\prime}} \varphi (x) d x \right| \leq \varepsilon .
$$

This means that the integral $\int_{a}^{b}\varphi (x)dx$ converges (as an improper integral between finite limits). Now we show that the given equality holds. Let $\varepsilon >0$ be chosen arbitrarily. Then there exists $\eta_0 > 0$ such that for an $0 < \eta < \eta_0$ ,

$$
\left| \int_ {b - \eta} ^ {b} f (x, y) d x \right| <   \varepsilon , \quad y \in A,
$$

and

$$
\left| \int_ {b - \eta} ^ {b} \varphi (x) d x \right| <   \varepsilon .
$$

Moreover, there is $\delta = \delta (\eta ,\varepsilon)$ such that

$$
\left| \int_ {a} ^ {b - \eta} f (x, y) d x - \int_ {a} ^ {b - \eta} \varphi (x) d x \right| <   \varepsilon ,
$$

if $|y - y_0| < \delta$ . Consequently,

$$
\left| \int_ {a} ^ {b} f (x, y) d x - \int_ {a} ^ {b} \varphi (x) d x \right| <   3 \varepsilon ,
$$

whenever $|y - y_0| < \delta$ .

Clearly we assume that $y_0$ is a limit point of $A$ . Moreover, the above reasoning can be applied to the case when $f(x, y)$ is Riemann integrable on $[a + \eta, b]$ , where $0 < \eta < b - a$ .

1.5.53. To apply the result in the previous problem with $\mathbf{A} = \mathbf{N}$ , observe that, given $\varepsilon > 0$ , there is $0 < \eta_0 < b - a$ such that for $0 < \eta < \eta_0$ ,

$$
\left| \int_ {b - \eta} ^ {b} f _ {n} (x) d x \right| \leq \int_ {b - \eta} ^ {b} | f _ {n} (x) | d x \leq \int_ {b - \eta} ^ {b} f (x) d x <   \varepsilon .
$$

1.5.54. Since

$$
\lim  _ {y \rightarrow \infty} e ^ {- x ^ {y}} = \varphi (x) = \left\{\begin{array}{l l}1&\text {i f} \quad x \in [ 0, 1),\\\frac {1}{e}&\text {i f} \quad x = 1,\\0&\text {i f} \quad x > 1,\end{array}\right.
$$

we see that the convergence is not uniform on $[0, b], b > 1$ , and the result in 1.5.40 cannot be applied. But we can write

$$
\int_ {0} ^ {\infty} e ^ {- x ^ {y}} d x = \int_ {0} ^ {1} e ^ {- x ^ {y}} d x + \int_ {1} ^ {2} e ^ {- x ^ {y}} d x + \int_ {2} ^ {\infty} e ^ {- x ^ {y}} d x.
$$

By the result in 1.5.52,

$$
\lim  _ {y \rightarrow \infty} \int_ {0} ^ {1} e ^ {- x ^ {y}} d x = \int_ {0} ^ {1} \varphi (x) d x = 1
$$

and

$$
\lim  _ {y \rightarrow \infty} \int_ {1} ^ {2} e ^ {- x ^ {y}} d x = \int_ {1} ^ {2} \varphi (x) d x = 0.
$$

Since the result in 1.5.40 can be applied to the integral $\int_{2}^{\infty} e^{-x^{y}} dx$ , the proof is complete.

1.5.55. Put

$$
f _ {n} (t) = \left\{ \begin{array}{l l} {\left(1 - \frac {t}{n}\right) ^ {n} t ^ {x - 1}} & {\text {i f} \quad 0 \leq t \leq n,} \\ {0} & {\text {i f} \quad t > n.} \end{array} \right.
$$

By I, 2.1.39, beginning with some value of the index $n$ , the sequence is strictly increasing on any interval $[0, a]$ . Moreover, $f_{n}(t)$ and the function $f(t) = e^{-t} t^{x - 1} = \lim_{n \to \infty} f_{n}(t)$ are continuous. By the Dini theorem (see, e.g., II, 3.1.16), $\{f_{n}\}$ converges to $f$ uniformly on $[0, a]$ . Since $\int_{0}^{\infty} f(t) dt = \Gamma(x) < \infty$ (see 1.5.30), given $\varepsilon > 0$ ,

$$
\int_ {a} ^ {\infty} f _ {n} (t) d t \leq \int_ {a} ^ {\infty} f (t) d t <   \varepsilon
$$

for sufficiently large $\pmb{a}$ . Therefore the result in 1.5.40 can be applied.

1.5.56. We first show that

(i) $\frac{1}{n}\int_{0}^{\pi /2}\left(\frac{\sin nx}{\sin x}\right)^{2}dx = \frac{\pi}{2}.$

We know (see (1) in the solution of 1.5.33) that

$$
\int_ {0} ^ {\pi / 2} \frac {\sin (2 n + 1) x}{\sin x} d x = \frac {\pi}{2}.
$$

Moreover, since

$$
\sum_ {k = 0} ^ {n - 1} \sin (2 k + 1) x = \frac {1 - \cos 2 n x}{2 \sin x} = \frac {\sin^ {2} n x}{\sin x}, \quad x \neq 0, \pm \pi , \pm 2 \pi , \dots ,
$$

equality (i) follows. Substituting $y = nx$ in (i) gives

$$
\int_ {0} ^ {n \pi / 2} \left(\frac {\sin y}{y}\right) ^ {2} \left(\frac {y / n}{\sin (y / n)}\right) ^ {2} d y = \frac {\pi}{2}.
$$

Now define

$$
f _ {n} (x) = \left\{ \begin{array}{l l} 1 & \text {f o r} x = 0, \\ \left(\frac {\sin x}{x}\right) ^ {2} \left(\frac {x / n}{\sin (x / n)}\right) ^ {2} & \text {f o r} 0 <   x \leq n \pi / 2, \\ 0 & \text {f o r} x > n \pi / 2. \end{array} \right.
$$

We have

$$
\lim  _ {n \rightarrow \infty} f _ {n} (x) = \left\{\begin{array}{l l}1&\text {f o r} x = 0,\\\left(\frac {\sin x}{x}\right) ^ {2}&\text {f o r} x > 0,\end{array}\right.
$$

and the convergence is uniform on each interval $[0, a]$ . Recall (see, e.g., II, 2.5.28(a)) that for $0 < x < \pi/2$ ,

$$
\frac {\sin x}{x} > \frac {2}{\pi}.
$$

So,

$$
f _ {n} (x) <   \left(\frac {\sin x}{x}\right) ^ {2} \frac {\pi^ {2}}{4}, \quad x > 0,
$$

and since $\int_0^\infty \left(\frac{\sin x}{x}\right)^2 dx < \infty$ , the uniform convergence of $\int_0^\infty f_n(x)dx$ follows from 1.5.35. Hence, by 1.5.40,

$$
\begin{array}{l} \frac {\pi}{2} = \lim  _ {n \rightarrow \infty} \int_ {0} ^ {\infty} f _ {n} (x) d x = \int_ {0} ^ {\infty} \lim  _ {n \rightarrow \infty} f _ {n} (x) d x \\ = \int_ {0} ^ {\infty} \left(\frac {\sin x}{x}\right) ^ {2} d x. \\ \end{array}
$$

1.5.57. We have

$$
\int_ {0} ^ {\infty} \frac {x ^ {a - 1}}{1 + x} d x = \int_ {0} ^ {1} \frac {x ^ {a - 1}}{1 + x} d x + \int_ {1} ^ {\infty} \frac {x ^ {a - 1}}{1 + x} d x = I _ {1} + I _ {2}.
$$

For $0 <   x <   1$

$$
\frac {x ^ {a - 1}}{1 + x} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {a + n - 1},
$$

and the series converges uniformly on $[\eta, 1 - \eta']$ , where $0 < \eta < 1 - \eta' < 1$ . Moreover,

$$
0 \leq S _ {n} (x) = \sum_ {k = 0} ^ {n - 1} (- 1) ^ {k} x ^ {a + k - 1} = \frac {x ^ {a - 1} (1 - (- x) ^ {n})}{1 + x} \leq x ^ {a - 1}.
$$

Since $\int_0^1 x^{a - 1}dx = 1 / a$ , we see that the assumptions of 1.5.53 are satisfied and

$$
I _ {1} = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \int_ {0} ^ {1} x ^ {a + n - 1} d x = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \frac {1}{a + n}.
$$

Furthermore, the substitution $x = 1 / y$ gives

$$
I _ {2} = \int_ {0} ^ {1} \frac {y ^ {- a}}{1 + y} d y = \int_ {0} ^ {1} \frac {y ^ {(1 - a) - 1}}{1 + y} d y = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \frac {1}{1 - a + n},
$$

where the last equality follows from the above. Hence

$$
\int_ {0} ^ {\infty} \frac {x ^ {a - 1}}{1 + x} d x = \frac {1}{a} + \sum_ {k = 1} ^ {\infty} (- 1) ^ {k} \left(\frac {1}{a + k} + \frac {1}{a - k}\right),
$$

which is the first equality to be proved. To prove the other one we start with the identity (scc, c.g., I, 3.8.37)

$$
\sin x = x \prod_ {n = 1} ^ {\infty} \left(1 - \frac {x ^ {2}}{n ^ {2} \pi^ {2}}\right).
$$

Thus if $x \neq k\pi, k \in \mathbb{Z}$ , then

$$
\ln | \sin x | = \ln | x | + \sum_ {n = 1} ^ {\infty} \ln \left| 1 - \frac {x ^ {2}}{n ^ {2} \pi^ {2}} \right|.
$$

Note that the derived series

$$
\sum_ {n = 1} ^ {\infty} \frac {2 x}{x ^ {2} - n ^ {2} \pi^ {2}}
$$

converges uniformly on each compact interval disjoint from the set $\{k\pi : k \in \mathbb{Z}\}$ . Hence we get

$$
\begin{array}{l} \cot x = \frac {\cos x}{\sin x} = \frac {1}{x} + \sum_ {n = 1} ^ {\infty} \frac {2 x}{x ^ {2} - n ^ {2} \pi^ {2}} \\ = \frac {1}{x} + \sum_ {n = 1} ^ {\infty} \left(\frac {1}{x - n \pi} + \frac {1}{x + n \pi}\right). \\ \end{array}
$$

It then follows that

$$
\begin{array}{l} \tan x = - \cot (x - \pi / 2) \\ = - \sum_ {n = 1} ^ {\infty} \left(\frac {1}{x - (2 n - 1) \pi / 2} + \frac {1}{x + (2 n - 1) \pi / 2}\right). \\ \end{array}
$$

Finally, using the identity

$$
\frac {1}{\sin x} = \frac {1}{2} \left(\cot \frac {x}{2} + \tan \frac {x}{2}\right),
$$

we obtain

$$
\sin x = \frac {1}{x} \left| \sum_ {n = 1} ^ {\infty} (1) ^ {n} \binom {1} {x - n \pi} \right| \frac {1}{x + n \pi},
$$

which implies the desired equality.

1.5.58. We have

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {x ^ {a - 1} - x ^ {b - 1}}{1 - x} d x \\ = \int_ {0} ^ {1} \frac {x ^ {a - 1} - x ^ {b - 1}}{1 - x} d x + \int_ {1} ^ {\infty} \frac {x ^ {a - 1} - x ^ {b - 1}}{1 - x} d x \\ = \int_ {0} ^ {1} \frac {x ^ {a - 1} - x ^ {b - 1}}{1 - x} d x + \int_ {0} ^ {1} \frac {(1 / x) ^ {a - 1} - (1 / x) ^ {b - 1}}{(1 - (1 / x)) x ^ {2}} d x \\ = \int_ {0} ^ {1} \frac {x ^ {a - 1} - x ^ {- a}}{1 - x} d x - \int_ {0} ^ {1} \frac {x ^ {b - 1} - x ^ {- b}}{1 - x} d x \\ - I _ {1} - I _ {2}. \\ \end{array}
$$

As in the solution of the preceding problem, we get

$$
I _ {1} = \frac {1}{a} + \sum_ {n = 1} ^ {\infty} \left(\frac {1}{a + n} - \frac {1}{a - n}\right) = \pi \cot \pi a.
$$

1.5.59. (a) The function

$$
\frac {\ln (1 - x)}{x} = - \sum_ {n = 1} ^ {\infty} \frac {x ^ {n - 1}}{n}, \quad x \in (0, 1),
$$

can be continuously extended to $[0,1)$ and the power series converges uniformly on each interval $[0,b]$ , $0 < b < 1$ . Moreover, if $S_{n}(x)$ denotes the $n$ th partial sum of the series, then

$$
| S _ {n} (x) | = - S _ {n} (x) \leq - \frac {\ln (1 - x)}{x}.
$$

It is easy to check that the integral $\int_0^1\frac{\ln(1 - x)}{x} dx$ converges. So the assumptions of 1.5.53 are satisfied. Consequently,

$$
\int_ {0} ^ {1} \frac {\ln (1 - x)}{x} d x = - \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {1} \frac {x ^ {n - 1}}{n} d x = - \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}} = - \frac {\pi^ {2}}{6}.
$$

(For an elementary proof of the last equality, see, e.g., I, 3.1.28(a).) (b) As in (a), we get

$$
\int_ {0} ^ {1} \frac {\ln (1 + x)}{x} d x = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n - 1} \int_ {0} ^ {1} \frac {x ^ {n - 1}}{n} d x = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{n ^ {2}} = \frac {\pi^ {2}}{1 2}.
$$

(c) We have

$$
\int_ {0} ^ {1} \frac {\ln (1 + x ^ {2})}{x} d x = \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n - 1}}{2 n ^ {2}} = \frac {\pi^ {2}}{2 4}.
$$

(d) Put

$$
f (x) = \int_ {0} ^ {x} \frac {\ln (1 - t)}{t} d t, \quad 0 \leq x \leq 1.
$$

Then integration by parts yields

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {\ln x \ln^ {2} (1 - x)}{x} d x = - \int_ {0} ^ {1} f (x) \left(\frac {\ln (1 - x)}{x} - \frac {\ln x}{1 - x}\right) d x \\ = - \int_ {0} ^ {1} f (x) f ^ {\prime} (x) d x + \int_ {0} ^ {1} f (x) \frac {\ln x}{1 - x} d x \\ = - \frac {1}{2} f ^ {2} (1) + \int_ {0} ^ {1} f (x) \frac {\ln x}{1 - x} d x. \\ \end{array}
$$

Since $f(x) = -\sum_{n=1}^{\infty} \frac{x^n}{n^2}$ , by (a) and 1.5.53, we get

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {\ln x \ln^ {2} (1 - x)}{x} d x = - \frac {1}{2} f ^ {2} (1) - \int_ {0} ^ {1} \left(\sum_ {n = 1} ^ {\infty} \frac {x ^ {n}}{n ^ {2}}\right) \left(\sum_ {n = 0} ^ {\infty} x ^ {n}\right) \ln x d x \\ = - \frac {1}{2} \zeta^ {2} (2) - \int_ {0} ^ {1} \sum_ {n = 1} ^ {\infty} \left(1 + \dots + \frac {1}{n ^ {2}}\right) x ^ {n} \ln x d x \\ = - \frac {1}{2} \zeta^ {2} (2) - \sum_ {n = 1} ^ {\infty} \left(1 + \dots + \frac {1}{n ^ {2}}\right) \int_ {0} ^ {1} x ^ {n} \ln x d x \\ = - \frac {1}{2} \zeta^ {2} (2) + \sum_ {n = 1} ^ {\infty} \left(1 + \frac {1}{2 ^ {2}} + \dots + \frac {1}{n ^ {2}}\right) \frac {1}{(n + 1) ^ {2}}. \\ \end{array}
$$

We now observe that

$$
\sum_ {n = 1} ^ {\infty} \left(1 + \frac {1}{2 ^ {2}} + \dots + \frac {1}{n ^ {2}}\right) \frac {1}{(n + 1) ^ {2}} = \sum_ {1 \leq m <   n} ^ {\infty} \frac {1}{m ^ {2} n ^ {2}} = \frac {1}{2} (\zeta^ {2} (2) - \zeta (4)).
$$

Since $\zeta(4) = \frac{\pi^4}{90}$ (for an elementary proof of this equality, see, e.g., I, 3.1.28(b)), we get

$$
\int_ {0} ^ {1} \frac {\ln x \ln^ {2} (1 - x)}{x} d x = - \frac {\pi^ {4}}{1 8 0}.
$$

1.5.60. (a) Using the result in 1.5.53, we get

$$
\begin{array}{l} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \left(\frac {1}{4 n + 1} + \frac {1}{4 n + 3}\right) = \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} \int_ {0} ^ {1} \left(x ^ {4 n} + x ^ {4 n + 2}\right) d x \\ = \int_ {0} ^ {1} \sum_ {n = 0} ^ {\infty} (- 1) ^ {n} x ^ {4 n} (1 + x ^ {2}) d x \\ = \int_ {0} ^ {1} \frac {1 + x ^ {2}}{1 + x ^ {4}} d x = \frac {\pi \sqrt {2}}{4}. \\ \end{array}
$$

(b) As in (a), we have

$$
\begin{array}{l} 1 + \sum_ {n = 1} ^ {\infty} \left(\frac {1}{8 n + 1} - \frac {1}{8 n - 1}\right) = 1 + \sum_ {n = 1} ^ {\infty} \int_ {0.} ^ {1} \left(x ^ {8 n} - x ^ {8 n - 2}\right) d x \\ = 1 + \int_ {0} ^ {1} \sum_ {n = 1} ^ {\infty} \left(x ^ {8 n} - x ^ {8 n - 2}\right) d x \\ = 1 - \int_ {0} ^ {1} \frac {x ^ {6}}{(1 + x ^ {2}) (1 + x ^ {4})} d x \\ = \frac {\pi}{4} \cdot \frac {1 + \sqrt {2}}{2}. \\ \end{array}
$$

1.5.61. (a) By the result in 1.5.1(c) with $\alpha = 2k$ and $n = 2$ , we get

$$
\begin{array}{l} \sum_ {k = 0} ^ {\infty} \frac {1}{(2 k + 1) (2 k + 2) (2 k + 3)} = \frac {1}{2 !} \sum_ {k = 0} ^ {\infty} \int_ {0} ^ {1} x ^ {2} (1 - x) ^ {2 k} d x \\ = \frac {1}{2} \int_ {0} ^ {1} x ^ {2} \sum_ {k = 0} ^ {\infty} (1 - x) ^ {2 k} d x \\ = \frac {1}{2} \int_ {0} ^ {1} \frac {x}{2 - x} d x = \ln 2 - \frac {1}{2}. \\ \end{array}
$$

(b) Likewise,

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{2 n (2 n + 1) (2 n + 2)} = \frac {3}{4} - \ln 2.
$$

1.5.62. For $x \in (0, 1]$ ,

$$
x ^ {- x} = e ^ {- x \ln x} = 1 + \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} \frac {x ^ {n} \ln^ {n} x}{n !}.
$$

The series converges uniformly on $(0,1]$ , because $\sup \{|x\ln x|:x\in (0,1]\} = 1 / e$ and the series $\sum_{n = 1}^{\infty}\frac{(1 / c)^n}{n!}$ converges. Thus

$$
\int_ {0} ^ {1} x ^ {- x} d x = 1 + \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {n}}{n !} \int_ {0} ^ {1} x ^ {n} \ln^ {n} x d x = 1 + \sum_ {n = 1} ^ {\infty} \frac {1}{(n + 1) ^ {n + 1}},
$$

where the last equality follows from 1.5.1(f).

1.5.63. For $x \geq 0$ ,

$$
\frac {x e ^ {- x}}{1 + e ^ {- x}} = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n - 1} x e ^ {- n x},
$$

and by the test given in II, 3.2.9, the series converges uniformly on $[0,\infty)$ . Moreover, if $S_{n}(x)$ denotes the $n$ th partial sum of the series, we have

$$
\left| S _ {n} (x) \right| \leq \sum_ {n = 1} ^ {\infty} x e ^ {- n x} = \frac {x e ^ {- x}}{1 - e ^ {- x}}
$$

and $\int_0^\infty \frac{x e^{-x}}{1 - e^{-x}} dx < +\infty$ . Consequently, $\int_0^\infty S_n(x)dx$ converges uniformly on $\mathbb{N}$ (see 1.5.35). Thus integration term by term yields

$$
\begin{array}{l} \int_ {0} ^ {\infty} \frac {x e ^ {- x}}{1 + e ^ {- x}} d x = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n - 1} \int_ {0} ^ {\infty} x e ^ {- n x} d x. \\ = \sum_ {n = 1} ^ {\infty} (- 1) ^ {n - 1} \frac {1}{n ^ {2}} = \frac {\pi^ {2}}{1 2}, \\ \end{array}
$$

where the last equality follows from I, 3.1.27 and I, 3.1.28(a).

1.5.64. It is clear that $B(a, b)$ is finite for all positive $a$ and $b$ . To show the first equality, we substitute $x = y / (1 + y)$ and get

$$
B (a, b) = \int_ {0} ^ {1} x ^ {a - 1} (1 - x) ^ {b - 1} d x = \int_ {0} ^ {\infty} \frac {y ^ {a - 1}}{(1 + y) ^ {a + b}} d y.
$$

Hence

$$
B (a, 1 - a) = \int_ {0} ^ {\infty} \frac {y ^ {a - 1}}{1 + y} d y.
$$

The other equality follows from 1.5.57.

1.5.65. We substitute $x = ty, t > 0$ , in

$$
\Gamma (a) = \int_ {0} ^ {\infty} x _ {1} ^ {a - 1} e ^ {- x} d x,
$$

and get

$$
\frac {\Gamma (a)}{t ^ {a}} = \int_ {0} ^ {\infty} y ^ {a - 1} e ^ {- t y} d y.
$$

Hence

$$
\frac {\Gamma (a + b)}{(1 + t) ^ {a + b}} = \int_ {0} ^ {\infty} y ^ {a + b - 1} e ^ {- (1 + t) y} d y.
$$

Multiplying both sides of this equality by $t^{a - 1}$ and integrating with respect to $t$ , we obtain

$$
\Gamma (a + b) \int_ {0} ^ {\infty} \frac {t ^ {a - 1}}{(1 + t) ^ {a + b}} d t = \int_ {0} ^ {\infty} t ^ {a - 1} \left(\int_ {0} ^ {\infty} y ^ {a + b - 1} e ^ {- (1 + t) y} d y\right) d t.
$$

It easy to see that the assumptions of 1.5.50 are satisfied, and therefore

$$
\begin{array}{l} \Gamma (a + b) \int_ {0} ^ {\infty} \frac {t ^ {a - 1}}{(1 + t) ^ {a + b}} d t = \int_ {0} ^ {\infty} y ^ {a + b - 1} e ^ {- y} \left(\int_ {0} ^ {\infty} t ^ {a - 1} e ^ {- t y} d t\right) d y \\ = \int_ {0} ^ {\infty} y ^ {a + b - 1} e ^ {- y} \frac {\Gamma (a)}{y ^ {a}} d y \\ = \Gamma (a) \int_ {0} ^ {\infty} y ^ {b - 1} e ^ {- y} d y \\ = \Gamma (a) \Gamma (b). \\ \end{array}
$$

If we put $b = 1 - a, 0 < a < 1$ , we get

$$
\Gamma (a) \Gamma (1 - a) = B (a, 1 - a) = \frac {\pi}{\sin a \pi},
$$

where the last equality follows from the previous problem.

1.5.66. We first show that for $a > 0$ ,

$$
\Gamma (a + 1) = a \Gamma (a).
$$

Indeed, integration by parts gives

$$
\Gamma (a + 1) = \int_ {0} ^ {\infty} x ^ {a} e ^ {- x} d x = - x ^ {a} e ^ {- x} \left| _ {0} ^ {\infty} + a \int_ {0} ^ {\infty} x ^ {a - 1} e ^ {- x} d x = a \Gamma (a). \right.
$$

Thus, since $\Gamma$ is continuous on $(0,\infty)$ ,

$$
\lim  _ {a \rightarrow 0 ^ {+}} a \Gamma (a) = \lim  _ {a \rightarrow 0 ^ {+}} \Gamma (a + 1) = \Gamma (1) = 1.
$$

1.5.67. It follows from the previous problem that the improper integral $\int_0^1\ln \Gamma (u)du = I$ converges. Moreover,

$$
\int_ {0} ^ {1} \ln \Gamma (a) d a = \int_ {0} ^ {1} \ln \Gamma (1 - a) d a.
$$

Consequently,

$$
\begin{array}{l} 2 I = \int_ {0} ^ {1} \ln (\Gamma (a) \Gamma (1 - a)) d a = \int_ {0} ^ {1} \ln \frac {\pi}{\sin \pi a} d a \\ = \ln \pi - \int_ {0} ^ {1} \ln (\sin \pi a) d a = \ln \pi - \frac {1}{\pi} \int_ {0} ^ {\pi} \ln (\sin x) d x \\ = \ln \pi - \frac {2}{\pi} \int_ {0} ^ {\pi / 2} \ln (\sin x) d x \\ = \ln 2 \pi , \\ \end{array}
$$

where the last equality follows from 1.5.1(b).

1.5.68. We first show that

$$
B (a, a) = \frac {1}{2 ^ {2 a - 1}} B (1 / 2, a).
$$

Indeed,

$$
\begin{array}{l} B (a, a) = \int_ {0} ^ {1} x ^ {a - 1} (1 - x) ^ {a - 1} d x = \int_ {0} ^ {1} \left(\frac {1}{4} - \left(\frac {1}{2} - x\right) ^ {2}\right) ^ {a - 1} d x \\ = 2 \int_ {0} ^ {1 / 2} \left(\frac {1}{4} - \left(\frac {1}{2} - x\right) ^ {2}\right) ^ {\alpha - 1} d x. \\ \end{array}
$$

Substituting $t = 4(1/2 - x)^2$ gives

$$
B (a, a) = \frac {1}{2 ^ {2 a - 1}} \int_ {0} ^ {1} t ^ {- 1 / 2} (1 - t) ^ {a - 1} d t = \frac {1}{2 ^ {2 a - 1}} B (1 / 2, a).
$$

This together with the result in 1.5.65 implies that

$$
\frac {\Gamma (a)}{\Gamma (2 a)} = \frac {1}{2 ^ {2 a - 1}} \frac {\Gamma (1 / 2)}{\Gamma (a + 1 / 2)} = \frac {1}{2 ^ {2 a - 1}} \frac {\sqrt {\pi}}{\Gamma (a + 1 / 2)}.
$$

1.5.69. (a) Substituting $y = \sin x$ , we get

$$
\begin{array}{l} \int_ {0} ^ {\pi / 2} \tan^ {a} x d x = \int_ {0} ^ {1} y ^ {a} (1 \quad y ^ {2}) ^ {- \frac {a}{2} - \frac {1}{2}} d y = \frac {1}{2} \int_ {0} ^ {1} t ^ {\frac {a}{2} - \frac {1}{2}} (1 \quad t) ^ {- \frac {a}{2} - \frac {1}{2}} d t \\ = \frac {1}{2} B \left(\frac {a}{2} + \frac {1}{2}, - \frac {a}{2} + \frac {1}{2}\right) = \frac {\pi}{2 \cos (\pi a / 2)}, \\ \end{array}
$$

where the last equality follows from 1.5.64.

(b) Since

$$
\int_ {0} ^ {\pi} \frac {d x}{\sqrt {3 - \cos x}} = \frac {1}{\sqrt {2}} \int_ {0} ^ {\pi} \frac {d x}{\sqrt {1 + \sin^ {2} (x / 2)}},
$$

the substitution $y = \sin (x / 2)$ yields

$$
\begin{array}{l} \int_ {0} ^ {\pi} \frac {d x}{\sqrt {3 - \cos x}} = \sqrt {2} \int_ {0} ^ {1} \frac {d y}{\sqrt {1 - y ^ {4}}} = \frac {\sqrt {2}}{4} \int_ {0} ^ {1} t ^ {- 3 / 4} (1 - t) ^ {- 1 / 2} d t \\ = \frac {\sqrt {2}}{4} B (1 / 4, 1 / 2) = \frac {\sqrt {2}}{4} \frac {\Gamma (1 / 4) \Gamma (1 / 2)}{\Gamma (3 / 4)}. \\ \end{array}
$$

Now using the identity $\Gamma(a)\Gamma(1 - a) = \frac{\pi}{\sin \pi a}, 0 < a < 1$ , we see that $\Gamma(1/2) = \sqrt{\pi}$ and $\Gamma(3/4) = \sqrt{2\pi} / (\Gamma(1/4))$ , which gives the desired equality.

(c) As in (a), we get

$$
\begin{array}{l} \int_ {0} ^ {\pi / 2} \sin^ {a - 1} x d x = \frac {1}{2} \int_ {0} ^ {1} t ^ {a / 2 - 1} (1 - t) ^ {- 1 / 2} d t \\ = \frac {1}{2} B (a / 2, 1 / 2) = 2 ^ {a - 2} B (a / 2, a / 2), \\ \end{array}
$$

where the last equality follows from the duplication formula.

1.5.70. There are many proofs of this formula. Here we present a proof due to W. Feller [Amer. Math. Monthly, 74(1967), 1223-1225]. Put

$$
A _ {n} = \ln n! - (n + 1 / 2) \ln n + n. \tag {1}
$$

Our aim is to show that

$$
\lim  _ {n \rightarrow \infty} A _ {n} = \ln \sqrt {2 \pi}.
$$

Let

$$
\begin{array}{l} a _ {k} = \frac {1}{2} \ln k - \int_ {k - 1 / 2} ^ {k} \ln x d x = \int_ {k - 1 / 2} ^ {k} \ln (k / x) d x, \\ b _ {k} = \int_ {k} ^ {k + 1 / 2} \ln x d x - \frac {1}{2} \ln k = \int_ {k} ^ {k + 1 / 2} \ln (x / k) d x. \\ \end{array}
$$

Then

$$
a _ {k} - b _ {k} = 1 + \ln k + \left(k - \frac {1}{2}\right) \ln \left(k - \frac {1}{2}\right) - \left(k + \frac {1}{2}\right) \ln \left(k + \frac {1}{2}\right).
$$

Consequently,

$$
\sum_ {k = 1} ^ {n} \left(a _ {k} - b _ {k}\right) = n + \ln n! + \frac {1}{2} \ln \frac {1}{2} - \left(n + \frac {1}{2}\right) \ln \left(n + \frac {1}{2}\right) = B _ {n}.
$$

Now we show that the series $\sum_{k=1}^{\infty}\left(a_k - b_k\right)$ converges. Since

$$
a _ {k} = \int_ {0} ^ {1 / 2} \ln \frac {1}{1 - t / k} d t \quad \text {a n d} \quad b _ {k} = \int_ {0} ^ {1 / 2} \ln (1 + t / k) d t, \tag {3}
$$

we see that $a_{k} > b_{k} > a_{k + 1} > 0$ . Moreover, $\lim_{k\to \infty}a_k = \lim_{k\to \infty}b_k = 0$ . Thus the series

$$
a _ {1} - b _ {1} + a _ {2} - b _ {2} + \dots + a _ {n} - b _ {n} + \dots
$$

converges by the Leibniz test. This means that $\lim_{n\to \infty}B_n$ exists and is equal to the sum of the series $\sum_{k = 1}^{\infty}(a_k - b_k)$ . It follows from (3) that

$$
a _ {k} - b _ {k} = - \int_ {0} ^ {1 / 2} \ln \left(1 - \frac {t ^ {2}}{k ^ {2}}\right) d t.
$$

Thus

$$
\sum_ {k = 1} ^ {\infty} \left(a _ {k} - b _ {k}\right) = - \int_ {0} ^ {1 / 2} \sum_ {k = 1} ^ {\infty} \ln \left(1 - \frac {t ^ {2}}{k ^ {2}}\right) d t,
$$

because the series on the right-hand side converges uniformly on $[0,1/2]$ . So,

$$
\begin{array}{l} \sum_ {k = 1} ^ {\infty} \left(a _ {k} - b _ {k}\right) = - \int_ {0} ^ {1 / 2} \ln \prod_ {k = 1} ^ {\infty} \left(1 - \frac {t ^ {2}}{k ^ {2}}\right) d t \\ = - \int_ {0} ^ {1 / 2} \ln \frac {\sin \pi t}{\pi t} d t, \\ \end{array}
$$

where the last equality follows from, e.g., I, 3.8.37. Using the result in 1.5.1(b), we get

$$
- \int_ {0} ^ {1 / 2} \ln \frac {\sin \pi t}{\pi t} d t = \frac {1}{2} (\ln \pi - 1).
$$

By (1) and (2),

$$
\lim  _ {n \rightarrow \infty} (A _ {n} - B _ {n}) = \lim  _ {n \rightarrow \infty} \left(n + \frac {1}{2}\right) \ln \left(1 + \frac {1}{2 n}\right) + \frac {1}{2} \ln 2 = \frac {1}{2} (1 + \ln 2).
$$

Finally, we arrive at

$$
\lim  _ {n \rightarrow \infty} A _ {n} = \lim  _ {n \rightarrow \infty} B _ {n} + \frac {1}{2} (1 + \ln 2) = \ln \sqrt {2 \pi}.
$$

1.5.71. We first note that $\Gamma$ is infinitely differentiable on $(0, \infty)$ . Indeed, the improper integral $\int_{0}^{\infty} x^{a - 1} \ln xe^{-x} dx$ converges uniformly on each interval $[c, d]$ , $0 < c < d$ , because each of the integrals

$$
\int_ {0} ^ {1} x ^ {a - 1} \ln x e ^ {- x} d x \quad \text {a n d} \quad \int_ {1} ^ {\infty} x ^ {a - 1} \ln x e ^ {- x} d x
$$

converges uniformly on $[c,d]$ . So, applying 1.5.44, we see that

$$
\Gamma^ {\prime} (a) = \int_ {0} ^ {\infty} x ^ {a - 1} \ln x e ^ {- x} d x.
$$

The formula

$$
\Gamma^ {(n)} (a) = \int_ {0} ^ {\infty} x ^ {a - 1} \ln^ {n} x e ^ {- x} d x
$$

can be obtained inductively. Now, by 1.5.65,

$$
\begin{array}{l} \Gamma (b) - B (a, b) = \Gamma (\dot {b}) - \frac {\Gamma (a) \Gamma (b)}{\Gamma (a + b)} = \frac {\Gamma (b) b}{\Gamma (a + b)} \cdot \frac {\Gamma (a + b) - \Gamma (a)}{b} \\ = \frac {\Gamma (b + 1)}{\Gamma (a + b)} \cdot \frac {\Gamma (a + b) - \Gamma (a)}{b}. \\ \end{array}
$$

Letting $b \to 0^{+}$ we get

$$
\frac {\Gamma^ {\prime} (a)}{\Gamma (a)} = \lim  _ {b \rightarrow 0 ^ {+}} (\Gamma (b) - B (a, b)).
$$

Since (see the solution of 1.5.65)

$$
B (a, b) = \int_ {0} ^ {\infty} \frac {x ^ {b - 1}}{(1 + x) ^ {a + b}} d x,
$$

we obtain

$$
\frac {\Gamma^ {\prime} (a)}{\Gamma (a)} - \lim  _ {b \rightarrow 0 ^ {+}} \int_ {0} ^ {\infty} x ^ {b - 1} \left(c ^ {- x} - \frac {1}{(1 + x) ^ {a + b}}\right) d x. \tag {1}
$$

Moreover, the improper integrals

$$
\int_ {0} ^ {1} x ^ {b - 1} \left(e ^ {- x} - \frac {1}{(1 + x) ^ {a + b}}\right) d x, \quad \int_ {1} ^ {\infty} x ^ {b - 1} \left(e ^ {- x} - \frac {1}{(1 + x) ^ {a + b}}\right) d x
$$

converge uniformly on $[0, b_0]$ . Thus the result in 1.5.43 can be applied, and we can switch the limit and the integral in (1). This completes the proof.

1.5.72. (a) We first show that the function

$$
F (x) = \frac {\sqrt {x} \Gamma (x + 1 / 2)}{\Gamma (x + 1)}
$$

is monotonically increasing for $x > 1$ . To this end, observe that

$$
\left(\ln F (x)\right) ^ {\prime} = \frac {1}{2 x} + \frac {\Gamma^ {\prime} \left(x + \frac {1}{2}\right)}{\Gamma \left(x + \frac {1}{2}\right)} - \frac {\Gamma^ {\prime} (x + 1)}{\Gamma (x + 1)}.
$$

By the preceding problem,

$$
\begin{array}{l} \frac {\Gamma^ {\prime} (x + 1)}{\Gamma (x + 1)} - \frac {\Gamma^ {\prime} \left(x + \frac {1}{2}\right)}{\Gamma \left(x + \frac {1}{2}\right)} = \int_ {0} ^ {\infty} \frac {1}{(1 + t) ^ {x + 1}} \frac {\sqrt {1 + t} - 1}{t} d t \\ = \int_ {0} ^ {\infty} \frac {1}{(1 + t) ^ {x + 1}} \frac {1}{\sqrt {1 + t} + 1} d t \\ <   \frac {1}{2} \int_ {0} ^ {\infty} \frac {1}{(1 + t) ^ {x + 1}} d t \\ = \frac {1}{2 x}, \\ \end{array}
$$

which shows that $(\ln F(x))' > 0$ . Consequently, $F$ increases on $(1,\infty)$ . So $\lim_{x\to \infty}F(x) = \lim_{n\to \infty}F(n)$ . To find this limit, we will use the duplication formula and the Stirling formula given in 1.5.68 and 1.5.70, respectively. Hence

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} F (n) = \lim  _ {n \rightarrow \infty} \frac {\sqrt {n} \Gamma (n + 1 / 2)}{\Gamma (n + 1)} = \lim  _ {n \rightarrow \infty} \frac {\sqrt {n} \Gamma (2 n) \sqrt {\pi}}{\Gamma (n) \Gamma (n + 1) 2 ^ {2 n - 1}} \\ = \lim  _ {n \rightarrow \infty} \frac {\sqrt {n \pi} (2 n - 1) !}{(n - 1) ! n ! 2 ^ {2 n - 1}} \\ = \lim  _ {n \rightarrow \infty} \beta_ {n} \frac {\sqrt {n} (2 n - 1) ^ {2 n - 1 / 2} e ^ {- (2 n - 1)}}{\sqrt {2} n (2 n - 2) ^ {2 n - 1} e ^ {- (2 n - 2)}} = 1, \\ \end{array}
$$

where $\{\beta_n\}$ is a sequence converging to 1.

(b) Note first that if $a = 1$ , then by 1.5.65,

$$
x ^ {a} B (a, x) = x B (1, x) = \frac {x \Gamma (1) \Gamma (x)}{\Gamma (x + 1)} = 1
$$

for all $x > 0$ . So, in this case, the limit to be found is 1. We will show that the function $F_{a}(x) = x^{a}B(a,x), x > 0$ , is monotonically

increasing if $a > 1$ , and monotonically decreasing if $0 < a < 1$ . We have

$$
\begin{array}{l} \left(\ln F _ {a} (x)\right) ^ {\prime} = \frac {a}{x} + \frac {\Gamma^ {\prime} (x)}{\Gamma (x)} - \frac {\Gamma^ {\prime} (x + a)}{\Gamma (x + a)} \\ = \frac {a}{x} - \int_ {0} ^ {\infty} \left(\frac {1}{(1 + t) ^ {x}} - \frac {1}{(1 + t) ^ {a + x}}\right) \frac {d t}{t}. \\ \end{array}
$$

If $a > 1$ , then

$$
\begin{array}{l} \int_ {0} ^ {\infty} \left(\frac {1}{(1 + t) ^ {x}} - \frac {1}{(1 + t) ^ {a + x}}\right) \frac {d t}{t} = \int_ {0} ^ {\infty} \frac {1 + t - (1 + t) ^ {1 - a}}{(1 + t) ^ {x + 1}} \frac {d t}{t} \\ <   a \int_ {0} ^ {\infty} \frac {1}{(1 + t) ^ {x + 1}} d t = \frac {a}{x}, \\ \end{array}
$$

where the last inequality follows from the inequality $(1 + t)^{1 - a} > 1 + (1 - a)t$ (see II, 2.3.7(a)). This shows that $(\ln F_{a}(x))' > 0$ , which means that $F_{a}$ is increasing. Similarly, if $0 < a < 1$ , then the inequality $(1 + t)^{1 - a} < 1 + (1 - a)t$ (see II, 2.3.7(b)) implies that $F_{a}$ is decreasing. Consequently, to find the desired limit it is enough to calculate $\lim_{n\to \infty}F_n(n)$ . We get

$$
\begin{array}{l} \lim  _ {n \rightarrow \infty} n ^ {a} B (a, n) = \lim  _ {n \rightarrow \infty} \frac {n ^ {a} \Gamma (a) \Gamma (n)}{\Gamma (a + n)} \\ = \lim  _ {n \rightarrow \infty} \frac {n ^ {a} \Gamma (a) (n - 1) !}{(a + n - 1) (a + n - 2) . . . (a + 1) a \Gamma (a)} \\ = \lim  _ {n \rightarrow \infty} \frac {n ^ {a - 1} n !}{(a + n - 1) (a + n - 2) \dots (a + 1) a} = \Gamma (a), \\ \end{array}
$$

where the last equality follows from 1.5.31.

# 1.6. Integral Inequalities

1.6.1. It is clear that

$$
\int_ {a} ^ {b} \left(\int_ {a} ^ {b} (f (x) g (y) - f (y) g (x)) ^ {2} d x\right) d y \geq 0.
$$

Hence

$$
2 \int_ {a} ^ {b} f ^ {2} (x) d x \int_ {a} ^ {b} g ^ {2} (x) d x - 2 \left(\int_ {a} ^ {b} f (x) g (x) d x\right) ^ {2} \geq 0,
$$

which gives the desired inequality. Now, if $f$ and $g$ are continuous on $[a, b]$ and the equality holds, then

$$
\int_ {a} ^ {b} (f (x) g (y) - f (y) g (x)) ^ {2} d x = 0
$$

for every $y \in [a, b]$ . Consequently, $f(x)g(y) - f(y)g(x) = 0$ for every $x \in [a, b]$ and $y \in [a, b]$ . So if there is a $y_0 \in [a, b]$ such that $g(y_0) \neq 0$ , then $f(x) = \frac{f(y_0)}{g(y_0)} g(x)$ . If $g$ is identically zero on $[a, b]$ , then we can take $\lambda_1 = 0$ and $\lambda_2 = 1$ .

1.6.2. It is an immediate consequence of the Schwarz inequality.

1.6.3. By the Schwarz inequality,

$$
(b - a) ^ {2} = \left(\int_ {a} ^ {b} \sqrt {f (x)} \sqrt {\frac {1}{f (x)}} d x\right) ^ {2} \leq \int_ {a} ^ {b} f (x) d x \int_ {a} ^ {b} \frac {d x}{f (x)}.
$$

Moreover, since

$$
\frac {(f (x) - m) (f (x) - M)}{f (x)} \leq 0 \quad \text {f o r} \quad a \leq x \leq b,
$$

we get

$$
\int_ {a} ^ {b} \frac {(f (x) - m) (f (x) - M)}{f (x)} d x \leq 0,
$$

which gives

$$
\int_ {a} ^ {b} f (x) d x + m M \int_ {a} ^ {b} \frac {d x}{f (x)} \leq (m + M) (b - a).
$$

Hence

$$
\begin{array}{l} m M \int_ {a} ^ {b} \frac {d x}{f (x)} \int_ {a} ^ {b} f (x) d x \\ \leq (m + M) (b - a) \int_ {a} ^ {b} f (x) d x - \left(\int_ {a} ^ {b} f (x) d x\right) ^ {2} \\ \leq \frac {(m + M) ^ {2} (b - a) ^ {2}}{4}. \\ \end{array}
$$

The last inequality follows from the fact that the function $x \mapsto -x^2 + \alpha x$ attains its maximum $\alpha^2 / 4$ at $x = \alpha / 2$ .

1.6.4. The substitution $t = (x - a) / (b - a)$ shows that it is enough to consider the case $a - 0, b - 1$ . For convenience, put

$$
F = \int_ {0} ^ {1} f (x) d x, \quad G = \int_ {0} ^ {1} g (x) d x
$$

and

$$
D (f, g) = \int_ {0} ^ {1} f (x) g (x) d x - F G.
$$

By the Schwarz inequality,

$$
D (f, f) = \int_ {0} ^ {1} f ^ {2} (x) d x - \left(\int_ {0} ^ {1} f (x) d x\right) ^ {2} \geq 0.
$$

On the other hand,

$$
D (f, f) = \left(M _ {1} - F\right) \left(F - m _ {1}\right) - \int_ {0} ^ {1} \left(M _ {1} - f (x)\right) \left(f (x) - m _ {1}\right) d x,
$$

which implies that

$$
D (f, f) \leq (M _ {1} - F) (F - m _ {1}).
$$

Clearly,

$$
D (\dot {f}, g) = \int_ {0} ^ {1} (f (x) - F) (g (x) - G) d x,
$$

and by the Schwarz inequality,

$$
(D (f, g)) ^ {2} \leq \int_ {0} ^ {1} (f (x) - F) ^ {2} d x \int_ {0} ^ {1} (g (x) - G) ^ {2} d x = D (f, f) D (g, g).
$$

It then follows that

$$
\begin{array}{l} (D (f, g)) ^ {2} \leq (M _ {1} - F) (F - m _ {1}) (M _ {2} - G) (G - m _ {2}) \\ \leq \frac {\left(M _ {1} - m _ {1}\right) ^ {2}}{4} \cdot \frac {\left(M _ {2} - m _ {2}\right) ^ {2}}{4}. \\ \end{array}
$$

1.6.5. We have

$$
\begin{array}{l} \int_ {a} ^ {b} x f (x) f ^ {\prime} (x) d x = \frac {1}{2} \int_ {a} ^ {b} x \left(f ^ {2} (x)\right) ^ {\prime} d x \\ = \frac {1}{2} \left(x f ^ {2} (x) \mid_ {a} ^ {b} - \int_ {a} ^ {b} f ^ {2} (x) d x\right) = - \frac {1}{2}, \\ \end{array}
$$

and therefore by the Schwarz inequality,

$$
\frac {1}{4} \leq \int_ {a} ^ {b} (f ^ {\prime} (x)) ^ {2} d x \int_ {a} ^ {b} x ^ {2} f ^ {2} (x) d x.
$$

1.6.6. By the Schwarz inequality,

$$
\begin{array}{l} 1 = \left| \int_ {0} ^ {1} f (x) d x \right| = \left| \int_ {0} ^ {1} f (x) \frac {\sqrt {1 + x ^ {2}}}{\sqrt {1 + x ^ {2}}} d x \right| \\ \leq \left(\int_ {0} ^ {1} (1 + x ^ {2}) f ^ {2} (x) d x\right) ^ {1 / 2} \left(\int_ {0} ^ {1} \frac {1}{1 + x ^ {2}} d x\right) ^ {1 / 2} \\ = \left(\int_ {0} ^ {1} (1 + x ^ {2}) f ^ {2} (x) d x\right) ^ {1 / 2} \frac {\sqrt {\pi}}{2}. \\ \end{array}
$$

Hence

$$
\inf  _ {f \in A} \int_ {0} ^ {1} (1 + x ^ {2}) f ^ {2} (x) d x \geq \frac {4}{\pi}.
$$

The infimum is equal to $4 / \pi$ and is attained for $f(x) = \frac{4}{\pi(1 + x^2)}$ .

1.6.7. The inequality follows from

$$
\int_ {a} ^ {b} (M - f (x)) (f (x) - m) d x \geq 0.
$$

1.6.8. Set

$$
F (t) = \left(\int_ {0} ^ {t} f (x) d x\right) ^ {2} - \int_ {0} ^ {t} (f (x)) ^ {3} d x, \quad t \in [ 0, 1 ].
$$

Then

$$
F ^ {\prime} (t) = f (t) \left(2 \int_ {0} ^ {t} f (x) d x - (f (t)) ^ {2}\right),
$$

and, if $G(t) = 2\int_{0}^{t} f(x) dx - (f(t))^{2}$ , then $G'(t) = 2f(t)(1 - f'(t)) \geq 0$ . Consequently, $G(t) \geq G(0) = 0$ , which gives $F'(t) \geq 0$ . So, $F(t) \geq 0$ and, in particular, $F(1) \geq 0$ .

Moreover, if $F(1) = 0$ , then $F(t) = 0$ for $t \in [0,1]$ , and therefore $F'(t) = f(t)G(t) = 0$ . This in turn, implies $G'(t) = 2f(t)(1 - f'(t)) = 0$ and $1 - f'(t) = 0$ for $t \in (0,1)$ .

1.6.9. It follows from the solution of 1.2.22 that the function

$$
g (x) = \frac {1}{x - a} \int_ {a} ^ {x} f (t) d t
$$

is monotonically increasing on $(a, b]$ . Thus $g(x) \leq g(b)$ . As in the solution of 1.2.22, one can show that the function

$$
h (x) = \frac {1}{b - x} \int_ {x} ^ {b} f (t) d t
$$

is monotonically increasing on $[a,b)$ , and therefore $h(a) \leq h(x)$ .

1.6.10. Assume first that both the functions are monotone in the same sense. We have

$$
\begin{array}{l} \int_ {a} ^ {b} \left(\int_ {a} ^ {b} (f (x) g (x) - f (x) g (y)) d x\right) d y \\ = (b - a) \int_ {a} ^ {b} f (x) g (x) d x - \int_ {a} ^ {b} f (x) d x \int_ {a} ^ {b} g (x) d x \\ \end{array}
$$

and

$$
\begin{array}{l} \int_ {a} ^ {b} \left(\int_ {a} ^ {b} (f (y) g (y) - f (y) g (x)) d x\right) d y \\ = (b - a) \int_ {a} ^ {b} f (x) g (x) d x - \int_ {a} ^ {b} f (x) d x \int_ {a} ^ {b} g (x) d x. \\ \end{array}
$$

Therefore

$$
\begin{array}{l} (b - a) \int_ {a} ^ {b} f (x) g (x) d x - \int_ {a} ^ {b} f (x) d x \int_ {a} ^ {b} g (x) d x \\ = \frac {1}{2} \int_ {a} ^ {b} \left(\int_ {a} ^ {b} (f (x) - f (y)) (g (x) - g (y)) d x\right) d y \geq 0, \\ \end{array}
$$

because, by assumption, $(f(x) - f(y))(g(x) - g(y)) \geq 0$ for all $x$ and $y$ in $[a, b]$ .

1.6.11. The proof is analogous to that of 1.6.10.

1.6.12. By the Chebyshev inequality (see 1.6.10),

$$
\begin{array}{l} \int_ {0} ^ {a} f (a - x) g (x) d x \leq \frac {1}{a} \int_ {0} ^ {a} f (a - x) d x \int_ {0} ^ {a} g (x) d x \\ = \frac {1}{a} \int_ {0} ^ {a} f (x) d x \int_ {0} ^ {a} g (x) d x \\ \leq \int_ {0} ^ {a} f (x) g (x) d x. \\ \end{array}
$$

1.6.13. It is enough to apply the generalized Chebyshev inequality (see 1.6.11) with $p(x) = q^2(x)$ , $f(x) = x$ and $g(x) = 1/(q(x))$ .

1.6.14. By the convexity of $f$ , we get

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d x = (b - a) \int_ {0} ^ {1} f ((1 - x) a + x b) d x \\ \leq (\dot {b} - a) \int_ {0} ^ {1} ((1 - x) f (a) + x f (b)) d x \\ = \frac {f (a) + f (b)}{2} (b - a). \\ \end{array}
$$

To prove the other inequality we substitute $x = (a + b) / 2 + t$ , and get

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d x = \int_ {- (b - a) / 2} ^ {(b - a) / 2} f \left(\frac {a + b}{2} + t\right) d t \\ = \int_ {0} ^ {(b - a) / 2} \left(f \left(\frac {a + b}{2} + t\right) + f \left(\frac {a + b}{2} - t\right)\right) d t \\ \geq \int_ {0} ^ {(b - a) / 2} 2 f \left(\frac {a + b}{2}\right) d t = (b - a) f \left(\frac {a + b}{2}\right). \\ \end{array}
$$

1.6.15. Let $f(x) = \frac{\ln x}{x}, x > 0$ . Since $f''(x) = (2\ln x - 3)/x^3$ , we see that $f$ is strictly convex on $(e^{3/2}, \infty)$ and strictly concave on $(0, e^{3/2})$ . Hence if $y > x \geq e^{3/2}$ , we have

$$
\frac {\ln A}{A} = f \left(\frac {x + y}{2}\right) <   \frac {1}{y - x} \int_ {x} ^ {y} \frac {\ln t}{t} d t = \frac {\ln^ {2} y - \ln^ {2} x}{2 (y - x)} = \frac {\ln G}{L},
$$

which gives $A^L < G^A$ . Analogous reasoning can be used to show that $A^L > G^A$ if $0 < x < y \leq e^{3/2}$ .

1.6.16. Let $c \in [a, b]$ be such that $f(c) = \max_{x \in [a, b]} f(x)$ . Then, by assumption,

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) d x = \int_ {a} ^ {c} f (x) d x + \int_ {c} ^ {b} f (x) d x \\ = (c - a) \int_ {0} ^ {1} f ((1 - x) a + x c) d x \\ + (b - c) \int_ {0} ^ {1} f ((1 - x) c + x b) d x \\ \end{array}
$$

$$
\begin{array}{l} > (c - a) \int_ {0} ^ {1} ((1 - x) f (a) + x f (c)) d x \\ + (b - c) \int_ {0} ^ {1} ((1 - x) f (c) + x f (b)) d x \\ = (c - a) \frac {f (a) + f (c)}{2} + (b - c) \frac {f (b) + f (c)}{2} \\ > \frac {1}{2} (b - a) f (c). \\ \end{array}
$$

1.6.17. Integrating by parts yields

$$
\begin{array}{l} \int_ {0} ^ {a} g (x) f ^ {\prime} (x) d x + \int_ {0} ^ {b} g ^ {\prime} (x) f (x) d x \\ = g (x) f (x) \left| _ {0} ^ {a} - \int_ {0} ^ {a} g ^ {\prime} (x) f (x) d x + \int_ {0} ^ {b} g ^ {\prime} (x) f (x) d x \right. \\ = f (a) g (a) + \int_ {a} ^ {b} g ^ {\prime} (x) f (x) d x \\ \geq f (a) g (a) + \int_ {a} ^ {b} g ^ {\prime} (x) f (a) d x = f (a) g (b). \\ \end{array}
$$

The case of equality follows immediately from the above.

1.6.18. Substituting $u = f^{-1}(t)$ and integrating by parts gives

$$
\begin{array}{l} \int_ {0} ^ {x} f (t) d t + \int_ {0} ^ {f (x)} f ^ {- 1} (t) d t = \int_ {0} ^ {x} f (t) d t + \int_ {0} ^ {x} u f ^ {\prime} (u) d u \\ = x f (x). \\ \end{array}
$$

1.6.19. Assume first that $f(a) < b = f(x)$ . Then by 1.6.18,

$$
\begin{array}{l} \int_ {0} ^ {a} f (t) d t + \int_ {0} ^ {b} f ^ {- 1} (t) d t \\ = \int_ {0} ^ {a} f (t) d t + \int_ {0} ^ {f (a)} f ^ {- 1} (t) d t + \int_ {f (a)} ^ {b} f ^ {- 1} (t) d t \\ = a f (a) + \int_ {a} ^ {x} u f ^ {\prime} (u) d u = x f (x) - \int_ {a} ^ {x} f (u) d u \\ \geq x f (x) - (x - a) f (x) = a f (x) = a b. \\ \end{array}
$$

Similarly, if $b \leq f(a) = y$ , then

$$
\begin{array}{l} \int_ {0} ^ {a} f (t) d t + \int_ {0} ^ {b} f ^ {- 1} (t) d t \\ = \int_ {0} ^ {f ^ {- 1} (b)} f (t) d t + \int_ {f ^ {- 1} (b)} ^ {a} f (t) d t + \int_ {0} ^ {b} f ^ {- 1} (t) d t \\ = f ^ {- 1} (b) b + \int_ {f ^ {- 1} (b)} ^ {f ^ {- 1} (y)} f (t) d t = f ^ {- 1} (b) b + \int_ {b} ^ {y} u \left(f ^ {- 1} (u)\right) ^ {\prime} d u \\ = y f ^ {- 1} (y) - \int_ {b} ^ {y} f ^ {- 1} (u) d u \\ \geq y f ^ {- 1} (y) - (y - b) f ^ {- 1} (y) = b f ^ {- 1} (y) = b a. \\ \end{array}
$$

1.6.20. Applying the Young inequality with $f(x) = \ln (1 + x)$ , we get

$$
\int_ {0} ^ {a} \ln (1 + x) d x + \int_ {0} ^ {b} (e ^ {x} - 1) d x \geq a b,
$$

which gives the desired inequality.

1.6.21. If there is $x_0$ such that $g^{-1}(x_0) > f(x_0)$ , then by assumption,

$$
\begin{array}{l} x _ {0} g ^ {- 1} \left(x _ {0}\right) \leq \int_ {0} ^ {x _ {0}} f (x) d x + \int_ {0} ^ {g ^ {- 1} \left(x _ {0}\right)} g (x) d x \\ <   \int_ {0} ^ {x _ {0}} g ^ {- 1} (x) d x + \int_ {0} ^ {g ^ {- 1} \left(x _ {0}\right)} g (x) d x \\ = x _ {0} g ^ {- 1} \left(x _ {0}\right), \\ \end{array}
$$

where the last equality follows from 1.6.18. A contradiction.

1.6.22. It follows from the Schwarz inequality that if $f \in A$ , then

$$
(2 + 3 b) ^ {2} = \left(\int_ {0} ^ {1} f (x) (x + b) d x\right) ^ {2} \leq \int_ {0} ^ {1} f ^ {2} (x) d x \int_ {0} ^ {1} (x + b) ^ {2} d x.
$$

Hence

$$
\int_ {0} ^ {1} f ^ {2} (x) d x \geq \frac {3 (2 + 3 b) ^ {2}}{3 b ^ {2} + 3 b + 1}.
$$

Since the last inequality holds for any real $b$ ,

$$
\int_ {0} ^ {1} f ^ {2} (x) d x \geq \max  _ {b \in \mathbb {R}} \frac {3 (2 + 3 b) ^ {2}}{3 b ^ {2} + 3 b + 1} = 1 2.
$$

The equality is attained at $f(x) = 6x$ .

1.6.23. Let $f \in A$ . Then by the Schwarz inequality,

$$
\left(\int_ {0} ^ {1} (1 - x) f ^ {\prime \prime} (x) d x\right) ^ {2} \leq \int_ {0} ^ {1} (1 - x) ^ {2} d x \int_ {0} ^ {1} \left(f ^ {\prime \prime} (x)\right) ^ {2} d x. \tag {1}
$$

Moreover,

$$
\int_ {0} ^ {1} (1 - x) f ^ {\prime \prime} (x) d x = (1 - x) f ^ {\prime} (x) \big | _ {0} ^ {1} + \int_ {0} ^ {1} f ^ {\prime} (x) d x = - a,
$$

and consequently,

$$
\int_ {0} ^ {1} (f ^ {\prime \prime} (x)) ^ {2} d x \geq 3 a ^ {2}.
$$

The equality in (1) holds if $f''(x) = \lambda (1 - x)$ with some real $\lambda$ . Since $f \in A$ , we find that $f(x) = \frac{a}{2} (x^3 - 3x^2 + 2x)$ .

1.6.24. By the mean value theorem, for $x \in (0, 2)$ ,

$$
\frac {f (x) - f (0)}{x} = \frac {f (x) - 1}{x} = f ^ {\prime} (\theta_ {1}) \geq - 1,
$$

which implies that $f(x) \geq 1 - x$ . Likewise,

$$
\frac {f (x) - f (2)}{x - 2} = \frac {f (x) - 1}{x - 2} = f ^ {\prime} (\theta_ {2}) \leq 1,
$$

which gives $f(x) \geq x - 1$ . Consequently, $f(x) \geq |x - 1|$ . Thus

$$
\int_ {0} ^ {2} f (x) d x \geq \int_ {0} ^ {2} | x - 1 | d x = 1.
$$

Since $f$ is continuous, the equality holds if and only if $f(x) = |x - 1|$ , $x \in [0,2]$ . But this function is not differentiable at $x = 1$ . So the answer to our question is no.

1.6.25. By the mean value theorem,

$$
f (x) = f ^ {\prime} \left(\theta_ {1}\right) (x - a) \quad \text {a n d} \quad f (x) = f ^ {\prime} \left(\theta_ {2}\right) (x - b).
$$

$$
\text {I f} M = \max  _ {x \in [ a, b ]} | f ^ {\prime} (x) |, \text {t h e n}
$$

$$
| f (x) | \leq M (x - a) \quad \text {a n d} \quad | f (x) | \leq M (b - x).
$$

Hence

$$
\begin{array}{l} \frac {4}{(b - a) ^ {2}} \int_ {a} ^ {b} | f (x) | d x \\ \leq \frac {4}{(b - a) ^ {2}} \int_ {a} ^ {(a + b) / 2} M (x - a) d x + \frac {4}{(b - a) ^ {2}} \int_ {(a + b) / 2} ^ {b} M (b - x) d x \\ = \frac {4}{(b - a) ^ {2}} \left(\frac {(b - a) ^ {2}}{8} M + \frac {(b - a) ^ {2}}{8} M\right) = M. \\ \end{array}
$$

1.6.26. We will apply the inequality

$$
x _ {1} ^ {\alpha_ {1}} x _ {2} ^ {\alpha_ {2}} \dots x _ {n} ^ {\alpha_ {n}} \leq \alpha_ {1} x _ {1} + \alpha_ {2} x _ {2} + \dots + \alpha_ {n} x _ {n}
$$

for $x_{i}, \alpha_{i} > 0, i = 1,2,\ldots,n$ , such that $\sum_{i=1}^{n} \alpha_{i} = 1$ (see, e.g., II, 2.4.13(b)). Assuming that no function is null, we put

$$
x _ {i} = \frac {f _ {i} (x)}{\int_ {a} ^ {b} f _ {i} (x) d x}, \quad i = 1, 2, \dots n,
$$

and get

$$
\begin{array}{l} \frac {\int_ {a} ^ {b} \prod_ {i = 1} ^ {n} f _ {i} ^ {\alpha_ {i}} (x) d x}{\prod_ {i = 1} ^ {n} \left(\int_ {a} ^ {b} f _ {i} (x) d x\right) ^ {\alpha_ {i}}} = \int_ {a} ^ {b} \prod_ {i = 1} ^ {n} \left(\frac {f _ {i} (x)}{\int_ {a} ^ {b} f _ {i} (x) d x}\right) ^ {\alpha_ {i}} \\ \leq \int_ {a} ^ {b} \left(\sum_ {i = 1} ^ {n} \frac {\alpha_ {i} f _ {i} (x)}{\int_ {a} ^ {b} f _ {i} (x) d x}\right) d x = 1. \\ \end{array}
$$

We remark that the function $x \mapsto \prod_{i=1}^{n} f_i^{\alpha_i}(x)$ is Riemann integrable on $[a, b]$ , because each of the functions $f_i^{\alpha_i}, i = 1, 2, \ldots$ , is Riemann integrable (see, e.g., Theorem 6.11 in [28]).

1.6.27. (a) It is enough to apply the Hölder inequality with $f_{1} = f^{p}$ and $f_{2} = g^{q}$ .

(b) Assume first that $0 < p < 1$ , and put $r = 1 / p > 1$ , $\frac{1}{r} + \frac{1}{s} = 1$ , and

$$
v = \frac {1}{g ^ {p}}, \quad u = \frac {f ^ {p}}{v}.
$$

Then $fg = u^r$ , $f^p = uv$ , and $g^q = v^s$ , and by (a),

$$
\begin{array}{l} \int_ {a} ^ {b} f ^ {p} (x) d x = \int_ {a} ^ {b} u (x) v (x) d x \leq \left(\int_ {a} ^ {b} u ^ {r} (x) d x\right) ^ {1 / r} \left(\int_ {a} ^ {b} v ^ {s} (x) d x\right) ^ {1 / s} \\ = \left(\int_ {a} ^ {b} f (x) g (x) d x\right) ^ {1 / r} \left(\int_ {a} ^ {b} g ^ {q} (x) d x\right) ^ {1 / a} \\ = \left(\int_ {a} ^ {b} f (x) g (x) d x\right) ^ {p} \left(\int_ {a} ^ {b} g ^ {q} (x) d x\right) ^ {1 - p}. \\ \end{array}
$$

If $p < 0$ , then $0 < q < 1$ , and the above reasoning can be used.

1.6.28. By the Hölder inequality, for $p > 1$ ,

$$
a = \int_ {0} ^ {1} f (x) ^ {\frac {1}{2 p} + 1 - \frac {1}{2 p}} d x \leq \left(\int_ {0} ^ {1} \sqrt {f (x)} d x\right) ^ {\frac {1}{p}} a ^ {\frac {2 p - 1}{3 p}},
$$

which gives

$$
a ^ {\frac {p + 1}{2}} \leq \int_ {0} ^ {1} \sqrt {f (x)} d x.
$$

Since $p > 1$ can be chosen arbitrarily, the inequality to be proved follows.

1.6.29. By the Jensen inequality (see, e.g., II, 2.4.3),

$$
\varphi \left(\sum_ {k = 1} ^ {n} \frac {1}{n} f \left(a + \frac {k (b - a)}{n}\right)\right) \leq \sum_ {k = 1} ^ {n} \frac {1}{n} \varphi \left(f \left(a + \frac {k (b - a)}{n}\right)\right).
$$

Letting $n \to \infty$ gives the desired inequality.

1.6.30. As in the previous problem, we apply the Jensen inequality and obtain

$$
\begin{array}{l} \varphi \left(\frac {\sum_ {k = 1} ^ {n} p \left(a + \frac {k (b - a)}{n}\right) f \left(a + \frac {k (b - a)}{n}\right)}{\sum_ {k = 1} ^ {n} p \left(a + \frac {k (b - a)}{n}\right)}\right) \\ \leq \frac {\sum_ {k = 1} ^ {n} p \left(a + \frac {k (b - a)}{n}\right) \varphi \left(f \left(a + \frac {k (b - a)}{n}\right)\right)}{\sum_ {k = 1} ^ {n} p \left(a + \frac {k (b - a)}{n}\right)}. \\ \end{array}
$$

Passage to the limit as $n \to \infty$ gives the desired result.

1.6.31. The function $\varphi(t) = -\sqrt{1 - t^2}$ is continuous and convex on $[-1, 1]$ . Therefore the inequality given 1.6.29 can be applied.

1.6.32. We remark first that the Schwarz inequality remains true if Riemann integrals are replaced by Riemann-Stieltjes integrals with respect to a monotone function $\alpha$ ; that is,

$$
\left(\int_ {a} ^ {b} f (x) g (x) d \alpha (x)\right) ^ {2} \leq \int_ {a} ^ {b} f ^ {2} (x) d \alpha (x) \int_ {a} ^ {b} g ^ {2} (x) d \alpha (x).
$$

Integrating by parts and using this inequality, we obtain

$$
\begin{array}{l} \left((a + b + 1) \int_ {0} ^ {1} x ^ {a + b} f (x) d x\right) ^ {2} = \left(f (1) - \int_ {0} ^ {1} x ^ {a + b + 1} d f (x)\right) ^ {2} \\ = f ^ {2} (1) - 2 f (1) \int_ {0} ^ {1} x ^ {a + b + 1} d f (x) + \left(\int_ {0} ^ {1} x ^ {a + b + 1} d f (x)\right) ^ {2} \\ \leq f ^ {2} (1) - 2 f (1) \int_ {0} ^ {1} x ^ {a + b + 1} d f (x) + \int_ {0} ^ {1} x ^ {2 a + 1} d f (x) \int_ {0} ^ {1} x ^ {2 b + 1} d f (x). \\ \end{array}
$$

Since

$$
\int_ {0} ^ {1} x ^ {k} d f (x) = f (1) - k \int_ {0} ^ {1} x ^ {k - 1} f (x) d x,
$$

we get

$$
\begin{array}{l} \left((a + b + 1) \int_ {0} ^ {1} x ^ {a + b} f (x) d x\right) ^ {2} \\ \leq (2 a + 1) \int_ {0} ^ {1} x ^ {2 a} f (x) d x (2 b + 1) \int_ {0} ^ {1} x ^ {2 b} f (x) d x \\ + f (1) \left(2 (a + b + 1) \int_ {0} ^ {1} x ^ {a + b} f (x) d x - (2 a + 1) \int_ {0} ^ {1} x ^ {2 a} f (x) d x \right. \\ - (2 b + 1) \int_ {0} ^ {1} x ^ {2 b} f (x) d x). \\ \end{array}
$$

To see that

$$
\int_ {0} ^ {1} f (x) \left(2 (a + b + 1) x ^ {a + b} - (2 a + 1) x ^ {2 a} - (2 b + 1) x ^ {2 b}\right) d x \leq 0,
$$

we integrate by parts and get

$$
\begin{array}{l} \int_ {0} ^ {1} f (x) \left(2 (a + b + 1) x ^ {a + b} - (2 a + 1) x ^ {2 a} - (2 b + 1) x ^ {2 b}\right) d x \\ = - \int_ {0} ^ {1} \left(2 x ^ {a + b + 1} - x ^ {2 a + 1} - x ^ {2 b + 1}\right) d f (x) \\ = \int_ {0} ^ {1} \left(x ^ {a} - x ^ {b}\right) ^ {2} x d f (x) \leq 0, \\ \end{array}
$$

because $\pmb{f}$ is decreasing.

1.6.33. [25] The inequality to be proved can be rewritten as

$$
\begin{array}{l} (2 a + 1) \int_ {0} ^ {1} x ^ {2 a} f (x) d x (2 b + 1) \int_ {0} ^ {1} x ^ {2 b} f (x) d x \\ \leq (a + b + 1) ^ {2} \left(\int_ {0} ^ {1} x ^ {a + b} f (x) d x\right) ^ {2}. \\ \end{array}
$$

It is easy to see that if $f$ is constant on $[0,1]$ or if $a = b$ , then equality holds. So assume that $f$ is not constant and $a \neq b$ . To prove this inequality, we consider the quadratic form

$$
Q (u, v) = A u ^ {2} + 2 B u v + C v ^ {2},
$$

with

$$
\begin{array}{l} A = (2 a + 1) \int_ {0} ^ {1} x ^ {2 a} f (x) d x, \quad B = (a + b + 1) \int_ {0} ^ {1} x ^ {a + b} f (x) d x, \\ C = (2 b + 1) \int_ {0} ^ {1} x ^ {2 b} f (x) d x, \\ \end{array}
$$

and show that this form is indefinite. Integration by parts gives

$$
\int_ {0} ^ {1} x ^ {c} f (x) d x = \frac {f (1)}{c \mid 1} - \int_ {0} ^ {1} \frac {x ^ {c + 1}}{c \mid 1} d f (x)
$$

for $c > 0$ . Therefore

$$
Q (u, v) = f (1) (u + v) ^ {2} - \int_ {0} ^ {1} \left(x ^ {a} u + x ^ {b} v\right) ^ {2} x d f (x).
$$

Thus $Q(1,1) = 4f(1) - \int_{0}^{1}(x^{a} + x^{b})^{2}xdf(x) > 4f(0) \geq 0$ , and clearly, $Q(1, -1) < 0$ . This shows that the quadratic form $Q(u,v)$ is indefinite, which means that $AC - B^2 < 0$ .

1.6.34. We have

$$
\int_ {a} ^ {b} \left(\int_ {- h} ^ {h} f (y + t) d y\right) d t = \int_ {- h} ^ {h} \left(\int_ {a} ^ {b} f (y + t) d t\right) d y.
$$

Moreover, note that

$$
\int_ {a} ^ {b} \left(\int_ {- h} ^ {h} f (y + t) d y\right) d t = \int_ {a} ^ {b} \left(\int_ {t - h} ^ {t + h} f (z) d z\right) d t = 2 h \int_ {a} ^ {b} f _ {h} (t) d t
$$

and

$$
\int_ {- h} ^ {h} \left(\int_ {a} ^ {b} f (y + t) d t\right) d y = \int_ {- h} ^ {h} \left(\int_ {a + y} ^ {b + y} f (z) d z\right) d y.
$$

Assume first that $f \geq 0$ . To prove the inequality in this case, it suffices to show that $\int_{a + y}^{b + y} f(z) dz \leq \int_{a}^{b} f(x) dx$ . If $y \geq 0$ , then $\int_{a + y}^{b + y} f(z) dz = \int_{a + y}^{b} f(z) dz \leq \int_{a}^{b} f(x) dx$ . If $y < 0$ , analogous reasoning can be applied. Assume now that $f$ is an arbitrary continuous function, and set $\tilde{f}_h(x) = \frac{1}{2h} \int_{x - h}^{x + h} |f(t)| dt$ . It follows from what we have proved that $\int_{a}^{b} \tilde{f}_h(x) dx \leq \int_{a}^{b} |f(x)| dx$ . Moreover, we have

$$
| f _ {h} (x) | = \left| \frac {1}{2 h} \int_ {x - h} ^ {x + h} f (t) d t \right| \leq \frac {1}{2 h} \int_ {x - h} ^ {x + h} | f (t) | d t = \bar {f} _ {h} (x).
$$

So, the inequality is proved.

1.6.35. (a) Put

$$
S _ {n} (x) = f _ {1} (x) + f _ {2} (x) + \dots + f _ {n} (x).
$$

Then, by the Hölder inequality (see, e.g., 1.6.27(a)),

$$
\begin{array}{l} \int_ {a} ^ {b} S _ {n} ^ {k} (x) d x = \int_ {a} ^ {b} f _ {1} (x) S _ {n} ^ {k - 1} (x) d x + \dots + \int_ {a} ^ {b} f _ {n} (x) S _ {n} ^ {k - 1} (x) d x \\ \leq \left(\int_ {a} ^ {b} f _ {1} ^ {k} (x) d x\right) ^ {\frac {1}{k}} \left(\int_ {a} ^ {b} S _ {n} ^ {k} (x) d x\right) ^ {\frac {k - 1}{k}} \\ + \dots + \left(\int_ {a} ^ {b} f _ {n} ^ {k} (x) d x\right) ^ {\frac {1}{k}} \left(\int_ {a} ^ {b} S _ {n} ^ {k} (x) d x\right) ^ {\frac {k - 1}{k}}, \\ \end{array}
$$

which implies the desired inequality.

(b) It suffices to apply the inequality given in 1.6.27(b).

1.6.36. The results follow from the fact that for $x_1, x_2, \ldots, x_n \geq 0$ we have

$$
(x _ {1} + x _ {2} + \dots + x _ {n}) ^ {k} \geq x _ {1} ^ {k} + x _ {2} ^ {k} + \dots + x _ {n} ^ {k} \tag {a}
$$

for $k > 1$ , and

$$
(x _ {1} + x _ {2} + \dots + x _ {n}) ^ {k} \leq x _ {1} ^ {k} + x _ {2} ^ {k} + \dots + x _ {n} ^ {k} \tag {b}
$$

for $0 < k < 1$ . (Compare with II, 2.5.25.)

1.6.37. Since $0 \leq \lambda \leq b - a$ , we see that $a + \lambda, b - \lambda \in [a, b]$ . Now we prove the left inequality. We have

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) g (x) d x - \int_ {b - \lambda} ^ {b} f (x) d x \\ = \int_ {a} ^ {b - \lambda} f (x) g (x) d x + \int_ {b - \lambda} ^ {b} f (x) (g (x) - 1) d x \\ \geq \int_ {a} ^ {b - \lambda} f (x) g (x) d x + f (b - \lambda) \left(\int_ {b - \lambda} ^ {b} g (x) d x - \lambda\right) \\ = \int_ {a} ^ {b - \lambda} f (x) g (x) d x + f (b - \lambda) \left(\int_ {b - \lambda} ^ {b} g (x) d x - \int_ {a} ^ {b} g (x) d x\right) \\ = \int_ {a} ^ {b - \lambda} f (x) g (x) d x - f (b - \lambda) \int_ {a} ^ {b - \lambda} g (x) d x \\ = \int_ {a} ^ {b - \lambda} g (x) (f (x) - f (b - \lambda)) d x \geq 0. \\ \end{array}
$$

The other inequality can be proved analogously.

1.6.38. [J. E. Pecarić, J. Math. Anal. Appl. 88 (1982), pp. 505-507] Assume first that $\int_0^1 g(x)dx > 0$ . Then using the generalized version of the Jensen inequality stated in 1.6.30 with $\varphi (x) = x^{p}, p \geq 1$ , we get

$$
\left(\int_ {0} ^ {1} f (x) g (x) d x\right) ^ {p} \leq \left(\int_ {0} ^ {1} g (x) d x\right) ^ {p - 1} \int_ {0} ^ {1} (f (x)) ^ {p} g (x) d x.
$$

Now it is enough to prove

$$
\left(\int_ {0} ^ {1} g (x) d x\right) ^ {p - 1} \int_ {0} ^ {1} (f (x)) ^ {p} g (x) d x \leq \int_ {0} ^ {\lambda} (f (x)) ^ {p} d x.
$$

To derive this inequality, set

$$
\mu = \left(\int_ {0} ^ {1} g (x) d x\right) ^ {p - 1}
$$

and proceed as follows:

$$
\begin{array}{l} \int_ {0} ^ {\lambda} (f (x)) ^ {p} d x - \mu \int_ {0} ^ {1} (f (x)) ^ {p} g (x) d x \\ = \int_ {0} ^ {\lambda} (f (x)) ^ {p} (1 - \mu g (x)) d x - \mu \int_ {\lambda} ^ {1} (f (x)) ^ {p} g (x) d x \\ \geq (f (\lambda)) ^ {p} \int_ {0} ^ {\lambda} (1 - \mu g (x)) d x - \mu \int_ {\lambda} ^ {1} (f (x)) ^ {p} g (x) d x \\ = (f (\lambda)) ^ {p} \left(\lambda - \mu \int_ {0} ^ {\lambda} g (x) d x\right) - \mu \int_ {\lambda} ^ {1} (f (x)) ^ {p} g (x) d x \\ = (f (\lambda)) ^ {p} \left(\left(\int_ {0} ^ {1} g (x) d x\right) ^ {p} - \mu \int_ {0} ^ {\lambda} g (x) d x\right) - \mu \int_ {\lambda} ^ {1} (f (x)) ^ {p} g (x) d x \\ = \mu \left((f (\lambda)) ^ {p} \int_ {\lambda} ^ {1} g (x) d x - \int_ {\lambda} ^ {1} (f (x)) ^ {p} g (x) d x\right) \\ = \mu \int_ {\lambda} ^ {1} g (x) ((f (\lambda)) ^ {p} - (f (x)) ^ {p}) d x \geq 0. \\ \end{array}
$$

The stated result holds also if $\int_0^1 g(x)dx = 0$ . In this case both sides of the inequality are equal to zero, which is a consequence of 2.3.6.

1.6.39. Use the substitution $x = (b - a)t + a, 0 \leq t \leq 1$ .

1.6.40. We have

$$
\begin{array}{l} \int_ {0} ^ {\infty} f (x) g (x) d x - A \int_ {0} ^ {\lambda} f (x) d x \\ = - \int_ {0} ^ {\lambda} (A - g (x)) (f (x) - f (\lambda)) d x - \int_ {\lambda} ^ {\infty} g (x) (f (\lambda) - f (x)) d x \leq 0. \\ \end{array}
$$

1.6.41. We note that integrating the inequality

$$
0 \leq g (x) \left(\int_ {a} ^ {b} g (t) d t\right) ^ {p - 1} \leq 1
$$

over $[a, b]$ gives $\lambda \in [0, b - a]$ . Assume first that $p \geq 1$ . Then by the generalized Jensen inequality (see the solution to 1.6.38),

$$
\left(\int_ {a} ^ {b} f (x) g (x) d x\right) ^ {p} \leq \mu \int_ {a} ^ {b} g (x) f ^ {p} (x) d x,
$$

where

$$
\mu = \left(\int_ {a} ^ {b} g (x) d x\right) ^ {p - 1}.
$$

We will use Apéry's idea presented in the previous solution. Note that, since $0 \leq \mu g(x) \leq 1$ ,

$$
\begin{array}{l} \int_ {a} ^ {a + \lambda} f ^ {p} (x) d x - \int_ {a} ^ {b} \mu g (x) f ^ {p} (x) d x \\ = \int_ {a} ^ {a + \lambda} \left(f ^ {p} (x) - f ^ {p} (a + \lambda)\right) (1 - \mu g (x)) d x \\ + \int_ {a + \lambda} ^ {b} (f ^ {p} (a + \lambda) - f ^ {p} (x)) \mu g (x) d x \geq 0. \\ \end{array}
$$

If $0 < p \leq 1$ , then by the generalized Jensen inequality (1.6.30),

$$
\left(\int_ {a} ^ {b} f (x) g (x) d x\right) ^ {p} \geq \mu \int_ {a} ^ {b} g (x) f ^ {p} (x) d x
$$

with $\pmb{\mu}$ defined above. Moreover,

$$
\begin{array}{l} \int_ {a} ^ {b} \mu g (x) f ^ {p} (x) d x - \int_ {b - \lambda} ^ {b} f ^ {p} (t) d t \\ = \int_ {a} ^ {b - \lambda} \left(f ^ {p} (x) - f ^ {p} (b - \lambda)\right) \mu g (x) d x \\ + \int_ {b - \lambda} ^ {b} (f ^ {p} (b - \lambda) - f ^ {p} (x)) (1 - \mu g (x)) d x \geq 0. \\ \end{array}
$$

1.6.42. Put $g(x) = g_{1}(x) - g_{2}(x)$ and $G(x) = \int_{a}^{x} g(t) dt$ . Since $G(x) \geq 0$ for $x \in [a, b]$ and $G(a) = G(b) = 0$ , integration by parts gives

$$
\begin{array}{l} \int_ {a} ^ {b} f (t) g (t) d t = \int_ {a} ^ {b} f (t) d G (t) = f (t) G (t) \left| _ {a} ^ {b} - \int_ {a} ^ {b} G (t) d f (t) \right. \\ = - \int_ {a} ^ {b} G (t) d f (t), \\ \end{array}
$$

which implies the desired results.

1.6.43. [H. Gauchman, J. Inequal. Pure and Appl. Math. 3(2002) no. 2, Article 26, 9 pp. (electronic)] We apply the Steffensen inequality given in 1.6.37 with $g(x) = \frac{f'(x) - m}{M - m}$ , and get

$$
\frac {\lambda^ {2}}{2} \leq \int_ {a} ^ {b} \frac {f ^ {\prime} (x) - m}{M - m} (b - x) d x \leq \frac {(b - a) ^ {2} - (b - a - \lambda) ^ {2}}{2}
$$

and

$$
- \frac {(b - a) ^ {2} - (b - a - \lambda) ^ {2}}{2} \leq \int_ {a} ^ {b} \frac {f ^ {\prime} (x) - m}{M - m} (a - x) d x \leq - \frac {\lambda^ {2}}{2},
$$

where $\lambda = \frac{f(b) - f(a) - m(b - a)}{M - m}$ . Multiplying the last inequalities by $-1$ and then adding them to earlier ones, we obtain

$$
\lambda^ {2} \leq \int_ {a} ^ {b} \frac {f ^ {\prime} (x) - m}{M - m} (b - a) d x \leq (b - a) ^ {2} - (b - a - \lambda) ^ {2}.
$$

A simple calculation shows that the above inequalities are equivalent to those to be proved.

It is worth noting here that this result is an improvement of the following trivial inequalities: $m \leq \frac{f(b) - f(a)}{b - a} \leq M$ .

1.6.44. [H. Gauchman, J. Inequal. Pure and Appl. Math. 3(2002) no. 2, Article 26, 9 pp. (electronic)] As in the solution to the last problem, we will apply the Steffensen inequality given in 1.6.37 with $g(x) = \frac{f'(x) - m}{M - m}$ . We first note that integration by parts yields

$$
\int_ {a} ^ {b} \frac {f ^ {\prime} (x) - m}{M - m} (b - x) d x = \frac {\int_ {a} ^ {b} f (x) d x - f (a) (b - a) - \frac {m (b - a) ^ {2}}{2}}{M - m}
$$

and

$$
\int_ {a} ^ {b} \frac {f ^ {\prime} (x) - m}{M - m} (a - x) d x = \frac {\int_ {a} ^ {b} f (x) d x - f (b) (b - a) + \frac {m (b - a) ^ {2}}{2}}{M - m}.
$$

By the Steffensen inequality,

$$
\frac {\lambda^ {2}}{2} \leq \frac {\int_ {a} ^ {b} f (x) d x - f (a) (b - a) - \frac {m (b - a) ^ {2}}{2}}{M - m} \leq \frac {(b - a) ^ {2}}{2} - \frac {(b - a - \lambda) ^ {2}}{2}
$$

and

$$
\frac {(b - a - \lambda) ^ {2}}{2} - \frac {(b - a) ^ {2}}{2} \leq \frac {\int_ {a} ^ {b} f (x) d x - f (b) (b - a) + \frac {m (b - a) ^ {2}}{2}}{M - m} \leq - \frac {\lambda^ {2}}{2}.
$$

Now summing the last inequalities, we see that

$$
\begin{array}{l} \frac {2}{M - m} \left| \int_ {a} ^ {b} f (x) d x - \frac {f (a) + f (b)}{2} (b - a) \right| \leq - \lambda^ {2} + \lambda (b - a) \\ = \frac {(f (b) - f (a) - m (b - a)) (M (b - a) - f (b) + f (a))}{(M - m) ^ {2}}. \\ \end{array}
$$

Finally, we observe that if $m = -M$ , then as a corollary we get

$$
\left| \int_ {a} ^ {b} f (x) d x - \frac {f (a) + f (b)}{2} (b - a) \right| \leq \frac {M (b - a) ^ {2}}{4} - \frac {(f (b) - f (a)) ^ {2}}{4 M}.
$$

1.6.45. For $0 \leq x \leq a$ , set

$$
h (x) = \int_ {0} ^ {x} | f ^ {\prime} (t) | d t.
$$

Then

$$
| f (x) | = \left| \int_ {0} ^ {x} f ^ {\prime} (t) d t \right| \leq \int_ {0} ^ {x} | f ^ {\prime} (t) | d t = h (x)
$$

and $h'(x) = |f'(x)|$ . Consequently,

$$
\begin{array}{l} \int_ {0} ^ {a} | f (x) f ^ {\prime} (x) | d x \leq \int_ {0} ^ {a} h (x) h ^ {\prime} (x) d x = \frac {1}{2} h ^ {2} (a) \\ = \frac {1}{2} \left(\int_ {0} ^ {a} | f ^ {\prime} (t) | d t\right) ^ {2} \\ \leq \frac {a}{2} \int_ {0} ^ {a} \left(f ^ {\prime} (x)\right) ^ {2} d x, \\ \end{array}
$$

where the last inequality follows from the Schwarz inequality.

Observe that the constant $a / 2$ is the best possible. Indeed, taking $f(x) = cx$ , we get the equality.

1.6.46. For $0 \leq x \leq a$ , set

$$
h (x) = \int_ {0} ^ {x} \left(\int_ {0} ^ {t _ {n - 1}} \left(\dots \left(\int_ {0} ^ {t _ {1}} | f ^ {(n)} (t) | d t\right) \dots\right) d t _ {n - 2}\right) d t _ {n - 1}.
$$

Then $h^{(n)}(x) = |f^{(n)}(x)|$ and

$$
\begin{array}{l} | f (x) | = \left| \int_ {0} ^ {x} \left(\int_ {0} ^ {t _ {n - 1}} \left(\dots \left(\int_ {0} ^ {t _ {2}} f ^ {(n)} (t) d t\right) \dots\right) d t _ {n - 2}\right) d t _ {n - 1} \right| \\ \leq \int_ {0} ^ {x} \left(\int_ {0} ^ {t _ {n - 1}} \left(\dots \left(\int_ {0} ^ {t _ {1}} | f ^ {(n)} (t) | d t\right) \dots\right) d t _ {n - 2}\right) d t _ {n - 1} \\ = h (x). \\ \end{array}
$$

Moreover, since the functions $h, h', \ldots$ , and $h^{(n-1)}$ are monotonically increasing, we see that

$$
\begin{array}{l} \int_ {0} ^ {a} | f (t) f ^ {(n)} (t) | d t \leq \int_ {0} ^ {a} h (t) h ^ {(n)} (t) d t \leq \int_ {0} ^ {a} t h ^ {\prime} (t) h ^ {(n)} (t) d t \\ \leq \dots \leq \int_ {0} ^ {a} t ^ {n - 1} h ^ {(n - 1)} (t) h ^ {(n)} (t) d t \\ \leq a ^ {n - 1} \frac {(h ^ {(n - 1)} (a)) ^ {2}}{2} \\ = \frac {a ^ {n - 1}}{2} \left(\int_ {0} ^ {a} h ^ {(n)} (t) d t\right) ^ {2} \leq \frac {a ^ {n}}{2} \int_ {0} ^ {a} (h ^ {(n)} (t)) ^ {2} d t, \\ \end{array}
$$

where the last inequality follows from the Schwarz inequality.

1.6.47. Set

$$
z (x) = \int_ {0} ^ {x} | f ^ {\prime} (t) | ^ {q} d t.
$$

Then $z'(x) = |f'(x)|^q$ and

$$
| f (x) | ^ {p} \leq \left(\int_ {0} ^ {x} | f ^ {\prime} (t) | d t\right) ^ {p}.
$$

Suppose that $q > 1$ and $q'$ is such that $\frac{1}{q} + \frac{1}{q'} = 1$ . By the Hölder inequality,

$$
| f (x) | ^ {p} \leq \left(\int_ {0} ^ {x} | f ^ {\prime} (t) | ^ {q} d t\right) ^ {p / q} a ^ {p / q ^ {\prime}}, \quad 0 \leq x \leq a.
$$

Consequently,

$$
\begin{array}{l} \int_ {0} ^ {a} | f (x) | ^ {p} | f ^ {\prime} (x) | ^ {q} d x \leq a ^ {p / q ^ {\prime}} \int_ {0} ^ {a} | f ^ {\prime} (x) | ^ {q} \left(\int_ {0} ^ {x} | f ^ {\prime} (t) | ^ {q} d t\right) ^ {p / q} d x \\ = a ^ {p / q ^ {\prime}} \int_ {0} ^ {a} z ^ {\prime} (x) (z (x)) ^ {p / q} d x \\ = a ^ {p / q ^ {\prime}} \frac {q}{p + q} z (a) ^ {\frac {p}{q} + 1} \\ = \frac {q}{p + q} a ^ {p / q ^ {\prime}} \left(\int_ {0} ^ {a} | f ^ {\prime} (x) | ^ {q} d x\right) ^ {\frac {p}{q} + 1} \\ \leq \frac {q}{p + q} a ^ {p} \int_ {0} ^ {a} | f ^ {\prime} (x) | ^ {p + q} d x, \\ \end{array}
$$

where the last inequality follows from the Jensen inequality (see, e.g., 1.6.29). The case $q = 1$ can be proved in a similar way.

1.6.48. Set

$$
P _ {n} (x) = (x - a) ^ {n} (x - b) ^ {n}
$$

and note that $P_{n}^{(k)}(a) = P_{n}^{(k)}(b) = 0$ for $k = 0,1,\ldots,n-1$ . So, by assumption,

$$
P _ {n} ^ {(k)} (a) f ^ {(2 n - k - 1)} (a) = P _ {n} ^ {(k)} (b) f ^ {(2 n - k - 1)} (b) = 0
$$

for $k = 0,1,\ldots ,2n - 1$ . Consequently, integrating by parts $2n$ times, we get

$$
\int_ {a} ^ {b} P _ {n} (x) f ^ {(2 n)} (x) d x = \int_ {a} ^ {b} P _ {n} ^ {(2 n)} (x) f (x) d x = (2 n)! \int_ {a} ^ {b} f (x) d x.
$$

It then follows that

$$
\left| \int_ {a} ^ {b} f (x) d x \right| \leq \frac {M}{(2 n) !} \int_ {a} ^ {b} | P _ {n} (x) | d x.
$$

Since $P_{n}(x)$ is either positive or negative on $(a, b)$ , it is enough to calculate $\int_{a}^{b} P_{n}(x) dx$ . The substitution $x = u + l(b - u)$ yields

$$
\begin{array}{l} \int_ {a} ^ {b} P _ {n} (x) d x = \int_ {a} ^ {b} (x - a) ^ {n} (x - b) ^ {n} d x \\ = (- 1) ^ {n} (b - a) ^ {2 n + 1} \int_ {0} ^ {1} t ^ {n} (1 - t) ^ {n} d t \\ = (- 1) ^ {n} (b - a) ^ {2 n + 1} \frac {(n !) ^ {2}}{(2 n + 1) !}, \\ \end{array}
$$

where the last equality follows from 1.5.1(c).

# 1.7. Jordan Measure

1.7.1. If $\mathbf{A}$ is Jordan measurable, then $|\mathbf{A}| = |\mathbf{A}|^{\epsilon} = |\mathbf{A}|_{\bullet} < +\infty$ . It then follows, by the definition of supremum and infimum, that, given $\varepsilon > 0$ , there are elementary sets $\mathbf{E}_1$ contained in $\mathbf{A}$ such that

$$
| \mathbf {A} | - | \mathbf {E} _ {1} | <   \frac {\varepsilon}{2},
$$

and $\mathbf{E_2}$ containing A such that

$$
\left| \mathbf {E} _ {2} \right| - \left| \mathbf {A} \right| <   \frac {\varepsilon}{2}.
$$

This proves the necessity of the condition. Now we show that the condition is also sufficient for the Jordan measurability of $\mathbf{A}$ . Indeed, given $\varepsilon > 0$ , we have

$$
\left| \mathbf {A} \right| ^ {*} - \left| \mathbf {A} \right| _ {\bullet} \leq \left| \mathbf {E} _ {2} \right| - \left| \mathbf {E} _ {1} \right| <   \varepsilon ,
$$

which implies that $|\mathbf{A}|^{*} = |\mathbf{A}|_{*}$

1.7.2. Since $\mathbf{A}_i, i = 1,2,\ldots,n$ , are Jordan measurable, by the result in the previous problem, given $\varepsilon > 0$ , there are elementary sets $\mathbf{E}_i$ and $\mathbf{E}_i'$ such that $\mathbf{E}_i \subset \mathbf{A}_i \subset \mathbf{E}_i'$ and $|\mathbf{E}_i'| - |\mathbf{E}_i| < \varepsilon/n$ . Thus for $i = 1,2,\ldots,n$ we have

$$
\left| \mathbf {A} _ {i} \right| - \frac {\varepsilon}{n} <   \left| \mathbf {E} _ {i} \right| \quad \text {a n d} \quad \left| \mathbf {E} _ {i} ^ {\prime} \right| <   \left| \mathbf {A} _ {i} \right| + \frac {\varepsilon}{n}.
$$

Note now that $\mathbf{E}_i$ are pairwise separate and

$$
\mathbf {E} _ {1} \cup \mathbf {E} _ {2} \cup \dots \cup \mathbf {E} _ {n} \subset \mathbf {A} _ {1} \cup \mathbf {A} _ {2} \cup \dots \cup \mathbf {A} _ {n},
$$

and $\mathbf{E}_1 \cup \mathbf{E}_2 \cup \dots \cup \mathbf{E}_n$ is an elementary set, whose volume is $|\mathbf{E}_1| + |\mathbf{E}_2| + \dots + |\mathbf{E}_n|$ . On the other hand,

$$
A _ {1} \cup A _ {2} \cup \dots \cup A _ {n} \subset E _ {1} ^ {\prime} \cup E _ {2} ^ {\prime} \cup \dots \cup E _ {n} ^ {\prime}
$$

and $\mathbf{E}_1' \cup \mathbf{E}_2' \cup \dots \cup \mathbf{E}_n'$ is an elementary set, whose volume is less than or equal to $|\mathbf{E}_1'| + |\mathbf{E}_2'| + \dots + |\mathbf{E}_n'|$ . Consequently,

$$
\begin{array}{l} \left| A _ {1} \right| + \left| A _ {2} \right| + \dots + \left| A _ {n} \right| - \varepsilon <   \left| E _ {1} \right| + \left| E _ {2} \right| + \dots \left| E _ {n} \right| \\ \leq | A _ {1} \cup A _ {2} \cup \dots \cup A _ {n} |. \\ \leq | A _ {1} \cup A _ {2} \cup \dots \cup A _ {n} | ^ {\bullet} \\ \leq | \mathbf {E} _ {1} ^ {\prime} | + | \mathbf {E} _ {2} ^ {\prime} | + \dots + | \mathbf {E} _ {n} ^ {\prime} | \\ <   | A _ {1} | + | A _ {2} | + \dots + | A _ {n} | + \varepsilon . \\ \end{array}
$$

Since $\varepsilon > 0$ can be chosen arbitrarily, the desired result follows.

1.7.3. It is clear that the statement is true for elementary sets. We first show that

$$
\left| A _ {1} \cup A _ {2} \right| ^ {\circ} + \left| A _ {1} \cap A _ {2} \right| ^ {\circ} \leq \left| A _ {1} \right| ^ {\circ} + \left| A _ {2} \right| ^ {\circ}. \tag {1}
$$

Indeed, if $\mathbf{A}_1$ and $\mathbf{A}_2$ are bounded, and if $\mathbf{E}_1$ and $\mathbf{E}_2$ are elementary sets such that $\mathbf{A}_1 \subset \mathbf{E}_1$ and $\mathbf{A}_2 \subset \mathbf{E}_2$ , then $\mathbf{E}_1 \cup \mathbf{E}_2$ and $\mathbf{E}_1 \cap \mathbf{E}_2$ are both elementary sets (or $\mathbf{E}_1 \cap \mathbf{E}_2 = \emptyset$ ), and $\mathbf{A}_1 \cup \mathbf{A}_2 \subset \mathbf{E}_1 \cup \mathbf{E}_2$ , $\mathbf{A}_1 \cap \mathbf{A}_2 \subset \mathbf{E}_1 \cap \mathbf{E}_2$ . Thus

$$
\begin{array}{l} \left| \mathbf {A} _ {1} \cup \mathbf {A} _ {2} \right| ^ {\bullet} + \left| \mathbf {A} _ {1} \cap \mathbf {A} _ {2} \right| ^ {\bullet} \leq \left| \mathbf {E} _ {1} \cup \mathbf {E} _ {2} \right| + \left| \mathbf {E} _ {1} \cap \mathbf {E} _ {2} \right| \\ = | \mathbf {E} _ {1} | + | \mathbf {E} _ {2} |. \\ \end{array}
$$

Taking the infimum over all elementary sets $\mathbf{E}_1 \supset \mathbf{A}_1$ and $\mathbf{E}_2 \supset \mathbf{A}_2$ , we get (1) for bounded sets. If at least one of the sets is unbounded, then (1) holds for $\mathbf{A}_1 \cap \mathbf{R}_k$ and $\mathbf{A}_2 \cap \mathbf{R}_k$ with $\mathbf{R}_k = [-k, k] \times \dots \times [-k, k]$ . Letting $k \to \infty$ , yields (1). Moreover, it follows directly from the definition of the inner Jordan measure that (see the first part of the proof of (1))

$$
\left| A _ {1} \cup A _ {2} \right| _ {\bullet} + \left| A _ {1} \cap A _ {2} \right| _ {\bullet} \geq \left| A _ {1} \right| _ {\bullet} + \left| A _ {2} \right| _ {\bullet}. \tag {2}
$$

Since $\mathbf{A}_1$ and $\mathbf{A}_2$ are Jordan measurable, (1) and (2) imply that

$$
\begin{array}{l} \left| A _ {1} \cup A _ {2} \right| _ {\bullet} + \left| A _ {1} \cap A _ {2} \right| _ {\bullet} \geq \left| A _ {1} \right| + \left| A _ {2} \right| \\ \geq | A _ {1} \cup A _ {2} | ^ {\circ} + | A _ {1} \cap A _ {2} | ^ {\circ}. \\ \end{array}
$$

Consequently, if $|\mathbf{A}_1|$ and $|\mathbf{A}_2|$ are finite, then

$$
\left(\left| \mathbf {A} _ {1} \cup \mathbf {A} _ {2} \right| ^ {\bullet} - \left| \mathbf {A} _ {1} \cup \mathbf {A} _ {2} \right| _ {*}\right) + \left(\left| \mathbf {A} _ {1} \cap \mathbf {A} _ {2} \right| ^ {\bullet} - \left| \mathbf {A} _ {1} \cap \mathbf {A} _ {2} \right| _ {*}\right) \leq 0.
$$

Since both the terms on the left-hand side are nonnegative, we conclude that $|\mathbf{A}_1 \cup \mathbf{A}_2|^* = |\mathbf{A}_1 \cup \mathbf{A}_2|_*$ and $|\mathbf{A}_1 \cap \mathbf{A}_2|^* = |\mathbf{A}_1 \cap \mathbf{A}_2|_*$ . If one of the sets has infinite outer Jordan measure, then $|\mathbf{A}_1 \cup \mathbf{A}_2|^* = |\mathbf{A}_1 \cup \mathbf{A}_2|_* = +\infty$ , and the Jordan measurability of $\mathbf{A}_1 \cap \mathbf{A}_2$ and $\mathbf{A}_1 \cup \mathbf{A}_2$ follows from the above considerations.

1.7.4. We first show that if $\mathbf{A}$ is contained in an interval $\mathbf{R}$ , then

(1) $|\mathbf{A}|_{*} = |\mathbf{R}| - |\mathbf{R}\setminus \mathbf{A}|^{*}$ and $|\mathbf{A}|^{*} = |\mathbf{R}| - |\mathbf{R}\setminus \mathbf{A}|_{*}$

To this end, take an elementary set $\mathbf{E}_1 \subset \mathbf{A}$ . Then the elementary set $\overline{\mathbf{R} \setminus \mathbf{E}_1}$ contains $\mathbf{R} \setminus \mathbf{A}$ , and

$$
| \mathbf {R} | - | \mathbf {E} _ {1} | = | \mathbf {R} \backslash \mathbf {E} _ {1} | \geq | \mathbf {R} \backslash \mathbf {A} | ^ {\bullet}.
$$

Hence $|\mathbf{E}_1| \leq |\mathbf{R}| - |\mathbf{R} \setminus \mathbf{A}|^*$ , and, taking the supremum over all $\mathbf{E}_1 \subset \mathbf{A}$ , we get

(2) $|\mathbf{A}|_{\bullet}\leq |\mathbf{R}| - |\mathbf{R}\setminus \mathbf{A}|^{\bullet}.$

Now, let $\mathbf{E}_2$ be an elementary set such that $\mathbf{R} \setminus \mathbf{A} \subset \mathbf{E}_2 \subset \mathbf{R}$ . Then $\mathbf{R} \setminus \mathbf{E}_2 \subset \mathbf{A}$ and $|\mathbf{R}| - |\mathbf{E}_2| - |\mathbf{R} \setminus \mathbf{E}_2| \leq |\mathbf{A}|_*$ , which gives $|\mathbf{R}| - |\mathbf{A}|_* \leq |\mathbf{E}_2|$ . Taking the infimum over all $\mathbf{E}_2 \supset \mathbf{R} \setminus \mathbf{A}$ , we see that

$$
| \mathbf {R} | - | \mathbf {A} | _ {*} \leq | \mathbf {R} \backslash \mathbf {A} | ^ {\bullet}.
$$

Combined with (2), this gives

$$
| \mathbf {A} | _ {\bullet} = | \mathbf {R} | - | \mathbf {R} \backslash \mathbf {A} | ^ {\circ}.
$$

The other equality in (1) can be proved analogously. Now we can turn to the proof of the stated result. Suppose first that $\mathbf{A}_2$ is bounded. Let $\mathbf{R}$ be an interval such that $\mathbf{A}_1 \subset \mathbf{A}_2 \subset \mathbf{R}$ , and put $\mathbf{A} = \mathbf{A}_2 \setminus \mathbf{A}_1$ . Then, by what we have proved,

$\left|\mathbf{R}\backslash \mathbf{A}\right|^{\ast} = \left|\left(\mathbf{R}\backslash \mathbf{A}_{2}\right)\cup \mathbf{A}_{1}\right|^{\ast}\leq \left|\mathbf{R}\backslash \mathbf{A}_{2}\right|^{\ast} + \left|\mathbf{A}_{1}\right|^{\ast} = \left|\mathbf{R}\right| - \left|\mathbf{A}_{2}\right|_{\bullet} + \left|\mathbf{A}_{1}\right|^{\ast}$ and consequently,

(3) $|\mathbf{A}|_{*} = |\mathbf{R}| - |\mathbf{R}\setminus \mathbf{A}|^{\bullet}\geq |\mathbf{A}_{2}|_{*} - |\mathbf{A}_{1}|^{\bullet}.$

Similar reasoning yields

(4) $|\mathbf{A}|^{*} = |\mathbf{R}| - |\mathbf{R}\setminus \mathbf{A}|_{*}\leq |\mathbf{A}_{2}|^{*} - |\mathbf{A}_{1}|_{*}.$

Since $\mathbf{A}_1$ and $\mathbf{A}_2$ are measurable, we get

$$
| \mathbf {A} | = | \mathbf {A} _ {2} \backslash \mathbf {A} _ {1} | = | \mathbf {A} _ {2} | - | \mathbf {A} _ {1} |. \tag {5}
$$

If $\mathbf{A}_2$ is unbounded, we consider the sets $\mathbf{A}_1 \cap \mathbf{R}_k$ and $\mathbf{A}_2 \cap \mathbf{R}_k$ . Their difference is $\mathbf{A} \cap \mathbf{R}_k$ , and it satisfies (5). Letting $k \to \infty$ gives the desired result, provided that $|\mathbf{A}_1| < +\infty$ .

1.7.5. The only rectangles contained in $\mathbf{A}$ are $[a, b] \times [c, c]$ , where $[a, b] \subset [0, 1]$ and $c \in [0, 1] \setminus \mathbb{Q}$ . Consequently, $|\mathbf{A}|_{*} = 0$ . On the other hand, the smallest rectangle containing $\mathbf{A}$ is $[0, 1] \times [0, 1]$ . Thus $|\mathbf{A}|^{*} = 1$ .

1.7.6. We will use the result in 1.7.1. Given $0 < \varepsilon < 1$ , there is $n_0 \in \mathbb{N}$ such that

$$
\frac {1}{n _ {0}} \leq \frac {\varepsilon}{2} <   \frac {1}{n _ {0} - 1}.
$$

Let $\mathbf{E}_1$ be the elementary set inscribed in $\mathbf{B}$ consisting of rectangles, of whose sides one is [0,1] and the other is of length

$$
\frac {1}{2} - \frac {\varepsilon}{2 n _ {0}}, \left(\frac {1}{2} - \frac {1}{3}\right) - \frac {\varepsilon}{2 n _ {0}}, \dots , \left(\frac {1}{n _ {0} - 1} - \frac {1}{n _ {0}}\right) - \frac {\varepsilon}{2 n _ {0}},
$$

respectively. Then

$$
\left| \mathbf {E} _ {1} \right| = 1 - \frac {1}{n _ {0}} - \frac {n _ {0} - 1}{n _ {0}} \cdot \frac {\varepsilon}{2} > 1 - \varepsilon .
$$

Taking $\mathbf{E}_2 = [0,1] \times [0,1]$ , we have $|\mathbf{E}_2| - |\mathbf{E}_1| < \varepsilon$ . It is clear that $|\mathbf{A}| = 1$ .

1.7.7. By (3) in the solution to 1.7.4,

$$
| \mathbf {A} | _ {\bullet} = | (\mathbf {A} \cup \mathbf {B}) \backslash (\mathbf {B} \backslash \mathbf {A}) | _ {\bullet} \geq | \mathbf {A} \cup \mathbf {B} | _ {\ast} - | \mathbf {B} \backslash \mathbf {A} | ^ {*} = | \mathbf {A} \cup \mathbf {B} | _ {\ast},
$$

where the last equality follows from the assumption $|\mathbf{B}|^{\bullet} = 0$ . So we have

$$
| \mathbf {A} | _ {*} \geq | \mathbf {A} \cup \mathbf {B} | _ {*}.
$$

Since the opposite inequality is obvious, the equality holds.

Now if we take $\mathbf{A}$ defined in 1.7.5 and $\mathbf{B} = ([0,1] \times [0,1]) \setminus \mathbf{A}$ , we see that

$$
1 = | \mathrm {A} \cup \mathrm {B} | _ {*} \neq 0 = | \mathrm {A} | _ {*},
$$

although $|\mathbf{B}|_{\bullet} = 0$

# 1.7.8. We first show that

$$
| \mathbf {A} | = | \mathbf {A} ^ {\circ} |. \tag {1}
$$

If an elementary set $\mathbf{E}'$ is contained in $\mathbf{A}$ , then $\mathbf{E}^{\prime\circ} \subset \mathbf{A}^{\circ}$ and $|\mathbf{E}'| = |\mathbf{E}^{\prime\circ}|_{\bullet} \leq |\mathbf{A}^{\circ}|_{\bullet}$ . Therefore $|\mathbf{A}| \leq |\mathbf{A}^{\circ}|_{\bullet}$ . The opposite inequality is obvious. It is also clear that $|\mathbf{A}^{\circ}|_{\bullet} \leq |\mathbf{A}^{\circ}|^{\bullet} \leq |\mathbf{A}|$ . This proves (1) and Jordan measurability of $\mathbf{A}^{\circ}$ in the case when $|\mathbf{A}| < \infty$ . If $|\mathbf{A}| = \infty$ , we have to show that $\mathbf{A}^{\circ} \cap \mathbf{R}$ is Jordan measurable for any interval $\mathbf{R}$ . Let $\mathbf{E}$ be an elementary set contained in $\mathbf{A} \cap \mathbf{R}$ . Then

$$
\mathbf {E} ^ {\circ} \subset (\mathbf {A} \cap \mathbf {R}) ^ {\circ} = \mathbf {A} ^ {\circ} \cap \mathbf {R} ^ {\circ} \subset \mathbf {A} ^ {\circ} \cap \mathbf {R}.
$$

Since $\mathbf{A} \cap \mathbf{R}$ is measurable and $|\mathbf{E}| = |\mathbf{E}^{\circ}|$ , we get

$$
| \mathbf {A} \cap \mathbf {R} | \leq | \mathbf {A} ^ {\circ} \cap \mathbf {R} |.
$$

Clearly,

$$
| \mathbf {A} ^ {\circ} \cap \mathbf {R} |. \leq | \mathbf {A} \cap \mathbf {R} |,
$$

which shows that $|\mathbf{A}^{\circ}\cap \mathbf{R}|_{\bullet} = |\mathbf{A}\cap \mathbf{R}|.$ Moreover,

$$
\left| \mathbf {A} ^ {\circ} \cap \mathbf {R} \right| ^ {\circ} \leq \left| \mathbf {A} \cap \mathbf {R} \right| = \left| \mathbf {A} ^ {\circ} \cap \mathbf {R} \right| _ {\bullet},
$$

which completes the proof of the Jordan measurability of $\mathbf{A}^{\alpha}$ .

Now we turn to the proof of the other part of the statement. If $\mathbf{A}$ is bounded, then for any elementary set $\mathbf{E}$ , $\mathbf{A} \subset \mathbf{E}$ if and only if $\overline{\mathbf{A}} \subset \mathbf{E}$ , because $\mathbf{E}$ is closed. This shows that $|\mathbf{A}| = |\overline{\mathbf{A}}|^{\bullet}$ . Since $|\mathbf{A}| \leq |\overline{\mathbf{A}}|_{\bullet}$ , we get

$$
| \mathbf {A} | = | \overline {{\mathbf {A}}} |. \tag {2}
$$

Now assume that $\mathbf{A}$ is unbounded. Since $\mathbb{R}^{\circ}$ is open,

$$
\mathbf {R} ^ {\circ} \cap \overline {{\mathbf {A}}} \subset \overline {{\mathbf {R} ^ {\circ} \cap \mathbf {A}}}.
$$

Moreover, the sets $\mathbf{R} \cap \overline{\mathbf{A}}$ and $\mathbf{R}^0 \cap \overline{\mathbf{A}}$ differ by a set of outer Jordan measure zero. It then follows, by 1.7.7, that

$$
\left| \mathbf {R} \cap \overline {{\mathbf {A}}} \right| _ {\bullet} = \left| \mathbf {R} ^ {\circ} \cap \overline {{\mathbf {A}}} \right| _ {\bullet} \leq \left| \overline {{\mathbf {R} ^ {\circ} \cap \mathbf {A}}} \right| _ {\bullet} \leq \left| \overline {{\mathbf {R} \cap \mathbf {A}}} \right| _ {\bullet} = \left| \mathbf {R} \cap \mathbf {A} \right| \leq \left| \mathbf {R} \cap \overline {{\mathbf {A}}} \right| _ {\bullet}.
$$

One can easily show that $|\mathbf{R} \cap \overline{\mathbf{A}}|^\bullet \leq |\mathbf{R} \cap \mathbf{A}| \leq |\mathbf{R} \cap \overline{\mathbf{A}}|^\bullet$ . Hence, for any interval $\mathbf{R}$ ,

$$
| \mathbf {R} \cap \overline {{\mathbf {A}}} | = | \mathbf {R} \cap \mathbf {A} |.
$$

Finally, taking $\mathbf{R} = \mathbf{R}_k$ and letting $k \to \infty$ , we get (2) for unbounded sets.

1.7.9. Suppose first that $\mathbf{A}$ is bounded. Since $\partial \mathbf{A} = \overline{\mathbf{A}} \setminus \mathbf{A}^{\circ}$ , we see that if $\mathbf{A}$ is Jordan measurable, then by the results in 1.7.4 and 1.7.8, $|\partial \mathbf{A}| = 0$ . Suppose now that $|\partial \mathbf{A}| = 0$ and $\mathbf{A}$ is contained in an interval $\mathbf{R}$ . Then, given $\varepsilon > 0$ , there is an elementary set $\mathbf{E} \subset \mathbf{R}$ containing the boundary of $\mathbf{A}$ and such that $|\mathbf{E}| < \varepsilon$ . Hence $\mathbf{R} \setminus \mathbf{E} = \mathbf{E}_1 \cup \mathbf{E}_2$ , where $\mathbf{E}_1 \subset \mathbf{A}^\circ$ and $\mathbf{A} \subset \mathbf{R} \setminus \mathbf{E}_2$ . Since $\overline{\mathbf{E}_1}$ is an elementary set, we get $|\mathbf{E}_1| = |\overline{\mathbf{E}_1}| \leq |\mathbf{A}|_\bullet$ . Clearly, $\mathbf{E}_1 \cup \mathbf{E}$ is an elementary set containing $\mathbf{A}$ , and therefore $|\mathbf{A}|^\bullet \leq |\mathbf{E}_1 \cup \mathbf{E}| = |\mathbf{E}_1| + |\mathbf{E}|$ . Thus $|\mathbf{A}|^\bullet - |\mathbf{A}|_\bullet < \varepsilon$ .

Now if $\mathbf{A}$ is unbounded and Jordan measurable, then either $|\mathbf{A}| < +\infty$ or $|\mathbf{A}| = +\infty$ . In the former case, by the results in 1.7.4 and 1.7.8, $|\partial \mathbf{A}| = 0$ . In the latter case, for any interval $\mathbf{R}$ ,

$$
\begin{array}{l} 0 \leq | \partial \mathbf {A} \cap \mathbf {R} | = | (\overline {{\mathbf {A}}} \backslash \mathbf {A} ^ {\circ}) \cap \mathbf {R} | = | \overline {{\mathbf {A}}} \cap \mathbf {R} | - | \mathbf {A} ^ {\circ} \cap \mathbf {R} | \\ = | \overline {{\mathbf {A}}} \cap \mathbf {R} ^ {\circ} | - | \mathbf {A} ^ {\circ} \cap \mathbf {R} ^ {\circ} |, \\ \end{array}
$$

because $|\partial \mathbf{R}| = 0$ . Moreover, since $\mathbf{R}^{\circ}$ is an open set we have $\overline{\mathbf{A}} \cap \mathbf{R}^{\circ} \subset \overline{\mathbf{A} \cap \mathbf{R}^{\circ}}$ , and consequently,

$0 \leq |\partial \mathbf{A} \cap \mathbf{R}| \leq |\overline{\mathbf{A} \cap \mathbf{R}^o}| - |(\mathbf{A} \cap \mathbf{R})^o| = |\mathbf{A} \cap \mathbf{R}^o| - |\mathbf{A} \cap \mathbf{R}| \leq 0,$ which implies $|\partial \mathbf{A}| = 0$ .

Finally, suppose that $\mathbf{A}$ is unbounded and $|\partial \mathbf{A}| = 0$ . Then for any interval $\mathbf{R}$ , $|\partial \mathbf{A} \cap \mathbf{R}| = 0$ , and, repeating the consideration from the beginning of the proof, one can show that, given $\varepsilon > 0$ , $|\mathbf{A} \cap \mathbf{R}|^{\bullet} \leq |\mathbf{A} \cap \mathbf{R}|_{\bullet} + \varepsilon$ , which gives the Jordan measurability of $\mathbf{A} \cap \mathbf{R}$ for any interval $\mathbf{R}$ . To prove that $|\mathbf{A}|^{\bullet} = |\mathbf{A}|_{\bullet}$ it suffices to show that $|\mathbf{A}|_{\bullet} = \lim_{k \to \infty} |\mathbf{A} \cap \mathbf{R}_{k}|_{\bullet}$ . To this end, put $l = \lim_{k \to \infty} |\mathbf{A} \cap \mathbf{R}_{k}|_{\bullet}$ . Clearly, $l \leq |\mathbf{A}|_{\bullet}$ . Moreover, if $\mathbf{E}$ is an elementary set contained in $\mathbf{A}$ , then $\mathbf{E} \subset \mathbf{A} \cap \mathbf{R}_{k}$ for sufficiently large $k$ , and consequently, $|\mathbf{A}|_{\bullet} \leq l$ .

1.7.10. Using 1.7.9 and the fact that

$$
\partial \left(A _ {1} \cup A _ {2} \cup \dots \cup A _ {n}\right) \subset \partial \left(A _ {1}\right) + \partial \left(A _ {2}\right) + \dots + \partial \left(A _ {n}\right),
$$

we see that the finite union of measurable sets is measurable. It follows from 1.7.3 and 1.7.8 that the stated equality holds for $n = 2$ . Indeed, if $A_1$ and $A_2$ are separate, then $(A_1 \cap A_2)^{\circ} = A_1^{\circ} \cap A_2^{\circ} = \emptyset$ , and consequently,

$$
\left| \mathbf {A} _ {1} \cup \mathbf {A} _ {2} \right| = \left| \mathbf {A} _ {1} \cup \mathbf {A} _ {2} \right| + \left| (\mathbf {A} _ {1} \cap \mathbf {A} _ {2}) ^ {\circ} \right| = \left| \mathbf {A} _ {1} \right| + \left| \mathbf {A} _ {2} \right|.
$$

Now we proceed by induction. Assuming the equality to hold for $n$ we will prove it for $n + 1$ . We have

$$
\begin{array}{l} \left| \left(\mathrm {A} _ {1} \cup \mathrm {A} _ {2} \cup \dots \cup \mathrm {A} _ {n}\right) \cup \mathrm {A} _ {n + 1} \right| + \left| \left(\mathrm {A} _ {1} \cup \mathrm {A} _ {2} \cup \dots \cup \mathrm {A} _ {n}\right) \cap \mathrm {A} _ {n + 1} \right| \\ = \left| A _ {1} \cup A _ {2} \cup \dots \cup A _ {n} \right| + \left| A _ {n + 1} \right| = \left| A _ {1} \right| + \dots + \left| A _ {n} \right| + \left| A _ {n + 1} \right|. \\ \end{array}
$$

To end the proof, it is enough to show that

$$
\left| \left(A _ {1} \cup A _ {2} \cup \dots \cup A _ {n}\right) \cap A _ {n + 1} \right| = 0.
$$

This from the fact that $\mathbf{A}_i\cap \mathbf{A}_{n + 1}\subset \partial (\mathbf{A}_i)$

1.7.11. Recall that $\mathbf{C} = \bigcap_{n=1}^{\infty} \mathbf{E}_n$ , where $\mathbf{E}_1 = [0,1/3] \cup [2/3,1]$ , $\mathbf{E}_2 = [0,1/9] \cup [2/9,3/9] \cup [6/9,7/9] \cup [8/9,1]$ and $\mathbf{E}_n$ is obtained from $\mathbf{E}_{n-1}$ by removing open middle thirds of all $2^{n-1}$ closed intervals constituting $\mathbf{E}_{n-1}$ . It follows from the construction that no interval $[a,b], a < b,$ is contained in $\mathbf{C}$ , and therefore $|\mathbf{C}|_* = 0$ . It is also clear that $\mathbf{C}$ is contained in each $\mathbf{E}_n$ . So, $|\mathbf{C}|^* \leq |\mathbf{E}_n| = (2/3)^n \underset{n \to \infty}{\longrightarrow} 0$ .

1.7.12. It follows from the construction of $\mathbf{A}$ that no interval $[a, b]$ , $a < b$ , is contained in $\mathbf{A}$ , and therefore $|\mathbf{A}|_{\bullet} = 0$ . Moreover, $\mathbf{A}^c = [0, 1] \setminus \mathbf{A}$ is a countable union of disjoint open intervals. By the result in 2.1.2, we have $|\mathbf{A}^c|_{\bullet} = \alpha$ . So, using (1) in the solution to 1.7.4, we see that

$$
| \mathbf {A} | ^ {\bullet} = 1 - | \mathbf {A} ^ {c} | _ {\bullet} = 1 - \alpha > | \mathbf {A} | _ {\bullet}.
$$

1.7.13. The set $\mathbf{A}$ is measurable, and its Jordan measure is zero. This will follow from the fact that $|\mathbf{A} \cap [0,k]|^{\bullet} = 0$ for any positive integer $k$ . Let $\varepsilon > 0$ be given. Then there is $n_0$ such that for $n > n_0$ we have $1/(n+1) < \varepsilon/k$ . So, the union of the intervals $[1,1 + \varepsilon/k], \ldots, [k-1,k-1+\varepsilon/k]$ covers $\mathbf{A} \cap [0,k]$ except for finitely many points. Thus $|\mathbf{A} \cap [0,k]|^{\bullet} \leq (k-1)\varepsilon/k < \varepsilon$ .

1.7.14. It is clear that $|\mathbf{A}|^{\bullet} \geq 1$ . On the other hand, if an elementary set $\mathbf{E}$ is contained in $\mathbf{A}$ , then $\bigcup_{k=1}^{\infty} \mathbf{I}_k$ is an open cover of the compact set $\mathbf{E}$ . By Borel's covering theorem, there is a finite subcover. Consequently, $|\mathbf{E}| \leq \sum_{k=1}^{\infty} \frac{1}{2^{k+1}} = \frac{1}{2}$ , and therefore $|\mathbf{A}|_{\bullet} \leq 1/2$ .

1.7.15. The set $\mathbf{A}$ defined in the previous problem is open and is not Jordan measurable. Since this set is bounded, it is contained in the closed interval $\mathbf{R}$ . Consequently, $\mathbf{R} \setminus \mathbf{A}$ is a closed set which is not Jordan measurable.

1.7.16. Let $P = \{x_0, x_1, \ldots, x_n\}$ denote a partition of $[a, b]$ . Then

$$
\underline {{\int_ {a} ^ {b}}} \chi_ {\mathbf {A}} (x) d x = \sup  \sum_ {i = 1} ^ {n} m _ {i} \left(x _ {i} - x _ {i - 1}\right),
$$

where

$$
m _ {i} = \left\{ \begin{array}{l l} 1 & \text {i f} [ x _ {i - 1}, x _ {i} ] \subset A, \\ 0 & \text {o t h e r w i s e ,} \end{array} \right.
$$

and the supremum is taken over all partitions $\pmb{P}$ . Thus

$$
\underline {{\int_ {a} ^ {b}}} \chi_ {\mathbf {A}} (x) d x = \sup  \sum_ {[ x _ {i - 1}, x _ {i} ] \subset \mathbf {A}} (x _ {i} - x _ {i - 1}) = \sup  _ {\mathbf {E} \subset \mathbf {A}} | \mathbf {E} | = | \mathbf {A} | _ {\bullet}.
$$

The other equality can be proved analogously.

1.7.17. We have $\underline{\int_{a}^{b}} f(x)dx = \sup \sum_{i=1}^{n} m_{i}(x_{i} - x_{i-1})$ , where $a = x_0 < x_1 < \dots < x_n = b$ is a partition of $[a, b]$ , $m_{i} = \inf \{f(x): x_{i-1} \leq x \leq x_i\}$ and the supremum is taken over all partitions of $[a, b]$ . Since rectangles $[x_{i-1}, x_i] \times [0, m_i]$ , $i = 1, 2, \ldots, n$ , form an elementary set contained in $\mathbf{A}_f$ , we see that

$$
| \mathbf {A} _ {f} | _ {\bullet} \geq \underline {{\int_ {a} ^ {b}}} f (x) d x.
$$

On the other hand, given $\varepsilon > 0$ , there is an elementary set $\mathbf{E} \subset \mathbf{A}_f$ such that $|\mathbf{E}| > |\mathbf{A}_f|_0 - \varepsilon$ . Suppose that the elementary set $\mathbf{E}$ is a union of rectangles $[a_i, b_i] \times [c_i, d_i]$ , $i = 1, 2, \ldots, m$ . If we order all the endpoints $a_i, b_i$ , then we get a partition $P = \{t_0, t_1, \ldots, t_s\}$ of $[a, b]$ . It is clear that $\mathbf{E}$ is contained in the elementary set consisting of rectangles $[t_{i-1}, t_i] \times [0, m_i]$ , $i = 1, 2, \ldots, s$ , where $m_i = \inf \{f(x): t_{i-1} \leq x \leq t_i\}$ . Thus

$$
\underline {{\int_ {a} ^ {b}}} f (x) d x \geq | A _ {f} | _ {\bullet} - \varepsilon .
$$

The proof of the other equality is analogous.

1.7.18. Suppose that $f$ is Riemann integrable on $[a, b]$ and, contrary to our claim, $|\mathbf{J}_{\epsilon}|^{\bullet} > 0$ for some $\epsilon > 0$ . If $P = \{x_0, x_1, \ldots, x_n\}$ is a partition of $[a, b]$ , and if $\mathbf{J}_{\epsilon} \cap [x_{i-1}, x_i] \neq \emptyset$ , then $M_i - m_i \geq \epsilon$ , and

the sum of the lengths of such intervals $[x_{i-1}, x_i]$ is greater than or equal to $|\mathbf{J}_{\varepsilon}|^{\bullet}$ . Hence

$$
U (P, f) - L (P, f) = \sum_ {i = 1} ^ {n} \left(M _ {i} - m _ {i}\right) \left(x _ {i} - x _ {i - 1}\right) \geq \varepsilon | \mathbf {J} _ {\epsilon} | ^ {*},
$$

which contradicts the Riemann integrability of $f$ (see Theorem 1 in 1.1). Now we prove the necessity of the condition. Let $\varepsilon > 0$ be given. Since $|\mathbf{J}_\varepsilon|^* = 0$ , there are finitely many separate subintervals covering $\mathbf{J}_\varepsilon$ whose sum of lengths is less than $\varepsilon$ . Consider the partition $P_0 = \{x_0, x_1, \ldots, x_n\}$ formed by the endpoints of these subintervals. If the interval $[x_{i-1}, x_i]$ contains no points of $\mathbf{J}_\varepsilon$ , then $o_f(x) < \varepsilon$ for $x \in [x_{i-1}, x_i]$ . It follows from the definition of $o_f(x)$ that there is $\delta_x$ such that $\text{diam} f(x - \delta_x, x + \delta_x) < o_f(x) + (\varepsilon - o_f(x)) = \varepsilon$ . The open intervals $(x - \delta_x, x + \delta_x)$ cover $[x_{i-1}, x_i]$ , so by Borel's covering theorem there is a finite subcover. This implies that $[x_{i-1}, x_i]$ can be divided into finitely many closed subintervals on which the oscillation of $f$ is less than $\varepsilon$ . In this way we obtain a refinement $P = \{t_0, t_1, \ldots, t_m\}$ of $P_0$ . Moreover,

$$
U (P, f) - L (P, f) = \sum_ {i = 1} ^ {m} \left(M _ {i} - m _ {i}\right) \left(t _ {i} - t _ {i - 1}\right) = S _ {1} + S _ {2},
$$

where $S_{1}$ contains the terms coming from subintervals containing points of $\mathbf{J}_{\varepsilon}$ and $S_{2}$ contains the remaining terms. If

$$
(M _ {i} - m _ {i}) \left(t _ {i} - t _ {i - 1}\right)
$$

is a term of $S_{2}$ , then $M_{i} - m_{i} < \varepsilon$ and therefore $S_{2} < \varepsilon (b - a)$ . For $S_{1}$ we have the estimate $S_{1} \leq (M - m)\varepsilon$ , where $m$ and $M$ are the infimum and supremum of $f$ on $[a,b]$ . Hence

$$
U (P, f) - L (P, f) <   \varepsilon (M - m + b - a),
$$

which proves, by Theorem 1 in 1.1, the Riemann integrability of $f$ .

1.7.19. If $\mathbf{A}$ is Jordan measurable, then, by definition, there exist sequences of elementary sets satisfying the condition. Now assume that there exist sequences $\{\mathbf{B}_n\}$ and $\{\mathbf{C}_n\}$ of Jordan measurable sets such that $\mathbf{B}_n \subset \mathbf{A} \subset \mathbf{C}_n$ and $\lim_{n \to \infty} |\mathbf{B}_n| = \lim_{n \to \infty} |\mathbf{C}_n| = L$ . Then, given $\varepsilon > 0$ , there is $n_0$ such that $|L - |\mathbf{B}_n|| < \varepsilon / 4$ and $|L - |\mathbf{C}_n|| < \varepsilon / 4$ for $n \geq n_0$ . Moreover, since $\mathbf{B}_n$ and $\mathbf{C}_n$ are Jordan measurable, there are

elementary sets $\mathbf{E}_n \subset \mathbf{B}_n$ and $\mathbf{E}_n' \supset \mathbf{C}_n$ such that $|\mathbf{B}_n| - |\mathbf{E}_n| < \varepsilon / 4$ and $|\mathbf{E}_n'| - |\mathbf{C}_n| < \varepsilon / 4$ . It then follows, by the result in 1.7.1, that $\mathbf{A}$ is Jordan measurable and $|\mathbf{A}| = L$ .

1.7.20. We will use the results given in 1.7.17 and 1.7.19. Define

$$
\mathbf {B} _ {0} = \left\{(x, y) \in \mathbb {R} ^ {2}: \frac {1}{\pi} \leq x \leq 1, 0 \leq y \leq \left| \sin \frac {1}{x} \right| \right\}
$$

and for $n\in \mathbb{N}$

$$
\mathbf {B} _ {n} = \left\{(x, y) \in \mathbb {R} ^ {2}: \frac {1}{(n + 1) \pi} \leq x \leq \frac {1}{n \pi}, 0 \leq y \leq \left| \sin \frac {1}{x} \right| \right\}.
$$

Then each $\mathbf{B}_n$ is Jordan measurable, and

$$
| \mathbf {B} _ {0} | = \int_ {\frac {1}{\pi}} ^ {1} \left| \sin \frac {1}{x} \right| d x, \quad | \mathbf {B} _ {n} | = \int_ {\frac {1}{(n + 1) \pi}} ^ {\frac {1}{n \pi}} \left| \sin \frac {1}{x} \right| d x.
$$

Moreover,

$$
\mathbf {B} _ {0} \cup \mathbf {B} _ {1} \cup \dots \cup \mathbf {B} _ {n} \subset \mathbf {A} \subset \mathbf {B} _ {0} \cup \mathbf {B} _ {1} \cup \dots \cup \mathbf {B} _ {n} \cup \mathbf {D} _ {n}
$$

with $\mathbf{D}_n = \{(x,y)\in \mathbb{R}^2:0\leq x\leq \frac{1}{n\pi}, 0\leq y\leq 1\}$ . Since

$$
\left| \mathbf {B} _ {0} \cup \mathbf {B} _ {1} \cup \dots \cup \mathbf {B} _ {n} \cup \mathbf {D} _ {n} \right| - \left| \mathbf {B} _ {0} \cup \mathbf {B} _ {1} \cup \dots \cup \mathbf {B} _ {n} \right| = \left| \mathbf {D} _ {n} \right| = \frac {1}{n \pi},
$$

the result follows.

1.7.21. It suffices to show the Jordan measurability of $\mathbf{B} = \bigcup_{n=1}^{\infty} \mathbf{K}_n$ . Note that the $\mathbf{K}_n$ are pairwise disjoint and

$$
\mathbf {B} _ {n} = \bigcup_ {k = 1} ^ {n} \mathbf {K} _ {k} \subset \mathbf {B} \subset \mathbf {B} _ {n} \cup \mathbf {D} _ {n} = \mathbf {C} _ {n}
$$

with $\mathbf{D}_n = \left\{(x,y)\in \mathbb{R}^2:0\leq x\leq \frac{1}{n}, - \frac{1}{4^n}\leq y\leq \frac{1}{4^n}\right\}$ . Now, since $|\mathbf{D}_n|$ tends to zero as $n\to \infty$ , the result follows from 1.7.19.

1.7.22. The Jordan measurability of the set $\mathbf{A}$ will follow from the result stated in 1.7.19. For a partition $\alpha = \theta_0 < \theta_1 < \dots < \theta_n = \beta$ , put $m_i = \min \{f(\theta) : \theta_{i-1} \leq \theta \leq \theta_i\}$ , and $M_i = \max \{f(\theta) : \theta_{i-1} \leq \theta \leq \theta_i\}$ , $i = 1, \ldots, n$ , and consider the sectors

$$
\begin{array}{l} \mathbf {S} _ {i} = \left\{\left(r, \theta\right): 0 \leq r \leq m _ {i}, \theta_ {i - 1} \leq \theta \leq \theta_ {i} \right\}, \\ \mathbf {S} _ {i} ^ {\prime} = \left\{\left(r, \theta\right): 0 \leq r \leq M _ {i}, \theta_ {i - 1} \leq \theta \leq \theta_ {i} \right\}. \\ \end{array}
$$

![](images/153ab510d78fa82f9f3a8245611eeebcf671359c2949da4abe16254f6d5d633b.jpg)

If $\mathbf{B}_n = \bigcup_{i=1}^{n} \mathbf{S}_i$ and $\dot{\mathbf{C}}_n = \bigcup_{i=1}^{n} \mathbf{S}_i'$ , then $\mathbf{B}_n$ and $\mathbf{C}_n$ are Jordan measurable sets such that $\mathbf{B}_n \subset \mathbf{A} \subset \mathbf{C}_n$ . Moreover,

$$
| B _ {n} | = \frac {1}{2} \sum_ {i = 1} ^ {n} m _ {i} ^ {2} \left(\theta_ {i} - \theta_ {i - 1}\right), \quad | C _ {n} | = \frac {1}{2} \sum_ {i = 1} ^ {n} M _ {i} ^ {2} \left(\theta_ {i} - \theta_ {i - 1}\right).
$$

Since $f$ is continuous, taking a sequence of partitions whose meshes tend to zero, we conclude the proof.

# 1.7.23. We have

$$
| \mathbf {A} | = \frac {1}{2} a ^ {2} \int_ {- \pi / 4} ^ {\pi / 4} \cos (2 \theta) d \theta = \frac {1}{2} a ^ {2},
$$

and the figure shows the case $a = 1$

![](images/db129b0b072bac72d3df449809ea2544f491694ff8ab91c92f6adf1aecfe6998.jpg)

1.7.24. Using the result in 1.7.22, we get

$$
| \mathbf {A} | = \frac {1}{2} a ^ {2} \int_ {- \pi / 3} ^ {\pi / 3} (1 + \cos (3 \theta)) ^ {2} d \theta = \frac {1}{2} \pi a ^ {2}.
$$

![](images/0699aa11cace46fbf0adb2fa568b3e01d24ab75fe7a53209daf4666e5d411432.jpg)

1.7.25. Consider first the case $a \geq b$ . The possibilities are illustrated in the two figures below.

![](images/470ed6536ef86f6b501c34c2031f0edc5281da7e67c37999ee199934cd9424d4.jpg)

![](images/e67b71573d0bc093c1a3a6358a76c6aaea9f0496115434e4ae2b27a1313c50b3.jpg)

Then, by the symmetry,

$$
| \mathbf {A} | = \int_ {0} ^ {\pi} (a + b \cos \theta) ^ {2} d \theta = \frac {\pi}{2} (2 a ^ {2} + b ^ {2}).
$$

Recall that, in using polar coordinates, $\pmb{r}$ is the directed distance of a point from the origin (or pole). If $r < 0$ , then coordinates $(r, \theta)$ and $(|r|, \theta + \pi)$ represent the same point. Now consider the case $a < b$ . The equation $a + b\cos \theta = 0$ has two solutions in $[0, 2\pi]$ : $\theta_{1} = \arccos(-a / b)$ and $\theta_{2} = 2\pi - \arccos(-a / b)$ . If $\theta \in [0, \theta_{1}]$ , then $r$ is nonnegative and we get the upper half of the outer loop of the limacon. The inner loop of the limacon corresponds to values of theta between $\theta_{1}$ and $\theta_{2}$ where $r$ is negative.

![](images/43e9579b524aa085c949fec022102eab7322123cf360656aabe996637feae64d.jpg)

Hence the area bounded by the inner loop is

$$
\begin{array}{l} \left| \mathbf {A} _ {1} \right| = \frac {1}{2} \int_ {\theta_ {1}} ^ {\theta_ {2}} (a + b \cos \theta) ^ {2} d \theta \\ = \frac {1}{2} \left(- 3 a \sqrt {b ^ {2} - a ^ {2}} + (b ^ {2} + 2 a ^ {2}) (\pi - \arccos (- a / b))\right). \\ \end{array}
$$

By the symmetry, the area bounded by the outer loop of the limacon is

$$
\begin{array}{l} \left| A _ {2} \right| = \int_ {0} ^ {\theta_ {1}} (a + b \cos \theta) ^ {2} d \theta \\ = \frac {1}{2} \left((2 a ^ {2} + b ^ {2}) \arccos  (- a / b) + 3 a \sqrt {b ^ {2} - a ^ {2}}\right). \\ \end{array}
$$

1.7.26. Transformation to polar coordinates gives

$$
r \left(\sin^ {5} \theta + \cos^ {5} \theta\right) = 5 a \sin^ {2} \theta \cos^ {2} \theta .
$$

The curve has one loop, which corresponds to values of $\theta$ between 0 and $\pi /2$ . Therefore

$$
\begin{array}{l} | \mathbf {A} | = \frac {2 5}{2} a ^ {2} \int_ {0} ^ {\pi / 2} \frac {\sin^ {4} \theta \cos^ {4} \theta}{(\sin^ {5} \theta + \cos^ {5} \theta) ^ {2}} d \theta \\ = \frac {2 5}{2} a ^ {2} \int_ {0} ^ {\pi / 2} \frac {\tan^ {4} \theta}{(1 + \tan^ {5} \theta) ^ {2} \cos^ {2} \theta} d \theta \\ = \frac {5}{2} a ^ {2} \int_ {0} ^ {\infty} \frac {5 u ^ {4}}{(1 + u ^ {5}) ^ {2}} d u = \frac {5}{2} a ^ {2} \int_ {1} ^ {\infty} \frac {d v}{v ^ {2}} \\ = \frac {5}{2} a ^ {2}. \\ \end{array}
$$

![](images/a440e53792a16154c6a780d44ff0acf25ec2628b3499a9fbcbe34ce5acd83f57.jpg)

1.7.27. The points of intersection of the limacon and the circle are given by $\cos \theta = 1 / 2$ .

![](images/0553368b3ac8c38acd93f40131da91eb593219d305a2918f04903d824b3e2fb8.jpg)

Thus, by the symmetry,

$$
| \mathbf {A} | = \int_ {0} ^ {\pi / 3} ((1 + 2 \cos \theta) ^ {2} - 2 ^ {2}) d \theta = \frac {5}{2} \sqrt {3} - \frac {\pi}{3}.
$$

1.7.28. To prove the formula, take a partition $a = x_0 < x_1 < \dots < x_n = b$ and put $m_i = \min \{f(x) : x \in [x_{i-1}, x_i]\}$ , $M_i = \max \{f(x) : x \in [x_{i-1}, x_i]\}$ . Let $B_n$ be the union of the $n$ cylinders obtained by revolving around the $x$ -axis the rectangles $[x_{i-1}, x_i] \times [0, m_i]$ , and let $C_n$ denote the union of the $n$ cylinders obtained by revolving the rectangles $[x_{i-1}, x_i] \times [0, M_i]$ . Since $f$ is Riemann integrable on $[a, b]$ , by 1.7.19,

$$
| V | = \pi \int_ {a} ^ {b} f ^ {2} (x) d x.
$$

![](images/642f6e1af45fdd1634cb3ae99b0dae45e3598e01bf8bebb1252cb584b88911c3.jpg)

![](images/380e466d8a1015686a33c1732531f9aa120b8782430b139af860c141b0f19ec3.jpg)

1.7.29. As in the solution of the previous result, we begin with a partition $a = x_0 < x_1 < \dots < x_n = b$ and consider the rectangles $[x_{i-1}, x_i] \times [0, m_i]$ and $[x_{i-1}, x_i] \times [0, M_i]$ , where $m_i = \min\{f(x): x \in [x_{i-1}, x_i]\}$ , $M_i = \max\{f(x): x \in [x_{i-1}, x_i]\}$ . When these rectangles are revolved about the $y$ -axis they sweep out cylindrical shells whose volumes are $\pi m_i (x_i^2 - x_{i-1}^2)$ and $\pi M_i (x_i^2 - x_{i-1}^2)$ , respectively. Since the Riemann-Stieltjes integral $\pi \int_a^b f(x) d(x^2)$ exists and is equal to $2\pi \int_a^b xf(x) dx$ , the desired result follows.

![](images/1dde0465c0fb94342721cb0ead54f661037d8eab19d6624c14932c9f09bdb991.jpg)

![](images/1319e7310188f6ed631332493638fd0fc9ca8ec239bcaa2ef2d16de354b7f59e.jpg)

1.7.30. By the result in 1.7.29, using symmetry, we get

$$
\begin{array}{l} | V | = 4 \pi \int_ {a - r} ^ {a + r} x \sqrt {r ^ {2} - (x - a) ^ {2}} d x \\ = 4 \pi \int_ {a - r} ^ {a + r} (x - a) \sqrt {r ^ {2} - (x - a) ^ {2}} d x \\ + 4 \pi a \int_ {a - r} ^ {a + r} \sqrt {r ^ {2} - (x - a) ^ {2}} d x \\ = 4 \pi a \int_ {a - r} ^ {a + r} \sqrt {r ^ {2} - (x - a) ^ {2}} d x = 2 \pi^ {2} a r ^ {2}. \\ \end{array}
$$

1.7.31. The volume is

$$
\begin{array}{l} | \mathbf {V} | = \sum_ {k = 0} ^ {\infty} \pi \int_ {2 k \pi} ^ {(2 k + 1) \pi} e ^ {- 2 x} \sin x d x = \frac {\pi}{5} \sum_ {k = 0} ^ {\infty} e ^ {- 4 k \pi} (1 + e ^ {- 2 \pi}) \\ = \frac {\pi}{5 (1 - e ^ {- 2 \pi})}. \\ \end{array}
$$

1.7.32. The parametric equation of the ellipse is

$$
\boldsymbol {x} = a \cos t, \quad \boldsymbol {y} = b \sin t, \quad 0 \leq t \leq 2 \pi .
$$

So

$$
\begin{array}{l} L = \int_ {0} ^ {2 \pi} \sqrt {\left(x ^ {\prime} (t)\right) ^ {2} + \left(y ^ {\prime} (t)\right) ^ {2}} d t = 4 \int_ {0} ^ {\pi / 2} \sqrt {a ^ {2} \sin^ {2} t + b ^ {2} \cos^ {2} t} d t \\ = 4 \int_ {0} ^ {\pi / 4} \sqrt {a ^ {2} \sin^ {2} t + b ^ {2} \cos^ {2} t} d t + 4 \int_ {\pi / 4} ^ {\pi / 2} \sqrt {a ^ {2} \sin^ {2} t + b ^ {2} \cos^ {2} t} d t. \\ \end{array}
$$

If we substitute $t = \pi / 2 - s$ in the last integral, we get

$$
L = 4 \int_ {0} ^ {\pi / 4} \left(\sqrt {a ^ {2} \sin^ {2} t + b ^ {2} \cos^ {2} t} + \sqrt {a ^ {2} \cos^ {2} t + b ^ {2} \sin^ {2} t}\right) d t.
$$

Calculation shows that the integrand is a monotonically increasing function on $[0, \pi / 4]$ . Therefore the desired estimates follow.

1.7.33. The length of the ellipse is

$$
\begin{array}{l} L = \int_ {0} ^ {2 \pi} \sqrt {\left(x ^ {\prime} (t)\right) ^ {2} + \left(y ^ {\prime} (t)\right) ^ {2}} d t = 4 \int_ {0} ^ {\pi / 2} \sqrt {a ^ {2} - \left(a ^ {2} - b ^ {2}\right) \cos^ {2} t} d t \\ = 4 a \int_ {0} ^ {\pi / 2} \sqrt {1 - e ^ {2} \cos^ {2} t} d t. \\ \end{array}
$$

By the Newton binomial formula (see, e.g., II, 3.4.4), if $|u| < 1$ , then

$$
\begin{array}{l} \sqrt {1 - u} = 1 + \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} \frac {\frac {1}{2} \left(\frac {1}{2} - 1\right) \dots \left(\frac {1}{2} - n + 1\right)}{n !} u ^ {n} \\ = 1 - \sum_ {n = 1} ^ {\infty} \frac {(2 n - 3) ! !}{(2 n) ! !} u ^ {n}. \\ \end{array}
$$

Putting $u = e\cos t$ , we get

$$
L = 4 a \left(\frac {\pi}{2} - \sum_ {n = 1} ^ {\infty} \frac {(2 n - 3) ! !}{(2 n) ! !} e ^ {2 n} \int_ {0} ^ {\pi / 2} \cos^ {2 n} t d t\right),
$$

because the series converges uniformly on $[0,\pi /2]$ . By 1.4.1(b),

$$
\int_ {0} ^ {\pi / 2} \cos^ {2 n} t d t = \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {\dot {\pi}}{2},
$$

and the desired result follows.

1.7.34. The parametric equation of the curve is

$$
\boldsymbol {x} = f (\theta) \cos \theta , \quad y = f (\theta) \sin \theta , \quad \alpha \leq \theta \leq \beta .
$$

Hence

$$
L = \int_ {a} ^ {\beta} \sqrt {(f (\theta)) ^ {2} + (f ^ {\prime} (\theta)) ^ {2}} d \theta .
$$

1.7.35. (a) We will apply the formula given in the previous problem. We have

$$
L = a \int_ {0} ^ {3 \pi} \sin^ {2} \frac {\theta}{3} d \theta = \frac {3 \pi a}{2}.
$$

![](images/738529013add5427c9c762a6e7e4187fa0872e2b0a969749c9c202a05ccfc88b.jpg)

(b) The parametric equation of the curve is

$$
x = \frac {1}{1 + \cos \theta} \cos \theta , \quad y = \frac {1}{1 + \cos \theta} \sin \theta , \quad \theta \in \left[ - \frac {\pi}{2}, \frac {\pi}{2} \right].
$$

One can easily check that the curve is an arc of the parabola $y^2 = 1 - 2x$ , $y \in [-1,1]$ . So its length is

$$
L = \int_ {- 1} ^ {1} \sqrt {1 + y ^ {2}} d y = \ln (1 + \sqrt {2}) + \sqrt {2}.
$$

![](images/6d65291ac51faeaee2b56dcaea75f1bc27bac40341499b4a9e4c90556dffcb2b.jpg)

1.7.36. Observe that if a curve has an equation $\theta = g(r)$ , $a \leq r \leq b$ , and $g$ is continuously differentiable on $[a, b]$ , then, as in 1.7.34, one can derive the following formula for its length:

$$
L = \int_ {a} ^ {b} \sqrt {1 + (r g ^ {\prime} (r)) ^ {2}} d r.
$$

Hence the length of the given curve is

$$
L = \int_ {1} ^ {3} \sqrt {1 + \left(\frac {1}{2} \left(r - \frac {1}{r}\right)\right) ^ {2}} d r = \frac {1}{2} \int_ {1} ^ {3} \left(r + \frac {1}{r}\right) d r = \frac {1}{2} (\ln 3 + 4).
$$

1.7.37. The parametric equation of the curve is

$$
x = (1 + \cos t) \cos \left(t - \tan \frac {t}{2}\right), \quad y = (1 + \cos t) \sin \left(t - \tan \frac {t}{2}\right),
$$

where $t \in [0, \beta]$ . Hence

$$
\begin{array}{l} L = \int_ {0} ^ {\beta} \sqrt {x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}} d t \\ = \int_ {0} ^ {\beta} \sqrt {\sin^ {2} t + (1 + \cos t) ^ {2} \left(1 - \frac {1}{2 \cos^ {2} \frac {t}{2}}\right) ^ {2}} d t = \int_ {0} ^ {\beta} d t = \beta . \\ \end{array}
$$

# Chapter 2

# The Lebesgue Integral

# 2.1. Lebesgue Measure on the Real Line

2.1.1. For any set $\mathbf{E} \subset \mathbb{R}$ we have $m^{\bullet}(\mathbf{E} \cap \mathbf{A}) \leq m^{\bullet}(\mathbf{A}) = 0$ and $m^{\bullet}(\mathbf{E} \setminus \mathbf{A}) \leq m^{\bullet}(\mathbf{E})$ . Thus $m^{\bullet}(\mathbf{E}) \geq m^{\bullet}(\mathbf{E} \cap \mathbf{A}) + m^{\bullet}(\mathbf{E} \setminus \mathbf{A})$ .

2.1.2. We know that each interval $\mathbf{I}$ is measurable and its Lebesgue measure $m(\mathbf{I})$ is equal to its length, which is also its Jordan measure $|\mathbf{I}|$ . Thus $\mathbf{S} = \bigcup_{n=1}^{\infty} \mathbf{I}_n$ is a measurable set. We know also that $\mathbf{S}$ can be represented, in infinitely many ways, in the form $\mathbf{S} = \bigcup_{n=1}^{\infty} \mathbf{J}_n$ , where the $\mathbf{J}_n$ are pairwise separate closed intervals. Moreover, if $\bigcup_{n=1}^{\infty} \mathbf{J}_n \subset \bigcup_{n=1}^{\infty} \mathbf{I}_n$ , where the $\mathbf{J}_n$ are pairwise separate, then $\sum_{n=1}^{\infty} |\mathbf{J}_n| \leq \sum_{n=1}^{\infty} |\mathbf{I}_n|$ . To show this, let $\varepsilon > 0$ be given and let $\mathbf{I}_n'$ be an open interval concentric with $\mathbf{I}_n$ and such that $|\mathbf{I}_n'| = |\mathbf{I}_n| + 2^{-n}\varepsilon$ . If $\mathbf{S}_N = \bigcup_{k=1}^{N} \mathbf{J}_k$ , then $\mathbf{S}_N$ is covered by $\bigcup_{n=1}^{\infty} \mathbf{I}_n'$ , and by Borel's covering theorem, there is a finite subcover $\bigcup_{k=1}^{n_N} \mathbf{I}_k'$ . Thus, for every positive integer $N$ , by 1.7.2,

$$
| \mathbf {S} _ {N} | = \sum_ {k = 1} ^ {N} | \mathbf {J} _ {k} | \leq \sum_ {k = 1} ^ {k _ {N}} | \mathbf {I} _ {k} ^ {\prime} | \leq \sum_ {k = 1} ^ {\infty} | \mathbf {I} _ {k} ^ {\prime} | = \sum_ {k = 1} ^ {\infty} | \mathbf {I} _ {k} | + \varepsilon .
$$

(Recall that $|\mathbf{A}|$ denotes the Jordan measure of $\mathbf{A} \subset \mathbb{R}$ .) This shows that $m(\mathbf{S}) = \sum_{k=1}^{\infty} |\mathbf{J}_k|$ and $m(\mathbf{S})$ does not depend on the choice of the $\mathbf{J}_k$ . If $\mathbf{E}$ is a finite union of separate closed intervals and $\mathbf{E} \subset \mathbf{S}$ ,

then $|\mathbf{E}| \leq m(\mathbf{S})$ , which shows that $|\mathbf{S}|_{\bullet} \leq m(\mathbf{S})$ . On the other hand, $\mathbf{S}_N = \bigcup_{k=1}^{N} \mathbf{J}_k \subset \mathbf{S}$ and $\{\mathbf{S}_N\}$ is a sequence of elementary sets such that $|\mathbf{S}_N| \to m(\mathbf{S})$ as $N \to \infty$ , so that $|\mathbf{S}|_{\bullet} \geq m(\mathbf{S})$ .

2.1.3. It follows from the result in the previous problem and from (2) in the solution to 1.7.3 that

$$
m \left(\mathbf {S} _ {1} \cup \mathbf {S} _ {2}\right) + m \left(\mathbf {S} _ {1} \cap \mathbf {S} _ {2}\right) \geq m \left(\mathbf {S} _ {1}\right) + m \left(\mathbf {S} _ {2}\right).
$$

The opposite inequality is certainly true when $m(\mathbf{S}_1)$ or $m(\mathbf{S}_2)$ is infinite. If both are finite, we put

$$
\mathbf {S} _ {1} = \bigcup_ {n = 1} ^ {\infty} \mathbf {J} _ {n} \quad \text {a n d} \quad \mathbf {S} _ {2} = \bigcup_ {n = 1} ^ {\infty} \mathbf {J} _ {n} ^ {\prime},
$$

where $\{\mathbf{J}_n\}$ and $\{\mathbf{J}_n^{\prime}\}$ are two sequences of pairwise separate closed intervals, so that

$$
m \left(\mathbf {S} _ {1}\right) = \sum_ {n = 1} ^ {\infty} \left| \mathbf {J} _ {n} \right| \quad \text {a n d} \quad m \left(\mathbf {S} _ {2}\right) = \sum_ {n = 1} ^ {\infty} \left| \mathbf {J} _ {n} ^ {\prime} \right|.
$$

Since

$$
S _ {1} \cup S _ {2} = \bigcup_ {n = 1} ^ {N} J _ {n} \cup \bigcup_ {n = 1} ^ {N} J _ {n} ^ {\prime} \cup \bigcup_ {n = N + 1} ^ {\infty} J _ {n} \cup \bigcup_ {n = N + 1} ^ {\infty} J _ {n} ^ {\prime}
$$

and

$$
\mathbf {S} _ {1} \cap \mathbf {S} _ {2} \subset \left(\bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} \cap \bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} ^ {\prime}\right) \cup \bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n} \cup \bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n} ^ {\prime},
$$

we obtain

$$
m \left(\mathbf {S} _ {1} \cup \mathbf {S} _ {2}\right) \leq \left| \bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} \cup \bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} ^ {\prime} \right| + m \left(\bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n}\right) + m \left(\bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n} ^ {\prime}\right)
$$

and

$$
m \left(\mathbf {S} _ {1} \cap \mathbf {S} _ {2}\right) \leq \left| \bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} \cap \bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} ^ {\prime} \right| + m \left(\bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n}\right) + m \left(\bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n} ^ {\prime}\right).
$$

Consequently, by 1.7.3 and by the solution to 2.1.2,

$$
\begin{array}{l} m \left(\mathrm {S} _ {1} \cup \mathrm {S} _ {2}\right) + m \left(\mathrm {S} _ {1} \cap \mathrm {S} _ {2}\right) \\ \leq \left| \bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} \right| + \left| \bigcup_ {n = 1} ^ {N} \mathbf {J} _ {n} ^ {\prime} \right| + 2 \left(m \left(\bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n}\right) + m \left(\bigcup_ {n = N + 1} ^ {\infty} \mathbf {J} _ {n} ^ {\prime}\right)\right) \\ = \sum_ {n = 1} ^ {N} | \mathbf {J} _ {n} | + \sum_ {n = 1} ^ {N} | \mathbf {J} _ {n} ^ {\prime} | + 2 \left(\sum_ {n = N + 1} ^ {\infty} | \mathbf {J} _ {n} | + \sum_ {n = N + 1} ^ {\infty} | \mathbf {J} _ {n} ^ {\prime} |\right). \\ \end{array}
$$

Since the last term tends to zero as $N \to \infty$ , we get the desired opposite inequality.

2.1.4. Let $\mathbf{S}_1 = \bigcup_{n=1}^{\infty} \mathbf{I}_n$ and $\mathbf{S}_2 = \bigcup_{n=1}^{\infty} \mathbf{I}_n'$ be coverings by closed intervals of $\mathbf{A}$ and $\mathbf{B}$ , respectively. Then $\mathbf{A} \cup \mathbf{B} \subset \mathbf{S}_1 \cup \mathbf{S}_2$ and $\mathbf{A} \cap \mathbf{B} \subset \mathbf{S}_1 \cap \mathbf{S}_2$ . Hence, by the result in the previous problem,

$$
m ^ {*} (\mathbf {A} \cup \mathbf {B}) + m ^ {*} (\mathbf {A} \cap \mathbf {B}) \leq m (\mathbf {S} _ {1} \cup \mathbf {S} _ {2}) + m (\mathbf {S} _ {1} \cap \mathbf {S} _ {2}) = m (\mathbf {S} _ {1}) + m (\mathbf {S} _ {2}).
$$

Taking the infimum over all coverings $\mathbf{S}_1$ of $\mathbf{A}$ and then the infimum over all coverings $\mathbf{S}_2$ of $\mathbf{B}$ , the desired inequality follows.

2.1.5. Since $\mathbf{G}$ is measurable, the Carathéodory condition implies that

$$
m ^ {*} (\mathbf {A} \cup \mathbf {B}) = m ^ {*} ((\mathbf {A} \cup \mathbf {B}) \cap \mathbf {G}) + m ^ {*} ((\mathbf {A} \cup \mathbf {B}) \backslash \mathbf {G}) = m ^ {*} (\mathbf {A}) + m ^ {*} (\mathbf {B}).
$$

Note that $\mathbf{G}$ can be replaced by any measurable set.

2.1.6. Assume that $d(\mathbf{A}, \mathbf{B}) = \eta > 0$ . Then the set

$$
\mathbf {G} = \bigcup_ {x \in A} (x - \eta / 2, x + \eta / 2)
$$

is an open superset of $\mathbf{A}$ disjoint from $\mathbf{B}$ . Thus the result is an immediate consequence of the previous problem.

2.1.7. We have

$$
m ^ {*} (\mathbf {B}) \leq m ^ {*} (\mathbf {A} \cup \mathbf {B}) \leq m ^ {*} (\mathbf {A}) + m ^ {*} (\mathbf {B}) = m ^ {*} (\mathbf {B}),
$$

which gives $m^{*}(\mathbf{A} \cup \mathbf{B}) = m^{*}(\mathbf{B})$ . Since $\mathbf{B} = (\mathbf{B} \setminus \mathbf{A}) \cup (\mathbf{A} \cap \mathbf{B})$ and $m^{*}(\mathbf{A} \cap \mathbf{B}) = 0$ , by the above $m^{*}(\mathbf{B} \setminus \mathbf{A}) = m^{*}(\mathbf{B})$ .

2.1.8. By the Carathéodory condition,

$$
m ^ {*} (\mathbf {B}) = m ^ {*} (\mathbf {B} \cap \mathbf {A}) + m ^ {*} (\mathbf {B} \setminus \mathbf {A}) = m (\mathbf {A}) + m ^ {*} (\mathbf {B} \setminus \mathbf {A}).
$$

2.1.9. By the additivity of the Lebesgue measure $m$ ,

$$
\begin{array}{l} m (\mathbf {A} \cup \mathbf {B}) + m (\mathbf {A} \cap \mathbf {B}) = (m (\mathbf {A} \setminus \mathbf {B}) + m (\mathbf {A} \cap \mathbf {B})) \\ + (m (\mathbf {B} \backslash \mathbf {A}) + m (\mathbf {A} \cap \mathbf {B})) \\ = m (\mathbf {A}) + m (\mathbf {B}). \\ \end{array}
$$

2.1.10. By the Carathéodory condition and by assumption,

$$
m (\mathbf {A} _ {1}) = m ^ {\bullet} (\mathbf {A}) = m ^ {\bullet} (\mathbf {A} \backslash \mathbf {A} _ {1}) + m ^ {\bullet} (\mathbf {A} \cap \mathbf {A} _ {1}) = m ^ {\bullet} (\mathbf {A} \backslash \mathbf {A} _ {1}) + m (\mathbf {A} _ {1}).
$$

Since $m(\mathbf{A}_1) < \infty$ , we see that $m^*(\mathbf{A} \setminus \mathbf{A}_1) = 0$ . Hence, by 2.1.1 and 2.1.7, for any set $\mathbf{B}$ ,

$$
m ^ {\bullet} (\mathbf {B}) = m ^ {\bullet} (\mathbf {B} \setminus \mathbf {A} _ {1}) + m ^ {\bullet} (\mathbf {B} \cap \mathbf {A} _ {1}) = m ^ {\bullet} (\mathbf {B} \setminus \mathbf {A}) + m ^ {\bullet} (\mathbf {B} \cap \mathbf {A}).
$$

The last equality follows from the fact that the sets $\mathbf{B} \setminus \mathbf{A}_1$ and $\mathbf{B} \setminus \mathbf{A}$ as well as the sets $\mathbf{B} \cap \mathbf{A}_1$ and $\mathbf{B} \cap \mathbf{A}$ differ by sets of outer measure zero.

2.1.11. It is enough to consider the case $m^{\bullet}(\mathbf{A}) < +\infty$ . It follows from the definition of outer measure that, given $\varepsilon > 0$ , there is a cover $\bigcup_{k=1}^{\infty} \mathbf{I}_k$ of $\mathbf{A}$ such that $\sum_{k=1}^{\infty} |\mathbf{I}_k| \leq m^{\bullet}(\mathbf{A}) + \varepsilon/2$ . If $\mathbf{I}_k'$ is an open interval concentric with $\mathbf{I}_k$ and such that $|\mathbf{I}_k'| = |\mathbf{I}_k| + 2^{-k-1}\varepsilon$ , then $\mathbf{G} = \bigcup_{k=1}^{\infty} \mathbf{I}_k'$ is an open set containing $\mathbf{A}$ and $m(\mathbf{G}) \leq \sum_{k=1}^{\infty} |\mathbf{I}_k'| \leq m^{\bullet}(\mathbf{A}) + \varepsilon$ . To prove the other statement, for $n \in \mathbb{N}$ , we take an open set $\mathbf{G}_n$ containing $\mathbf{A}$ and such that $m(\mathbf{G}_n) \leq m^{\bullet}(\mathbf{A}) + 1/n$ , and we put $\mathbf{A}_2 = \bigcap_{n=1}^{\infty} \mathbf{G}_n$ .

2.1.12. We first show that (i) implies (ii). If $m(\mathbf{A}) < \infty$ , then the implication follows from 2.1.11 and 2.1.8. If $m(\mathbf{A}) = \infty$ , then $\mathbf{A} = \bigcup_{n=1}^{\infty} \mathbf{A}_n$ , where $\mathbf{A}_n = \mathbf{A} \cap [-n, n]$ . Since $m(\mathbf{A}_n) < \infty$ , there is an open set $\mathbf{G}_n$ such that $\mathbf{A}_n \subset \mathbf{G}_n$ and $m(\mathbf{G}_n \setminus \mathbf{A}_n) < \varepsilon/(2^n)$ . If $\mathbf{G} = \bigcup_{n=1}^{\infty} \mathbf{G}_n$ , then $\mathbf{A} \subset \mathbf{G}$ and $\mathbf{G} \setminus \mathbf{A} \subset \bigcup_{n=1}^{\infty} (\mathbf{G}_n \setminus \mathbf{A}_n)$ . Consequently, $m(\mathbf{G} \setminus \mathbf{A}) \leq \sum_{n=1}^{\infty} \varepsilon/(2^n) = \varepsilon$ . To see that (iii) follows from (ii) it suffices to proceed as in the solution to the second statement in 2.1.11. Now we show that (iii) implies (i). If (iii) is satisfied, then the set $\mathbf{A} = \mathbf{U} \setminus (\mathbf{U} \setminus \mathbf{A})$ is measurable, as a difference of two measurable sets (see 2.1.1). So, the first three conditions are equivalent.

To see that (i) implies (iv), note that if $\mathbf{A}$ is measurable, then so is $\mathbf{A}^c$ . By (ii) there is an open set $\mathbf{G} \supset \mathbf{A}^c$ such that $m^*(\mathbf{G} \setminus \mathbf{A}^c) < \varepsilon$ . Hence $\mathbf{F} = \mathbb{R} \setminus \mathbf{G}$ is a closed subset of $\mathbf{A}$ and $m^*(\mathbf{A} \setminus \mathbf{F}) = m^*(\mathbf{G} \setminus \mathbf{A}^c) < \varepsilon$ . To show that (iv) implies (v), for $n \in \mathbb{N}$ , take a closed set $\mathbf{F}_n \subset \mathbf{A}$ such that $m^*(\mathbf{A} \setminus \mathbf{F}_n) < 1/n$ and put $\mathbf{V} = \bigcup_{n=1}^{\infty} \mathbf{F}_n$ . Then $\mathbf{V}$ is an $\mathcal{F}_{\sigma}$ subset of $\mathbf{A}$ , and since $m^*(\mathbf{A} \setminus \mathbf{V}) < 1/n$ for $n \in \mathbb{N}$ , we get $m^*(\mathbf{A} \setminus \mathbf{V}) = 0$ . Finally, if (v) is satisfied, then $\mathbf{A}$ is measurable, as a sum of two measurable sets. Thus the conditions (i), (iv) and (v) are also equivalent.

2.1.13. Suppose first that $\mathbf{A}$ is measurable. Since $m(\mathbf{A}) < \infty$ , given $\varepsilon > 0$ , there is a countable covering of $\mathbf{A}$ by open intervals $\mathbf{I}_n$ such that $\sum_{n=1}^{\infty} |\mathbf{I}_n| < m(\mathbf{A}) + \varepsilon/2$ , and there is $N$ such that $\sum_{n=N+1}^{\infty} |\mathbf{I}_n| < \varepsilon/2$ . Taking $\mathbf{W} = \bigcup_{n=1}^{N} \mathbf{I}_n$ , we see that

$$
m (\mathbf {W} \triangle \mathbf {A}) \leq m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {I} _ {n} \backslash \mathbf {A}\right) + m \left(\bigcup_ {n = N + 1} ^ {\infty} \mathbf {I} _ {n}\right) <   \varepsilon / 2 + \varepsilon / 2 = \varepsilon .
$$

Now we will prove that the condition is also sufficient. Given $\varepsilon > 0$ , there is a finite union $\mathbf{W}$ of open intervals such that $m^{*}(\mathbf{W} \triangle \mathbf{A}) < c / 3$ . Thus $m^{*}(\mathbf{A} \setminus \mathbf{W}) < c / 3$ . By the definition of the Lcobsguc outer measure, there is a countable covering of $\mathbf{A} \setminus \mathbf{W}$ by open intervals $\mathbf{J}_n$ such that $\sum_{n=1}^{\infty} |\mathbf{J}_n| < m^{*}(\mathbf{A} \setminus \mathbf{W}) + \varepsilon / 3 < 2\varepsilon / 3$ . The set $\mathbf{G} = \mathbf{W} \cup \bigcup_{n=1}^{\infty} \mathbf{J}_n$ is an open superset of $\mathbf{A}$ , and

$$
m ^ {*} (\mathbf {G} \backslash \mathbf {A}) \leq m ^ {*} (\dot {\mathbf {W}} \backslash \mathbf {A}) + m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {J} _ {n}\right) <   \frac {\varepsilon}{3} + \frac {2}{3} \varepsilon = \varepsilon .
$$

By (ii) in the previous problem, the set $\mathbf{A}$ is measurable.

2.1.14. (a) If $\mathbf{A}$ is measurable, then clearly, $m_{*}(\mathbf{A}) \geq m(\mathbf{A}) = m^{*}(\mathbf{A})$ . So, if $m(\mathbf{A}) = +\infty$ , the result is proved. If $m(\mathbf{A}) < +\infty$ , then, given $\varepsilon > 0$ , there is a countable collection of closed intervals $\mathbf{I}_{n}$ such that

$$
\mathbf {A} \subset \bigcup_ {n = 1} ^ {\infty} \mathbf {I} _ {n}, \quad \text {a n d} \quad \sum_ {n = 1} ^ {\infty} | \mathbf {I} _ {n} | <   m ^ {*} (\mathbf {A}) + \varepsilon .
$$

Thus if $\mathbf{B} \subset \mathbf{A}$ and $\mathbf{B}$ is measurable, then $m(\mathbf{B}) \leq m^{*}(\mathbf{A}) + \varepsilon$ . It then follows that $m_{*}(\mathbf{A}) \leq m^{*}(\mathbf{A})$ .

(b) By the result in 2.1.11, there is a measurable set $\mathbf{A}_2$ such that $\mathbf{I} \setminus \mathbf{A} \subset \mathbf{A}_2$ and $m(\mathbf{A}_2) = m^*(\mathbf{I} \setminus \mathbf{A})$ . Thus

$$
| \mathbf {I} | = m (\mathbf {I} \backslash \mathbf {A} _ {2}) + m (\mathbf {A} _ {2}) = m (\mathbf {I} \backslash \mathbf {A} _ {2}) + m ^ {*} (\mathbf {I} \backslash \mathbf {A}).
$$

Since $\mathbf{I} \setminus \mathbf{A}_2$ is a measurable subset of $\mathbf{A}$ , we obtain

$$
| \mathbf {I} | \leq m _ {*} (\mathbf {A}) + m ^ {*} (\mathbf {I} \backslash \mathbf {A}).
$$

Now we show that the opposite inequality also holds. If $\mathbf{B}$ is a measurable subset of $\mathbf{A}$ , then $\mathbf{I} \setminus \mathbf{A} \subset \mathbf{I} \setminus \mathbf{B}$ , and, consequently, $m^{*}(\mathbf{I} \setminus \mathbf{A}) \leq m^{*}(\mathbf{I} \setminus \mathbf{B}) = m(\mathbf{I}) - m(\mathbf{B})$ , where the last equality follows from 2.1.8. Taking the supremum over all measurable $\mathbf{B} \subset \mathbf{A}$ , we get $|\mathbf{I}| \geq m_{*}(\mathbf{A}) + m^{*}(\mathbf{I} \setminus \mathbf{A})$ .

(c) It follows from the definition of the Lebesgue inner measure that for $n \in \mathbb{N}$ , there is a measurable $\mathbf{B}_n \subset \mathbf{A}$ such that $m_{*}(\mathbf{A}) - 1 / n < m(\mathbf{B}_n)$ . Since $\bigcup_{n=1}^{\infty} \mathbf{B}_n \subset \mathbf{A}$ ,

$$
m _ {*} (\mathbf {A}) - 1 / n <   m \left(\mathbf {B} _ {n}\right) \leq m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {B} _ {n}\right) \leq m _ {*} (\mathbf {A}).
$$

It then follows that

$$
m \left(\bigcup_ {n = 1} ^ {\infty} \mathrm {B} _ {n}\right) = m _ {*} (\mathrm {A}) = m ^ {*} (\mathrm {A}),
$$

where the last equality is our assumption. Now the measurability of $\mathbf{A}$ follows from 2.1.10.

(d) We have

$$
\begin{array}{l} m _ {*} (\mathbf {A} \cup \mathbf {C}) + m _ {*} (\mathbf {A} \cap \mathbf {C}) \\ \geq \sup  \{m (\mathbf {B} \cup \mathbf {D}): \mathbf {B}, \mathbf {D} \in \mathfrak {M}, \mathbf {B} \subset \mathbf {A}, \mathbf {D} \subset \mathbf {C} \} \\ + \sup  \left\{m (\mathbf {B} \cap \mathbf {D}): \mathbf {B}, \mathbf {D} \in \mathfrak {M}, \mathbf {B} \subset \mathbf {A}, \mathbf {D} \subset \mathbf {C} \right\} \\ \geq \sup  \{m (\mathbf {B} \cup \mathbf {D}) + m (\mathbf {B} \cap \mathbf {D}): \mathbf {B}, \mathbf {D} \in \mathfrak {M}, \mathbf {B} \subset \mathbf {A}, \mathbf {D} \subset \mathbf {C} \} \\ = \sup  \left\{m (\mathbf {B}) + m (\mathbf {D}): \mathbf {B}, \mathbf {D} \in \mathfrak {M}, \mathbf {B} \subset \mathbf {A}, \mathbf {D} \subset \mathbf {C} \right\} \\ = \sup  \left\{m (\mathbf {B}): \mathbf {B} \in \mathfrak {M}, \mathbf {B} \subset \mathbf {A} \right\} + \sup  \left\{m (\mathbf {D}): \mathbf {D} \in \mathfrak {M}, \mathbf {D} \subset \mathbf {C} \right\} \\ = m _ {*} (\mathbf {A}) + m _ {*} (\mathbf {C}). \\ \end{array}
$$

(e) It follows from (d), by induction, that if the $A_{n}$ , $n = 1,2,\ldots,N$ , are pairwise disjoint, then

$$
m _ {\bullet} \left(\bigcup_ {n = 1} ^ {N} A _ {n}\right) \geq \sum_ {n = 1} ^ {N} m _ {\bullet} (A _ {n}).
$$

Consequently,

$$
m _ {n} \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) \geq m _ {n} \left(\bigcup_ {n = 1} ^ {N} \mathbf {A} _ {n}\right) \geq \sum_ {n = 1} ^ {N} m _ {n} (\mathbf {A} _ {n}),
$$

and letting $N \to \infty$ gives the desired result.

(f) By the definition of the Lebesgue inner measure, given $\varepsilon > 0$ , there is a measurable set $\mathbf{B} \subset \mathbf{A} \cup \mathbf{M}$ such that $m_{*}(\mathbf{A} \cup \mathbf{M}) - \varepsilon < m(\mathbf{B})$ . Thus

$$
m _ {\bullet} (\mathbf {A} \cup \mathbf {M}) - \varepsilon <   m (\mathbf {B}) = m (\mathbf {B} \setminus \mathbf {M}) \leq m _ {\bullet} (\mathbf {A}),
$$

because $\mathbf{B}\backslash \mathbf{M}\subset \mathbf{A}$

2.1.15. The necessity of the condition is obvious. To prove that the condition is sufficient, it is enough to apply the result in the previous problem.

2.1.16. [M. Machover, Amer. Math. Monthly 74(1967), 1080-1081.] Suppose first that there are measurable sets $\mathbf{A}_1$ and $\mathbf{B}_1$ such that $\mathbf{A} \subset \mathbf{A}_1$ , $\mathbf{B} \subset \mathbf{B}_1$ and $m(\mathbf{A}_1 \cap \mathbf{B}_1) = 0$ . By the definition of the Lebesgue outer measure, given $\varepsilon > 0$ , there is an open set $\mathbf{G}$ such that $\mathbf{A} \cup \mathbf{B} \subset \mathbf{G}$ and

$$
m (\mathbf {G}) <   m ^ {\circ} (\mathbf {A} \cup \mathbf {B}) + \varepsilon .
$$

Since $\mathbf{A} \subset \mathbf{G} \cap \mathbf{A}_1$ and $\mathbf{B} \subset \mathbf{G} \cap \mathbf{B}_1$ , we get

$$
\begin{array}{l} m ^ {\bullet} (\mathbf {A}) + m ^ {\bullet} (\mathbf {B}) \leq m (\mathbf {G} \cap \mathbf {A} _ {1}) + m (\mathbf {G} \cap \mathbf {B} _ {1}) = m (\mathbf {G} \cap (\mathbf {A} _ {1} \cup \mathbf {B} _ {1})) \\ \leq m (\mathbf {G}) <   m ^ {\bullet} (\mathbf {A} \cup \mathbf {B}) + \varepsilon \leq m ^ {\bullet} (\mathbf {A}) + m ^ {\bullet} (\mathbf {B}) + \varepsilon . \\ \end{array}
$$

Letting $\varepsilon \to 0$ , we see that $m^{\bullet}(\mathbf{A}\cup \mathbf{B}) = m^{\bullet}(\mathbf{A}) + m^{\bullet}(\mathbf{B})$ .

Assume now that $m^{\bullet}(\mathbf{A} \cup \mathbf{B}) = m^{\bullet}(\mathbf{A}) + m^{\bullet}(\mathbf{B})$ . By the result in 2.1.11, there are $\mathcal{G}_{\delta}$ sets $\mathbf{A}_1$ and $\mathbf{B}_1$ such that $\mathbf{A} \subset \mathbf{A}_1$ , $\mathbf{B} \subset \mathbf{B}_1$ and $m(\mathbf{A}_1) = m^{\bullet}(\mathbf{A})$ , $m(\mathbf{B}_1) = m^{\bullet}(\mathbf{B})$ . We will show that $m(\mathbf{A}_1 \cap \mathbf{B}_1) =$

0. Indeed, if $m(\mathbf{A}_1 \cap \mathbf{B}_1) > 0$ , then using 2.1.9, we obtain

$$
\begin{array}{l} m ^ {*} (\mathbf {A} \cup \mathbf {B}) = m ^ {*} (\mathbf {A}) + m ^ {*} (\mathbf {B}) = m (\mathbf {A} _ {1}) + m (\mathbf {B} _ {1}) \\ = m \left(\mathbf {A} _ {1} \cup \mathbf {B} _ {1}\right) + m \left(\mathbf {A} _ {1} \cap \mathbf {B} _ {1}\right) \\ > m \left(\mathrm {A} _ {1} \cup \mathrm {B} _ {1}\right) \geq m ^ {*} (\mathrm {A} \cup \mathrm {B}), \\ \end{array}
$$

a contradiction. Note that the theorem proved here generalizes the results 2.1.5 and 2.1.6.

2.1.17. [M. Machover, Amer. Math. Monthly 74(1967), 1080-1081.] It follows from the definition of the Lebesgue inner measure (see 2.1.14) that, given $\varepsilon > 0$ , there is a measurable set $\mathbf{C} \subset \mathbf{A} \cup \mathbf{B}$ such that $m_{*}(\mathbf{A} \cup \mathbf{B}) - \varepsilon < m(\mathbf{C})$ . By the previous result, there are measurable sets $\mathbf{A}_{1}$ and $\mathbf{B}_{1}$ such that $\mathbf{A} \subset \mathbf{A}_{1}$ and $\mathbf{B} \subset \mathbf{B}_{1}$ , $m(\mathbf{A}_{1} \cap \mathbf{B}_{1}) = 0$ . Consequently, using 2.1.14(d), we get

$$
\begin{array}{l} m _ {\bullet} (\mathbf {A}) + m _ {\bullet} (\mathbf {B}) - \varepsilon \leq m _ {\bullet} (\mathbf {A} \cup \mathbf {B}) - \varepsilon <   m (\mathbf {C}) \\ = m \left(\mathbf {C} \cap \left(\mathbf {A} _ {1} \cup \mathbf {B} _ {1}\right)\right) \\ = m \left(\mathbf {C} \cap \mathbf {A} _ {1}\right) + m \left(\mathbf {C} \cap \mathbf {B} _ {1}\right). \\ \end{array}
$$

Since $\mathbf{C} \cap \mathbf{A}_1 \subset (\mathbf{A} \cup \mathbf{B}) \cap \mathbf{A}_1 = \mathbf{A} \cup (\mathbf{B} \cap \mathbf{A}_1) \subset \mathbf{A} \cup (\mathbf{B}_1 \cap \mathbf{A}_1)$ , we have $m(\mathbf{C} \cap \mathbf{A}_1) \leq m_*(\mathbf{A} \cup (\mathbf{B}_1 \cap \mathbf{A}_1))$ . Likewise, $m(\mathbf{C} \cap \mathbf{B}_1) \leq m_*(\mathbf{B} \cup (\mathbf{B}_1 \cap \mathbf{A}_1))$ . It then follows that

$$
\begin{array}{l} m _ {*} (\mathbf {A}) + m _ {*} (\mathbf {B}) - \varepsilon \leq m _ {*} (\mathbf {A} \cup \mathbf {B}) - \varepsilon \\ <   m _ {\bullet} (\mathbf {A} \cup (\mathbf {B} _ {1} \cap \mathbf {A} _ {1})) + m _ {\bullet} (\mathbf {B} \cup (\mathbf {B} _ {1} \cap \mathbf {A} _ {1})) \\ = m _ {*} (\mathbf {A}) + m _ {*} (\mathbf {B}), \\ \end{array}
$$

where the last equality follows from 2.1.14(f).

2.1.18. Set $\mathbf{B}_1 = \mathbf{A}_1$ and $\mathbf{B}_n = \mathbf{A}_n \setminus \mathbf{A}_{n-1}$ for $n \geq 2$ . Then the $\mathbf{B}_n$ are pairwise disjoint measurable sets, and for every $N \in \mathbb{N}$ we have $\bigcup_{n=1}^{N} \mathbf{A}_n = \bigcup_{n=1}^{N} \mathbf{B}_n$ , and $\bigcup_{n=1}^{\infty} \mathbf{A}_n = \bigcup_{n=1}^{\infty} \mathbf{B}_n$ . Hence

$$
\begin{array}{l} m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {B} _ {n}\right) = \sum_ {n = 1} ^ {\infty} m (\mathbf {B} _ {n}) \\ = \lim  _ {N \rightarrow \infty} \sum_ {n = 1} ^ {N} m (\mathbf {B} _ {n}) = \lim  _ {N \rightarrow \infty} m (\mathbf {A} _ {N}). \\ \end{array}
$$

2.1.19. Without loss of generality we can assume that $m(\mathbf{A}_1)$ is finite. Using De Morgan's formula, the results in 2.1.8 and in the previous problem, we get

$$
\begin{array}{l} m \left(\mathbf {A} _ {1}\right) - m \left(\bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = m \left(\mathbf {A} _ {1} \backslash \bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = m \left(\bigcup_ {n = 1} ^ {\infty} \left(\mathbf {A} _ {1} \backslash \mathbf {A} _ {n}\right)\right) \\ = \lim  _ {n \rightarrow \infty} m \left(\mathrm {A} _ {1} \backslash \mathrm {A} _ {n}\right) = m \left(\mathrm {A} _ {1}\right) - \lim  _ {n \rightarrow \infty} m \left(\mathrm {A} _ {n}\right). \\ \end{array}
$$

To show that the assumption $m(\mathbf{A}_k) < \infty$ for at least one $k$ is essential, one can consider $\mathbf{A}_n = (n,\infty), n \in \mathbb{N}$ .

2.1.20. (a) The sets $\mathbf{B}_k = \bigcap_{n=k}^{\infty} \mathbf{A}_n$ satisfy $\mathbf{B}_k \subset \mathbf{A}_k$ and $\mathbf{B}_k \subset \mathbf{B}_{k+1}$ . Therefore, by 2.1.18,

$$
m \left(\lim  _ {n \rightarrow \infty} \mathbf {A} _ {n}\right) = m \left(\bigcup_ {k = 1} ^ {\infty} \mathbf {B} _ {k}\right) = \lim  _ {k \rightarrow \infty} m (\mathbf {B} _ {k}) \leq \lim  _ {k \rightarrow \infty} m (\mathbf {A} _ {k}),
$$

where the last inequality follows, e.g., from I, 2.4.14(a).

(b) Using 2.1.19, this follows by the same method as in (a).

2.1.21. (a) If, for example, $\{\mathbf{A}_n\}$ is an increasing sequence of sets, then for each $k$ , $\bigcup_{n=k}^{\infty} \mathbf{A}_n = \bigcup_{n=1}^{\infty} \mathbf{A}_n$ . Thus $\varlimsup_{n \to \infty} \mathbf{A}_n = \bigcup_{n=1}^{\infty} \mathbf{A}_n$ . Moreover, since $\bigcap_{n=k}^{\infty} \mathbf{A}_n = \mathbf{A}_k$ , we see that $\varliminf_{n \to \infty} \mathbf{A}_n = \bigcup_{k=1}^{\infty} \mathbf{A}_k$ .

(b) By the monotonicity of the Lebesgue outer measure, each of the $\mathbf{A}_n$ is of finite measure, and the results in 2.1.20(a) and (b) can be applied. Thus

$$
\lim  _ {n \rightarrow \infty} m (\mathbf {A} _ {n}) \geq m (\lim  _ {n \rightarrow \infty} \mathbf {A} _ {n}) \geq \overline {{\lim  _ {n \rightarrow \infty}}} m (\mathbf {A} _ {n}).
$$

2.1.22. We have

$$
m (\mathbf {A}) = 1 - m ([ 0, 1 ] \backslash \mathbf {A}) = 1 - \left(\frac {\alpha}{2} + 2 \frac {\alpha}{2 ^ {3}} + 2 ^ {2} \frac {\alpha}{2 ^ {5}} + \dots\right) = 1 - \alpha .
$$

2.1.23. We divide $[0,1]$ into ten equal parts and remove the open interval $(0.7,0.8)$ . At the second stage we divide each of the remaining nine intervals $[0,0.1],\ldots,[0.6,0.7],[0.8,0.9],[0.9,1]$ into ten equal parts and remove the open intervals $(0.07,0.08),\ldots,(0.67,0.68),$ $(0.87,0.88),(0.97,0.98)$ . Continuing the procedure, at the $n$ th stage we remove $9^{n-1}$ open intervals each of length $\frac{1}{10^n}$ . Note that if $(a_i, b_i)$ ,

$i = 1,2,\ldots$ , is the sequence of removed intervals, then

$$
\mathbf {A} = [ 0, 1 ] \backslash \bigcup_ {i = 1} ^ {\infty} (a _ {i}, b _ {i}).
$$

Thus

$$
m ([ 0, 1 ] \backslash \mathbf {A}) = \frac {1}{1 0} + 9 \frac {1}{1 0 ^ {2}} + 9 ^ {3} \frac {1}{1 0 ^ {3}} + \dots + 9 ^ {n} \quad 1 \frac {1}{1 0 ^ {n}} + \dots = 1.
$$

So, $m(\mathbf{A}) = 0$ . It is also worth noting here that the set $\mathbf{A}$ is perfect and nowhere dense.

2.1.24. We have

$$
\mathbf {B} = \bigcup_ {n \in \mathbf {Z}} (\mathbf {B} \cap [ n, n + 1 ])
$$

and the set $\mathbf{B} \cap [n, n + 1]$ is obtained by translating the set $\mathbf{A}$ defined in the previous problem, that is, $\mathbf{B} \cap [n, n + 1] = \mathbf{A} + n = \{x + n : x \in \mathbf{A}\}$ . Since the Lebesgue measure is translation invariant, it follows from the result in the previous problem that $m(\mathbf{B}) = 0$ .

2.1.25. We divide the interval $[0, 1]$ into four equal parts and remove two open intervals $(1/4, 1/2)$ and $(3/4, 1)$ , and denote the union of the two remaining intervals by $\mathbf{A}_1$ . Clearly, the set $\mathbf{A}_1$ consists of all the numbers in $[0, 1]$ which allow binary expansions with zero in the second binary position. At the second stage we divide each of the two remaining closed intervals into four equal parts and remove the four following intervals: $(1/4^2, 2/4^2), (3/4^2, 4/4^2), (9/4^2, 10/4^2), (11/4^2, 12/4^2)$ , and denote by $\mathbf{A}_2$ the union of four remaining closed intervals. So the set $\mathbf{A}_2$ consists of all the numbers in $[0, 1]$ which allow binary expansions with zeros in the second and fourth binary position. Continuing the procedure, at the $n$ th stage we get the set $\mathbf{A}_n$ consisting of $2^n$ closed intervals each of length $4^{-n}$ . It is obvious that

$$
A _ {1} \supset A _ {2} \supset \dots \supset A _ {n} \supset \dots
$$

and

$$
\mathbf {A} = \bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}.
$$

Since $m(\mathbf{A}_n) = 2^n 4^{-n} = 2^{-n}$ , the set $\mathbf{A}$ has Lebesgue measure zero.

2.1.26. Denote by $\mathbf{A}_i$ the set of points in $[0,1]$ which admit decimal expansions containing the digit $i$ , $i \in \{1,2,\ldots,9\}$ . Then the set $\mathbf{A}$ of points in $[0,1]$ which admit decimal expansions containing all the digits $1,2,\ldots,9$ is the intersection $\bigcap_{i=1}^{9} \mathbf{A}_i$ . By the result in 2.1.23, $m([0,1] \setminus \mathbf{A}_i) = 0$ , and therefore we get $m([0,1] \setminus \bigcap_{i=1}^{9} \mathbf{A}_i) = 0$ , and consequently, $m(\mathbf{A}) = 1$ .

2.1.27. Let $\mathbf{A}$ be the set. Then $\mathbf{A}$ is contained in each of the sets $\mathbf{A}_n$ defined as follows. We divide the interval $[0,1]$ into a thousand equal parts and remove the interval $(0.222, 0.223)$ , and denote by $\mathbf{A}_1$ the union of the remaining 999 closed intervals. Next we divide each of the remaining intervals into a thousand equal parts and remove the corresponding intervals of the form $(0.d_1d_2d_3222, 0.d_1d_2d_3223)$ . In this way we get the set $\mathbf{A}_2$ , which is the union of the remaining $999^2$ closed intervals. Continuing the process, we obtain the sequence of sets $\{\mathbf{A}_n\}$ , where $\mathbf{A}_n$ is the union of $999^n$ closed intervals each of length $10^{-3n}$ and

$$
\mathbf {A} = \bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}.
$$

Since $\{\mathbf{A}_n\}$ is a decreasing sequence, by 2.1.17,

$$
m (\mathbf {A}) = \lim  _ {n \rightarrow \infty} m (\mathbf {A} _ {n}) = \lim  _ {n \rightarrow \infty} \left(\frac {9 9 9}{1 0 0 0}\right) ^ {n} = 0.
$$

2.1.28. We have

$$
\begin{array}{l} \mathbf {A} = \left(- \frac {1}{2 0}, \frac {1}{9} + \frac {1}{2 0}\right) \cup \left(\frac {2}{9} - \frac {1}{2 0}, \frac {1}{3} + \frac {1}{2 0}\right) \cup \left(\frac {2}{3} - \frac {1}{2 0}, \frac {7}{9} + \frac {1}{2 0}\right) \\ \cup \left(\frac {8}{9} - \frac {1}{2 0}, 1 + \frac {1}{2 0}\right) \\ \end{array}
$$

and therefore $m(\mathbf{A}) = \frac{38}{45}$ .

2.1.29. Let $\mathbf{A} \subset [a, b]$ . Then the function $f(x) = m([a, x] \cap \mathbf{A})$ , $x \in [a, b]$ , is increasing, continuous, and $f(a) = 0$ , $f(b) = p$ . Thus the result follows from the intermediate value property.

2.1.30. If $\mathbf{A}$ is a bounded set, the result is contained in the previous problem. If $\mathbf{A}$ is unbounded, we put $\mathbf{A}_n = \mathbf{A} \cap [-n, n]$ , $n \in \mathbb{N}$ , and get $m(\mathbf{A}) = \lim_{n \to \infty} m(\mathbf{A}_n)$ (see 2.1.18). So, for $q < m(\mathbf{A})$ there is $N$

such that $m(\mathbf{A}_N) > q$ , and the result in the previous problem can be applied.

2.1.31. In the proof we will use the Cantor-Bendixson theorem, which asserts that every closed set $\mathbf{A} \subset \mathbb{R}$ is a union of a perfect set $\mathbf{P}$ and a countable set $\mathbf{C}$ . To prove the Cantor-Bendixson theorem, define

$$
\mathbf {P} = \{x \in \mathbb {R}: x \text {i s a c o n d e n s a t i o n p o i n t o f A} \}.
$$

Recall that $\pmb{x}$ is a condensation point of $\mathbf{A}$ if every neighborhood of $\pmb{x}$ contains uncountably many points of $\mathbf{A}$ . It is clear that every condensation point of $\mathbf{A}$ is a limit point of $\mathbf{A}$ . So, $\mathbf{P} \subset \mathbf{A}$ and $\mathbf{A} = \mathbf{P} \cup (\mathbf{A} \setminus \mathbf{P})$ . If $\pmb{x} \in \mathbf{A} \setminus \mathbf{P}$ , then there is an open interval $\mathbf{U}$ with rational endpoints containing $\pmb{x}$ and such that $\mathbf{A} \cap \mathbf{U}$ is countable. Consequently, $\mathbf{C} = \mathbf{A} \setminus \mathbf{P}$ is a countable set. We now show that $\mathbf{P}$ is perfect, that is, it is equal to the set of its own limit points. Let $x \in \mathbf{P}$ and let $\mathbf{U}$ be a neighborhood of $x$ . Then $\mathbf{U} \cap \mathbf{A}$ is uncountable and $\mathbf{U} \cap \mathbf{C}$ is countable. Hence $\mathbf{U} \cap \mathbf{P} = (\mathbf{U} \cap \mathbf{A}) \cap (\mathbf{U} \cap \mathbf{C})^c$ is uncountable, and therefore $x$ is a limit point of $\mathbf{P}$ . To see that $\mathbf{P}$ is closed, take $z \in \mathbf{P}^c$ . Then $z$ has a neighborhood $V$ such that $V \cap A$ is countable. If there were $y \in V \cap P$ , then $V \cap A$ would be uncountable, a contradiction. This shows that $P^c$ is an open set.

Now we turn to the proof of our result. It follows from the previous problem that there is a measurable set $\mathbf{B} \subset \mathbf{A}$ such that $m(\mathbf{B}) = q' < q < m(\mathbf{A})$ . Moreover, by (iv) in 2.1.12, there is a closed set $\mathbf{F} \subset \mathbf{B}$ such that $m(\mathbf{B} \setminus \mathbf{F}) = q - q'$ . Then $m(\mathbf{F}) = q$ , and the desired result follows from the Cantor-Bendixson theorem.

2.1.32. The result will follow from the previous problem if we show that every nonempty perfect set has the cardinality of the continuum. Let $\mathbf{P}$ be such a set, that is, a closed set with no isolated points. If $G_{n} = \{x\in \mathbb{R}:\mathrm{dist}(x,\mathbf{P}) < 1 / n\}$ , $n = 1,2,\ldots$ , then

$$
\mathbf {P} = \bigcap_ {n = 1} ^ {\infty} \mathbf {G} _ {n}.
$$

There are at least two different points in $\mathbf{P}$ , say, $x_0$ and $x_1$ . At the first stage we choose two disjoint open intervals $\mathbf{I}_0$ and $\mathbf{I}_1$ containing $x_0$ and $x_1$ , respectively, and closed subintervals $\mathbf{J}_0 \subset \mathbf{I}_0$ and $\mathbf{J}_1 \subset \mathbf{I}_1$ , both of length less than 1 and such that $\mathbf{J}_0 \subset \mathbf{G}_1$ , $\mathbf{J}_1 \subset \mathbf{G}_1$ . At

the second stage we choose open disjoint intervals $\mathbf{I}_{00}, \mathbf{I}_{01} \subset \mathbf{J}_0$ and $\mathbf{I}_{10}, \mathbf{I}_{11} \subset \mathbf{J}_1$ and closed subintervals $\mathbf{J}_{00}, \mathbf{J}_{01}, \mathbf{J}_{10}, \mathbf{J}_{11}$ , all of length less than $1/2$ and such that

$$
\mathbf {J} _ {0 0}, \mathbf {J} _ {0 1} \subset \mathbf {G} _ {2} \cap \mathbf {J} _ {0}, \quad \mathbf {J} _ {1 0}, \mathbf {J} _ {1 1} \subset \mathbf {G} _ {2} \cap \mathbf {J} _ {1}.
$$

Note that since $x_0$ and $x_1$ are limit points of $\mathbf{P}$ , the above construction is possible. Continuing the procedure, at the $n$ th stage we get $2^n$ pairwise disjoint and closed intervals $\mathbf{J}_{i_1i_2\dots i_n}$ , where $i_k$ takes the values 0 or 1, all of length less than $1/n$ and such that $\mathbf{J}_{i_1i_2\dots i_n} \subset \mathbf{G}_n \cap \mathbf{J}_{i_1i_2\dots i_{n-1}}$ . By Cantor's nested set theorem, there is exactly one point $x_{i_1i_2\dots}$ in the intersection of the closed intervals $\mathbf{J}_{i_1}, \mathbf{J}_{i_1i_2}, \mathbf{J}_{i_1i_2i_3}, \ldots$ . It also follows from the above that the different sequences $\{i_n\}$ and $\{i_n'\}$ of 0's and 1's generate different points $x_{i_1i_2\dots}$ and $x_{i_1'i_2\dots}$ . Since the set of all sequences of 0's and 1's is of continuum cardinality, the set of all points $x_{i_1i_2\dots}$ is also of continuum cardinality. Since all $x_{i_1i_2\dots}$ are in $\mathbf{P}$ , the set $\mathbf{P}$ has the cardinality of the continuum.

2.1.33. To prove that $\mathbf{A}$ is nowhere dense, we will show that each interval contains a subinterval disjoint from $\mathbf{A}$ . Let $\mathbf{I} \subset \mathbb{R}$ be an interval. Since $m(\mathbf{A}) = 0$ , $\mathbf{I}$ cannot be a subset of $\mathbf{A}$ . Therefore $\mathbf{I} \cap \mathbf{A}^c \neq \emptyset$ . Since $\mathbf{A}^c$ is an open set, there is an interval $\mathbf{J} \subset \mathbf{I} \cap \mathbf{A}^c$ , which proves that $\mathbf{A}$ is nowhere dense.

2.1.34. No. To see this, consider the set $\mathbf{A}$ defined in 1.7.12. It is a nowhere dense subset of $[0,1]$ of positive measure. Let $\mathbf{B}$ consist of all the endpoints of the intervals which are removed from $[0,1]$ in the construction of $\mathbf{A}$ . Then $\mathbf{B}$ is a nowhere dense countable set. Consequently, $m(\mathbf{B}) = 0$ and $\overline{\mathbf{B}} = \mathbf{A}$ , which shows that $m(\overline{\mathbf{B}}) > 0$ .

2.1.35. Since $m(\mathbf{A}) > 0$ , the set has the cardinality of the continuum (see 2.1.32). Let $x_0 \in \mathbf{A}$ be fixed; then the set of numbers $|x_0 - x|$ where $x \in \mathbf{A}$ , is of continuum cardinality, and therefore not all of its elements are rationals.

2.1.36. Yes. Let $\mathbf{A}_n$ be a nowhere dense and perfect subset of $[0,1]$ of Lebesgue measure $1 - 1/n$ (note that such sets were constructed and discussed in 1.7.12 and 2.1.22). If $\mathbf{A} = \bigcup_{n=1}^{\infty} \mathbf{A}_n$ , then $1 - 1/n \leq m(\mathbf{A}_n) \leq m(\mathbf{A}) \leq 1$ . So, $m(\mathbf{A}) = 1$ .

2.1.37. No. If $\mathbf{A}$ were such a set, then $[0,1] \setminus \mathbf{A}$ would be an open set of Lebesgue measure 0 and therefore an empty set.

2.1.38. Let $\{\mathbf{U}_n\}$ be a sequence of all open intervals with rational endpoints. Let $\mathbf{A}_1$ denote a nowhere dense subset of $\mathbf{U}_1$ of positive Lebesgue measure (see, e.g., 1.7.12 for a construction of such a set). Since $\mathbf{A}_1$ is nowhere dense, there is an open interval $(a,b)\subset \mathbf{U}_1$ disjoint from $\mathbf{A}_1$ . Thus we can find a nowhere dense set $\mathbf{A}_2\subset (a,b)$ of positive measure. So we have two disjoint nowhere dense sets $\mathbf{A}_1,\mathbf{A}_2$ such that $\mathbf{A}_1\cup \mathbf{A}_2\subset \mathbf{U}_1$ . Since $\mathbf{A}_1\cup \mathbf{A}_2$ is a nowhere dense set, there is $(c,d)\subset \mathbf{U}_2$ disjoint from $\mathbf{A}_1\cup \mathbf{A}_2$ . Next we take a nowhere dense set $\mathbf{A}_3\subset (c,d)$ of positive measure, and an open interval $(e,f)\subset (c,d)$ disjoint from $\mathbf{A}_3$ , and a nowhere dense set $\mathbf{A}_4\subset (e,f)$ of positive measure. Continuing the procedure, we obtain a sequence of pairwise disjoint nowhere dense sets $\{\mathbf{A}_n\}$ such that $\mathbf{A}_{2n}\cup \mathbf{A}_{2n - 1}\subset \mathbf{U}_n$ and $m(\mathbf{A}_n) > 0$ . Set $\mathbf{A} = \bigcup_{n = 1}^{\infty}\mathbf{A}_{2n}$ . Now we show that the set $\mathbf{A}$ has the desired property. Indeed, given an interval $(\alpha ,\beta)$ , there is a $\mathbf{U}_k\subset (\alpha ,\beta)$ , and therefore $m(\mathbf{A}\cap (\alpha ,\beta))\geq m(\mathbf{A}_{2k}) > 0$ . It is also clear that $m((\mathbb{R}\setminus \mathbf{A})\cap (\alpha ,\beta))\geq m(\mathbf{A}_{2k - 1}) > 0$ .

2.1.39. For each positive integer $n$ , define

$$
\mathbf {A} _ {n} = \mathbf {A} \cap \left(\left(- \frac {1}{n}, - \frac {1}{n + 1} \right] \cup \left[ \frac {1}{n + 1}, \frac {1}{n}\right)\right).
$$

If $m(\mathbf{A}_n) > 0$ , then by the result in 2.1.31 there is a perfect set $\mathbf{B}_n \subset \mathbf{A}_n$ such that $m(\mathbf{B}_n) \geq \frac{1}{2} m(\mathbf{A}_n)$ . If $m(\mathbf{A}_n) = 0$ , then we set $\mathbf{B}_n = \emptyset$ . We will show that

$$
\mathbf {B} = \bigcup_ {n = 1} ^ {\infty} \mathbf {B} _ {n} \cup \{0 \}
$$

has the desired property. Note first the B is a perfect set. It is clear that every point in B is a limit point of B. To show that B is a closed set, assume that $x = \lim_{k\to \infty}x_k$ , where $x_{k}\in \mathbf{B}$ . If $x > 0$ , then there is a positive integer $m$ such that $x\in [1 / m,1 / (m - 1))$ . So, beginning with some value of the index $k$ , $x_{k}\in (1 / (m + 1),1 / (m - 1))$ , and consequently, $x_{k}\in \mathbf{B}_{m}\cup \mathbf{B}_{m - 1}$ , which gives $x\in \mathbf{B}_m\cup \mathbf{B}_{m - 1}$ . If $x < 0$ , a similar reasoning can be applied. The case $x = 0$ is obvious. Now, if $\delta >0$ , then there is a positive integer $N$ such that $1 / N < \delta$ .

Then, by the construction of $\mathbf{B}$

$$
\mathbf {B} \cap (- \delta , \delta) \supset \mathbf {B} \cap \left(- \frac {1}{N}, \frac {1}{N}\right) = \bigcup_ {n = N} ^ {\infty} \mathbf {B} _ {n} \cup \{0 \}.
$$

Thus

$$
\begin{array}{l} m (\mathbf {B} \cap (- \delta , \delta)) \geq m \left(\bigcup_ {n = N} ^ {\infty} \mathbf {B} _ {n}\right) = \sum_ {n = N} ^ {\infty} m (\mathbf {B} _ {n}) \\ \geq \frac {1}{2} m \left(\mathbf {A} \cap \left(- \frac {1}{N}, \frac {1}{N}\right)\right) > 0. \\ \end{array}
$$

2.1.40. We have

$$
\lim  _ {h \rightarrow 0 ^ {+}} \frac {m (\mathbf {A} \cap [ x - h , x + h ])}{2 h} = \left\{\begin{array}{l l}1&\text {i f} x \in (- 1, 1),\\\frac {1}{2}&\text {i f} x \in \{- 1, 1 \},\\0&\text {o t h e r w i s e .}\end{array}\right.
$$

2.1.41. Assume first that $x_0 = 0$ . For a positive integer $n$ , set

$$
\mathbf {P} _ {n} = \left(- \frac {1}{n}, - \frac {1}{n + 1} \right] \cup \left[ \frac {1}{n + 1}, \frac {1}{n}\right)
$$

and choose a measurable set $\mathbf{A}_n \subset \mathbf{P}_n$ such that $m(\mathbf{A}_n) = \alpha m(\mathbf{P}_n)$ . Setting $\mathbf{A} = \bigcup_{n=1}^{\infty} \mathbf{A}_n$ , we show that $\mathbf{A}$ has density $\alpha$ at 0. To this end, note that if $\frac{1}{n+1} \leq h < \frac{1}{n}$ , then

$$
\begin{array}{l} \frac {m (\mathbf {A} \cap [ - h , h ])}{2 h} \leq \frac {m \left(\mathbf {A} \cap [ - \frac {1}{n} , \frac {1}{n} ]\right)}{\frac {2}{n + 1}} = \frac {\alpha_ {n} ^ {2}}{\frac {2}{n + 1}} \\ = \alpha \left(1 + \frac {1}{n}\right) \leq \alpha (1 + 2 h). \\ \end{array}
$$

On the other hand,

$$
\begin{array}{l} \frac {m (\mathbf {A} \cap [ - h , h ])}{2 h} \geq \frac {m \left(\mathbf {A} \cap \left[ - \frac {1}{n + 1} , \frac {1}{n + 1} \right]\right)}{\frac {2}{n}} = \frac {\alpha \frac {2}{n + 1}}{\frac {2}{n}} \\ = \alpha \left(1 - \frac {1}{n + 1}\right) \geq \alpha (1 - h). \\ \end{array}
$$

Since Lebesgue measure is invariant under translation, if $x_0 \neq 0$ , then the set $\mathbf{A} + x_0$ has the desired property.

2.1.42. For a positive integer $n$ , define

$$
\mathbf {A} _ {n} = \mathbf {A} \cap \left(\left(- \frac {1}{n}, - \frac {1}{n + 1} \right] \cup \left[ \frac {1}{n + 1}, \frac {1}{n}\right)\right)
$$

and choose a perfect set $\mathbf{B}_n\subset \mathbf{A}_n$ such that $m(\mathbf{B}_n)\geq \left(1 - \frac{1}{n}\right)m(\mathbf{A}_n)$ We will show that

$$
\mathbf {B} = \bigcup_ {n = 1} ^ {\infty} \mathbf {B} _ {n} \cup \{0 \}
$$

has the desired property. The set $\mathbf{B}$ is perfect (see the solution of 2.1.39). Now, for $h > 0$ , let $N$ be the integral part of $\frac{1}{h}$ . Then, by the construction of $\mathbf{B}$ ,

$$
\begin{array}{l} \frac {m (\mathbf {B} \cap [ - h , h ])}{2 h} \geq \frac {m \left(\mathbf {B} \cap \left[ - \frac {1}{N + 1} , \frac {1}{N + 1} \right]\right)}{\frac {2}{N}} = \frac {N}{2} \sum_ {n = N + 1} ^ {\infty} m \left(\mathbf {B} _ {n}\right) \\ \geq \frac {N}{2} \left(\sum_ {n = N + 1} ^ {\infty} m \left(A _ {n}\right) - \frac {1}{N} \sum_ {n = N + 1} ^ {\infty} m \left(A _ {n}\right)\right) \\ = \frac {N}{2} m \left(\mathbf {A} \cap \left[ - \frac {1}{N + 1}, \frac {1}{N + 1} \right]\right) \left(1 - \frac {1}{N}\right) \\ = \frac {m (\mathbf {A} [ 1 ] \left[ - \frac {1}{N + 1} , \frac {1}{N + 1} \right])}{\frac {2}{N}} \cdot \frac {N - 1}{N}. \\ \end{array}
$$

2.1.43. Let $T_{a}(\mathbf{A})$ denote the translate of $\mathbf{A}$ , that is,

$$
T _ {u} (A) = A + a = \{x + a: x \in A \}.
$$

Then

$$
\mathbf {A} + a (\mathrm {m o d} 1) = T _ {a} (\mathbf {A} \cap [ 0, 1 - a)) \cup T _ {a - 1} (\mathbf {A} \cap [ 1 - a, 1)).
$$

Setting $\mathbf{A}_1 = \mathbf{A} \cap [0, 1 - a)$ , $\mathbf{A}_2 = \mathbf{A} \cap [1 - a, 1)$ and $\mathbf{B}_1 = T_a(\mathbf{A}_1)$ , $\mathbf{B}_2 = T_{a-1}(\mathbf{A}_2)$ , and $\mathbf{B} = \mathbf{A} + a (\bmod 1)$ , we can write $\mathbf{B} = \mathbf{B}_1 \cup \mathbf{B}_2$ . Since $m^*$ is translation invariant, we have

$$
m ^ {*} (\mathbf {B} _ {1}) = m ^ {*} (\mathbf {A} _ {1}) \quad \text {a n d} \quad m ^ {*} (\mathbf {B} _ {2}) = m ^ {*} (\mathbf {A} _ {2}).
$$

It follows from 2.1.5 (see the solution) that

$$
\begin{array}{l} m ^ {*} (\mathbf {A}) = m ^ {*} (\mathbf {A} \cap ([ 0, 1 - a) \cup [ 1 - a, 1)))) \\ = m ^ {*} (\mathbf {A} _ {1}) + m ^ {*} (\mathbf {A} _ {2}). \\ \end{array}
$$

Consequently,

$$
\begin{array}{l} m ^ {*} (\mathbf {B}) = m ^ {*} \left(\mathbf {B} _ {1} \cup \mathbf {B} _ {2}\right) = m ^ {*} \left(\left(\mathbf {B} _ {1} \cap [ a, 1)\right) \cup \left(\mathbf {B} _ {2} \cap [ 0, a)\right)\right) \\ = m ^ {*} \left(\mathbf {B} _ {1} \cap [ a, 1)\right) + m ^ {*} \left(\mathbf {B} _ {2} \cap [ 0, a)\right), \\ \end{array}
$$

where the last equality follows from 2.1.5. It then follows that

$$
m ^ {*} (\mathbf {B}) = m ^ {*} (\mathbf {A} _ {1}) + m ^ {*} (\mathbf {A} _ {2}) = m ^ {*} (\mathbf {A}).
$$

2.1.44. Here we adopt the notation introduced in the solution of the previous problem.

If $\mathbf{A}$ is measurable, then so are $\mathbf{A}_1$ and $\mathbf{A}_2$ , and since $m$ is translation invariant, the sets $\mathbf{B}_1$ and $\mathbf{B}_2$ are also measurable. Thus the measurability of $\mathbf{A} + a (\bmod \mathbf{I})$ follows from the equality

$$
\mathbf {A} + a (\mathrm {m o d} \mathbf {1}) = \mathbf {B} = \mathbf {B _ {1}} \cup \mathbf {B _ {2}}.
$$

On the other hand, if $\mathbf{B}$ is measurable, then $\mathbf{B}_1 = \mathbf{B} \cap [a, 1)$ and $\mathbf{B}_2 = \mathbf{B} \cap [0, a)$ , and therefore the sets $\mathbf{B}_1$ and $\mathbf{B}_2$ are measurable. Since $\mathbf{A}_1 = T_{-a}(\mathbf{B}_1)$ , $\mathbf{A}_2 = T_{1 - a}(\mathbf{B}_2)$ and $\mathbf{A} = \mathbf{A}_1 \cup \mathbf{A}_2$ , the measurability of $\mathbf{A}$ follows.

2.1.45. Assume, contrary to our claim, that $\mathbf{V}$ is a measurable set. Let $\{r_n\}$ be a sequence of all rationals in $[0,1)$ with $r_0 = 0$ , and define $\mathbf{V}_n = \mathbf{V} + r_n (\bmod 1)$ . Then, by the result in the preceding problem, each $\mathbf{V}_n$ is also measurable and $m(\mathbf{V}_n) = m(\mathbf{V})$ . Now we show that the $\mathbf{V}_n$ are pairwise disjoint and $\bigcup_{n=0}^{\infty} \mathbf{V}_n = [0,1)$ . Indeed, if $x \in \mathbf{V}_i \cap \mathbf{V}_j$ , then $x = v_i + r_i (\bmod 1)$ and $x = v_j + r_j (\bmod 1)$ , with $v_i$ and $v_j$ belonging to $\mathbf{V} = \mathbf{V}_0$ . Consequently, $v_i - v_j \in \mathbb{Q}_1$ which means that $v_i \sim v_j$ and therefore $i = j$ . This shows that $\mathbf{V}_i \cap \mathbf{V}_j = \emptyset$ if $i \neq j$ . Since each $x \in [0,1)$ is in some equivalence class, $x$ differs modulo 1 from an element in $\mathbf{V}$ by a rational number, say $r_k$ , in $[0,1)$ . Thus $x \in \mathbf{V}_k$ , which proves that $[0,1) \subset \bigcup_{n=0}^{\infty} \mathbf{V}_n$ . The opposite inclusion is obvious. It then follows that

$$
\mathbf {1} = m ([ 0, 1)) = \sum_ {n = 0} ^ {\infty} m (\mathbf {V} _ {n}) = \sum_ {n = 0} ^ {\infty} m (\mathbf {V})
$$

and the right side is either zero or infinite, depending on whether $m(\mathbf{V})$ is zero or positive, a contradiction.

2.1.46. Let $\{r_n\}$ be a sequence of all rationals in $[0, 1)$ with $r_0 = 0$ and define $\mathbf{A}_n = \mathbf{A} + r_n (\bmod 1)$ . Then each $\mathbf{A}_n$ is also measurable

and $m(\mathbf{A}_n) = m(\mathbf{A})$ . Since $\mathbf{A} \subset \mathbf{V}$ , the sets $\mathbf{A}_n$ are pairwise disjoint (see the solution of the preceding problem). Hence

$$
\sum_ {n = 0} ^ {\infty} m (\mathbf {A}) = \sum_ {n = 0} ^ {\infty} m (\mathbf {A} _ {n}) = m \left(\bigcup_ {n = 0} ^ {\infty} \mathbf {A} _ {n}\right) \leq m ([ 0, 1)) = 1,
$$

which gives $m(\mathbf{A}) = 0$ .

2.1.47. [M. Machover, Amer. Math. Monthly 74(1967), 1080-1081.] Let $\mathbf{A} = [-2, -1], \mathbf{B} = [2, 3]$ and let $\mathbf{V}$ be the Vitali set defined in 2.1.45. It follows from the previous result that $m_{\bullet}(\mathbf{V}) = 0$ . Since $\mathbf{V}$ is nonmeasurable, $m^{\bullet}(\mathbf{V}) > 0$ . By 2.1.6,

$$
\begin{array}{l} m ^ {\bullet} (\mathbf {A} \cup \mathbf {V}) = m (\mathbf {A}) + m ^ {\bullet} (\mathbf {V}), \quad m ^ {\bullet} (\mathbf {B} \cup \mathbf {V}) = m (\mathbf {B}) + m ^ {\bullet} (\mathbf {V}), \\ m ^ {\bullet} ((\mathbf {A} \cup \mathbf {V}) \cup (\mathbf {B} \cup \mathbf {V})) = m (\mathbf {A}) + m (\mathbf {B}) + m ^ {\bullet} (\mathbf {V}). \\ \end{array}
$$

On the other hand, we have

$$
m _ {\bullet} (\mathbf {A} \cup \mathbf {V}) + m _ {\bullet} (\mathbf {B} \cup \mathbf {V}) = m _ {\bullet} ((\mathbf {A} \cup \mathbf {V}) \cup (\mathbf {B} \cup \mathbf {V})).
$$

This equality follows from the fact that if $\mathbf{A}$ is a measurable set and $m_{\bullet}(\mathbf{V}) = 0$ , then $m_{\bullet}(\mathbf{A} \cup \mathbf{V}) = m(\mathbf{A})$ . Indeed, if $\mathbf{M}$ is measurable and $\mathbf{M} \subset \mathbf{A} \cup \mathbf{V}$ , then $\mathbf{M} \setminus \mathbf{A}$ is a measurable subset of $\mathbf{V}$ , and therefore $m(\mathbf{M} \setminus \mathbf{A}) = 0$ . Thus $m(\mathbf{M}) = m(\mathbf{M} \cap \mathbf{A}) \leq m(\mathbf{A})$ , which shows that $m_{\bullet}(\mathbf{A} \cup \mathbf{V}) \leq m(\mathbf{A})$ .

2.1.48. Let $\mathbf{A}$ be of positive outer measure. Suppose first that $\mathbf{A} \subset (0, 1)$ . Then we put $\mathbf{B}_n = \mathbf{A} \cap \mathbf{V}_n$ , where $\mathbf{V}_n$ is defined in the solution of 2.1.45. Note that if $\mathbf{B}_n$ is measurable, then $m(\mathbf{B}_n) = 0$ . Indeed, $\mathbf{B}_n = \mathbf{B} + r_n (\bmod 1)$ , where $\mathbf{B}$ is a subset of $\mathbf{V}$ . By 2.1.43, $m^*(\mathbf{B}_n) = m^*(\mathbf{B})$ ; and by 2.1.44, $\mathbf{B}_n$ is measurable if and only if $\mathbf{B}$ is measurable. On the other hand, by the result in the previous problem, if $\mathbf{B}$ is measurable, then $m(\mathbf{B}) = 0$ . Finally, if all the $\mathbf{B}_n$ were measurable, then $0 = m \left( \bigcup_{n=0}^{\infty} \mathbf{B}_n \right) = m^*(\mathbf{A}) > 0$ , a contradiction. This means that at least one of the $\mathbf{B}_n$ is nonmeasurable. Now if $\mathbf{A}$ is not contained in $[0, 1)$ , then there is an interval $[-k, k)$ such that $\mathbf{A} \cap (-k, k)$ is of positive outer measure. Analysis similar to that used in the solution to 2.1.45 can be applied to construct a nonmeasurable set contained in $[-k, k)$ . Consequently, the above reasoning can be repeated.

2.1.49. Set $\mathbf{A}_n = \mathbf{V}_n$ , where the $\mathbf{V}_n$ are defined in the solution to 2.1.45. Since the $\mathbf{A}_n$ are nonmeasurable, $m^*(\mathbf{A}_n) > 0$ (compare 2.1.1). Moreover, all the $\mathbf{A}_n$ are of the same outer measure. Thus

$$
\mathbf {1} = m \left(\left[ 0, 1\right)\right) = m ^ {*} \left(\bigcup_ {n = 0} ^ {\infty} \mathbf {A} _ {n}\right) <   \sum_ {n = 0} ^ {\infty} m ^ {*} \left(\mathbf {A} _ {n}\right) = \infty .
$$

2.1.50. We put $\mathbf{A}_n = \bigcup_{k=n}^{\infty} \mathbf{V}_k$ , where the $\mathbf{V}_k$ are defined in the solution to 2.1.45. Clearly, $\{\mathbf{A}_n\}$ is a decreasing sequence. Since the $\mathbf{V}_k$ are pairwise disjoint, we see that $\bigcap_{n=0}^{\infty} \mathbf{A}_n = \emptyset$ . Moreover, $m^*(\mathbf{A}_n) \geq m^*(\mathbf{V}_n) = m^*(\mathbf{V}) = a > 0$ . Thus

$$
0 = m ^ {*} \left(\bigcap_ {n = 0} ^ {\infty} A _ {n}\right) <   \lim  _ {n \rightarrow \infty} m ^ {*} (A _ {n}) \geq a > 0.
$$

2.1.51. Assume first that $m(\mathbf{A})$ is finite. By the definition of the Lebesgue measure, given $\alpha \in (0, 1)$ , there is a sequence $\{\mathbf{I}_n\}$ of open intervals such that $\mathbf{A} \subset \bigcup_{n=1}^{\infty} \mathbf{I}_n$ and

$$
\alpha \sum_ {n = 1} ^ {\infty} | I _ {n} | \leq m (A).
$$

Hence

$$
\alpha \sum_ {n = 1} ^ {\infty} | \mathbf {I} _ {n} | \leq m \left(\mathbf {A} \cap \bigcup_ {n = 1} ^ {\infty} \mathbf {I} _ {n}\right) \leq \sum_ {n = 1} ^ {\infty} m (\mathbf {A} \cap \mathbf {I} _ {n}).
$$

Consequently, there is $n_0$ such that $\alpha |\mathbf{I}_{n_0}| \leq m(\mathbf{A} \cap \mathbf{I}_{n_0})$ . Taking $\alpha = \frac{3}{4}$ , we find an open interval $\mathbf{I}$ such that $\frac{3}{4} |\mathbf{I}| \leq m(\mathbf{A} \cap \mathbf{I})$ . Put $\delta = \frac{1}{2} |\mathbf{I}|$ . If $|x| < \delta$ , then

$$
(\mathbf {A} \cap \mathbf {I}) \cup ((\mathbf {A} \cap \mathbf {I}) + x) \subset \mathbf {I} \cup (\mathbf {I} + x),
$$

and $\mathbf{I} \cup (\mathbf{I} + x)$ is an interval whose length is less than $\frac{3}{2} |\mathbf{I}|$ . Now we show that $(\mathbf{A} \cap \mathbf{I}) \cap ((\mathbf{A} \cap \mathbf{I}) + x) \neq \emptyset$ . Indeed, if $(\mathbf{A} \cap \mathbf{I}) \cap ((\mathbf{A} \cap \mathbf{I}) + x) = \emptyset$ , then

$$
m ((\mathbf {A} \cap \mathbf {I}) \cup ((\mathbf {A} \cap \mathbf {I}) + x)) = 2 m (\mathbf {A} \cap \mathbf {I}) \geq \frac {3}{2} | \mathbf {I} |,
$$

a contradiction. If $m(\mathbf{A}) = +\infty$ , then by what we have proved, the assertion holds for $\mathbf{A} \cap [-n, n]$ , and consequently, also for $\mathbf{A}$ .

2.1.52. We know that $m^{*}(\mathbf{A}_{n}) > 0$ . If $\mathbf{A}_{n}$ were measurable, then by the foregoing problem, there would exist $\delta > 0$ such that $\mathbf{A}_{n} \cap (\mathbf{A}_{n} + x) \neq \emptyset$ , whenever $|x| < \delta$ . We choose such a rational $x$ different from

$r_i - r_j, r_i - r_j + 1, r_i - r_j - 1, i, j \in \{0, 1, \ldots, n\}$ (see the solution to 2.1.45). There is $y \in \mathbf{A}_n \cap (\mathbf{A}_n + x)$ , that is, $y = v_k + r_k \pmod{1} = x + v_i + r_i \pmod{1}$ with some $v_k$ and $v_i$ in the Vitali set $\mathbf{V}$ defined in 2.1.45. Since $v_k - v_i$ is irrational, so is $x$ , a contradiction.

2.1.53. Assume, contrary to our claim, that $m(\mathbf{A}^c) > 0$ . By the definition of the Lcobsguc measure, given $\alpha \subset (0,1)$ , there is a sequence $\{\mathbf{I}_n\}$ of open intervals such that $\mathbf{A}^c \subset \bigcup_{n=1}^{\infty} \mathbf{I}_n$ and

$$
a \sum_ {n = 1} ^ {\infty} | \mathbf {I} _ {n} | \leq m (\mathbf {A} ^ {c}).
$$

Hence

$$
\alpha \sum_ {n = 1} ^ {\infty} | \mathbf {I} _ {n} | \leq m \left(\dot {\mathbf {A}} ^ {c} \cap \bigcup_ {n = 1} ^ {\infty} \mathbf {I} _ {n}\right) \leq \sum_ {n = 1} ^ {\infty} m (\mathbf {A} ^ {c} \cap \mathbf {I} _ {n}).
$$

Consequently, there is $n_0$ such that $\alpha |\mathbf{I}_{n_0}| \leq m(\mathbf{A}^c \cap \mathbf{I}_{n_0})$ . This together with the given condition implies

$$
\left| \mathbf {I} _ {n _ {0}} \right| = m (\mathbf {A} \cap \mathbf {I} _ {n _ {0}}) + m \left(\mathbf {A} ^ {\mathrm {c}} \cap \mathbf {I} _ {n _ {0}}\right) \geq (c + \alpha) \left| \mathbf {I} _ {n _ {0}} \right|. \tag {1}
$$

Since $0 < c \leq 1$ , we can choose $\alpha \in (0,1)$ so that $c + \alpha > 1$ , which shows that (1) is impossible.

2.1.54. Define sets $\mathbf{A}_0, \mathbf{A}_1$ and $\mathbf{A}_2$ as follows:

$$
\begin{array}{l} \mathbf {A} _ {0} = \{r + n \sqrt {2}: r \in \mathbb {Q}, n \in \mathbb {Z} \}, \\ \mathbf {A} _ {1} = \{r + 2 n \sqrt {2}: r \in \mathbb {Q}, n \in \mathbb {Z} \}, \\ \mathbf {A} _ {2} = \{r + (2 n + 1) \sqrt {2}: r \in \mathbb {Q}, n \in \mathbb {Z} \}. \\ \end{array}
$$

Then $\mathbf{A}_2 = \mathbf{A}_1 + \sqrt{2}$ and $\mathbf{A}_0 = \mathbf{A}_1 \cup \mathbf{A}_2$ . Now define an equivalence relation $\sim$ on $\mathbb{R}$ by letting $x \sim y$ if and only if $x - y \in \mathbf{A}_0$ . By the axiom of choice there is a set $\mathbf{B}$ which contains exactly one element from each equivalence class under $\sim$ . Let

$$
\mathbf {A} = \mathbf {B} + \mathbf {A} _ {1} = \{b + a _ {1}: b \in \mathbf {B}, a _ {1} \in \mathbf {A} _ {1} \}.
$$

Let $\mathbf{C}$ be a measurable subset of $\mathbf{A}$ and suppose that $m(\mathbf{C}) > 0$ . By the result in 2.1.51, there is $\delta > 0$ such that $\mathbf{C} \cap (\mathbf{C} + x)$ is nonempty whenever $|x| < \delta$ . This implies that $\mathbf{A} \cap (\mathbf{A} + x)$ is nonempty whenever $|x| < \delta$ . Since $\mathbf{A}_2$ is dense in $\mathbb{R}$ , there is an $x \in \mathbf{A}_2$ such that $|x| < \delta$ . Since $\mathbf{A} \cap (\mathbf{A} + x)$ is nonempty, there is $y = x + b_1 + a_1 = b_2 + a_1'$ .

with some $b_1, b_2 \in \mathbf{B}$ and $a_1, a_1' \in \mathbf{A}_1$ . Hence $b_2 - b_1 \in \mathbf{A}_0$ , and therefore $b_2 = b_1$ . Consequently, $x = a_1' - a_1$ cannot be an element of $\mathbf{A}_2$ , a contradiction. This proves that each measurable subset of $\mathbf{A}$ has Lebesgue measure zero. It is easy to check that $\mathbf{A}^c = \mathbf{B} + \mathbf{A}_2$ . Hence $\mathbf{A}^c = \mathbf{A} + \sqrt{2}$ , and therefore each measurable subset of $\mathbf{A}^c$ is of the form $\mathbf{C} + \sqrt{2}$ for some Lebesgue measurable subset $\mathbf{C}$ of $\mathbf{A}$ . It then follows that each measurable subset of $\mathbf{A}^c$ has Lebesgue measure zero.

It is worth mentioning here that $\mathbf{A}$ and $\mathbf{A}^c$ are nonmeasurable sets.

2.1.55. Assume that $f$ is Riemann integrable on $[a, b]$ and, for $\varepsilon > 0$ , set $\mathbf{J}_{\varepsilon} = \{x : o_{f}(x) \geq \varepsilon\}$ , where $o_{f}(x)$ denotes the oscillation of $f$ at $x$ (see, e.g., II, 1.7.12). It follows from the result in 1.7.18 that $|\mathbf{J}_{\varepsilon}| = 0$ for every $\varepsilon > 0$ , where $|\mathbf{J}_{\varepsilon}|$ is the Jordan measure of $\mathbf{J}_{\varepsilon}$ . If $x$ is a point of discontinuity of $f$ , then $o_{f}(x) \neq 0$ (see, e.g., II, 1.7.12). This means that there is a positive integer $n$ such that $o_{f}(x) \geq 1 / n$ . Consequently, the set $\mathbf{D}$ of points of discontinuity of $f$ satisfies

$$
\mathbf {D} \subset \bigcup_ {n = 1} ^ {\infty} \mathbf {J} _ {1 / n}.
$$

Since $|\mathbf{J}_{1/n}|^* = 0$ , we also have $m^*(\mathbf{J}_{1/n}) = 0$ , and therefore $m^*(\mathbf{D}) = m(\mathbf{D}) = 0$ . To prove that the condition is also sufficient, assume that $m^*(\mathbf{D}) = m(\mathbf{D}) = 0$ . By the result in 1.7.18, it is enough to show that $|\mathbf{J}_c| = 0$ for every $\varepsilon > 0$ . Since $\mathbf{J}_c \subset \mathbf{D}$ , we have $m^*(\mathbf{J}_c) = 0$ . Thus given $\delta > 0$ , there is a countable covering of $\mathbf{J}_c$ by open intervals $\{\mathbf{I}_n\}$ such that $\sum_{n=1}^{\infty} |\mathbf{I}_n| < \delta$ . Since $\mathbf{J}_\varepsilon$ is a compact set (see, e.g., II, 1.7.13), by Borel's covering theorem, there is a finite subcover $\bigcup_{k=1}^{N} \mathbf{I}_{n_k}$ . This shows that $|\mathbf{J}_\varepsilon|^* < \delta$ . Letting $\delta$ go to zero, we get $|\mathbf{J}_\varepsilon|^* = 0$ .

2.1.56. [Leo M. Levine, Amer. Math. Monthly 84 (1977), 205]. We first show that $\mathbf{D} \cap \mathbf{L}$ is countable. As in the solution to the preceding problem, we set $\mathbf{J}_{1/n} = \{x \in [a,b] : o_{f}(x) > 1/n\}$ . Since $\mathbf{D} \cap \mathbf{L} = \bigcup_{n=1}^{\infty} (\mathbf{J}_{1/n} \cap \mathbf{L})$ , it suffices to show that each set $\mathbf{J}_{1/n} \cap \mathbf{L}$ is countable. If $x_0 \in \mathbf{J}_{1/n} \cap \mathbf{L}$ , then there is $\delta > 0$ such that

$$
| f (x) - f \left(x _ {0} ^ {-}\right) | <   1 / (2 n)
$$

for $x \in (x_0 - \delta, x_0)$ . Therefore

$$
| f (z) - f (u) | <   1 / n
$$

for $z, u \in (x_0 - \delta, x_0)$ . Consequently, if $x \in (x_0 - \delta, x_0)$ , $o_f(x) \leq 1 / n$ , so that $x \notin \mathbf{J}_{1 / n}$ . Thus any point of $\mathbf{J}_{1 / n} \cap \mathbf{L}$ is the right endpoint of an open interval which contains no point of $\mathbf{J}_{1 / n} \cap \mathbf{L}$ . Since these open intervals are disjoint, they form a countable set. So, $\mathbf{J}_{1 / n} \cap \mathbf{L}$ is countable.

Since $\mathbf{D} = (\mathbf{D} \cap \mathbf{L}) \cup (\mathbf{D} \cap \mathbf{L}^c) = (\mathbf{D} \cap \mathbf{L}) \cup ([a, b] \setminus \mathbf{L})$ and $m(\mathbf{D} \cap \mathbf{L}) = 0$ , the stated criterion for Riemann integrability is a consequence of the Lebesgue criterion stated in the previous problem.

2.1.57. We first note that since $f$ is continuous, the set $\mathbf{A}$ is closed and so Lebesgue measurable. Moreover, $\mathbf{A}' = \{h \in [0,1] : 1 - h \in \mathbf{A}\}$ has the same Lebesgue measure. Our aim is to show that $\mathbf{A} \cup \mathbf{A}' = [0,1]$ . For $h \in [0,1]$ , define

$$
g (x) = \left\{ \begin{array}{l l} f (x + h) - f (x) & \text {i f} x + h \leq 1, \\ f (x + h - 1) - f (x) & \text {i f} x + h > 1. \end{array} \right.
$$

By assumption, $g$ is continuous on $[0,1]$ . If $f$ attains its minimum and maximum values at $x_0$ and $x_1$ , respectively, then $g(x_0) \geq 0$ and $g(x_1) \leq 0$ . By the intermediate value property, there is $x_2$ such that $g(x_2) = 0$ . It then follows that $h$ is either in $\mathbf{A}$ or in $\mathbf{A}'$ .

# 2.2. Lebesgue Measurable Functions

2.2.1. If $f$ is measurable, then for every real $c$ , the sets $\{x : f(x) > c\}$ and $\{x : f(x) < -c\}$ are measurable, and so is $\{x : |f(x)| > c\} = \{x : f(x) > c\} \cup \{x : f(x) < -c\}$ . The following example shows that the opposite implication is not true. Let $A$ be a measurable set and $V$ a nonmeasurable subset of $A$ . Then the function $f$ given by

$$
f (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x \in \mathbf {V}, \\ - 1 & \text {i f} x \in \mathbf {A} \backslash \mathbf {V} \end{array} \right.
$$

is nonmeasurable, although $|f|$ is measurable.

2.2.2. Let $f$ be a function defined in the solution to the previous problem, and let $g = -f$ .

2.2.3. Let $\mathbf{V}$ be a nonmeasurable subset of $[0,1]$ , and consider the function $f$ defined as follows:

$$
f (x) = \left\{ \begin{array}{l l} x & \text {i f} x \in \mathbf {V}, \\ - x & \text {i f} x \in [ 0, 1 ] \setminus \mathbf {V}. \end{array} \right.
$$

Then the sets $f^{-1}(c)$ are either empty or singletons, and so they are measurable, but the function $f$ is not measurable.

2.2.4. Given a real $a$ , there is an increasing sequence $\{c_n\}$ of elements in $\mathbf{C}$ such that $a = \lim_{n\to \infty}c_n$ . Hence

$$
\{x \in \mathbf {A}: f (x) \geq a \} = \bigcap_ {n = 1} ^ {\infty} \{x \in \mathbf {A}: f (x) \geq c _ {n} \}
$$

is a measurable set.

2.2.5. Suppose first that $f^{-1}(\mathbf{G})$ is measurable for every open $\mathbf{G} \subset \mathbb{R}$ . Then, in particular, $f^{-1}((c,\infty))$ is measurable for every real $c$ . On the other hand, each open set $\mathbf{G}$ is a union of countably many open intervals

$$
\mathbf {G} = \bigcup_ {n = 1} ^ {\infty} (a _ {n}, b _ {n}). \quad \text {w h e r e} \quad a _ {n}, b _ {n} \in \mathbb {R}. a _ {n} <   b _ {n},
$$

and since $f^{-1}((a_n, b_n)) = f^{-1}((- \infty, b_n)) \cap f^{-1}((a_n, \infty))$ is a measurable set, so is $f^{-1}(\mathbf{G})$ .

2.2.6. The set $\mathfrak{A} = \{\mathbf{A} \subset \mathbb{R} : f^{-1}(\mathbf{A}) \in \mathfrak{M}\}$ , where $\mathfrak{M}$ is the $\sigma$ -algebra of all Lebesgue measurable sets of $\mathbb{R}$ , is a $\sigma$ -algebra. By the result in the preceding problem, open sets belong to $\mathfrak{A}$ , and since the collection $\mathfrak{B}$ of Borel sets is the smallest $\sigma$ -algebra which contains all of the open sets in $\mathbb{R}$ , $\mathfrak{B} \subset \mathfrak{A}$ .

2.2.7. Let $f$ be a continuous function on the measurable set $\mathbf{A}$ , and $c$ any real number. We must show that $\mathbf{B} = \{x \in \mathbf{A} : f(x) > c\}$ is a measurable subset of $\mathbf{A}$ . When $\mathbf{B}$ is empty, then it is measurable. Otherwise, if $x \in \mathbf{B}$ , then, by the continuity, $f(x) > c$ in some neighborhood of $x$ , say, $(x - \delta(x), x + \delta(x)) \cap \mathbf{A}$ . Consequently,

$$
\mathbf {B} = \bigcup_ {\boldsymbol {x} \in \mathbf {B}} ((\boldsymbol {x} - \delta (\boldsymbol {x}), \boldsymbol {x} + \delta (\boldsymbol {x})) \cap \mathbf {A}) = \left(\bigcup_ {\boldsymbol {x} \in \mathbf {B}} (\boldsymbol {x} - \delta (\boldsymbol {x}), \boldsymbol {x} + \delta (\boldsymbol {x}))\right) \cap \mathbf {A}.
$$

This shows that $\mathbf{B}$ , as the intersection of an open set and the measurable set $\mathbf{A}$ , is itself measurable.

2.2.8. We must show that $\{x \in \mathbf{A} : g(x) > c\}$ is a measurable subset of $\mathbf{A}$ for every real $c$ . To this end, set $\mathbf{B} = \{x \in \mathbf{A} : f(x) \neq g(x)\}$ . Then, since

$$
\begin{array}{l} \{x \in A: y (x) > c \} = \{x \in A \backslash B: y (x) > c \} \cup \{x \in B: y (x) > c \} \\ = \{x \in A \backslash B: f (x) > c \} \cup \{x \in B: g (x) > c \} \\ = \left(\{x \in A: f (x) > c \} \cap (A \backslash B)\right) \\ \cup \{x \in \mathbf {B}: g (x) > c \}, \\ \end{array}
$$

we see that the set $\{x\in \mathbf{A}:g(x) > c\}$ is measurable.

2.2.9. This is an immediate consequence of 2.2.7, 2.1.55 and 2.2.8.

2.2.10. We know that each function of bounded variation on $[a, b]$ is a difference of two monotonic functions, and therefore, by the result in 1.1.21, it is Riemann integrable on that interval. Thus the result follows from the previous problem.

2.2.11. We first show that $\varphi$ maps the Cantor set onto $[0, 1]$ . Indeed, any number in $[0, 1]$ can be written as $\sum_{n=1}^{\infty} \frac{b_n}{2^n}$ with $b_n = 0$ or $1$ . So

$$
\sum_ {n = 1} ^ {\infty} \frac {b _ {n}}{2 ^ {n}} = \varphi \left(\sum_ {n = 1} ^ {\infty} \frac {2 b _ {n}}{3 ^ {n}}\right).
$$

Now observe that the Cantor function $\varphi$ is constant on each open interval that is removed during the construction of the Cantor set $\mathbf{C}$ (see, e.g., II, 1.3.1 for the construction of $\mathbf{C}$ ). Since $\varphi(1/3) = \varphi(2/3) = 1/2$ , we have

$$
\varphi (x) = \begin{array}{l} 1 \\ 2 \end{array} \quad \text {f o r} \quad x \in \left( \begin{array}{l l} 1 & 2 \\ \bar {3} & \bar {3} \end{array} \right).
$$

Further, since $\varphi(1/9) = \varphi(2/9) = 1/4$ and $\varphi(7/9) = \varphi(8/9) = 3/4$ ,

$$
\varphi (x) = \frac {1}{2 ^ {2}} \quad \text {f o r} \quad x \in \left(\frac {1}{3 ^ {2}}, \frac {2}{3 ^ {2}}\right), \quad \varphi (x) = \frac {3}{2 ^ {2}} \quad \text {f o r} \quad x \in \left(\frac {7}{3 ^ {2}}, \frac {8}{3 ^ {2}}\right).
$$

By induction, the function $\varphi$ consecutively equals

$$
\frac {1}{2 ^ {n}}, \frac {3}{2 ^ {n}}, \frac {5}{2 ^ {n}}, \dots , \frac {2 ^ {n} - 1}{2 ^ {n}}
$$

on the intervals removed at the nth stage of the construction of C. A graph of $\varphi$ is sketched below.

![](images/3ba9847be1c0f0a4675463213a26959cdbc668d5a72dd7afeeb30578d97c556e.jpg)

It then follows that the Cantor function $\varphi$ is increasing. We now show that it is continuous. Since $\varphi$ is monotonically increasing, for each $x_0 \in (0,1)$ , we have $\varphi(x_0^-) \leq \varphi(x_0) \leq \varphi(x_0^+)$ (see, e.g., II, 1.1.35). If, for example, $\varphi(x_0^-) < \varphi(x_0)$ , then there are no values of $\varphi$ in the interval $(\varphi(x_0^-), \varphi(x_0))$ . On the other hand, $\varphi(\mathbf{C}) = [0,1]$ , a contradiction. Likewise, one can show that $\varphi$ is continuous at 0 and at 1. Since $\varphi$ is a constant function on each removed open interval and the Cantor set has Lebesgue measure zero, $\varphi'(x) = 0$ almost everywhere on $[0,1]$ .

2.2.12. We first recall that if $f$ is a one-one map of $\mathbf{X}$ onto $\mathbf{Y}$ , then for $\mathbf{A}, \mathbf{B} \subset \mathbf{X}$ ,

$$
f (\mathbf {A} \cap \mathbf {B}) = f (\mathbf {A}) \cap f (\mathbf {B}) \quad \text {a n d} \quad f (\mathbf {A} \backslash \mathbf {B}) = f (\mathbf {A}) \backslash f (\mathbf {B}).
$$

Now we set

$$
\mathfrak {A} = \{\mathrm {A} \subset \mathbb {R}: f (\mathrm {A}) \in \mathfrak {B} \},
$$

where $\mathfrak{B}$ denotes the collection of Borel sets. We claim that $\mathfrak{A}$ is a $\sigma$ -algebra if $f$ is a one-one mapping of $\mathbb{R}$ onto $\mathbb{R}$ . Indeed, if $\mathbf{A} \in \mathfrak{A}$ , then $\mathbf{A}^c \in \mathfrak{A}$ , because $f(\mathbf{A}^c) = f(\mathbb{R} \setminus \mathbf{A}) = \mathbb{R} \setminus f(\mathbf{A})$ . Moreover, if $\{\mathbf{A}_n\}$ is a sequence of sets in $\mathfrak{A}$ , then $f\left(\bigcup_{n=1}^{\infty} \mathbf{A}_n\right) = \bigcup_{n=1}^{\infty} f(\mathbf{A}_n)$ , which shows that $\bigcup_{n=1}^{\infty} \mathbf{A}_n \in \mathfrak{A}$ . Furthermore, since $f$ is strictly monotonic (see, e.g., II, 1.3.16), we have $f([a, b]) = [f(a), f(b)]$ or $f([a, b]) =$

$[f(b), f(a)]$ . Hence $\mathfrak{A}$ contains all closed intervals, and consequently all Borel sets.

2.2.13. (a) Let $\varphi$ be the Cantor function defined in 2.2.11. Extend the function to all of $\mathbb{R}$ by setting $\varphi(x) = 0$ for $x < 0$ and $\varphi(x) = 1$ for $x > 1$ , and put $f(x) = x + \varphi(x)$ . Then $f$ is a strictly increasing and continuous map of $\mathbb{R}$ onto $\mathbb{R}$ . By the result in the previous problem, $f$ maps Borel sets to Borel sets. Let $\mathbf{C} = [0,1] \setminus \bigcup_{n=1}^{\infty}(a_n, b_n)$ , where $\{(a_n, b_n)\}$ is the sequence of intervals that were removed during the construction of the Cantor set $\mathbf{C}$ . We will show that $m(f(\mathbf{C})) = 1$ . To this end, note that

$$
\begin{array}{l} m (f ([ 0, 1 ] \backslash \mathbf {C})) = m \left(\bigcup_ {n = 1} ^ {\infty} f ((a _ {n}, b _ {n}))\right) = \sum_ {n = 1} ^ {\infty} m (f ((a _ {n}, b _ {n}))) \\ = \sum_ {n = 1} ^ {\infty} m ((a _ {n} + \varphi (a _ {n}), b _ {n} + \varphi (b _ {n}))) \\ = \sum_ {n = 1} ^ {\infty} m ((a _ {n}, b _ {n})) = 1. \\ \end{array}
$$

Since the image of $[0,1]$ under $f$ is $[0,2]$ , we get

$$
2 = m ([ 0, 2 ]) = m (f (\mathbf {C})) + m (f ([ 0, 1 ] \backslash \mathbf {C})) = m (f (\mathbf {C})) + 1.
$$

Thus $m(f(\mathbf{C})) = 1$ . By the result in 2.1.48, there is a nonmeasurable set $\mathbf{V}$ contained in $f(\mathbf{C})$ . Then $\mathbf{A} = f^{-1}(\mathbf{V}) \subset \mathbf{C}$ and therefore is measurable, but its image $f(\mathbf{A}) = f(f^{-1}(\mathbf{V})) = \mathbf{V}$ is nonmeasurable. (b) It suffices to take $g = f^{-1}$ , where $f$ is the function defined above.

2.2.14. Note that the set $\mathbf{A} = f^{-1}(\mathbf{V})$ constructed in the preceding solution is an example of a measurable set that is not Borel. Indeed, if it were a Borel set, then by the result in 2.2.12 $f(\mathbf{A}) = \mathbf{V}$ would also be a Borel set, a contradiction.

2.2.15. Suppose first that a continuous function $f$ satisfies the condition

(1) $\mathbf{E} \subset [a, b]$ and $m(\mathbf{E}) = 0$ implies $m(f(\mathbf{E})) = 0$ .

If $\mathbf{A} \subset [a, b]$ is measurable, then there are an $\mathcal{F}_{\sigma}$ set $\mathbf{F} \subset \mathbf{A}$ and $\mathbf{E} \subset [a, b]$ of measure zero such that $\mathbf{A} = \mathbf{F} \cup \mathbf{E}$ (see, e.g., 2.1.12). Since $f(\mathbf{A}) = f(\mathbf{F}) \cup f(\mathbf{E})$ , where $f(\mathbf{F})$ is an $\mathcal{F}_{\sigma}$ set and $m(f(\mathbf{E})) = 0$ , $f(\mathbf{A})$

is measurable. Suppose now that the image $f(\mathbf{A})$ of any measurable $\mathbf{A}$ is measurable. If condition (1) is not satisfied, then there is $\mathbf{E}_0$ of measure zero such that $m(f(\mathbf{E}_0)) > 0$ . By the result in 2.1.45, there is a nonmeasurable set $\mathbf{V} \subset f(\mathbf{E}_0)$ , a contradiction.

2.2.16. For every real $c$ , we have

$$
(f \circ g) ^ {- 1} ((- \infty , c)) = g ^ {- 1} (f ^ {- 1} ((- \infty , c))).
$$

By the continuity of $f$ , the set $f^{-1}((-\infty, c))$ is open in $g(\mathbf{A})$ ; that is, $f^{-1}((-\infty, c)) = g(\mathbf{A}) \cap \mathbf{G}$ , where $\mathbf{G}$ is open in $\mathbb{R}$ . Consequently,

$$
(f \circ g) ^ {- 1} ((- \infty , c)) = g ^ {- 1} (g (\mathbf {A}) \cap \mathbf {G}) = \mathbf {A} \cap g ^ {- 1} (\mathbf {G})
$$

is a measurable set.

2.2.17. The following example shows that the answer is NO. Let $f$ be the function defined in the solution to 2.2.13(a). Then $f$ is strictly increasing and continuous on [0,1], and the image of [0,1] under $f$ is [0,2]. Moreover, since $m(f(\mathbf{C})) = 1$ , where $\mathbf{C}$ is the Cantor set, there is a nonmeasurable set $\mathbf{V} \subset f(\mathbf{C})$ (see, e.g., 2.1.48). It is also clear that $\mathbf{A} = f^{-1}(\mathbf{V}) \subset \mathbf{C}$ is measurable. Now let $g(x) = f^{-1}(x)$ , $x \in [0,2]$ , and let $h = \chi_{\mathbf{A}}$ be the characteristic function of $\mathbf{A}$ . To see that $h \circ g$ is not measurable, observe that

$$
\{x \in [ 0, 2 ]: (h \circ g) (x) > 0 \} = V.
$$

2.2.18. It suffices to use the results in 2.2.5 and 2.2.6 and the fact that

$$
(f \circ g) ^ {- 1} (\mathbf {G}) = g ^ {- 1} (f ^ {- 1} (\mathbf {G})).
$$

It is worth noting here that the result in 2.2.16 is contained as a special case of 2.2.18.

2.2.19. Let $f$ be the function defined in the solution to 2.2.13(a). Then the image of [0,1] under $f$ is [0,2] and $m(f(\mathbf{C})) = 1$ , where $\mathbf{C}$ is the Cantor set. By the result in 2.1.48, there is a nonmeasurable set $\mathbf{V} \subset f(\mathbf{C})$ . Moreover, since $\mathbf{A} = f^{-1}(\mathbf{V}) \subset \mathbf{C}$ , the set $\mathbf{A}$ is measurable. Without loss of generality we can assume that $0, 1 \in \mathbf{A}$ . Define

$$
f _ {1} (x) = \left\{ \begin{array}{l l} f (x) & \text {i f} x \in \mathbf {A}, \\ 2 + f (x) & \text {i f} x \in [ 0, 1 ] \backslash \mathbf {A} \end{array} \right.
$$

and

$$
g (x) = \left\{ \begin{array}{l l} f _ {1} (x) & \text {i f} x \in [ 0, 1 ], \\ f _ {1} (x - 1) + 2 & \text {i f} x \in (\mathbf {A} + 1) \backslash \{1 \}, \\ f _ {1} (x - 1) - 2 & \text {i f} x \in ([ 0, 1 ] \backslash \mathbf {A}) + 1. \end{array} \right.
$$

Then $g$ is a one-one mapping of [0,2] onto [0,4]. Since $\mathbf{A}$ is a measurable set and $f$ is a measurable function, $g$ is also measurable. To show that $g^{-1}$ is not measurable, observe first that

$$
g ([ 0, 1 ]) = g (\mathbf {A}) \cup g ([ 0, 1 ] \backslash \mathbf {A}) = \dot {\mathbf {V}} \cup (2 + ([ 0, 2 ] \backslash V)).
$$

This means that

$$
(g ^ {- 1}) ^ {- 1} ([ 0, 1 ]) = \mathbf {V} \cup (2 + ([ 0, 2 ] \backslash V)).
$$

If $(g^{-1})^{-1}([0,1])$ were measurable, then the set

$$
(g ^ {- 1}) ^ {- 1} ([ 0, 1 ]) \setminus [ 2, 4 ] = \mathbf {V} \setminus \{2 \}
$$

would also be measurable, a contradiction.

2.2.20. We extend the function $f$ by setting $f(x) = f'(b)(x - b) + f(b)$ for $x > b$ so that the extended function $f$ is differentiable on $[a, \infty)$ . Now observe that for $x \in [a, b]$ ,

$$
f ^ {\prime} (x) = \lim  _ {n \rightarrow \infty} n \left(f \left(x + \frac {1}{n}\right) - f (x)\right).
$$

The result follows from Theorem 3 and 2.2.7.

2.2.21. We put

$$
\mathbf {A} _ {n} = \{x \in \mathbf {A}: | f (x) | > n \}, \quad n = 1, 2, \dots
$$

If $\mathbf{C} = \{x\in \mathbf{A}:|f(x)| = \infty \}$ , then by assumption $m(\mathbf{C}) = 0$ . Moreover,

$$
\mathbf {A} _ {1} \supset \mathbf {A} _ {2} \supset \mathbf {A} _ {3} \supset \dots \quad \text {a n d} \quad \mathbf {C} = \bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}.
$$

By the result in 2.1.17, $\lim_{n\to \infty}m(\mathbf{A}_n) = m(\mathbf{C}) = 0$ . Hence, given $\varepsilon >0$ there is $n_0$ such that $m(\mathbf{A}_{n_0}) < \varepsilon$ . So we put $\mathbf{B} = \mathbf{A}\setminus \mathbf{A}_{n_0}$ .

2.2.22. By assumption, there is $\mathbf{A}_0\subset \mathbf{A}$ with $m(\mathbf{A}_0) = 0$ such that for every $x\in \mathbf{A}_1 = (\mathbf{A}\setminus \mathbf{A}_0)$

$$
\lim  _ {n \rightarrow \infty} f _ {n} (x) = f (x), \quad | f _ {n} (x) | <   \infty , n \in \mathbb {N}.
$$

For positive integers $n$ and $m$ , define

$$
\begin{array}{l} \mathbf {A} _ {m, n} = \{x \in \mathbf {A} _ {1}: | f _ {j} (x) - f (x) | <   1 / m \quad \text {f o r a l l} j \geq n \} \\ = \bigcap_ {j = n} ^ {\infty} \left\{x \in A _ {1}: | f _ {j} (x) - f (x) | <   1 / m \right\}. \\ \end{array}
$$

We have

$$
\mathbf {A} _ {m, 1} \subset \mathbf {A} _ {m, 2} \subset \dots \quad \text {f o r} \quad m = 1, 2, \dots ,
$$

and

$$
\mathbf {A} _ {1} = \bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {m, n},
$$

because the sequence $\{f_n\}$ converges to $f$ on $\mathbf{A_1}$ . By the result in 2.1.16,

$$
m \left(\mathbf {A} _ {1}\right) = \lim  _ {n \rightarrow \infty} m \left(\mathbf {A} _ {m, n}\right).
$$

Thus, given $m \in \mathbb{N}$ and $\varepsilon > 0$ , there is a positive integer $n_m$ such that

$$
m \left(\mathrm {A} _ {1} \backslash \mathrm {A} _ {m, n _ {m}}\right) = m \left(\mathrm {A} _ {1}\right) - m \left(\mathrm {A} _ {m, n _ {m}}\right) <   \frac {\varepsilon}{2 ^ {m}}.
$$

So, if

$$
\mathbf {A} _ {2} = \mathbf {A} _ {0} \cup \bigcup_ {m = 1} ^ {\infty} (\mathbf {A} _ {1} \backslash \mathbf {A} _ {m, n _ {m}}),
$$

then

$$
m \left(A _ {2}\right) \leq \sum_ {m = 1} ^ {\infty} m \left(A _ {1} \backslash A _ {m, n _ {m}}\right) <   \sum_ {m = 1} ^ {\infty} \frac {\varepsilon}{2 ^ {m}} = \varepsilon .
$$

We set $\mathbf{B} = \mathbf{A} \setminus \mathbf{A}_2$ and note that $\mathbf{B} = \bigcap_{m=1}^{\infty} \mathbf{A}_{m,n_m}$ . Hence if $x \in \mathbf{B}$ , then $x \in \mathbf{A}_{m,n_m}$ for $m = 1, 2, \ldots$ , which means that

$$
\left| f _ {j} (x) - f (x) \right| <   1 / m \quad \text {f o r} \quad j \geq n _ {m}.
$$

This shows that the sequence $\{f_n\}$ converges uniformly to $f$ on $\mathbf{B}$ .

2.2.23. If $\mathbf{A} = [0, \infty)$ and $f_n = \chi_{[n, \infty)}$ , then $\{f_n\}$ converges to $f = 0$ on $\mathbf{A}$ . Assume that there is $\mathbf{B}$ such that $m(\mathbf{A} \setminus \mathbf{B}) < \varepsilon$ and $\{f_n\}$ converges uniformly to the zero function on $\mathbf{B}$ . Then $m(\mathbf{B}) = \infty$ , and consequently, $\mathbf{B}$ is an unbounded set. Thus for every $n \in \mathbb{N}$ there is $x_n \in \mathbf{B} \cap [n, \infty)$ . So, $f_n(x_n) = 1$ , a contradiction.

2.2.24. Suppose first that $m(\mathbf{A}) < \infty$ . By the Egorov theorem there is $\mathbf{B}_1 \subset \mathbf{A}$ such that $m(\mathbf{A} \setminus \mathbf{B}_1) < 1/2$ and $f_n$ converges uniformly on $\mathbf{B}_1$ to $f$ . Applying the Egorov theorem to the set $\mathbf{A} \setminus \mathbf{B}_1$ , we find $\mathbf{B}_2 \subset (\mathbf{A} \setminus \mathbf{B}_1)$ such that $m(\mathbf{A} \setminus (\mathbf{B}_1 \cup \mathbf{B}_2)) < 1/2^2$ and $f_n$ converges uniformly on $\mathbf{B}_2$ to $f$ . By induction, we find a sequence of measurable sets $\{\mathbf{B}_i\}$ such that $\mathbf{B}_i \subset \mathbf{A} \setminus \bigcup_{k=1}^{i-1} \mathbf{B}_k$ and $m(\mathbf{A} \setminus \bigcup_{k=1}^{i} \mathbf{B}_k) < 1/2^i$ and $f_n$ converges uniformly on $\mathbf{B}_i$ to $f$ . Setting $\mathbf{B} = \bigcup_{k=1}^{\infty} \mathbf{B}_k$ , we see that

$$
m (\mathbf {A} \backslash \mathbf {B}) = m \left(\mathbf {A} \backslash \bigcup_ {k = 1} ^ {\infty} \mathbf {B} _ {k}\right) \leq m \left(\mathbf {A} \backslash \bigcup_ {k = 1} ^ {i} \mathbf {B} _ {k}\right) <   \frac {1}{2 ^ {i}}
$$

for every $i = 1,2,\ldots$ , which gives $m(\mathbf{A} \setminus \mathbf{B}) = 0$ . Suppose now that $m(\mathbf{A}) = \infty$ . Then $\mathbf{A} = \bigcup_{k=1}^{\infty} \mathbf{A}_k$ , where $m(\mathbf{A}_k) < \infty$ , and one can apply the result just proved to each $\mathbf{A}_k$ .

2.2.25. We have $[0,1) = \bigcup_{n=0}^{\infty} V_n$ and $V_i \cap V_j = \emptyset$ for $i \neq j$ . So, if $x \in [0,1)$ , then there is $n_0$ such that $x \in V_{n_0}$ . Consequently, $x \notin \bigcup_{i=n}^{\infty} V_i$ for $n > n_0$ , which means that $f_n(x) = 0$ for $n > n_0$ . Therefore $\lim_{n \to \infty} f_n(x) = 0$ . We know from the solution of 2.1.45 that for every $n$ , the outer measure $m^*(V_n) = m^*(V) = \alpha > 0$ . Now we take $\varepsilon = \alpha/2$ and suppose, contrary to our claim, that there is a measurable set $B$ with $m([0,1) \setminus B) < \varepsilon$ and $f_n \to 0$ uniformly on $B$ . It then follows that there is $n_1$ such that $f_n(x) = 0$ for $n > n_1$ and all $x \in B$ . On the other hand,

$$
f _ {n} (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x \in \bigcup_ {i = 0} ^ {n - 1} \mathbf {V} _ {i}, \\ 1 & \text {i f} x \in \bigcup_ {i = n} ^ {\infty} \mathbf {V} _ {i}, \end{array} \right.
$$

which implies $\mathbf{B} \subset \bigcup_{i=0}^{n-1} \mathbf{V}_i$ for $n > n_1$ . Hence

$$
m ([ 0, 1) \backslash B) \geq m ^ {*} \left(\bigcup_ {i = n} ^ {\infty} V _ {i}\right) \geq m ^ {*} (V _ {n}) = \alpha ,
$$

a contradiction. Finally, we remark that this example shows that the assumption of measurability of $f_{n}$ is essential and cannot be omitted in the Egorov theorem.

2.2.26. Let $f_n, n = 1, 2, \ldots$ , be given by

$$
f _ {n} (x) = \left\{ \begin{array}{l l} 0 & \text {i f} x = 0, \\ n & \text {i f} 0 <   x \leq 1 / n, \\ 1 / n & \text {i f} 1 / n <   x \leq 1. \end{array} \right.
$$

Then the pointwise limit of $\{f_n\}$ on $[0,1]$ is the zero function. If $m(\mathbf{B}) = 1$ , then $\max \{f_n(x):x\in \mathbf{B}\} = n$ , so the convergence cannot be uniform on $\mathbf{B}$ . We remark that this example shows that in the Egorov theorem the assertion $m(\mathbf{A}\setminus \mathbf{B}) < \varepsilon$ cannot be replaced by $m(\mathbf{A}\setminus \mathbf{B}) = 0$ .

2.2.27. We first show that the condition is sufficient for measurability of $f$ . Let $c \in \mathbb{R}$ be arbitrarily chosen, and set $\mathbf{A}_0 = \{x \in \mathbf{A} : f(x) \geq c\}$ . Given $\varepsilon > 0$ , there is a closed set $\mathbf{F} \subset \mathbf{A}$ such that $m(\mathbf{A} \backslash \mathbf{F}) < \varepsilon$ and $f$ restricted to $\mathbf{F}$ is continuous. This implies that the set $\mathbf{F}_0 = \{x \in \mathbf{F} : f(x) \geq c\} = \mathbf{A}_0 \cap \mathbf{F}$ is closed. Since $\mathbf{A}_0 \setminus \mathbf{F}_0 \subset \mathbf{A} \setminus \mathbf{F}$ , we get $m(\mathbf{A}_0 \setminus \mathbf{F}_0) < \varepsilon$ . Hence the measurability of $\mathbf{A}_0$ follows from 2.1.12(iv). Thus $f$ is measurable. We now show that the condition is necessary. Assume first that $f$ is a bounded function. Then by the approximation theorem for measurable functions (Theorem 4), there is a sequence $\{\varphi_n\}$ of simple functions uniformly convergent to $f$ on $\mathbf{A}$ . We note that for each simple function $\varphi_n$ there is a closed set $\mathbf{F}_n$ such that $m(\mathbf{A} \setminus \mathbf{F}_n) < \varepsilon / 2^n$ and $\varphi_n$ restricted to $\mathbf{F}_n$ is continuous. Hence $f$ restricted to $\mathbf{F} = \bigcap_{n=1}^{\infty} \mathbf{F}_n$ is continuous, and

$$
m (\mathbf {A} \backslash \mathbf {F}) = m \left(\bigcup_ {n = 1} ^ {\infty} (\mathbf {A} \backslash \mathbf {F} _ {n})\right) <   \sum_ {n = 1} ^ {\infty} \frac {\varepsilon}{2 ^ {n}} = \varepsilon .
$$

In the case when $f$ is unbounded, one can consider $g(x) = \arctan f(x)$ (so $f = \tan g$ ) and apply 2.2.16.

2.2.28. Let $\mathbf{A}$ be the set constructed in the solution to 2.1.38 and let $f$ be the characteristic function of $\mathbf{A}$ . Then $f$ restricted to $\mathbb{R} \setminus \mathbf{E}$ is given by

$$
f (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x \in \mathbf {A} \backslash \mathbf {E}, \\ 0 & \text {i f} x \in (\mathbb {R} \backslash \mathbf {A}) \backslash \mathbf {E}. \end{array} \right.
$$

It follows from the property of $\mathbf{A}$ that for any open interval $(\alpha, \beta)$ ,

$$
m ((\alpha , \beta) \cap (\mathbf {A} \setminus \mathbf {E})) > 0 \quad \text {a n d} \quad m ((\alpha , \beta) \cap ((\mathbb {R} \setminus \mathbf {A}) \setminus \mathbf {E})) > 0.
$$

So, if $x_0 \in \mathbf{A} \setminus \mathbf{E}$ , then every neighborhood of $x_0$ contains points of $\mathbf{A} \setminus \mathbf{E}$ and points of $(\mathbb{R} \setminus \mathbf{A}) \setminus \mathbf{E}$ . Thus $f$ is not continuous at $x_0$ . The same reasoning can be applied in the case when $x_0 \in (\mathbb{R} \setminus \mathbf{A}) \setminus \mathbf{E}$ .

2.2.29. Set $m_{f}(y) = m(\{x \in [0, a] : f(x) > y\})$ . Then $m_{f}$ is a decreasing function on $\mathbb{R}$ , and $\lim_{y \to \infty} m_{f}(y) = 0$ , $\lim_{y \to -\infty} m_{f}(y) = a$ . Moreover, the function is continuous to the right. Indeed, if $\{y_{n}\}$ is a decreasing sequence convergent to $y$ , then

$$
\begin{array}{l} m _ {f} (y) = m \left(f ^ {- 1} (y, \infty)\right) = m \left(\bigcup_ {n = 1} ^ {\infty} f ^ {- 1} \left(y _ {n}, \infty\right)\right) \\ = \lim  _ {n \rightarrow \infty} m (f ^ {- 1} (y _ {n}, \infty)) = \lim  _ {n \rightarrow \infty} m _ {f} (y _ {n}). \\ \end{array}
$$

In the case when $y \mapsto m_f(y)$ is continuous and strictly decreasing, its inverse is the desired function $g$ , because

$$
\begin{array}{l} m _ {g} (y) = m \left(g ^ {- 1} (y, \infty)\right) = m \left(m _ {f} ((y, \infty))\right) \\ = m ((0, m _ {f} (y))) = m _ {f} (y). \\ \end{array}
$$

If $y_0$ is a point of discontinuity of $m_f$ , then we put $g(x) = y_0$ for $x \in (m(y_0), m_f(y_0^-))$ . If $m_f(y) = x_0$ on some interval, then we put $g(x_0) = \inf \{y : m_f(y) = x_0\}$ . Taking into account the discontinuities and the intervals of constancy of $m_f(y)$ , one can verify that the set $\{x : g(x) > y\}$ is an interval of length $m_f(y)$ . Finally, note that the function $g$ can be defined by $g(x) = \inf \{y : m_f(y) \leq x\}$ .

2.2.30. For $\varepsilon > 0$ we have

$$
\begin{array}{l} \{x \in A: | f (x) - g (x) | > \varepsilon \} \subset \{x \in A: | f (x) - f _ {n} (x) | > \varepsilon / 2 \} \\ \cup \{x \in \mathbf {A}: | f _ {n} (x) - g (x) | > \varepsilon / 2 \}. \\ \end{array}
$$

Hence $m(\{x \in \mathbf{A} : |f(x) - g(x)| > \varepsilon\}) = 0$ . Moreover, since

$$
\{x \in \mathbf {A}: f (x) \neq g (x) \} = \bigcup_ {k = 1} ^ {\infty} \{x \in \mathbf {A}: | f (x) - g (x) | > k / k \},
$$

the claim follows.

2.2.31. Let $\varepsilon > 0$ be arbitrarily chosen. For $n \in \mathbb{N}$ , set

$$
\mathbf {B} _ {n} = \left\{x \in \mathbf {A}: | f _ {n} (x) - f (x) | > \varepsilon \right\} \quad \text {a n d} \quad \mathbf {A} _ {n} = \bigcup_ {k = n} ^ {\infty} \mathbf {B} _ {k}.
$$

Then $\{\mathbf{A}_n\}$ is a decreasing sequence of measurable sets, and, by 2.1.19 and 2.1.21,

$$
\lim  _ {n \rightarrow \infty} m (\mathbf {A} _ {n}) = m \left(\bigcap_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = m (\overline {{\lim }} _ {n \rightarrow \infty} \mathbf {B} _ {n}).
$$

Since $\lim_{n\to \infty}\mathbf{B}_n\subset \{x\in \mathbf{A}:f_n(x)\rightarrow f(x)\}$ and the sequence $\{f_n\}$ converges to $f$ a.e. on $\mathbf{A}$ , we get $m(\lim_{n\to \infty}\mathbf{B}_n) = 0$ , and consequently, $\lim_{n\to \infty}m(\mathbf{B}_n) = 0$ .

2.2.32. Let $\mathbf{A} = [0,\infty)$ and

$$
f _ {n} (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x \in [ n, n + 1 ], \\ 0 & \text {i f} x \in [ 0, \infty) \setminus [ n, n + 1 ]. \end{array} \right.
$$

Then $\{f_n\}$ converges to the zero function on $[0, \infty)$ , but for every $n \in \mathbb{N}$ we have $m(\{x \in [0, \infty) : f_n(x) > 1/2\}) = 1$ .

2.2.33. It is clear that any positive integer $n$ can be uniquely represented as $n = 2^k + r$ , where $k \in \mathbb{N} \cup \{0\}$ and $0 \leq r < 2^k$ . For $n = 2^k + r$ we define

$$
f _ {n} (x) = \left\{ \begin{array}{l l} 1 & \text {i f} x \in \left[ r / 2 ^ {k}, (r + 1) / 2 ^ {k}\right), \\ 0 & \text {o t h e r w i s e .} \end{array} \right.
$$

![](images/f2f0dada1d2dbdb1b9cfe54ef427cfaded9d458867ec2b99ef71e875b92f2370.jpg)

The first eight terms of the sequence are sketched above. The marching sequence $\{f_n\}$ converges in measure to the zero function on $[0,1]$ . On the other hand, it does not converge to zero at any point of $[0,1]$ .

2.2.34. The subsequence $\{f_{2^n}\}$ converges to zero on $(0,1]$ .

2.2.35. Since $\{f_n\}$ converges in measure to $f$ on $\mathbf{A}$ , for any positive integer $k$ there is $n_k$ such that

$$
m \left(\left\{x \in A: \left| f _ {n _ {k}} (x) - f (x) \right| > 1 / k \right\}\right) \leq \frac {1}{2 ^ {k}}.
$$

We can assume that the sequence $\{n_k\}$ is strictly increasing. We put

$$
\mathbf {A} _ {m} = \mathbf {A} \backslash \bigcup_ {k = m} ^ {\infty} \{x \in \mathbf {A}: | f _ {n _ {k}} (x) - f (x) | > 1 / k \}.
$$

Then

$$
m (\mathbf {A} \backslash \mathbf {A} _ {m}) \leq \sum_ {k = m} ^ {\infty} \frac {1}{2 ^ {k}} = \frac {1}{2 ^ {m - 1}}
$$

and, for $x \in \mathbf{A}_m$ ,

$$
\left| f _ {n _ {k}} (x) - f (x) \right| \leq \frac {1}{k} \quad \text {f o r} \quad k \geq m.
$$

Thus $\{f_{n_k}\}$ converges to $f$ on $\bigcup_{m=1}^{\infty} \mathbf{A}_m$ and $m(\mathbf{A} \setminus \bigcup_{m=1}^{\infty} \mathbf{A}_m) = 0$ .

2.2.36. Let $x_0$ be a point of the continuity of $f$ and assume, contrary to our claim, that $f_n(x_0) \nrightarrow f(x_0)$ . Then there are $\varepsilon > 0$ and a subsequence $f_{n_k}$ such that $|f_{n_k}(x_0) - f(x_0)| > \varepsilon$ , or equivalently,

$$
f _ {n _ {k}} \left(x _ {0}\right) - f \left(x _ {0}\right) > \varepsilon \quad \text {o r} \quad f _ {n _ {k}} \left(x _ {0}\right) - f \left(x _ {0}\right) <   - \varepsilon . \tag {1}
$$

Since $f$ is continuous at $x_0$ , there is $\delta > 0$ such that

$$
f (x _ {0}) - \frac {\varepsilon}{2} <   f (x) <   f (x _ {0}) + \frac {\varepsilon}{2}
$$

whenever $|x - x_0| < \delta$ . By the monotonicity of $f_{n_k}$ , $f_{n_k}(x) \geq f_{n_k}(x_0)$ for $x > x_0$ . Consequently, if the first case in (1) holds, then

$$
f _ {n _ {k}} (x) - f (x) > f _ {n _ {k}} \left(x _ {0}\right) - f \left(x _ {0}\right) - \frac {\varepsilon}{2} > \frac {\varepsilon}{2}
$$

for $x \in (x_0, x_0 + \delta)$ . Therefore

$$
m (\{x \in (a, b): | f _ {n _ {k}} (x) - f (x) | > \varepsilon / 2 \}) \geq \delta ,
$$

a contradiction.

2.2.37. It follows from the Lusin theorem (see, e.g., 2.2.27) that for each $n \in \mathbb{N}$ there is a closed set $\mathbf{F}_n \subset \mathbf{A}$ such that $m(\mathbf{A} \setminus \mathbf{F}_n) < 1 / n$ , and $f$ restricted to $\mathbf{F}_n$ is continuous. The sets $\mathbf{H}_n = \bigcup_{i=1}^n \mathbf{F}_i$ are closed, and $f$ restricted to $\mathbf{H}_n$ is continuous. Put $\mathbf{H} = \bigcup_{n=1}^\infty \mathbf{H}_n$ . Then $\mathbf{H}$ is an $\mathcal{F}_{\sigma}$ set and $m(\mathbf{A} \setminus \mathbf{H}) = 0$ . According to Tietze's extension theorem there is a continuous extension $f_n$ of $f_{|\mathbf{H}_n}$ which is defined on $\mathbb{R}$ , and $f_n = f$ on $\mathbf{H}_n$ . It is clear that $f_n$ converges to $f$ on $\mathbf{H}$ .

2.2.38. Let $\mathbf{H}_n$ and $\mathbf{H}$ be the sets defined in the solution to the previous problem, and set

$$
f _ {n} (x) = \left\{ \begin{array}{l l} f (x) & \text {i f} x \in \mathbf {H} _ {n}, \\ 0 & \text {i f} x \in \mathbf {A} \setminus \mathbf {H} _ {n}. \end{array} \right.
$$

We now show that each $f_n$ is in the first Baire class on $\mathbf{A}$ . To this end, put $f_{n,m}(x) = f(x)$ if $x \in \mathbf{H}_n$ and $f_{n,m}(x) = 0$ if $\mathrm{dist}(x,\mathbf{H}_n) \geq 1 / m$ , and using Tietze's extension theorem extend this function continuously onto $\mathbb{R}$ (the extended function is also denoted by $f_{n,m}$ ). Then $f_n(x) = \lim_{m\to \infty}f_{n,m}(x)$ for $x \in \mathbf{A}$ . Now if

$$
g (x) = \lim  _ {n \rightarrow \infty} f _ {n} (x) = \left\{\begin{array}{l l}f (x)&\text {i f} x \in \mathbf {H},\\0&\text {i f} x \in \mathbf {A} \backslash \mathbf {H},\end{array}\right.
$$

then $g$ is in the second Baire class and $f = g$ a.e. on $\mathbf{A}$ .

# 2.3. Lebesgue Integration

2.3.1. Since $m(\mathbb{Q}) = 0$ , we get $\int_{[0,1]} f dm = \int_{[0,1]} x^2 dm = \int_0^1 x^2 dx = 1/3$ . The function is not Riemann integrable on [0,1], because every point in [0,1] is a point of discontinuity of $f$ (compare 2.1.55).

2.3.2. Since $m(\mathbf{C}) = 0$ , we have

$$
\int_ {[ 0, 1 ]} f d m = \int_ {[ 0, 1 ] \backslash \mathbf {C}} f d m = \sum_ {n = 1} ^ {\infty} n 2 ^ {n - 1} \frac {1}{3 ^ {n}} = 3.
$$

2.3.3. It follows from the properties of the Lebesgue integral that

$$
\int_ {[ 0, 1 ]} f d m = \int_ {0} ^ {1 / 2} \sin (\pi x) d x + \int_ {1 / 2} ^ {1} \cos (\pi x) d x = 0.
$$

2.3.4. By the definition of the Lebesgue integral, there is an increasing sequence $\{\varphi_n\}$ of nonnegative simple functions convergent to $|f|$ on $\mathbf{A}$ such that

$$
\int_ {A} | f | d m = \lim  _ {n \rightarrow \infty} \int_ {A} \varphi_ {n} d m.
$$

Hence, given $\varepsilon > 0$ , there is an $n_0$ such that

$$
\int_ {A} (| f | - \varphi_ {n _ {0}}) d m = \int_ {A} | f | d m - \int_ {A} \varphi_ {n _ {0}} d m <   \varepsilon / 2.
$$

Clearly, $|f| - \varphi_{n_0} \geq 0$ and $\varphi_{n_0} \leq M$ with some positive $M$ . Put $\delta = \frac{e}{2M}$ . If $\mathbf{B} \subset \mathbf{A}$ and $m(\mathbf{B}) < \delta$ , then

$$
\begin{array}{l} \int_ {\mathbf {B}} | f | d m = \int_ {\mathbf {B}} (| f | - \varphi_ {n _ {0}}) d m + \int_ {\mathbf {B}} \varphi_ {n _ {0}} d m \\ \leq \int_ {A} (| f | - \varphi_ {n _ {0}}) d m + \int_ {B} M d m <   \frac {\varepsilon}{2} + \frac {\varepsilon}{2 M} M = \varepsilon . \\ \end{array}
$$

2.3.5. We first note that $m(\mathbf{A}_n) \to 0$ as $n \to \infty$ . Indeed, since

$$
n \cdot m (\mathbf {A} _ {n}) \leq \int_ {\mathbf {A} _ {0}} | f | d m \leq \int_ {\mathbf {A}} | f | d m = M <   \infty ,
$$

we get $m(\mathbf{A}_n) \leq M / n$ . It follows from the result in the previous problem that $\lim_{n \to \infty} \int_{\mathbf{A}_n} |f| dm = 0$ . Thus $\lim_{n \to \infty} n \cdot m(\mathbf{A}_n) = 0$ , because $n \cdot m(\mathbf{A}_n) \leq \int_{\mathbf{A}_n} |f| dm$ .

2.3.6. Put $\mathbf{A}_n = \{x\in \mathbf{A}:f(x) > 1 / n\}$ . Then

$$
0 = \int_ {A} f d m \geq \int_ {A _ {\infty}} f d m \geq \int_ {A _ {n}} \frac {1}{n} d m = \frac {1}{n} m (A _ {n}) \geq 0.
$$

Hence $m(\mathbf{A}_n) = 0$ , and consequently, by 2.1.18,

$$
m (\{x \in \mathbf {A}: f (x) \neq 0 \}) = m \left(\bigcup_ {n = 1} ^ {\infty} \mathbf {A} _ {n}\right) = \lim  _ {n \rightarrow \infty} m (\mathbf {A} _ {n}) = 0.
$$

2.3.7. Set $\mathbf{B} = \{x \in \mathbf{A} : f(x) \geq 0\}$ . Then $0 = \int_{\mathbf{B}} f \, dm = \int_{\mathbf{A}} f^{+} \, dm$ . By the result in the previous problem, $f^{+} = 0$ a.e. on $\mathbf{A}$ . Likewise, $f^{-} = 0$ a.e. on $\mathbf{A}$ .

2.3.8. Suppose, for example, that $\int_{\mathbf{A}} f dm \geq 0$ . Then $\int_{\mathbf{A}} |f| dm = \int_{\mathbf{A}} f dm$ . By the result in 2.3.6, $\int_{\mathbf{A}} (|f| - f) dm = 0$ if and only if $|f| - f = 0$ a.e. on $\mathbf{A}$ . In the case when $\int_{\mathbf{A}} f dm \leq 0$ , one can apply the above reasoning to $-f$ .

2.3.9. Suppose that $\lim_{n\to \infty}\int_{\mathbf{A}}f_ndm = 0$ and let $\varepsilon >0$ be given. Set $\mathbf{A}_n = \{x\in \mathbf{A}:f_n(x) > \varepsilon \}$ . Then

$$
m \left(\mathrm {A} _ {n}\right) = \frac {1}{\varepsilon} \int_ {\mathrm {A} _ {n}} \varepsilon d m \leq \frac {1}{\varepsilon} \int_ {\mathrm {A} _ {n}} f _ {n} d m \leq \frac {1}{\varepsilon} \int_ {\mathrm {A}} f _ {n} d m.
$$

Consequently, $\lim_{n\to \infty}m(\mathbf{A}_n) = 0$

The marching sequence $\{f_n\}$ defined in the solution to 2.2.33 satisfies the condition $\lim_{n\to \infty}\int_{[0,1]}f_ndm = 0$ , but it does not converge to zero at any point of [0, 1].

2.3.10. Given $\varepsilon > 0$ , put $\mathbf{A}_n = \{x \in \mathbf{A} : |f_n(x)| > \varepsilon\}$ . Then

$$
\frac {\varepsilon}{1 + \varepsilon} m (\mathbf {A} _ {n}) \leq \int_ {\mathbf {A}} \frac {| f _ {n} |}{1 + | f _ {n} |} d m \leq m (\mathbf {A} _ {n}) + \frac {\varepsilon}{1 + \varepsilon} m (\mathbf {A} \setminus \mathbf {A} _ {n}),
$$

which implies the desired results.

To show that the assumption $m(\mathbf{A}) < \infty$ is essential, consider $f_{n}(x) = 1 / (nx)$ for $x \in (0,\infty)$ . Then $m(\{x > 0 : 1 / (nx) > \varepsilon\}) = 1 / (\varepsilon n)$ , but for every $n \in \mathbb{N}$ ,

$$
\int_ {(0, \infty)} \frac {1}{1 + n x} d m = + \infty .
$$

2.3.11. Assume that a function $f$ is Lebesgue integrable on $\mathbf{A}$ and the series $\sum_{k=0}^{\infty} km(\mathbf{A}_k)$ diverges. Setting

$$
f _ {n} (x) = \left\{ \begin{array}{l l} f (x) & \text {i f} \quad f (x) <   n, \\ n & \text {i f} \quad f (x) \geq n, \end{array} \right.
$$

we get

$$
\int_ {A} f d m \geq \int_ {A} f _ {n} d m \geq \sum_ {k = 0} ^ {n - 1} \int_ {A _ {k}} f d m \geq \sum_ {k = 0} ^ {n - 1} k m (A _ {k}).
$$

Since $\lim_{n\to \infty}\sum_{k = 0}^{n - 1}km(\mathbf{A}_k) = \infty$ , we see that $\int_{\mathbf{A}}fdm = \infty$ , a contradiction. Assume now that the series $\sum_{k = 0}^{\infty}km(\mathbf{A}_k)$ converges. Then also $\sum_{k = 0}^{\infty}(k + 1)m(\mathbf{A}_k)$ converges. Moreover, if we put $g(x) = k + 1$ for

$x \in \mathbf{A}_k$ , then $0 \leq f(x) \leq g(x)$ , $x \in \mathbf{A}$ , and consequently,

$$
\int_ {\mathbf {A}} f d m \leq \int_ {\mathbf {A}} g d m = \sum_ {k = 0} ^ {\infty} (k + 1) m (\mathbf {A} _ {k}) <   \infty .
$$

2.3.12. If $\mathbf{A}_k$ are the sets defined in the previous problem, then the result will be proved if we show that the series $\sum_{k=0}^{\infty} m(\mathbf{B}_k)$ converges if and only if $\sum_{k=0}^{\infty} km(\mathbf{A}_k)$ converges. We have $\mathbf{B}_k = \mathbf{A}_k \cup \mathbf{A}_{k+1} \cup \ldots$ , and since $\mathbf{A}_i \cap \mathbf{A}_j = \emptyset$ for $i \neq j$ , we get $m(\mathbf{B}_k) = m(\mathbf{A}_k) + m(\mathbf{A}_{k+1}) + \ldots$ . We put $b_k = m(\mathbf{B}_k)$ and $a_k = m(\mathbf{A}_k)$ . Then

$$
\sum_ {k = 1} ^ {n} b _ {k} = \sum_ {k = 0} ^ {n} k a _ {k} + \sum_ {k = n + 1} ^ {\infty} n a _ {k}.
$$

If the series $\sum_{k=0}^{\infty} k a_k$ converges, then

$$
\sum_ {k = n + 1} ^ {\infty} n a _ {k} \leq \sum_ {k = n + 1} ^ {\infty} k a _ {k} \underset {n \rightarrow \infty} {\longrightarrow} 0,
$$

and consequently, $\sum_{k=0}^{\infty} b_k < \infty$ . On the other hand, if $\sum_{k=0}^{\infty} b_k < \infty$ , then

$$
\sum_ {k = 0} ^ {n} k a _ {k} = \sum_ {k = 1} ^ {n} b _ {k} - \sum_ {k = n + 1} ^ {\infty} n a _ {k} \leq \sum_ {k = 1} ^ {\infty} b _ {k} <   \infty .
$$

2.3.13. The sets $\mathbf{A}_n$ are measurable and pairwise disjoint, and $\mathbf{A} = \bigcup_{n=0}^{\infty} \mathbf{A}_n \cup \mathbf{B}$ , where $\mathbf{B} = \{x \in \mathbf{A} : f(x) = \infty\}$ is of measure zero. We have

$$
S (\varepsilon) = \sum_ {n = 0} ^ {\infty} n \varepsilon m (A _ {n}) = \sum_ {n = 0} ^ {\infty} \int_ {A _ {n}} n \varepsilon d m \leq \sum_ {n = 0} ^ {\infty} \int_ {A _ {n}} f d m = \int_ {A} f d m,
$$

because the Lebesgue integral is countably additive. Likewise,

$$
S (\varepsilon) + \varepsilon m (A) = \sum_ {n = 0} ^ {\infty} (n + 1) \varepsilon m (A _ {n}) \geq \int_ {A} f d m.
$$

It then follows that

$$
\int_ {A} f d m - \varepsilon m (A) \leq S (\varepsilon) \leq \int_ {A} f d m,
$$

and since $m(\mathbf{A}) < \infty$ , passage to the limit as $\varepsilon \to 0$ gives the desired result.

2.3.14. By Fatou's theorem,

$$
\begin{array}{l} \int_ {A} f d m \leq \lim  _ {n \rightarrow \infty} \int_ {A} f _ {n} d m \leq \overline {{\lim  _ {n \rightarrow \infty}}} \int_ {A} f _ {n} d m \\ \leq \varlimsup_ {n \rightarrow \infty} \left(\int_ {\mathbb {R}} f _ {n} d m - \int_ {\mathbb {R} \backslash A} f _ {n} d m\right) \\ = \lim  _ {n \rightarrow \infty} \int_ {\mathbb {R}} f _ {n} d m - \lim  _ {n \rightarrow \infty} \int_ {\mathbb {R} \backslash A} f _ {n} d m \\ \leq \int_ {\mathbb {R}} f d m - \int_ {\mathbb {R} \backslash \mathbf {A}} f d m = \int_ {\mathbf {A}} f d m. \\ \end{array}
$$

Consequently, $\lim_{n\to \infty}\int_{\mathbf{A}}f_ndm = \int_{\mathbf{A}}fdm.$

2.3.15. Since $\{f_n\}$ is uniformly convergent on $\pmb{\Lambda}$ , there is $n_0$ such that $|f_{n}(x) - f_{n_{0}}(x)|\leq 1$ for $n > n_0$ and $x\in \mathbf{A}$ . Thus $|f_{n}|\leq |f_{n_{0}}| + 1$ , and since $\mathbf{A}$ is of finite measure, $|f_{n_0}| + 1$ is integrable on $\mathbf{A}$ . So it suffices to apply the Lebesgue dominated convergence theorem.

2.3.16. Suppose first that

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} | f _ {n} - f | ^ {p} d m = 0.
$$

Then, by the Minkowski inequality,

$$
\| f _ {n} \| _ {p} \leq \| f _ {n} - f \| _ {p} + \| f \| _ {p} \quad \text {a n d} \quad \| f \| _ {p} \leq \| f _ {n} - f \| _ {p} + \| f _ {n} \| _ {p}.
$$

Hence $\| f_n\| _p - \| f\| _p\leq \| f_n - f\| _p$ , which shows that

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} | f _ {n} | ^ {p} d m = \int_ {\mathbf {A}} | f | ^ {p} d m.
$$

To prove the reverse implication, assume first that $\mathbf{A}$ has finite measure. It follows from the absolute continuity of the Lebesgue integral (see, e.g., 2.3.4) that, given $\varepsilon > 0$ , there is $\delta > 0$ such that $\int_{\mathbf{B}} |f|^p dm < \varepsilon$ if $m(\mathbf{B}) < \delta$ . By Egorov's theorem there is $\mathbf{C} \subset \mathbf{A}$ such that $m(\mathbf{C}) < \delta$ and $f_n \Rightarrow f$ . It follows from 2.3.14 that

A\C

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {C}} | f _ {n} | ^ {p} d m = \int_ {\mathbf {C}} | f | ^ {p} d m.
$$

Hence for sufficiently large $n$ ,

$$
\begin{array}{l} \int_ {\mathbf {A}} | f _ {n} - f | ^ {p} d m = \int_ {\mathbf {A} \backslash \mathbf {C}} | f _ {n} - f | ^ {p} d m + \int_ {\mathbf {C}} | f _ {n} - f | ^ {p} d m \\ \leq \int_ {\mathbf {A} \backslash \mathbf {C}} | f _ {n} - f | ^ {p} d m + 2 ^ {p} \left(\int_ {\mathbf {C}} | f | ^ {p} d m + \int_ {\mathbf {C}} | f _ {n} | ^ {p} d m\right) \\ \leq \int_ {\mathbf {A} \backslash \mathbf {C}} | f _ {n} - f | ^ {p} d m + 2 ^ {p + 1} \int_ {\mathbf {C}} | f | ^ {p} d m + \varepsilon \\ \leq \int_ {\mathbf {A} \backslash \mathbf {C}} | f _ {n} - f | ^ {p} d m + (2 ^ {p + 1} + 1) \varepsilon . \\ \end{array}
$$

Now it suffices to apply the result in 2.3.15.

If $m(\mathbf{A}) = \infty$ , then, given $\varepsilon > 0$ , we find a subset $\mathbf{B}$ of $\mathbf{A}$ of finite measure and such that

$$
\int_ {\mathbf {A}} | f | ^ {p} d m <   \int_ {\mathbf {B}} | f | ^ {p} d m + \varepsilon .
$$

Indeed, taking

$$
g _ {n} (x) = \left\{ \begin{array}{l l} | f (x) | ^ {p} & \text {i f} x \in \mathbf {A} \cap [ - n, n ], \\ 0 & \text {i f} x \in \mathbf {A} \setminus [ - n, n ], \end{array} \right.
$$

we get, by the Lebesgue monotone convergence theorem,

$$
\lim  _ {n \rightarrow \infty} \int_ {\mathbf {A}} g _ {n} d m = \lim  _ {n \rightarrow \infty} \int_ {\mathbf {A} \cap [ - n, n ]} | f | ^ {p} d m = \int_ {\mathbf {A}} | f | ^ {p} d m.
$$

So it is enough to set $\mathbf{B} = \mathbf{A}\cap [-n_0,n_0]$ with sufficiently large $n_0$ . Consequently, for $n$ large enough,

$$
\begin{array}{l} \int_ {\mathbf {A}} | f _ {n} - f | ^ {p} d m = \int_ {\mathbf {B}} | f _ {n} - f | ^ {p} d m + \int_ {\mathbf {A} \backslash \mathbf {B}} | f _ {n} - f | ^ {p} d m \\ \leq \int_ {\mathbf {B}} | f _ {n} - f | ^ {p} d m + 2 ^ {p + 1} \int_ {\mathbf {A} \backslash \mathbf {B}} | f | ^ {p} d m + \varepsilon \\ <   \int_ {\mathbf {B}} | f _ {n} - f | ^ {p} d m + (2 ^ {p + 1} + 1) \varepsilon <   (2 ^ {p + 1} + 2) \varepsilon , \\ \end{array}
$$

where the last inequality follows from the first part of the proof.

2.3.17. We have $g - f_n \geq 0$ and $g + f_n \geq 0$ . By the Fatou theorem,

$$
\int_ {\mathbf {A}} \underline {{\lim }} (f _ {n} + g) d m \leq \underline {{\lim }} _ {n \rightarrow \infty} \int_ {\mathbf {A}} (f _ {n} + g) d m
$$

and

$$
\int_ {A} \underline {{\lim }} _ {n \rightarrow \infty} (g - f _ {n}) d m \leq \underline {{\lim }} _ {n \rightarrow \infty} \int_ {A} (g - f _ {n}) d m.
$$

Consequently, using the properties of the limit inferior and superior (see, e.g., I, 2.4.19 and I, 2.4.21), we get

$$
\int_ {A} \lim  _ {n \rightarrow \infty} f _ {n} d m + \int_ {A} g d m \leq \lim  _ {n \rightarrow \infty} \int_ {A} f _ {n} d m + \int_ {A} g d m
$$

and

$$
\int_ {A} g d m - \int_ {A} \varlimsup_ {n \rightarrow \infty} f _ {n} d m <   \int_ {A} g d m - \varliminf_ {n \rightarrow \infty} \int_ {A} f _ {n} d m.
$$

Since $g$ is integrable, the result follows.

2.3.18. We have $\sum_{n=1}^{\infty} f_n(x) = 1$ and $\int_{(0,1)} \sum_{n=1}^{\infty} f_n dm = 1$ . On the other hand, $\int_{(0,1)} f_n dm = 0$ , $n = 1, 2, \ldots$ . Moreover, since

$$
\int_ {(0, 1)} | f _ {n} | d m = \int_ {0} ^ {\frac {n}{n + 1}} f _ {n} (x) d x + \int_ {\frac {n}{n + 1}} ^ {1} - f _ {n} (x) d x = \frac {2 :}{(1 + \frac {1}{n}) ^ {n}} \frac {1}{n + 1},
$$

we see that $\sum_{n=1}^{\infty} \int_{(0,1)} |f_n| dm = \infty$ .

2.3.19. It follows from the Lebesgue monotone convergence theorem that

$$
\sum_ {n = 1} ^ {\infty} \int_ {\mathbf {A}} | f _ {n} | d m = \int_ {\mathbf {A}} \sum_ {n = 1} ^ {\infty} | f _ {n} | d m <   \infty ,
$$

which implies that the series $\sum_{n=1}^{\infty} |f_n|$ converges a.e. This in turn implies the a.e. convergence of $\sum_{n=1}^{\infty} f_n$ . Now it is enough to apply the Lebesgue dominated convergence theorem.

2.3.20. Let $\varepsilon > 0$ be arbitrarily chosen. By the equi-integrability of $f_{n}$ , there is $\delta > 0$ such that $\int_{\mathbf{B}} |f_{n}| dm < \varepsilon / 2, n = 1, 2, \ldots$ , whenever $m(\mathbf{B}) < \delta$ . Observe also that if $m(\mathbf{B}) < \delta$ , then, by the Fatou theorem,

$$
\int_ {B} | f | d m \leq \lim  _ {n \rightarrow \infty} \int_ {B} | f _ {n} | d m \leq \varepsilon / 2,
$$

where $f(x) = \lim_{n\to \infty}f_n(x)$ . It follows from the Egorov theorem that there is $\mathbf{C}\subset \mathbf{A}$ such that $m(\mathbf{C}) < \delta$ and $f_{n}\Rightarrow f$ . Thus

$$
\begin{array}{l} \int_ {A} | f _ {n} - f | d m = \int_ {A \backslash C} | f _ {n} - f | d m + \int_ {C} | f _ {n} - f | d m \\ \leq \int_ {A \backslash C} | f _ {n} - f | d m + \int_ {C} | f _ {n} | d m + \int_ {C} | f | d m \\ \leq \int_ {\mathbf {A} \backslash \mathbf {C}} | f _ {n} - f | d m + \varepsilon . \\ \end{array}
$$

Now it suffices to apply the result in 2.3.15.

2.3.21. Suppose, contrary to our claim, that the sequence $\{a_n\}$ , where $a_n = \int_{\mathbf{A}} f_n dm$ , does not converge to $a = \int_{\mathbf{A}} f dm$ . Then there is a subsequence $\{a_{m_n}\}$ convergent to $b \neq a$ . On the other hand, by the Riesz theorem (see, e.g., 2.2.35), there is a subsequence $\{f_{m_{k_n}}\}$ converging to $f$ a.e. on $\mathbf{A}$ . Thus by Lebesgue's dominated convergence theorem $a_{m_{k_n}} \to a$ as $n \to \infty$ , a contradiction.

2.3.22. The proof is like that of the previous problem.

2.3.23. We first note that by 2.2.16 the functions $g(f_n)$ and $g(f)$ are measurable on $\mathbf{A}$ . Clearly, $g$ is uniformly continuous on $[-C, C]$ and consequently, given $\varepsilon > 0$ , there is $\delta > 0$ such that

$$
\left| g \left(f _ {n} (x)\right) - g (f (x)) \right| <   \varepsilon
$$

for all $x \in \mathbf{A}$ and $n \in \mathbb{N}$ for which $|f_n(x) - f(x)| < \delta$ . It then follows that

$$
\{x \in A: | g (f _ {n} (x)) - g (f (x)) | \geq \varepsilon \} \subset \{x \in A: | f _ {n} (x) - f (x) | \geq \delta \},
$$

which shows that $g(f_n) \to g(f)$ in measure. Moreover, since $m(A) < \infty$ and $|y(f_n(x))| \leq M$ , where $M = \max \{|y(x)| : x \in [-C, C]\}$ , the result in 2.3.21 can be applied.

2.3.24. Reasoning similar to that used in the solution of the previous problem can be applied.

2.3.25. (i) We know that there are nondecreasing sequences of nonnegative simple functions $\{\varphi_{1,n}\}$ and $\{\varphi_{2,n}\}$ defined on $[a,b]$ such that $\varphi_{1,n} \to f^{+}$ and $\varphi_{2,n} \to f^{-}$ . Setting $\varphi_{n} = \varphi_{1,n} - \varphi_{2,n}$ , we see

that $\{\varphi_n\}$ is a sequence of simple functions converging to $f$ such that $|\varphi_n| \leq |f|$ . Since $|\varphi_n - f|^p \to 0$ and $|\varphi_n - f|^p \leq 2^{p+1} |f|^p$ , the Lebesgue dominated convergence theorem implies that

$$
\lim  _ {n \rightarrow \infty} \int_ {[ a, b ]} | \varphi_ {n} - f | ^ {p} d m = 0.
$$

(ii) In view of (i) it is enough to show that if $\chi_{\mathbf{A}}$ is the characteristic function of a measurable set $\mathbf{A} \subset [a, b]$ , then, given $\delta > 0$ , there is a step function $\psi$ such that $\int_{[a, b]} |\chi_{\mathbf{A}} - \psi|^p dm < \delta$ . By 2.1.12 there is an open set $\mathbf{G}$ such that $\mathbf{A} \subset \mathbf{G}$ and $m(\mathbf{G} \setminus \mathbf{A}) < \delta$ . On the other hand, $\mathbf{G}$ is a union of countably many disjoint open intervals $(a_i, b_i)$ . Thus we have

$$
m (\mathbf {G}) = \sum_ {i = 1} ^ {\infty} (b _ {i} - a _ {i}) <   m (\mathbf {A}) + \delta .
$$

Let $\psi$ be the characteristic function of $[a, b] \cap \bigcup_{i=1}^{N}(a_i, b_i)$ , where $N$ is sufficiently large. If $h$ is the characteristic function of $[a, b] \cap \bigcup_{i=1}^{\infty}(a_i, b_i)$ , then by the Minkowski inequality

$$
\begin{array}{l} \| \chi_ {A} - \psi \| _ {p} \leq \| \chi_ {A} - h \| _ {p} + \| h - \psi \| _ {p} \\ \left. \leq \left(m \left(\bigcup_ {i = 1} ^ {\infty} \left(a _ {i}, b _ {i}\right) \backslash A\right)\right) ^ {1 / p} + \left(m \left(\bigcup_ {i = N + 1} ^ {\infty} \left(a _ {i}, b _ {i}\right)\right)\right) ^ {1 / p} \right. \\ <   \delta^ {1 / p} + \delta^ {1 / p} = 2 \delta^ {1 / p}. \\ \end{array}
$$

Since $\delta > 0$ can be chosen arbitrarily small, the proof is complete.

2.3.26. It follows from 2.1.38 that there exists a measurable subset $\mathbf{A}$ of $[a, b]$ such that for any interval $(\alpha, \beta) \subset [a, b]$ ,

$$
m (\mathbf {A} \cap (\alpha , \beta)) > 0 \quad \text {a n d} \quad m (([ a, b ] \backslash \mathbf {A}) \cap (\alpha , \beta)) > 0.
$$

We will show that $f = \chi_{\mathbf{A}}$ has the desired property. Indeed, if $\psi$ is a step function that is equal to $c$ on $(\alpha, \beta) \subset [a, b]$ , then

$$
\| \chi_ {A} - \psi \| _ {\infty} \geq \max  \{| c |, | 1 - c | \} \geq \frac {1}{2}.
$$

It is worth noting here that this example shows that the result in 2.3.25 (ii) is false when $p = \infty$ .

2.3.27. In view of the result in 2.3.25, given $\varepsilon > 0$ , there is a step function $\psi$ such that $\|f - \psi\|_p < \varepsilon/2$ . So, it is enough to show that there is a continuous function $g$ such that $\|\psi - g\|_p < \varepsilon/2$ . Put $M = \sup \{|\psi(x)| : x \in [a,b]\}$ and construct a piecewise linear function $g$ on $[a,b]$ such that $m(\{x \in [a,b] : \psi(x) \neq g(x)\}) < \left(\frac{\varepsilon}{4M}\right)^p$ and $|g(x)| \leq M$ . Then

$$
\begin{array}{l} \| \psi - g \| _ {p} = \left(\int_ {[ a, b ]} | \psi - g | ^ {p} d m\right) ^ {1 / p} \\ \leq ((2 M) ^ {p} m (\{x \in [ a, b ]: \psi (x) \neq g (x) \})) ^ {1 / p} <   \frac {\varepsilon}{2}. \\ \end{array}
$$

2.3.28. For $a < c < b$ , let $\mathbf{A} = [a, c]$ and $f = \chi_{\mathbf{A}}$ . If $g$ is a continuous function on $[a, b]$ , then $\lim_{x \to c^-} g(x) = \lim_{x \to c^+} g(x) = g(c)$ . Consequently,

$$
\| f - g \| _ {\infty} \geq \max  \left\{\left| g (c) \right|, \left| g (c) - 1 \right| \right\} \geq \frac {1}{2}.
$$

2.3.29. We first note that by 2.2.16 the functions $g(f_n)$ , $g(f)$ and $g(G)$ are measurable on $\mathbf{A}$ . As in the solution to 2.3.23, one can show that $g(f_n) \to g(f)$ in measure on $[a,b]$ . Now we show that $g(G)$ is integrable on $[a,b]$ . By 2.3.27, given $\varepsilon > 0$ , there is a continuous function $h$ such that $\int_{[a,b]} |G - h| dm < \varepsilon$ . Thus

$$
\begin{array}{l} \int_ {[ a, b ]} | g (G) | d m \leq \int_ {[ a, b ]} | g (G) - g (h) | d m + \int_ {[ a, b ]} | g (h) | d m \\ \leq L \varepsilon + \int_ {[ a, b ]} | g (h) | d m, \\ \end{array}
$$

where $L$ is the Lipschitz constant of $g$ . Since $g(h)$ is continuous, $g(G)$ is integrable on $[a,b]$ . So, the result follows from 2.3.21.

2.3.30. We first find a closed interval $[a, b]$ and a bounded measurable function $h$ on $\mathbf{A}$ that vanishes outside $[a, b]$ and

$$
\int_ {A} | f - h | ^ {p} d m <   \varepsilon / 3. \tag {1}
$$

To this end, consider the sequence of functions given by

$$
f _ {n} (x) = \left\{ \begin{array}{l l} f (x) & \text {i f} x \in [ - n, n ] \cap \mathbf {A} \quad \text {a n d} \quad | f (x) | \leq n, \\ n & \text {i f} x \in [ - n, n ] \cap \mathbf {A} \quad \text {a n d} \quad f (x) > n, \\ - n & \text {i f} x \in [ - n, n ] \cap \mathbf {A} \quad \text {a n d} \quad f (x) <   - n, \\ 0 & \text {i f} x \notin [ - n, n ]. \end{array} \right.
$$

Then $f_n \to f$ a.e. on $\mathbf{A}$ and $|f_n|^p \leq |f|^p$ . By the Lebesgue dominated convergence theorem, $\lim_{n \to \infty} \int_{\mathbf{A}} |f_n|^p dm = \int_{\mathbf{A}} |f|^p dm$ . Using the result in 2.3.16, we see that $\lim_{n \to \infty} \int_{\mathbf{A}} |f_n - f|^p dm = 0$ . So we can pick a sufficiently large $N$ and put $h = f_N$ and $[a, b] = [-N, N]$ . This proves the claim stated at the beginning. By the Lusin theorem, there is a closed set $\mathbf{F} \subset \mathbf{A} \cap [-N, N]$ such that $h$ is continuous on $\mathbf{F}$ and $m(\mathbf{A} \cap [-N, N] \setminus \mathbf{F}) < \frac{\varepsilon}{3(2N)^p}$ . Next, by the Tietze extension theorem, there is a continuous function $g$ such that $|g| \leq N$ and $g = h$ on $\mathbf{F} \cup (-\infty, -N - \varepsilon / (6N^p)) \cup [N + \varepsilon / (6N^p), \infty)$ . Then

$$
\begin{array}{l} \int_ {\mathbf {A}} | h - g | ^ {p} d m \leq \int_ {\mathbf {A} \cap [ - N, N ] \backslash \mathbf {F}} | h - g | ^ {p} d m + \int_ {[ - N - \frac {\epsilon}{6 N ^ {p}}, - N ]} | h - g | ^ {p} d m \\ + \int_ {[ N, N + \frac {\epsilon}{6 N ^ {p}} ]} | h - g | ^ {p} d m \\ \leq \frac {\varepsilon}{3 (2 N) ^ {p}} (2 N) ^ {p} + 2 \frac {\varepsilon}{6 N ^ {p}} N ^ {p} = \frac {2 \varepsilon}{3}. \\ \end{array}
$$

Combined with (1), this shows that the function $g$ resolves our problem.

2.3.31. Observe that by Fatou's theorem,

$$
\int_ {[ a, b ]} | f | ^ {p} d m \leq \lim  _ {n \rightarrow \infty} \int_ {[ a, b ]} | f _ {n} | ^ {p} d m \leq C ^ {p}.
$$

So $|f|^p$ is integrable on $[a, b]$ . We now show that the $f_n$ are equi-integrable on $[a, b]$ . Indeed, given $\varepsilon > 0$ , there is $\delta = \frac{\varepsilon^q}{C^q}$ such that if $m(\mathbf{B}) < \delta$ , then, by Hölder's inequality,

$$
\int_ {\mathbf {B}} | f _ {n} | d m \leq \| f _ {n} \| _ {p} (m (\mathbf {B})) ^ {\frac {1}{q}} \leq C \delta^ {\frac {1}{q}} = \varepsilon .
$$

Hence, by 2.3.20,

$$
\lim  _ {n \rightarrow \infty} \int_ {[ a, b ]} f _ {n} d m = \int_ {[ a, b ]} f d m.
$$

It is also easy to show that this equality holds when $[a, b]$ is replaced by any subinterval $[a_i, b_i]$ of $[a, b]$ . Therefore if $S$ is a step function on $[a, b]$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {[ a, b ]} f _ {n} S d m = \int_ {[ a, b ]} f S d m.
$$

It follows from the equi-integrability of $|f_n|^p$ that

$$
\lim  _ {n \rightarrow \infty} \int_ {[ a, b ]} | f _ {n} | ^ {p} d m = \int_ {[ a, b ]} | f | ^ {p} d m.
$$

So, by 2.3.16, $\| f_n - f\| _p\to 0$ . If $g\in L^{q}[a,b]$ , then by the Hölder inequality,

$$
\int_ {[ a, b ]} | f _ {n} g - f g | d m \leq \| f _ {n} - f \| _ {p} \| g \| _ {q},
$$

and the result follows.

2.3.32. We first note that since $|g_n| \leq C$ , we get $|g_n f|^p \leq C^p |f|^p$ and Lebesgue's dominated convergence theorem can be applied to obtain $\int_{[a, b]} |g_n f|^p dm \to \int_{[a, b]} |gf|^p$ . So, by the result in 2.3.16, the sequence $\{g_n f\}$ converges to $gf$ in norm in $L^p [a, b]$ . Moreover,

$$
\begin{array}{l} \int_ {[ a, b ]} \left| f _ {n} g _ {n} - f g \right| ^ {p} d m \\ \leq 2 ^ {p} \left(\int_ {[ a, b ]} | g _ {n} | ^ {p} | f _ {n} - f | ^ {p} d m + \int_ {[ a, b ]} | f g _ {n} - f g | ^ {p} d m\right) \\ \leq 2 ^ {p} \left(C ^ {p} \| f _ {n} - f \| _ {p} ^ {p} + \| f g _ {n} - f g \| _ {p} ^ {p}\right), \\ \end{array}
$$

and the desired result follows.

2.3.33. The reader is referred to the remark at the beginning of this section for the definition of $\| f\|_{\infty}$ . If $\| f\|_{\infty} = 0$ , the result is obvious. Suppose that $\| f\|_{\infty} > 0$ . Since $|f(x)| \leq \| f\|_{\infty}$ a.e., we see that

$$
\varlimsup_ {p \rightarrow \infty} \left(\int_ {[ a, b ]} | f | ^ {p} d m\right) ^ {1 / p} \leq \lim  _ {p \rightarrow \infty} (b - a) ^ {1 / p} \| f \| _ {\infty} = \| f \| _ {\infty}.
$$

On the other hand, given $0 < \varepsilon < \| f\|_{\infty}$ , we have

$$
m (\{x: | f (x) | > \| f \| _ {\infty} - \varepsilon \}) = \delta > 0,
$$

and, consequently,

$$
\int_ {[ a, b ]} | f | ^ {p} d m \geq (\| f \| _ {\infty} - \varepsilon) ^ {p} \delta ,
$$

which implies

$$
\varlimsup_ {p \rightarrow \infty} \left(\int_ {[ a, b ]} | f | ^ {p} d m\right) ^ {1 / p} \geq \| f \| _ {\infty} - \varepsilon .
$$

Letting $\varepsilon \to 0$ gives the desired equality.

2.3.34. We first prove that if $\varphi$ is convex on $\mathbb{R}$ , then the graph of $\varphi$ has at least one supporting line at each $x_0 \in \mathbb{R}$ , that is, a line through $(x_0, \varphi(x_0))$ that is always below the graph of $\varphi$ . To this end, we note that if $\varphi$ is convex, then one-sided derivatives $\varphi_{+}', \varphi_{-}'$ exist and, for $x < x_0 < x_1$ ,

$$
\frac {\varphi (x) - \varphi (x _ {0})}{x - x _ {0}} \leq \varphi_ {-} ^ {\prime} (x _ {0}) \leq \varphi_ {+} ^ {\prime} (x _ {0}) \leq \frac {\varphi (x _ {1}) - \varphi (x _ {0})}{x _ {1} - x _ {0}}
$$

(see, e.g., II, 2.4.19). It then follows that $y = A(x - x_0) + \varphi(x_0)$ is a supporting line at $x_0$ if and only if $\varphi_{-}^{\prime}(x_0) \leq A \leq \varphi_{+}^{\prime}(x_0)$ . So our claim is proved. Now take

$$
x _ {0} = \frac {1}{b - a} \int_ {[ a, b ]} f d m
$$

and let $y = A(x - x_0) + \varphi (x_0)$ be a supporting line at $x_0$ . Then

$$
\varphi (f (x)) \geq A (f (x) - x _ {0}) + \varphi (x _ {0}).
$$

Integrating both sides of this inequality with respect to $x$ gives the desired result.

2.3.35. Let $p = p_2 / p_1$ and $1 / p + 1 / p' = 1$ . Then by the Hölder inequality,

$$
\begin{array}{l} \int_ {A} | f | ^ {p _ {1}} d m \leq \left(\int_ {A} | f | ^ {p p _ {1}} d m\right) ^ {1 / p} \left(\int_ {A} 1 ^ {p ^ {\prime}} d m\right) ^ {1 / p ^ {\prime}} \\ = \left(\int_ {A} | f | ^ {p _ {2}} d m\right) ^ {1 / p} (m (A)) ^ {1 / p ^ {\prime}} <   \infty . \\ \end{array}
$$

2.3.36. Let $r = \alpha p_1 + (1 - \alpha)p_2$ , $0 < \alpha < 1$ . If $p = 1 / \alpha$ and $1 / p + 1 / p' = 1$ , then $p' = 1 / (1 - \alpha)$ , and by the Hölder inequality,

$$
\begin{array}{l} \int_ {A} | f | ^ {r} d m = \int_ {A} | f | ^ {\alpha p _ {1}} | f | ^ {(1 - \alpha) p _ {2}} d m \\ \leq \left(\int_ {A} | f | ^ {p _ {1}} d m\right) ^ {\alpha} \left(\int_ {A} | f | ^ {p _ {2}} d m\right) ^ {1 - \alpha} <   \infty . \\ \end{array}
$$

Hence

$$
\| f \| _ {r} ^ {r} \leq \left(\| f \| _ {p _ {1}} ^ {p _ {1}}\right) ^ {\alpha} \left(\| f \| _ {p _ {2}} ^ {p _ {2}}\right) ^ {1 - \alpha}.
$$

Taking the logarithm of both sides of this inequality, we get

$$
\varphi (r) \leq \alpha \varphi (p _ {1}) + (1 - \alpha) \varphi (p _ {2}).
$$

2.3.37. It follows from 2.3.35 that if $f \in L^{1}[a, b]$ , then $f \in L^{p}[a, b]$ with $0 < p \leq 1$ . Using the inequality $\ln t < t - 1$ , $t > 0$ , and the Jensen inequality with $\varphi(x) = -\ln x$ , we obtain

$$
\begin{array}{l} \frac {1}{p} \cdot \frac {1}{b - a} \int_ {[ a, b ]} (| f | ^ {p} - 1) d m \geq \frac {1}{p} \ln \left(\frac {1}{b - a} \int_ {[ a, b ]} | f | ^ {p} d m\right) \\ \geq \frac {1}{b - a} \int_ {[ a, b ]} \ln | f | d m. \\ \end{array}
$$

Since $\frac{|f(x)|^p - 1}{p}$ decreases to $\ln |f(x)|$ as $p$ decreases to zero, by the Lebesgue monotone convergence theorem,

$$
\lim  _ {p \rightarrow 0 ^ {+}} \frac {1}{p} \cdot \frac {1}{b - a} \int_ {[ a, b ]} (| f | ^ {p} - 1) d m = \frac {1}{b - a} \int_ {[ a, b ]} \ln | f | d m.
$$

It then follows that

$$
\lim  _ {p \rightarrow 0 ^ {+}} \frac {1}{p} \ln \left(\frac {1}{b - a} \int_ {[ a, b ]} | f | ^ {p} d m\right) = \frac {1}{b - a} \int_ {[ a, b ]} \ln | f | d m.
$$

2.3.38. (a) If $f$ is the characteristic function of a measurable set $A$ , then the equality to be proved follows from the translation invariance of the Lebesgue measure. Therefore the equality holds also for simple functions. If $f$ is nonnegative, then there is an increasing sequence $\{f_n\}$ of simple functions converging to $f$ . Consequently, by what we have proved and by the Lebesgue monotone convergence theorem,

$$
\int_ {\mathbb {R}} f d m = \lim  _ {n \rightarrow \infty} \int_ {\mathbb {R}} f _ {n} d m = \lim  _ {n \rightarrow \infty} \int_ {\mathbb {R}} (f _ {n}) _ {t} d m = \int_ {\mathbb {R}} f _ {t} d m.
$$

Finally, the result follows from the fact that

$$
\int_ {\mathbb {R}} f d m = \int_ {\mathbb {R}} f ^ {+} d m - \int_ {\mathbb {R}} f ^ {-} d m.
$$

(b) By 2.3.30, given $\varepsilon > 0$ , there is a continuous function $\varphi$ vanishing outside a finite interval, say $[a, b]$ , such that $\int_{\mathbb{R}} |f - \varphi| dm < \varepsilon$ . If $|g(x)| \leq M$ , then using (a) we get

$$
\begin{array}{l} \int_ {\mathbb {R}} | g (f - f _ {t}) | d m \leq \int_ {\mathbb {R}} | g (f - \varphi) | d m + \int_ {\mathbb {R}} | g (f _ {t} - \varphi_ {t}) | d m \\ + \int_ {R} | g (\varphi - \varphi_ {t}) | d m \\ \leq M \varepsilon + \int_ {\mathbb {R}} | g (f _ {t} - \varphi_ {t}) | d m + M \int_ {\mathbb {R}} | \varphi - \varphi_ {t} | d m \\ = M \varepsilon + \int_ {\mathbb {R}} | g _ {- t} (f - \varphi) | d m + M \int_ {\mathbb {R}} | \varphi - \varphi_ {t} | d m \\ \leq 2 M \varepsilon + M \int_ {\mathbb {R}} | \varphi - \varphi_ {i} | d m. \\ \end{array}
$$

Since $\varphi$ is continuous and vanishes outside $[a, b]$ , it is uniformly continuous. Thus there is $0 < \delta < 1$ such that $|\varphi(x) - \varphi_t(x)| < \varepsilon$ if $|t| < \delta$ . It then follows that, given $\varepsilon > 0$ , there is $0 < \delta < 1$ such that if $|t| < \delta$ , then

$$
\int_ {\mathbb {R}} | g (f - f _ {t}) | d m \leq 2 M \varepsilon + M \varepsilon (b - a + 1).
$$

2.3.39. By 2.3.30, given $\varepsilon > 0$ , there is a continuous function $g$ vanishing outside a finite interval, say $[a, b]$ , such that $\|f - g\|_p < \varepsilon$ . Since $g$ is uniformly continuous, there is $0 < \delta < 1$ such that $|g(x) - g_t(x)| < \varepsilon$ if $|t| < \delta$ . Consequently, using 2.3.38(a) we see that, given $\varepsilon > 0$ , there is $0 < \delta < 1$ such that if $|t| < \delta$ , then

$$
\begin{array}{l} \| f - f _ {t} \| _ {p} \leq \| f - g \| _ {p} + \| g - g _ {t} \| _ {p} + \| g _ {t} - f _ {t} \| _ {p} \\ <   \varepsilon + \varepsilon (b - a + 1) ^ {1 / p} + \varepsilon . \\ \end{array}
$$

2.3.40. By assumption, $f$ is integrable on $\mathbf{A}$ and

$$
\int_ {A \backslash A _ {6}} f d m \leq \delta \alpha m (A).
$$

Hence $\int_{\mathbf{A}_{\delta}} f dm \geq (1 - \delta) \alpha m(\mathbf{A})$ . On the other hand, by the Schwarz inequality,

$$
\int_ {\mathbf {A} _ {\delta}} f d m \leq \left(\int_ {\mathbf {A} _ {\delta}} f ^ {2} d m\right) ^ {1 / 2} (m (\mathbf {A} _ {\delta})) ^ {1 / 2} \leq (\beta m (\mathbf {A})) ^ {1 / 2} (m (\mathbf {A} _ {\delta})) ^ {1 / 2}.
$$

It then follows that

$$
(1 - \delta) \alpha m (\mathbf {A}) \leq (\beta m (\mathbf {A})) ^ {1 / 2} (m (\mathbf {A} _ {\delta})) ^ {1 / 2},
$$

which implies the desired inequality.

# 2.4. Absolute Continuity, Differentiation and Integration

2.4.1. Since $f$ is absolutely continuous on $[a, b]$ , there is $\delta > 0$ such that

$$
\sum_ {k = 1} ^ {n} | f (x _ {k}) - f (x _ {k} ^ {\prime}) | <   1
$$

for every finite collection $\{(x_k, x_k')\}$ of pairwise disjoint open intervals of $[a, b]$ with

$$
\sum_ {k = 1} ^ {n} \left(x _ {k} ^ {\prime} - x _ {k}\right) <   \delta .
$$

Let $a = c_0 < c_1 < \dots < c_m = b$ be a partition of mesh less than $\delta$ . Then the total variation $V(f; c_{k-1}, c_k)$ of $f$ on every $[c_{k-1}, c_k]$ is less than 1. Consequently, $V(f; a, b) < m$ .

2.4.2. In view of the previous problem it is enough to consider the function defined in 1.2.5 with $\alpha = \beta = 1$ .

2.4.3. If $\alpha >\beta >0$ , then

$$
f (x) = \int_ {0} ^ {x} \left(\alpha t ^ {\alpha - 1} \sin \frac {1}{t ^ {\beta}} - \beta t ^ {\alpha - \beta - 1} \cos \frac {1}{t ^ {\beta}}\right) d t,
$$

and the integrand is integrable on $[0,1]$ . By Theorem 2, $f$ is absolutely continuous. If $0 < \alpha \leq \beta$ , then reasoning similar to that used in 1.2.5 shows that $f$ is not of bounded variation, and, by 2.4.1, is not absolutely continuous.

2.4.4. Observe that the function

$$
f ^ {*} (x) = \left\{ \begin{array}{l l} x ^ {2} \sin (1 / x) & \text {i f} \quad x \in (0, 1 ], \\ 0 & \text {i f} \quad x = 0, \end{array} \right.
$$

has bounded derivative on $[0,1]$ . So $f^*$ satisfies the Lipschitz condition and therefore is absolutely continuous. Hence $f = |f^*|$ is also absolutely continuous on $[0,1]$ . Moreover, since $g(x) = \sqrt{x} = \frac{1}{2} \int_{0}^{x} \frac{dt}{\sqrt{t}}$ and $t \mapsto \frac{1}{\sqrt{t}}$ is integrable on $[0,1]$ (we can extend this function by assigning any value at 0), by Theorem 2, $g$ is absolutely continuous. By 2.4.3, the function

$$
h (x) = \left\{ \begin{array}{l l} x \sin \frac {1}{\sqrt {x}} & \text {i f} \quad x \in (0, 1 ], \\ 0 & \text {i f} \quad x = 0 \end{array} \right.
$$

is absolutely continuous on $[0,1]$ , and therefore so is $f(g(x)) = |h(x)|$ . On the other hand, $x \mapsto g(f(x))$ as a function of unbounded variation is not absolutely continuous.

2.4.5. Given $\varepsilon > 0$ , there is $\delta > 0$ such that

$$
\sum_ {k = 1} ^ {n} | f (x _ {k}) - f \left(x _ {k} ^ {\prime}\right) | <   \varepsilon
$$

for every finite collection $\{(x_k, x_k')\}$ of pairwise disjoint open intervals of $[a, b]$ with

$$
\sum_ {k = 1} ^ {n} \left(x _ {k} ^ {\prime} - x _ {k}\right) <   \delta .
$$

Suppose, for example, that $g$ is monotonically increasing. Since it is absolutely continuous, there is $\delta_1 > 0$ such that $\sum_{k=1}^{m} (t_k' - t_k) < \delta_1$ implies $\sum_{k=1}^{m} (g(t_k') - g(t_k)) < \delta$ . It then follows that

$$
\sum_ {k = 1} ^ {m} | f (g (t _ {k})) - f (g (t _ {k} ^ {\prime})) | <   \varepsilon .
$$

2.4.6. (a) Suppose $\mathbf{A} \subset [a, b]$ is of measure zero. Without loss of generality we can assume that $\mathbf{A} \subset (a, b)$ . Let $\varepsilon > 0$ be given. By the

absolute continuity of $f$ there is $\delta > 0$ such that

$$
\sum_ {k = 1} ^ {\pi} | f (x _ {k}) - f \left(x _ {k} ^ {\prime}\right) | <   \varepsilon
$$

for every finite collection $\{(x_k, x_k')\}$ of pairwise disjoint open intervals of $[a, b]$ with $\sum_{k=1}^{n} (x_k' - x_k) < \delta$ . Since $m(\mathbf{A}) = 0$ , there is an open set $\mathbf{G}$ such that $\mathbf{A} \subset \mathbf{G} \subset (a, b)$ and $m(\mathbf{G}) < \delta$ . We know that $\mathbf{G}$ is a countable union of open pairwise disjoint intervals $(\alpha_i, \beta_i)$ . So we have $\sum_{i=1}^{\infty} (\beta_i - \alpha_i) < \delta$ . For a positive integer $i$ , let $x_i < x_i'$ be points in $[\alpha_i, \beta_i]$ at which $f$ attains its maximum and minimum values. Then $f$ maps the interval $[\alpha_i, \beta_i]$ onto the closed interval with endpoints $f(x_i)$ and $f(x_i')$ . Clearly, $\sum_{k=1}^{n} (x_k' - x_k) < \delta$ for $n \in \mathbb{N}$ . Consequently, $\sum_{k=1}^{n} |f(x_k) - f(x_k')| < \varepsilon$ . Letting $n \to \infty$ , we see that $\sum_{k=1}^{\infty} |f(x_k) - f(x_k')| \leq \varepsilon$ . On the other hand,

$$
f (\mathbf {A}) \subset f (\mathbf {G}) = \bigcup_ {i = 1} ^ {\infty} f (\alpha_ {i}, \beta_ {i}) \subset \bigcup_ {i = 1} ^ {\infty} f ([ \alpha_ {i}, \beta_ {i} ]).
$$

Hence there is a countable cover of $f(\mathbf{A})$ by closed intervals whose total measure is not greater than $\varepsilon$ .

(b) This is an immediate consequence of 2.2.15.

2.4.7. No. The Cantor function $\varphi$ defined in 2.2.11 maps the Cantor set (which is of measure zero) onto $[0,1]$ . In view of the preceding result, $\varphi$ is not absolutely continuous, although it is continuous and monotonically increasing.

2.4.8. We follow the proof presented in [22]. For $n \in \mathbb{N}$ , set $\mathbf{I}_{k,n} - (a + k(b - a)2^{-n}, a + (k + 1)(b - a)2^{-n})$ , $k = 0, 1, \ldots, 2^{n} - 1$ , and define

$$
v _ {n} (y) = \sum_ {k = 0} ^ {2 ^ {n} - 1} \chi_ {\mathbf {B} _ {k, n}} (y),
$$

where $\mathbf{B}_{k,n} = f(\mathbf{I}_{k,n})$ . The function $v_{n}$ counts the number of $\mathbf{I}_{k,n}$ on which the equation $f(x) = y$ has at least one solution. Moreover, if $m_{k,n} = \inf \{f(x):x\in \mathbf{I}_{k,n}\}$ and $M_{k,n} = \sup \{f(x):x\in \mathbf{I}_{k,n}\}$ ,

then $\mathbf{B}_{k,n} = f(\mathbf{I}_{k,n})$ is an interval with end points $m_{k,n}$ and $M_{k,n}$ . Therefore $v_{n}$ is measurable, and

$$
\int_ {\mathbb {R}} v _ {n} (y) d y = \sum_ {k = 0} ^ {2 ^ {n} - 1} m \left(\mathrm {B} _ {k, n}\right) = \sum_ {k = 0} ^ {2 ^ {n} - 1} \left(M _ {k, n} - m _ {k, n}\right).
$$

It then follows by 1.2.16 that $\lim_{n\to \infty}\int_{\mathbb{R}}v_n(y)dy = V(f;a,b)$ . On the other hand, $\{v_n\}$ is an increasing sequence and $v_{n}(y)\leq v(y)$ . If we show that $\lim_{n\to \infty}v_n(y) = v(y)$ a.e., the result will follow from the monotone convergence theorem. To this end, note that if $y\neq f(a + k(b - a)2^{-n})$ and if $v(y) = p\in \mathbb{N}$ , then also $v_{n}(y) = p$ for sufficiently large $n$ . If $v(y) = \infty$ , where $y\neq f(a + k(b - a)2^{-n})$ , then, given $q\in \mathbb{N}$ , there is $N$ such that $v_{N}(y)\geq q$ . This shows that $\lim_{n\to \infty}v_n(y) = v(y)$ for all $y\neq f(a + k(b - a)2^{-n})$ .

2.4.9. We follow the proof presented in [22]. Suppose $f$ is not absolutely continuous; a contradiction will follow. Then there is $\varepsilon_0$ such that for any $\delta > 0$ , there exists a finite collection $\{(x_k, x_k')\}$ of pairwise disjoint open intervals of $[a, b]$ with $\sum_{k=1}^{n} (x_k' - x_k) < \delta$ and such that $\sum_{k=1}^{n} |f(x_k) - f(x_k')| \geq \varepsilon_0$ . We choose a sequence $\{\delta_i\}$ such that the series $\sum_{i=1}^{\infty} \delta_i$ converges. For each $\delta_i$ we find a finite collection $\{(x_{k,i}, x_{k,i}')\}$ of pairwise disjoint open intervals of $[a, b]$ with $\sum_{k=1}^{n_i} (x_{k,i}' - x_{k,i}) < \delta_i$ for which

$$
\sum_ {k = 1} ^ {n _ {i}} \left(M _ {k, i} - m _ {k, i}\right) \geq \sum_ {k = 1} ^ {n _ {i}} \left| f \left(x _ {k, i} ^ {\prime}\right) - f \left(x _ {k, i}\right) \right| \geq \varepsilon_ {0},
$$

where $M_{k,i} = \sup \{f(x) : x \in (x_{k,i}, x_{k,i}')\}$ and $m_{k,i} = \inf \{f(x) : x \in (x_{k,i}, x_{k,i}')\}$ . We put

$$
\mathbf {A} _ {i} = \bigcup_ {i = 1} ^ {n _ {i}} \left(x _ {k, i}, x _ {k, i} ^ {\prime}\right) \quad \text {a n d} \quad \mathbf {A} = \bigcap_ {n = 1} ^ {\infty} \bigcup_ {i = n} ^ {\infty} \mathbf {A} _ {i}.
$$

It is easy to check that $m(\mathbf{A}) = 0$ . So, by assumption, $m(f(\mathbf{A})) = 0$ . As in the solution to the previous problem, we define

$$
w _ {i} (y) = \sum_ {k = 1} ^ {n _ {i}} \chi_ {\mathbf {B} _ {k, i}} (y),
$$

where $\mathbf{B}_{k,i} = f((x_{k,i}, x_{k,i}'))$ . The function $w_i(y)$ counts the number of intervals $(x_{k,i}, x_{k,i}')$ on which the equation $f(x) = y$ has at least one solution. Consequently, we have $w_i(y) \leq v(y)$ , where $v(y)$ is the Banach indicatrix defined in the previous problem. We also have

$$
\int_ {\mathbb {R}} w _ {i} (y) d y = \sum_ {k = 1} ^ {n _ {i}} \left(M _ {k, i} - m _ {k, i}\right) \geq \varepsilon_ {0}.
$$

Since $v(y)$ is integrable, the set $\mathbf{C} = \{y : v(y) = \infty\}$ is of measure zero. Let $\mathbf{B} = \{y : \lim_{i \to \infty} w_i(y) \neq 0\}$ . We will show that $\mathbf{B} \setminus \mathbf{C} \subset f(\mathbf{A})$ . If $y_0 \in \mathbf{B} \setminus \mathbf{C}$ , then there is a sequence $\{i_r\}$ such that $w_{i_r}(y_0) \geq 1$ . Since $w_{i_r}(y_0) \leq v(y_0) < \infty$ , there are only a finite number of distinct elements in the sequence $\{x_{i_r}\}$ such that $f(x_{i_r}) = y_0$ and $x_{i_r} \in A_{i_r}$ . Therefore there is an element, say $x_0$ , which appears infinitely many times in the sequence. Since $x_{i_r} \in A_{i_r}$ , we see that $x_0 \in A$ . So, $f(x_0) = y_0 \in f(A)$ , which proves the inclusion $B \setminus C \subset f(A)$ . Hence $m(B) = 0$ , and consequently, $\lim_{i \to \infty} w_i(y) = 0$ a.e. By the Lebesgue dominated convergence theorem, $\lim_{i \to \infty} \int_R w_i(y) dy = 0$ , which contradicts the fact that $\int_R w_i(y) dy \geq \varepsilon_0$ .

2.4.10. The result follows immediately from the preceding problem, and from 2.4.1. and 2.4.6.

2.4.11. We first show that $V(F; a, b) \leq \int_{a}^{b} |f(t)| dt$ . Indeed, if $a = x_0 < x_1 < \dots < x_n = b$ is a partition of $[a, b]$ , then

$$
\begin{array}{l} \sum_ {k = 0} ^ {n - 1} | F (x _ {k + 1}) - F (x _ {k}) | = \sum_ {k = 0} ^ {n - 1} \left| \int_ {x _ {k}} ^ {x _ {k + 1}} f (t) d t \right| \\ \leq \sum_ {k = 0} ^ {n - 1} \int_ {x _ {k}} ^ {x _ {k + 1}} | f (t) | d t = \int_ {a} ^ {b} | f (t) | d t, \\ \end{array}
$$

which implies $V(F; a, b) \leq \int_{a}^{b} |f(t)| dt$ . To prove the opposite inequality, define

$$
\mathbf {P} = \{x \in (a, b): f (x) \geq 0 \} \quad \text {a n d} \quad \mathbf {N} = \{x \in (a, b): f (x) <   0 \}.
$$

Then

$$
\int_ {a} ^ {b} | f (t) | d t = \int_ {\mathbf {P}} f (t) d t - \int_ {\mathbf {N}} f (t) d t.
$$

By the absolute continuity of the Lebesgue integral (see, e.g., 2.3.4), given $\varepsilon > 0$ , there is $\delta > 0$ such that $\int_{\mathbf{E}} |f(t)| dt < \varepsilon$ if $\mathbf{E} \subset [a, b]$ and $m(\mathbf{E}) < \delta$ . Since $\mathbf{P}$ and $\mathbf{N}$ are measurable, there are closed sets $\mathbf{F}_{\mathbf{P}} \subset \mathbf{P}$ and $\mathbf{F}_{\mathbf{N}} \subset \mathbf{N}$ such that $m(\mathbf{P} \setminus \mathbf{F}_{\mathbf{P}}) < \delta$ and $m(\mathbf{N} \setminus \mathbf{F}_{\mathbf{N}}) < \delta$ . Thus

$$
\int_ {a} ^ {b} | f (t) | d t <   \int_ {\mathbf {F} _ {\mathbf {P}}} f (t) d t - \int_ {\mathbf {F} _ {\mathbf {N}}} f (t) d t + 2 \varepsilon .
$$

Since the sets $\mathbf{F}_{\mathbb{P}}$ and $\mathbf{F}_{\mathbb{N}}$ are closed and disjoint, there are disjoint open subsets of $(a,b)$ , say $\mathbf{G}_{\mathbb{P}}$ and $\mathbf{G}_{\mathbb{N}}$ , containing $\mathbf{F}_{\mathbb{P}}$ and $\mathbf{F}_{\mathbb{N}}$ , respectively, and such that $m(\mathbf{G}_{\mathbb{P}} \setminus \mathbf{F}_{\mathbb{P}}) < \delta$ and $m(\mathbf{G}_{\mathbb{N}} \setminus \mathbf{F}_{\mathbb{N}}) < \delta$ . Consequently,

$$
\int_ {a} ^ {b} | f (t) | d t <   \int_ {C _ {F}} f (t) d t - \int_ {C _ {N}} f (t) d t + 4 \varepsilon .
$$

We know that any open set is a union of countably many pairwise disjoint open intervals. Therefore there is a finite union $\bigcup_{k=1}^{n} (\alpha_k, \beta_k) = \mathbf{G}_n$ such that $m(\mathbf{G}_{\mathbf{P}} \setminus \mathbf{G}_n) < \delta$ . So we have

$$
\int_ {G _ {P}} f (t) d t - \int_ {G _ {n}} f (t) d t <   \varepsilon .
$$

Since

$$
\int_ {G _ {n}} f (t) d t = \sum_ {k = 1} ^ {n} \int_ {\alpha_ {k}} ^ {\beta_ {k}} f (t) d t = \sum_ {k = 1} ^ {n} \left(F \left(\beta_ {k}\right) - F \left(\alpha_ {k}\right)\right),
$$

we obtain

$$
\int_ {\mathbf {G} _ {\mathbb {P}}} f (t) d t <   \sum_ {k = 1} ^ {n} \left(F \left(\beta_ {k}\right) - F \left(\alpha_ {k}\right)\right) + \varepsilon .
$$

Likewise, if $\mathbf{G_N} = \bigcup_{k=1}^{\infty} (\sigma_k, \tau_k)$ , where $(\sigma_k, \tau_k)$ are pairwise disjoint, there is $m$ such that

$$
\int_ {G _ {N}} f (t) d t > \sum_ {k = 1} ^ {m} \left(F \left(\tau_ {k}\right) - F \left(\sigma_ {k}\right)\right) - \varepsilon .
$$

It then follows that

$$
\int_ {a} ^ {b} | f (t) | d t <   \sum_ {k = 1} ^ {n} \left(F \left(\beta_ {k}\right) - F \left(\alpha_ {k}\right)\right) - \sum_ {k = 1} ^ {m} \left(F \left(\tau_ {k}\right) - F \left(\sigma_ {k}\right)\right) + 6 \varepsilon ,
$$

which implies

$$
\int_ {a} ^ {b} | f (t) | d t <   \sum_ {k = 1} ^ {n} | F (\beta_ {k}) - F ^ {\prime} (\alpha_ {k}) | + \sum_ {k = 1} ^ {m} | F ^ {\prime} (\tau_ {k}) - F ^ {\prime} (\sigma_ {k}) | + 6 \varepsilon .
$$

Since the pairwise disjoint intervals $(\alpha_{k},\beta_{k})$ are disjoint from the pairwise disjoint intervals $(\sigma_{i},\tau_{i})$ , we see that

$$
\sum_ {k = 1} ^ {n} | F (\beta_ {k}) - F (\alpha_ {k}) | + \sum_ {k = 1} ^ {m} | F (\tau_ {k}) - F (\sigma_ {k}) | \leq V (F; a, b),
$$

and consequently,

$$
\int_ {a} ^ {b} | f (t) | d t <   V (F; a, b) + 6 \varepsilon .
$$

2.4.12. (a) Put $\mathbf{A} = g(\mathbf{E})$ . We know from 2.4.6 that $\mathbf{A}$ is a measurable subset of $[c, d]$ . If $\mathbf{A}$ is open, then $\mathbf{A} = \bigcup_{n=1}^{\infty} (\alpha_n, \beta_n)$ , where $(\alpha_n, \beta_n)$ are pairwise disjoint and $\alpha_n = g(x_n)$ , $\beta_n = g(y_n)$ . Using Theorem 2, we get

$$
\begin{array}{l} m (\mathbf {A}) = \sum_ {n = 1} ^ {\infty} \left(\beta_ {n} - \alpha_ {n}\right) = \sum_ {n = 1} ^ {\infty} \left(g \left(y _ {n}\right) - g \left(x _ {n}\right)\right) \\ = \sum_ {n = 1} ^ {\infty} \int_ {x _ {n}} ^ {y _ {n}} g ^ {\prime} (x) d x = \int_ {E} g ^ {\prime} (x) d x. \\ \end{array}
$$

If $\mathbf{A}$ is closed, then $(c,d)\setminus \mathbf{A}$ is open, and by what we have proved and by Theorem 2, we see that the stated equality is true also in this case. Since $\mathbf{A}$ is measurable, given $\varepsilon >0$ , there are an open set $\mathbf{G}$ and a closed set $\mathbf{F}$ such that $\mathbf{F}\subset \mathbf{A}\subset \mathbf{G}$ and $m(\mathbf{G}) < m(\mathbf{A}) + \varepsilon$ and $m(\mathbf{F}) > m(\mathbf{A}) - \varepsilon$ . Since $g^{\prime}\geq 0$ , we have

$$
\int_ {g ^ {- 1} (\mathbf {F})} g ^ {\prime} d m \leq \int_ {\mathbf {E}} g ^ {\prime} d m \leq \int_ {g ^ {- 1} (\mathbf {G})} g ^ {\prime} d m,
$$

which implies that

$$
m (\mathbf {A}) - \varepsilon <   m (\mathbf {F}) \leq \int_ {\mathbf {E}} g ^ {\prime} d m \leq m (\mathbf {G}) <   m (\mathbf {A}) + \varepsilon .
$$

(b) Without loss of generality we can assume that $\mathbf{A} \subset (c, d)$ . Since $m(\mathbf{A}) = 0$ , there is a sequence of open sets $\mathbf{G}_n$ such that

$$
\mathbf {A} \subset \mathbf {G} _ {n + 1} \subset \mathbf {G} _ {n} \subset (c, d), \quad n \in \mathbb {N},
$$

and $\lim_{n\to \infty}m(\mathbf{G}_n) = 0$ . Put $\tilde{\mathbf{A}} = \bigcap_{n = 1}^{\infty}\mathbf{G}_{n}$ . Then $\mathbf{A}\subset \tilde{\mathbf{A}}$ $m(\tilde{\mathbf{A}}) = 0$ and $g^{-1}(\tilde{\mathbf{A}}) = \bigcap_{n = 1}^{\infty}g^{-1}(\mathbf{G}_n)$ is measurable. By (a),

$$
0 = m (\bar {\mathbf {A}}) = \int_ {g ^ {- 1} (\bar {\mathbf {A}})} g ^ {\prime} d m = \int_ {g ^ {- 1} (\bar {\mathbf {A}}) \cap \mathbf {H}} g ^ {\prime} d m.
$$

Hence $m(g^{-1}(\tilde{\mathbf{A}}) \cap \mathbf{H}) = 0$ , and since $g^{-1}(\mathbf{A}) \subset g^{-1}(\tilde{\mathbf{A}})$ , the claim follows.

(c) By 2.1.12, there are a $\mathcal{G}_{\delta}$ set $\mathbf{U}$ and a set $\mathbf{A}$ of measure zero such that $\mathbf{B} = \mathbf{U} \cup \mathbf{A}$ . Then $g^{-1}(\mathbf{B}) = g^{-1}(\mathbf{U}) \cup g^{-1}(\mathbf{A})$ , and since $g$ is continuous and strictly increasing, $g^{-1}(\mathbf{U})$ is also a $\mathcal{G}_{\delta}$ set. It follows from (b) that $m(g^{-1}(\mathbf{A}) \cap \mathbf{H}) = 0$ . Consequently, $g^{-1}(\mathbf{B}) \cap \mathbf{H}$ is measurable. Moreover,

$$
\int_ {\mathbf {C}} g ^ {\prime} d m = \int_ {g ^ {- 1} (\mathbf {U}) \cap \mathbf {H}} g ^ {\prime} d m = \int_ {g ^ {- 1} (\mathbf {U})} g ^ {\prime} d m = m (\mathbf {U}) = m (\mathbf {B}),
$$

where the third equality comes from (a). We also have

$$
\begin{array}{l} \int_ {C} g ^ {\prime} d m = \int_ {g ^ {- 1} (B) \cap H} g ^ {\prime} d m = \int_ {a} ^ {b} \chi_ {g ^ {- 1} (B) \cap H} (x) g ^ {\prime} (x) d x \\ - \int_ {a} ^ {b} \chi_ {B} (g (x)) g ^ {\prime} (x) d x. \\ \end{array}
$$

2.4.13. Suppose first that $f$ is a simple function on $[c, d]$ , that is, $f(x) = \sum_{i=1}^{n} c_i \chi_{\mathbf{A}_i}(x)$ , where $[c, d] = \bigcup_{i=1}^{n} \mathbf{A}_i$ . Then by 2.4.12(c),

$$
\begin{array}{l} \int_ {c} ^ {d} f (t) d t = \sum_ {i = 1} ^ {n} c _ {i} m \left(\mathrm {A} _ {i}\right) = \sum_ {i = 1} ^ {n} c _ {i} \int_ {a} ^ {b} \chi_ {\mathrm {A} _ {i}} (g (x)) g ^ {\prime} (x) d x \\ = \int_ {a} ^ {b} f (g (x)) g ^ {\prime} (x) d x. \\ \end{array}
$$

If $f$ is nonnegative, then there is an increasing sequence $\{f_n\}$ of simple functions converging to $f$ , and the desired equality follows from the Lebesgue monotone convergence theorem. Finally, if $f$ is an arbitrary

integrable function, the equality to be proved is a consequence of the fact that $\int_{c}^{d} f(t) dt = \int_{c}^{d} f^{+}(t) dt - \int_{c}^{d} f^{-}(t) dt$ .

2.4.14. By Theorem 2, $F$ and $G$ are absolutely continuous on $[a, b]$ . We will show that $FG$ is also absolutely continuous. To this end, denote by $A$ and $B$ the supremum of $|F(x)|$ and $|G(x)|$ over $[a, b]$ , respectively, and observe that

$$
| F (t) G (t) - F (s) G (s) | \leq A | G (t) - G (s) | + B | F (t) - F (s) |.
$$

This clearly implies the absolute continuity of $FG$ . Hence $FG$ is differentiable a.e. and $(FG)' = FG' + F'G = Fg + fG$ , where the last equality comes from Theorem 2. The desired equality follows if we appeal to Theorem 2 again.

2.4.15. This is an immediate consequence of Theorem 2 and the result in the previous problem.

2.4.16. Any increasing function $f$ on $[a, b]$ is differentiable a.e., and by Theorem 1, $f'$ is integrable. Hence by Theorem 2,

$$
g (x) = f (a) + \int_ {a} ^ {x} f ^ {\prime} (t) d t
$$

is absolutely continuous and $g'(x) = f'(x)$ a.e. So if we set $h(x) = f(x) - g(x)$ we get the representation $f(x) = g(x) + h(x)$ , where $g$ is absolutely continuous and $h$ singular. To see that $h$ is monotonically increasing, we appeal again to Theorem 1 and obtain

$$
h \left(x _ {2}\right) - h \left(x _ {1}\right) = f \left(x _ {2}\right) - f \left(x _ {1}\right) - \int_ {x _ {1}} ^ {x _ {2}} f ^ {\prime} (t) d t \geq 0
$$

for $x_2 > x_1$ .

2.4.17. The following example is due to L. Takács [Amer. Math. Monthly, 85(1978), 35-37]. For

$$
x = \sum_ {n = 1} ^ {\infty} 2 ^ {- a _ {n}}, \tag {1}
$$

where $a_1 < a_2 < \ldots$ are positive integers, we set

$$
f (x) = \sum_ {n = 1} ^ {\infty} \frac {r ^ {n}}{(1 + r) ^ {a _ {n}}}; \quad r > 0.
$$

In this way $f$ is well defined on $[0,1]$ , and we put $f(0) = 0$ . We first prove that $f$ is strictly increasing on $[0,1]$ . Clearly, $f(0) < f(x)$ for $0 < x \leq 1$ . If $0 < x < y \leq 1$ and $y = \sum_{n=1}^{\infty} 2^{-b_n}$ , where $b_1 < b_2 < \ldots$ are positive integers, then there is a smallest integer $k$ such that $a_k > b_k$ . Consequently,

$$
\begin{array}{l} \sum_ {n = k} ^ {\infty} \frac {r ^ {n}}{(1 + r) ^ {a _ {n}}} \leq \frac {r ^ {k}}{(1 + r) ^ {a _ {k}}} \left(1 + \frac {r}{1 + r} + \frac {r ^ {2}}{(1 + r) ^ {2}} + \dots\right) \\ = \frac {r ^ {k}}{(1 + r) ^ {a _ {k} - 1}} \leq \frac {r ^ {k}}{(1 + r) ^ {b _ {k}}} <   \sum_ {n = k} ^ {\infty} \frac {r ^ {n}}{(1 + r) ^ {b _ {n}}}, \\ \end{array}
$$

which shows that $f(x) < f(y)$ . For $x$ given by (1), define

$$
x _ {n} = \sum_ {a _ {k} \leq n} 2 ^ {- a _ {k}} \quad \text {a n d} \quad y _ {n} = x _ {n} + 2 ^ {- n}.
$$

Then $x_{n} < x \leq y_{n}$ and $f(y_{n}) - f(x_{n}) = \frac{r^{k_{n} + 1}}{(1 + r)^{n}}$ , where $k_{n}$ is the number of $a_{k}$ which are not greater than $n$ . Since $k_{n} \leq n$ , one can easily check that $\lim_{n \to \infty} (f(y_{n}) - f(x_{n})) = 0$ , which implies the continuity of $f$ on $(0,1]$ . Clearly, $\lim_{x \to 0} f(x) = 0$ .

We know that $f'$ exists and is finite a.e. Thus (see, e.g., II, 2.1.14),

$$
f ^ {\prime} (x) = \lim  _ {n \rightarrow \infty} \frac {f \left(y _ {n}\right) - f \left(x _ {n}\right)}{y _ {n} - x _ {n}} = \lim  _ {n \rightarrow \infty} \left(\frac {2}{1 + r}\right) ^ {n} r ^ {k _ {n} + 1}.
$$

It then follows that if $f'(x) \neq 0$ , then $\lim_{n \to \infty} r^{k_n - k_{n-1}} = \frac{1 + r}{2}$ . So, either $r = 1$ or $\lim_{n \to \infty} (k_n - k_{n-1}) = k$ . In the latter case (see, e.g., I, 2.3.14) we have $\lim_{n \to \infty} k_n / n = k$ . Since $0 \leq k_n \leq n$ are integers, we conclude that $k = 0$ or $k = 1$ . In both cases we get $r = 1$ . Consequently, $f' = 0$ a.e. if $r \neq 1$ .

2.4.18. Assume first that a function $f$ on $\mathbb{R}$ has the form $f(x) = \int_{-\infty}^{x} \varphi(t) dt$ for some integrable function $\varphi$ on $\mathbb{R}$ . Then the absolute continuity of $f$ on $[-K, K]$ follows from the absolute continuity of the Lebesgue integral (see, e.g., 2.3.4). Furthermore, we know from 2.4.11 that

$$
V (f; - K, K) = \int_ {- K} ^ {K} | \varphi (x) | d x \leq \int_ {\mathbb {R}} | \varphi | d m,
$$

which implies that $V(f; -\infty, \infty) < \infty$ . Let $\{x_n\}$ be a sequence diverging to $-\infty$ . Then $\varphi \cdot \chi_{(-\infty, x_n]}$ converges to zero on $\mathbb{R}$ and, by the Lebesgue dominated convergence theorem,

$$
\lim  _ {n \rightarrow \infty} f (x _ {n}) = \int_ {\mathbb {R}} \varphi \cdot \chi_ {(- \infty , x _ {n} ]} d m = 0.
$$

Conversely, if $f$ is absolutely continuous on $[-K, K]$ , then, by Theorem 2,

$$
f (x) = f (- K) + \int_ {- K} ^ {x} f ^ {\prime} (t) d t,
$$

and letting $K$ go to $\infty$ , we get

$$
f (x) = \lim  _ {K \rightarrow \infty} \int_ {- K} ^ {x} f ^ {\prime} (t) d t.
$$

Moreover, we have

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} | f ^ {\prime} (t) | d t = \lim  _ {n \rightarrow \infty} \int_ {- n} ^ {n} | f ^ {\prime} (t) | d t \\ = \lim  _ {n \rightarrow \infty} V (f; - n, n) = V (f; - \infty , \infty) <   \infty , \\ \end{array}
$$

where the second equality follows from 2.4.11.

2.4.19. In the formula for integration by parts given in 2.4.15 take limits as $a \to -\infty$ and $b \to \infty$ and apply the result in the previous problem.

2.4.20. We first note that $f_h$ is well defined because $L^p[a, b] \subset L^1[a, b]$ (see, e.g., 2.3.35). Since

$$
f _ {h} (x) = \frac {1}{2 h} (F (x + h) - F (x - h)), \quad \text {w h e r e} \quad F (x) = \int_ {a - h} ^ {x} f (t) d t,
$$

the continuity of $f_h$ follows from Theorem 2. For $p > 1, 1/p + 1/p' = 1$ , by Hölder's inequality,

$$
\begin{array}{l} \left| f _ {h} (x) \right| ^ {p} \leq \frac {1}{(2 h) ^ {p}} \left(\int_ {x - h} ^ {x + h} 1 d t\right) ^ {\frac {p}{p}} \int_ {x - h} ^ {x + h} | f (t) | ^ {p} d t \\ = \frac {1}{2 h} \int_ {x - h} ^ {x + h} | f (t) | ^ {p} d t. \\ \end{array}
$$

Clearly, for $p = 1$ we have

$$
| f _ {h} (x) | \leq \frac {1}{2 h} \int_ {x - h} ^ {x + h} | f (t) | d t.
$$

Hence, using Fubini's theorem and the change of variable formula, we obtain

$$
\begin{array}{l} \int_ {a} ^ {b} | f _ {h} (x) | ^ {p} d x \leq \frac {1}{2 h} \int_ {a} ^ {b} \left(\int_ {x - h} ^ {x + h} | f (t) | ^ {p} d t\right) d x \\ = \frac {1}{2 h} \int_ {a} ^ {b} \left(\int_ {- h} ^ {h} | f (t + x) | ^ {p} d t\right) d x \\ = \frac {1}{2 h} \int_ {- h} ^ {h} \left(\int_ {a} ^ {b} | f (t + x) | ^ {p} d x\right) d t \\ = \frac {1}{2 h} \int_ {- h} ^ {h} \left(\int_ {a + t} ^ {b + t} | f (u) | ^ {p} d u\right) d t \\ \leq \frac {1}{2 h} \int_ {- h} ^ {h} \left(\int_ {a} ^ {b} | f (u) | ^ {p} d u\right) d t = \int_ {a} ^ {b} | f (u) | ^ {p} d u, \\ \end{array}
$$

where the last inequality follows from the fact that $f$ vanishes outside $[a, b]$ . Thus the inequality $\| f_h \|_p \leq \| f \|_p$ is proved.

2.4.21. If $p > 1$ and $1/p + 1/p' = 1$ , then by Hölder's inequality,

$$
\begin{array}{l} \| f _ {h} - f \| _ {p} ^ {r} = \int_ {a} ^ {b} \left| \frac {1}{2 h} \int_ {x - h} ^ {x + h} f (t) d t - \frac {1}{2 h} \int_ {x - h} ^ {x + h} f (x) d t \right| ^ {p} d x \\ \leq \frac {1}{(2 h) ^ {p}} \int_ {a} ^ {b} \left(\int_ {x - h} ^ {x + h} | f (t) - f (x) | d t\right) ^ {p} d x \\ \leq \frac {1}{(2 h) ^ {p}} \int_ {a} ^ {b} \left(\int_ {x - h} ^ {x + h} | f (t) - f (x) | ^ {p} d t\right) (2 h) ^ {p / p ^ {\prime}} d x \\ = \frac {1}{2 h} \int_ {a} ^ {b} \left(\int_ {x - h} ^ {x + h} | f (t) - f (x) | ^ {p} d t\right) d x \\ = \frac {1}{2 h} \int_ {- h} ^ {h} \left(\int_ {a} ^ {b} | f (t + x) - f (x) | ^ {p} d x\right) d t, \\ \end{array}
$$

where the last equality follows from the change of variable formula and Fubini's theorem. It is clear that the obtained inequality holds also for $p = 1$ . So, by 2.3.39, given $\varepsilon > 0$ , there is $\delta > 0$ such that $\int_{a}^{b} |f(t + x) - f(x)|^{p} dx < \varepsilon$ for $|t| < \delta$ . Consequently, if $0 < h < \delta$ , then $\| f_h - f \|_p^p < \varepsilon$ .

It is worth noting here that since the function $f_{h}$ is continuous on $[a, b]$ , it realizes the approximation stated in 2.3.27.

2.4.22. We have

$$
\begin{array}{l} \left| \frac {F (x + h) - F (x)}{h} - f (x) \right| = \left| \frac {1}{h} \int_ {x} ^ {x + h} (f (t) - f (x)) d t \right| \\ \leq \frac {1}{h} \int_ {x} ^ {x + h} | f (t) - f (x) | d t, \\ \end{array}
$$

which gives $F'(x) = f(x)$ .

2.4.23. If $f$ is continuous at $x$ , then given $\varepsilon > 0$ , there is $\delta > 0$ such that $|f(t) - f(x)| < \varepsilon$ if $|t - x| < \delta$ . So, for $|h| < \delta$ ,

$$
\frac {1}{h} \int_ {\dot {x}} ^ {x + h} | f (t) - f (x) | d t <   \varepsilon .
$$

2.4.24. If $r$ is a rational number, then the function $t \mapsto |f(t) - r|$ is integrable on $[a, b]$ , and by Theorem 2,

$$
\lim  _ {h \rightarrow 0} \frac {1}{h} \int_ {x} ^ {x + h} | f (t) - r | d t = | f (x) - r |
$$

for almost all $x \in [a, b]$ . Let $\mathbf{E}(r)$ denote the set of all points in $[a, b]$ at which the above equality fails to hold. Then $m(\mathbf{E}(r)) = 0$ . If $\{r_n\}$ is a sequence of all rationals, then the set

$$
\mathbf {E} = \bigcup_ {n = 1} ^ {\infty} \mathbf {E} (r _ {n}) \cup \{x \in [ a, b ]: f (x) = \pm \infty \}
$$

is of measure zero. Our task is to show that every point in $[a, b] \setminus \mathbf{E}$ is a Lebesgue point for $f$ . Suppose that $x_0 \in [a, b] \setminus \mathbf{E}$ and let $\varepsilon > 0$ be given. Then there is $r_n$ such that $|f(x_0) - r_n| < \varepsilon / 3$ , and therefore,

$$
\left| \frac {1}{h} \int_ {x _ {0}} ^ {x _ {0} + h} | f (t) - r _ {n} | d t - \frac {1}{h} \int_ {x _ {0}} ^ {x _ {0} + h} | f (t) - f (x _ {0}) | d t \right| <   \frac {\varepsilon}{3}.
$$

Since $x_0 \notin \mathbf{E}$ , there is $\delta > 0$ such that if $|h| < \delta$ , then

$$
\left| \frac {1}{h} \int_ {x _ {0}} ^ {x _ {0} + h} | f (t) - r _ {n} | d t - | f (x _ {0}) - r _ {n} | \right| <   \frac {\varepsilon}{3},
$$

which implies

$$
\frac {1}{h} \int_ {x _ {0}} ^ {x _ {0} + h} | f (t) - r _ {\pi} | d t <   \frac {2}{3} \varepsilon .
$$

It then follows that for $|h| < \delta$ ,

$$
\frac {1}{h} \int_ {x _ {0}} ^ {x _ {0} + h} | f (t) - f (x _ {0}) | d t <   \varepsilon .
$$

2.4.25. Without loss of generality we can assume that $\mathbf{A}$ is bounded, say, $\mathbf{A} \subset [\alpha, \beta]$ . Put $a = \alpha - 1$ and $b = \beta + 1$ . Then $F(x) = \int_{a}^{x} \chi_{\mathbf{A}}(t) dt$ satisfies $F'(x) = \chi_{\mathbf{A}}(x)$ for a.e. $x \in [a, b]$ . In particular, $F'(x) = 1$ a.c. on $\mathbf{A}$ . If $x$ is such that $F'(x) = 1$ , then

$$
\begin{array}{l} 1 = F ^ {\prime} (x) = \lim  _ {h \rightarrow 0} \frac {F (x + h) - F (x - h)}{2 h} = \lim  _ {h \rightarrow 0} \frac {1}{2 h} \int_ {x - h} ^ {x + h} \chi_ {\mathbf {A}} (t) d t \\ = \lim  _ {h \rightarrow 0} \frac {m (A \cap [ x - h , x + h ])}{2 h}. \\ \end{array}
$$

2.4.26. We know, by 2.1.11, that there is a $\mathcal{G}_{\delta}$ set $\mathbf{E}$ such that $\mathbf{A} \subset \mathbf{E}$ and $m(\mathbf{E}) = m^{*}(\mathbf{A})$ . Without loss of generality we can assume that $m^{*}(\mathbf{A}) < \infty$ . Thus, for any interval $\mathbf{I}$ ,

$$
\begin{array}{l} m (\mathbf {E} \cap \mathbf {I}) = m (\mathbf {E}) - m (\mathbf {E} \setminus \mathbf {I}) = m ^ {*} (\mathbf {A}) - m (\mathbf {E} \setminus \mathbf {I}) \\ \leq m ^ {*} (\mathbf {A}) - m ^ {*} (\mathbf {A} \backslash \mathbf {I}) \leq m ^ {*} (\mathbf {A} \cap \mathbf {I}), \\ \end{array}
$$

and the first statement follows from the result given in the previous problem. To prove the second statement, note that if $\mathbf{A}$ is measurable, then so is $\mathbf{A}^c$ , and therefore almost all points in $\mathbf{A}^c$ are points of its density, thus points of dispersion of $\mathbf{A}$ . To prove the opposite implication, assume that $\mathbf{A}$ is nonmeasurable. By 2.1.11 there is a measurable cover $\mathbf{E}$ for $\mathbf{A}$ with $m^{*}(\mathbf{A}) = m(\mathbf{E})$ . Since $\mathbf{E}$ is measurable, almost all points in $\mathbf{E} \setminus \mathbf{A}$ are points of density for $\mathbf{E}$ and, by the above, they are also points of outer density for $\mathbf{A}$ . Since $\mathbf{A}$ is nonmeasurable, $m^{*}(\mathbf{E} \setminus \mathbf{A}) > 0$ . This implies that the set of points in $\mathbf{A}^c$ which are not points of outer dispersion for $\mathbf{A}$ is a set of positive outer measure.

2.4.27. Suppose $f$ is measurable on $[a, b]$ . It follows from the Lusin theorem (see, e.g., 2.2.27) that, given $\varepsilon > 0$ , there is a closed set $\mathbf{F} \subset [a, b]$ such that $m([a, b] \setminus \mathbf{F}) < \varepsilon$ and $f_{|\mathbf{F}}$ is continuous. It follows from the previous problem that almost all points in $\mathbf{F}$ are points of

dispersion for $\mathbf{F}^c$ . So if $x_0 \in \mathbf{F}$ is a point of dispersion of $\mathbf{F}^c$ , then for any $\varepsilon_1 > 0$ we have

$$
\{x \in [ x _ {0} - h, x _ {0} + h ]: | f (x) - f (x _ {0}) | \geq \varepsilon_ {1} \} \subset [ x _ {0} - h, x _ {0} + h ] \cap \mathbf {F} ^ {\mathrm {c}}
$$

for sufficiently small $h > 0$ , which shows that the set on which $f$ is not approximately continuous is of measure less than $\varepsilon$ . Since $\varepsilon > 0$ can be arbitrarily chosen, the proof of necessity is complete. Suppose now that $f$ is approximately continuous a.e. on $[a, b]$ . Let $c$ be any real number. We will show that the set $\mathbf{A} = \{x \in [a, b] : f(x) > c\}$ is measurable. In view of 2.4.26, it suffices to show that almost all points in $\mathbf{A}^c$ are points of outer dispersion for $\mathbf{A}$ . Let $x_0 \in \mathbf{A}$ be a point of approximate continuity of $f$ , and take $\varepsilon = f(x_0) - c > 0$ . Then

$$
\begin{array}{l} \frac {m ^ {*} \left(\left\{x \in \left[ x _ {0} - h , x _ {0} + h \right] : | f (x) - f \left(x _ {0}\right) | \geq \varepsilon \right\}\right)}{2 h} \\ \geq \frac {m ^ {\bullet} (\{x \in [ x _ {0} - h , x _ {0} + h ] : f (x) \leq c \})}{2 h} \\ = \frac {m ^ {\circ} ([ x _ {0} - h ; x _ {0} + h ] \cap A ^ {c})}{2 h}, \\ \end{array}
$$

and it follows from the definition of approximate continuity that

$$
\lim  _ {h \rightarrow 0} \frac {m ^ {*} ([ x _ {0} - h , x _ {0} + h ] \cap \mathbf {A} ^ {c})}{2 h} = 0,
$$

which means that $x_0$ is a point of outer dispersion for $\mathbf{A}^c$ . Since almost all points in $\mathbf{A}$ are points of approximate continuity of $f$ , the proof of sufficiency is finished.

It is worth noting here that a bounded function on $[a, b]$ is Riemann integrable if and only if it is a.e. continuous (see, e.g., 2.1.55). The above result shows that a bounded function on $[a, b]$ is measurable, and so Lebesgue integrable, if and only if it is a.e. approximately continuous.

2.4.28. Suppose that $x_0$ is a Lebesgue point for $f$ . For any $\varepsilon > 0$ we have

$$
\begin{array}{l} \underbrace {m \left(\left\{x \in \left[ x _ {0} , x _ {0} + h \right] : | f (x) - f \left(x _ {0}\right) | \geq \varepsilon \right\}\right)} _ {h} \\ \leq \frac {1}{\varepsilon} \cdot \frac {1}{h} \int_ {x _ {0}} ^ {x _ {0} + h} | f (x) - f (x _ {0}) | d x. \\ \end{array}
$$

It then follows from the definition of a Lebesgue point that

$$
\lim  _ {h \rightarrow 0 ^ {+}} \frac {m (\{x \in [ x _ {0} , x _ {0} + h ] : | f (x) - f (x _ {0}) | \geq \varepsilon \})}{h} = 0,
$$

which implies that each Lebesgue point of a Lebesgue integrable function is a point of its approximate continuity.

To show that the inverse is not true, consider the function defined on $[-1, 1]$ by

$$
f (x) = \left\{ \begin{array}{l l} 2 ^ {n} & \text {i f} \frac {1}{2 ^ {n}} - \frac {1}{2 ^ {2 n + 1}} <   x \leq \frac {1}{2 ^ {n}}; n = 0, 1, \dots , \\ 0 & \text {o t h e r w i s e .} \end{array} \right.
$$

We first show that $\pmb{f}$ is integrable on $[-1, 1]$ . We have

$$
\int_ {- 1} ^ {1} f (x) d x = \sum_ {n = 0} ^ {\infty} 2 ^ {n} \frac {1}{2 ^ {2 n + 1}} = 1.
$$

Now we observe that $\mathbf{0}$ is a point of approximate continuity of $f$ . If $1/(2^{n+1}) < h \leq 1/(2^n)$ , then for $0 < \varepsilon < 1$ ,

$$
\begin{array}{l} \frac {m \left(\left[ - h , h \right] \cap \{x : f (x) > \varepsilon \}\right)}{2 h} \leq \frac {m \left(\left[ - \frac {1}{2 ^ {n}} , \frac {1}{2 ^ {n}} \right] \cap \{x : f (x) > \varepsilon \}\right)}{\frac {2}{2 ^ {n + 1}}} \\ = \frac {\frac {1}{2 ^ {2 n + 1}} + \frac {1}{2 ^ {2 (n + 1) + 1}} + \dots}{\frac {1}{2 ^ {n}}} \\ = \frac {1}{3 \cdot 2 ^ {n - 1}} \xrightarrow [ n \rightarrow \infty ]{} 0. \\ \end{array}
$$

Since

$$
\begin{array}{l} 2 ^ {n} \int_ {0} ^ {1 / (2 ^ {n})} | f (x) - f (0) | d x = 2 ^ {n} \int_ {0} ^ {1 / (2 ^ {n})} f (x) d x \\ = 2 ^ {n} \sum_ {k = n} ^ {\infty} 2 ^ {k} \frac {1}{2 ^ {2 k + 1}} = 1, \\ \end{array}
$$

zero is not a Lebesgue point of $f$ .

2.4.29. In view of the result in the previous problem, it is enough to show that if $f$ is bounded and measurable on $[a, b]$ , then every point of approximate continuity for $f$ is a Lebesgue point of $f$ . If $x \in (a, b)$ is a point of approximate continuity of $f$ and $|f(t)| \leq M, a \leq t \leq b$ ,

then, given $\varepsilon > 0$ ,

$$
\begin{array}{l} \frac {1}{h} \int_ {x} ^ {x + h} | f (t) - f (x) | d t = \frac {1}{h} \int_ {[ x, x + h ] \cap \{t: | f (t) - f (x) | \geq e \}} | f (t) - f (x) | d t \\ + \frac {1}{h} \int_ {[ x, x + h ] \cap \{t: | f (t) - f (x) | <   e \}} | f (t) - f (x) | d t \\ \leq 2 M \frac {m ([ x , x + h ] \cap \{t : | f (t) - f (x) | \geq \varepsilon \})}{h} + \varepsilon . \\ \end{array}
$$

Passage to the limit as $h \to 0$ gives

$$
\lim  _ {h \rightarrow 0} \frac {1}{h} \int_ {x} ^ {x + h} | f (t) - f (x) | d t \leq \varepsilon .
$$

Since $\varepsilon > 0$ can be arbitrarily small, the required result follows.

2.4.30. Assume that $x_0 \in (a, b)$ is a point of approximate continuity of $f$ in the sense of the definition given in 2.4.27. For $n \in \mathbb{N}$ , define

$$
\mathbf {B} _ {n} = \left\{x \in [ a, b ]: | f (x) - f (x _ {0}) | \geq \frac {1}{n} \right\},
$$

and for positive $h$ put

$$
\mathbf {B} _ {n, h} = \mathbf {B} _ {n} \cap [ x _ {0} - h, x _ {0} + h ].
$$

We know from 2.1.11 that there is a $\mathcal{G}_{\delta}$ set $\mathbf{G}_n$ such that $\mathbf{B}_n \subset \mathbf{G}_n$ and $m^*(\mathbf{B}_n) = m(\mathbf{G}_n)$ . If $\mathbf{G}_{n,h} = \mathbf{G}_n \cap [x_0 - h, x_0 + h]$ , then $\mathbf{G}_{n,h}$ is a measurable set containing $\mathbf{B}_{n,h}$ and $m^*(\mathbf{B}_{n,h}) = m(\mathbf{G}_{n,h})$ . Indeed, we have

$$
\begin{array}{l} \mathbf {G} _ {n} = \mathbf {G} _ {n, h} \cup \left(\mathbf {G} _ {n} \backslash [ x _ {0} - h, x _ {0} + h ]\right), \\ \mathbf {B} _ {n} = \mathbf {B} _ {n, h} \cup \left(\mathbf {B} _ {n} \backslash \left[ x _ {0} - h, x _ {0} + h \right]\right), \\ \end{array}
$$

and, since $\mathbf{B}_n\subset \mathbf{G}_n$ and $\mathbf{B}_{n,h}\subset \mathbf{G}_{n,h}$ , we get

$$
\begin{array}{l} m ^ {*} (\mathbf {B} _ {n}) \leq m ^ {*} (\mathbf {B} _ {n, h}) + m ^ {*} (\mathbf {B} _ {n} \backslash [ x _ {0} - h, x _ {0} + h ]) \\ \leq m \left(\mathrm {G} _ {n, h}\right) + m \left(\mathrm {G} _ {n} \backslash [ x _ {0} - h, x _ {0} + h ]\right) \\ = m \left(\mathbf {G} _ {n}\right) = m ^ {*} \left(\mathbf {B} _ {n}\right). \\ \end{array}
$$

This implies that $m^{*}(\mathbf{B}_{n,h}) = m(\mathbf{G}_{n,h})$ and $m^{*}(\mathbf{B}_n\backslash [x_0 - h,x_0 + h]) = m(\mathbf{G}_n\setminus [x_0 - h,x_0 + h])$ . By the definition of approximate continuity,

$$
\lim  _ {h \rightarrow 0} \frac {m ^ {*} \left(\mathrm {B} _ {n} \cap [ x _ {0} - h , x _ {0} + h ]\right)}{2 h} = 0,
$$

so there is $h_n$ such that

$$
\frac {m ^ {*} \left(\mathrm {B} _ {n} \cap [ x _ {0} - h , x _ {0} + h ]\right)}{2 h} \leq \frac {1}{n}
$$

for $0 < h \leq h_n$ . Now if $\mathbf{C}_n = [a, b] \setminus \mathbf{B}_n$ , then $\mathbf{C}_n \supset [a, b] \setminus \mathbf{G}_n = \mathbf{H}_n$ and $m^*(\mathbf{C}_n) \geq m(\mathbf{H}_n) = b - a - m(\mathbf{G}_n)$ . Moreover, for $0 < h \leq h_n$ we have

$$
\frac {m ^ {*} \left(\mathbf {C} _ {n} \cap [ x _ {0} - h , x _ {0} + h ]\right)}{2 h} \geq \frac {m \left(\mathbf {H} _ {n , h}\right)}{2 h} \geq \frac {2 h - m \left(\mathbf {G} _ {n , h}\right)}{2 h} \geq 1 - \frac {1}{n},
$$

where $\mathbf{H}_{n,h} = \mathbf{H}_n\cap [x_0 - h,x_0 + h]$ . Furthermore, observe that $h_n$ can be chosen so that $h_{n + 1} < h_n$ and $\lim_{n\to \infty}h_n = 0$ . Then we define

$$
\mathbf {A} _ {n} = \mathbf {H} _ {n, h _ {n}} \backslash \left[ x _ {0} - \frac {h _ {n + 1}}{n}, x _ {0} + \frac {h _ {n + 1}}{n} \right]
$$

and put

$$
\mathbf {A} = \bigcup_ {n = 3} ^ {\infty} \mathbf {A} _ {n} \cup \{x _ {0} \}.
$$

It follows from the above that for $h_{n+1} < h \leq h_n$ ,

$$
\begin{array}{l} \frac {m \left(\mathrm {A} \cap [ x _ {0} - h , x _ {0} + h ]\right)}{2 h} \geq \frac {m \left(\mathrm {A} _ {n} \cap [ x _ {0} - h , x _ {0} + h ]\right)}{2 h} \\ = \frac {m \left(\mathrm {H} _ {n , h}\right) - 2 ^ {\frac {h _ {n + 1}}{n}}}{2 h} \geq 1 - \frac {1}{n} - \frac {h _ {n + 1}}{n h} \\ > 1 - \frac {2}{n}, \\ \end{array}
$$

which proves that $x_0$ is a point of density for $\mathbf{A}$ . Now we show that $f_{|\mathbf{A}}$ is continuous at $x_0$ . Given $\varepsilon > 0$ , there is $n \in \mathbb{N}$ such that $\frac{1}{n} < \varepsilon$ . If $|x - x_0| < \frac{h_n}{n-1}$ and $x \in \mathbf{A}$ , then it follows from the construction of $\mathbf{A}$ that $x \notin \mathbf{A}_m$ for $m < n$ . Thus $x \in \mathbf{A}_k$ with some $k \geq n$ . Consequently, $|f(x) - f(x_0)| < 1 / k \leq 1 / n < \varepsilon$ .

Suppose now that there is a measurable set $\mathbf{A}$ such that $x_0$ is a point of density for $\mathbf{A}$ and such that the restriction of $f$ to $\mathbf{A}$ is continuous at $x_0$ . Then, given $\varepsilon > 0$ , there is a positive $h > 0$ such that

$$
\{x \in [ x _ {0} - h, x _ {0} + h ]: | f (x) - f (x _ {0}) | \geq \varepsilon \} \subset [ x _ {0} - h, x _ {0} + h ] \backslash A.
$$

Consequently,

$$
\begin{array}{l} \lim  _ {h \rightarrow 0} \frac {m ^ {*} (\{x \in \left[ x _ {0} - h , x _ {0} + h \right] : | f (x) - f \left(x _ {0}\right) | \geq \varepsilon \})}{2 h} \\ \leq 1 - \lim  _ {h \rightarrow 0} \frac {m (A \cap [ x _ {0} - h , x _ {0} + h ])}{2 h} = 0, \\ \end{array}
$$

where the last equality follows from the fact that $x_0$ is a point of density for $\mathbf{A}$ .

2.4.31. [C. Goffman, Amer. Math. Monthly 84(1977), 205-206]. Let $\mathbf{A}$ be a Cantor like set constructed in 1.7.12 with $\alpha = 1/2$ . Then $\mathbf{G} = [0,1] \backslash \mathbf{A}$ is an open and dense subset of $[0,1]$ . If $\mathbf{G} = \bigcup_{n=1}^{\infty} \mathbf{I}_n$ , where $\mathbf{I}_n$ are open and pairwise disjoint intervals, then $m(\mathbf{G}) = \sum_{n=1}^{\infty} |\mathbf{I}_n| = 1/2$ . For each $n$ , let $\mathbf{J}_n \subset \mathbf{I}_n$ be a closed interval in the center of $\mathbf{I}_n$ and such that $|\mathbf{J}_n| = |\mathbf{I}_n|^2$ . For each $n$ , define $f$ on $\mathbf{J}_n$ to be continuous, $1$ at the center, $0$ at the endpoints and always between $0$ and $1$ . If $x$ is not in $\bigcup_{n=1}^{\infty} \mathbf{J}_n$ , then we define $f(x) = 0$ . We first show that $f$ is not Riemann integrable on $[0,1]$ . Let $0 = x_0 < x_1 < \dots < x_m = 1$ be a partition of $[0,1]$ . If $(x_{k-1}, x_k) \cap \mathbf{A} \neq \emptyset$ , then the oscillation of $f$ on $[x_{k-1}, x_k]$ is $1$ . Since $m(\mathbf{A}) = 1/2$ , the sum of lengths of the intervals $[x_{k-1}, x_k]$ on which the oscillation of $f$ is $1$ exceeds $1/2$ . Consequently,

$$
\overline {{\int_ {0} ^ {1}}} f (x) d x - \underline {{\int_ {0} ^ {1}}} f (x) d x \geq \frac {1}{2}.
$$

Now we show that $f$ is approximately continuous on $[0,1]$ . By definition, $f$ is continuous on $\mathbf{G}$ . So, suppose that $x_0 \in \mathbf{A}$ and let $0 < \varepsilon < 1$ be given. It is clear that any interval $[x_0 - h, x_0 + h]$ , $h > 0$ , contains infinitely many intervals $\mathbf{I}_n$ . If $h$ is small, then only intervals $\mathbf{I}_n$ with sufficiently large $n$ can be contained in $[x_0 - h, x_0 + h]$ . Thus, for $h$ small enough,

$$
\frac {m \left(\left\{x \in [ x _ {0} - h , x _ {0} + h ] : | f (x) - f \left(x _ {0}\right) | > \varepsilon \right\}\right)}{2 h} \leq \frac {\sum^ {\prime} \left| J _ {n} \right| + r _ {1} + r _ {2}}{2 h},
$$

where $\sum'$ denotes the summation over such $n$ that $\mathbf{I}_n \subset [x_0 - h, x_0 + h]$ , and $r_1 = m(\mathbf{J}_k \cap [x_0 - h, x_0 + h])$ if $x_0 - h \in \mathbf{J}_k$ and $r_1 = 0$ otherwise, $r_2 = m(\mathbf{J}_s \cap [x_0 - h, x_0 + h])$ if $x_0 + h \in \mathbf{J}_s$ and $r_2 = 0$ otherwise. We

have

$$
\frac {r _ {1}}{2 h} \leq \frac {\left| I _ {k} \right| ^ {2}}{\left| I _ {k} \right| - \left| J _ {k} \right|} = \frac {\left| I _ {k} \right|}{1 - \left| I _ {k} \right|},
$$

and a similar estimate holds for $\frac{r_2}{2h}$ . Moreover,

$$
\frac {\sum^ {\prime} \left| \mathbf {J} _ {n} \right|}{2 h} \leq \frac {\sum^ {\prime} \left| \mathbf {J} _ {n} \right|}{\sum^ {\prime} \left| \mathbf {I} _ {n} \right|} = \frac {\sum^ {\prime} \left| \mathbf {I} _ {n} \right| ^ {2}}{\sum^ {\prime} \left| \mathbf {I} _ {n} \right|} \leq \sum^ {\prime} \frac {\left| \mathbf {I} _ {n} \right| ^ {2}}{\left| \mathbf {I} _ {n} \right|} = \sum^ {\prime} \left| \mathbf {I} _ {n} \right|.
$$

It then follows that $x_0$ is a point of approximate continuity of $f$ . Now it is enough to appeal to the results in 2.4.22 and 2.4.29.

2.4.32. Observe first that $G$ is an increasing function on $\mathbb{R}$ and $\lim_{t \to -\infty} G(t) = 0$ and $\lim_{t \to \infty} G(t) = b - a$ . For arbitrarily chosen $n \in \mathbb{N}$ and $k \in \mathbb{Z}$ , set

$$
\mathbf {I} _ {k} = \left[ \frac {k - 1}{n}, \frac {k}{n} \right] \quad \text {a n d} \quad \mathbf {A} _ {k} = \left\{x \in [ a, b ]: \frac {k - 1}{n} \leq f (x) <   \frac {k}{n} \right\}.
$$

Then $G\left(\frac{k}{n}\right) - G\left(\frac{k - 1}{n}\right) = m(A_k)$ ,

$$
\frac {k - 1}{n} m \left(\mathrm {A} _ {k}\right) \leq \int_ {\mathrm {A} _ {k}} f d m \leq \frac {k}{n} m \left(\mathrm {A} _ {k}\right),
$$

and

$$
\begin{array}{l} \frac {k - 1}{n} \left(G \left(\frac {k}{n}\right) - G \left(\frac {k - 1}{n}\right)\right) \leq \int_ {(k - 1) / n} ^ {k / n} t d (G (t)) \\ \leq \frac {k}{n} \left(G \left(\frac {k}{n}\right) - G \left(\frac {k - 1}{n}\right)\right). \\ \end{array}
$$

Consequently,

$$
\left| \int_ {A _ {k}} f d m - \int_ {(k - 1) / n} ^ {k / n} t d (G (t)) \right| \leq \frac {1}{n} \left(G \left(\frac {k}{n}\right) - G \left(\frac {k - 1}{n}\right)\right).
$$

Since

$$
\sum_ {k = 1} ^ {\infty} \frac {1}{n} \left(G \left(\frac {k}{n}\right) - G \left(\frac {k - 1}{n}\right)\right) = \frac {1}{n} (b - a - G (0))
$$

and $\sum_{k=1}^{\infty} \int_{A_k} f dm = \int_a^b f^+(x) dx < \infty$ , we see that $\sum_{k=1}^{\infty} \int_{(k-1)/n}^{k/n} td(G(t))$ converges, which means that the integral $\int_0^\infty td(G(t))$ converges and

we have

$$
\left| \int_ {0} ^ {\infty} t d (G (t)) - \int_ {a} ^ {b} f ^ {+} (x) d x \right| \leq \frac {1}{n} (b - a - G (0)).
$$

Passage to the limit as $n \to \infty$ shows that

$$
\int_ {0} ^ {\infty} t d (G (t)) = \int_ {a} ^ {b} f ^ {+} (x) d x.
$$

In a completely similar manner one can show that

$$
\int_ {- \infty} ^ {0} t d (G (t)) = \int_ {a} ^ {b} f ^ {-} (x) d x.
$$

# 2.5. Fourier Series

2.5.1. If $\rho_{n} = \sqrt{a_{n}^{2} + b_{n}^{2}}\neq 0$ , then

$$
a _ {n} \cos n x + b _ {n} \sin n x = \rho_ {n} \left(\frac {a _ {n}}{\rho_ {n}} \cos n x + \frac {b _ {n}}{\rho_ {n}} \sin n x\right),
$$

and it suffices to take $\alpha_{n}$ such that $\sin \alpha_{n} = \frac{a_{n}}{\rho_{n}}$ and $\cos \alpha_{n} = \frac{b_{n}}{\rho_{n}}$ .

2.5.2. It follows from 2.3.27 that, given $\varepsilon >0$ , there is a continuous function $g$ on $[- \pi ,\pi ]$ such that

$$
\int_ {- \pi} ^ {\pi} | f (x) - g (x) | d x <   \frac {\varepsilon}{2}.
$$

Since, by 1.4.11,

$$
\lim  _ {n \rightarrow \infty} \int_ {- \pi} ^ {\pi} g (x) \cos n x d x = \lim  _ {n \rightarrow \infty} \int_ {- \pi} ^ {\pi} g (x) \sin n x d x = 0,
$$

we get

$$
\begin{array}{l} \left| \int_ {- \pi} ^ {\pi} f (x) \cos n x d x \right| \leq \int_ {- \pi} ^ {\pi} | f (x) - g (x) | d x + \left| \int_ {- \pi} ^ {\pi} g (x) \cos n x d x \right| \\ \leq \frac {\varepsilon}{2} + \frac {\varepsilon}{2} = \varepsilon \\ \end{array}
$$

for sufficiently large $n$ .

2.5.3. Substituting $x = t + \pi / n$ , we get

$$
\begin{array}{l} a _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos n x d x = - \frac {1}{\pi} \int_ {- \pi - \frac {\pi}{n}} ^ {\pi - \frac {\pi}{n}} f \left(t + \frac {\pi}{n}\right) \cos n t d t \\ = - \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (t + \frac {\pi}{n}) \cos n t d t, \\ \end{array}
$$

where the last equality follows from the periodicity of the integrand. Hence

$$
a _ {n} = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \left(\tilde {f} (x) - f \left(t + \frac {\pi}{n}\right)\right) \cos n x d x = O \left(n ^ {- a}\right).
$$

2.5.4. We first observe that since $f$ is of bounded variation on $[-\pi, \pi]$ , it is Riemann (and so Lebesgue) integrable on that interval. Moreover, $f$ can be represented as a difference of two nonnegative increasing functions, say, $f = f_1 - f_2$ . By the Bonnet form of the second mean value theorem (see, e.g., 1.3.17(a)),

$$
\int_ {- \pi} ^ {\pi} f _ {1} (x) \cos n x d x = f _ {1} (\pi) \int_ {c} ^ {\pi} \cos n x d x = - f _ {1} (\pi) \frac {\sin n c}{n} = O (n ^ {- 1}).
$$

2.5.5. Since $f$ is absolutely continuous on $[-\pi, \pi]$ , there exists $g \in L^{1}[-\pi, \pi]$ such that

$$
f (x) = f (- \pi) + \int_ {- \pi} ^ {x} g (t) d t
$$

(see Theorem 2 stated at the beginning of Section 2.4). Thus integration by parts (2.4.14 or 2.4.15) gives

$$
\begin{array}{l} a _ {n} = \frac {1}{\pi} \left(f (x) \frac {\sin n x}{n} \Big | _ {- \pi} ^ {\pi} - \frac {1}{n} \int_ {- \pi} ^ {\pi} g (x) \sin n x d x\right) \\ = - \frac {1}{n \pi} \int_ {- \pi} ^ {\pi} g (x) \sin n x d x. \\ \end{array}
$$

Now it suffices to apply the result in 2.5.2 to see that $a_{n} = o(n^{-1})$ . Likewise, $b_{n} = o(n^{-1})$ .

2.5.6. Integrating $k$ times by parts, we see that the Fourier coefficients of $f$ are equal to

$$
\pm \frac {1}{\pi n ^ {k}} \int_ {- \pi} ^ {\pi} f ^ {(k)} (x) \cos n x d x \quad \text {o r} \quad \pm \frac {1}{\pi n ^ {k}} \int_ {- \pi} ^ {\pi} f ^ {(k)} (x) \sin n x d x.
$$

Since $f^{(k)}$ is continuous on $[-\pi, \pi]$ , by the result in 1.4.11,

$$
\lim  _ {n \rightarrow \infty} \int_ {- \pi} ^ {\pi} f ^ {(k)} (x) \sin n x d x = \lim  _ {n \rightarrow \infty} \int_ {- \pi} ^ {\pi} f ^ {(k)} (x) \cos n x d x = 0.
$$

2.5.7. We have

$$
\begin{array}{l} s _ {n} (x) = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} f (t) d t + \sum_ {k = 1} ^ {n} \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (t) (\cos k t \cos k x + \sin k t \sin k x) d t \\ = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (t) \left(\frac {1}{2} + \sum_ {k = 1} ^ {n} \cos k (t - x)\right) d t \\ = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (t) \frac {\sin \left(n + \frac {1}{2}\right) (t - x)}{2 \sin \frac {1}{2} (t - x)} d t, \\ \end{array}
$$

where the last equality follows from the well known trigonometric identity

$$
\frac {1}{2} + \sum_ {k = 1} ^ {n} \cos k \alpha = \frac {\sin \left(n + \frac {1}{2}\right) \alpha}{2 \sin \frac {1}{2} \alpha}, \quad \alpha \neq 2 m \pi , m \in \mathbb {Z}.
$$

2.5.8. As in the solution to 1.4.8, one can show that if $f$ is periodic with period $2\pi$ and integrable on $[-\pi, \pi]$ , then for any real $x$ ,

$$
\int_ {- \pi + x} ^ {\pi + x} f (t) d t = \int_ {- \pi} ^ {\pi} f (t) d t.
$$

Thus, using the formula proved in 2.5.7, we get

$$
\begin{array}{l} s _ {n} (x) = \frac {1}{\pi} \int_ {- \pi + x} ^ {\pi + x} f (t) \frac {\sin \left(n + \frac {1}{2}\right) (t - x)}{2 \sin \frac {1}{2} (t - x)} d t \\ = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (t + x) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t, \\ \end{array}
$$

where the last equality follows from the change of variable formula for Lebesgue integrals (e.g., 2.4.13). Hence

$$
\begin{array}{l} s _ {n} (x) = \frac {1}{\pi} \int_ {- \pi} ^ {0} f (t + x) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t + \frac {1}{\pi} \int_ {0} ^ {\pi} f (t + x) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t \\ = \frac {1}{\pi} \int_ {0} ^ {\pi} f (x - t) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t + \frac {1}{\pi} \int_ {0} ^ {\pi} f (t + x) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t. \\ \end{array}
$$

2.5.9. Our aim is to show that $\lim_{n\to \infty}s_n(x_0) = f(x_0)$ , where $\{s_n(x_0)\}$ is the sequence of partial sums of the Fourier series of $f$ at $x_0$ . Applying the formula for $s_n(x)$ derived in the preceding problem to $f(x)\equiv 1$ , we get

$$
1 = \frac {2}{\pi} \int_ {0} ^ {\pi} \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t.
$$

Hence

$$
\begin{array}{l} s _ {n} \left(x _ {0}\right) - f \left(x _ {0}\right) \\ - \frac {1}{\pi} \int_ {0} ^ {\pi} (f (x _ {0} + t) + f (x _ {0} - t) - 2 f (x _ {0})) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t. \\ \end{array}
$$

Setting $\varphi(t) = f(x_0 + t) + f(x_0 - t) - 2f(x_0)$ , we have $|\varphi(t)| \leq 2L|t|^{\alpha}$ for $|t| < \delta$ . We now note that $\varphi(t)/t$ is integrable on $[0, \pi]$ . Indeed,

$$
\int_ {0} ^ {\delta} \frac {| \varphi (t) |}{t} d t \leq \int_ {0} ^ {\delta} 2 L t ^ {\alpha - 1} d t <   \infty .
$$

Thus the function

$$
\frac {| \varphi (t) |}{\sin \frac {1}{2} t} = \frac {| \varphi (t) |}{t} \cdot \frac {t}{\sin \frac {1}{2} t}
$$

is also integrable on $[0,\pi ]$ . It follows from the solution to 2.5.2 that

$$
\lim  _ {n \rightarrow \infty} (s _ {n} (x _ {0}) - f (x _ {0})) = \lim  _ {n \rightarrow \infty} \frac {1}{\pi} \int_ {0} ^ {\pi} \varphi (t) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t = 0.
$$

2.5.10. We first prove the following fact.

Lemma 1. If $g$ is monotonically increasing on $[0, a]$ , then

$$
\lim  _ {n \rightarrow \infty} \int_ {0} ^ {\alpha} g (x) \frac {\sin n x}{x} d x = \frac {\pi}{2} g (0 ^ {+}).
$$

We have

$$
\int_ {0} ^ {a} g (x) \frac {\sin n x}{x} d x = g \left(0 ^ {+}\right) \int_ {0} ^ {a} \frac {\sin n x}{x} d x + \int_ {0} ^ {a} \left(g (x) - g \left(0 ^ {+}\right)\right) \frac {\sin n x}{x} d x.
$$

Substituting $nx = t$ and using the result in 1.5.33, we obtain

$$
g (0 ^ {+}) \int_ {0} ^ {a} \frac {\sin n x}{x} d x = g (0 ^ {+}) \int_ {0} ^ {n a} \frac {\sin t}{t} d t \xrightarrow [ n \to \infty ]{} g (0 ^ {+}) \frac {\pi}{2}.
$$

Moreover, given $\varepsilon > 0$ , there is $\delta > 0$ such that $0 \leq g(x) - g(0^{+}) < \varepsilon$ for $0 < x \leq \delta$ . Now we write

$$
\begin{array}{l} \int_ {0} ^ {a} (g (x) - g (0 ^ {+})) \frac {\sin n x}{x} d x = \int_ {0} ^ {\delta} (g (x) - g (0 ^ {+})) \frac {\sin n x}{x} d x \\ + \int_ {\delta} ^ {a} (g (x) - g (0 ^ {+})) \frac {\sin n x}{x} d x \\ = I _ {1} + I _ {2}. \\ \end{array}
$$

Using the Bonnet form of the second mean value theorem given in 1.3.17(a), we get

$$
I _ {1} = \left(g (\delta) - g (0 ^ {+})\right) \int_ {c} ^ {\delta} \frac {\sin n x}{x} d x = \left(g (\delta) - g (0 ^ {+})\right) \int_ {n c} ^ {n \delta} \frac {\sin x}{x} d x
$$

with some $c \in [0, \delta]$ . Since $\int_0^\infty \frac{\sin x}{x} dx = \pi / 2$ , the function $z \mapsto \int_0^z \frac{\sin x}{x} dx$ is bounded. Consequently, there is $M > 0$ such that $\left| \int_{nc}^{n\delta} \frac{\sin x}{x} dx \right| \leq M$ . So, $|I_1| < M\varepsilon$ . Finally, by 1.3.18, $I_2$ tends to zero as $n \to \infty$ , which ends the proof of the lemma.

We now turn to the proof of the Dirichlet-Jordan test. We have

$$
\begin{array}{l} s _ {n} \left(x _ {0}\right) = \frac {1}{\pi} \int_ {0} ^ {\delta} \left(f \left(x _ {0} + t\right) + f \left(x _ {0} - t\right)\right) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t \\ + \frac {1}{\pi} \int_ {\delta} ^ {\pi} (f (x _ {0} + t) + f (x _ {0} - t)) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t \\ = J _ {1} + J _ {2}. \\ \end{array}
$$

Since the function

$$
t \mapsto \frac {f \left(x _ {0} + t\right) + f \left(x _ {0} - t\right)}{2 \sin \frac {1}{2} t}
$$

is integrable on $[\delta, \pi]$ , one can show, as in the solution to 2.5.2, that $J_{2}$ tends to zero as $n \to \infty$ . Furthermore $J_{1}$ can be rewritten as

$$
J _ {1} = \frac {1}{\pi} \int_ {0} ^ {\delta} (f (x _ {0} + t) + f (x _ {0} - t)) \frac {\frac {1}{2} t}{\sin \frac {1}{2} t} \frac {\sin \left(n + \frac {1}{2}\right) t}{t} d t.
$$

Since $t \mapsto \frac{\frac{1}{2}t}{\sin\frac{1}{2}t}$ is an increasing function on $[0, \delta]$ , the function $t \mapsto (f(x_0 + t) + f(x_0 - t)) \frac{\frac{1}{2}t}{\sin\frac{1}{2}t}$ is of bounded variation on $[0, \delta]$ ,

and therefore it is a difference of two monotonically increasing functions. Applying the lemma to these functions, we obtain the desired result.

2.5.11. Consider the function given by

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{\ln (| x | / 2 \pi)} & \text {i f} x \in [ - \pi , \pi ] \setminus \{0 \}, \\ 0 & \text {i f} x = 0. \end{array} \right.
$$

Then $f$ is of bounded variation on $[-\pi, \pi]$ but does not satisfy any Lipschitz condition (see 1.2.13). On the other hand, the function given by

$$
g (x) = \left\{ \begin{array}{l l} x \cos \frac {\pi}{2 x} & \text {i f} \quad x \in [ - \pi , \pi ] \setminus \{0 \}, \\ 0 & \text {i f} \quad x = 0 \end{array} \right.
$$

satisfies the Lipschitz condition at zero, that is, $|g(x) - g(0)| \leq |x|$ , but $g$ is not of bounded variation on any neighborhood of zero (see 1.2.5).

2.5.12. Set $f(x) = \frac{\pi - x}{2}$ for $x \in (0, 2\pi)$ , $f(0) = 0$ , and extend this function onto $\mathbb{R}$ periodically with period $2\pi$ . Then by the Dirichlet-Jordan test, the Fourier series of $f$ converges to $f$ . Since

$$
a _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \frac {\pi - x}{2} \cos n x d x = 0 \quad \text {f o r} n = 0, 1, 2, \dots
$$

and

$$
b _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \frac {\pi - x}{2} \sin n x d x = \frac {1}{n} \quad \text {f o r} n = 1, 2, \dots ,
$$

we get

$$
\frac {\pi - x}{2} = \sum_ {n = k} ^ {\infty} \frac {\sin n x}{n}, \quad 0 <   x <   2 \pi .
$$

Replacing $x$ by $2x$ , we see that

$$
\frac {\pi - 2 x}{4} = \sum_ {n = 1} ^ {\infty} \frac {\sin 2 n x}{2 n}, \quad 0 <   x <   \pi .
$$

Hence

$$
\frac {\pi}{4} = \sum_ {n = 1} ^ {\infty} \frac {\sin (2 n - 1) x}{2 n - 1}, \quad 0 <   x <   \pi .
$$

Now if we substitute subsequently $x = \pi / 2$ and $x = \pi / 3$ , we obtain the last two equalities.

2.5.13. If $f(x) = \sum_{n=1}^{\infty} \frac{\cos nx}{n^2}$ , then by the result in the previous problem, $f'(x) = -\frac{\pi - x}{2}$ . Since $f(0) = \frac{\pi^2}{6}$ , we see that $f(x) = \frac{\pi^2}{6} - \frac{\pi x}{2} + \frac{x^2}{4}$ . Likewise, if we put

$$
g (x) = \sum_ {n = 1} ^ {\infty} \frac {\sin n x}{n ^ {3}},
$$

then $g''(x) = -\frac{\pi - x}{2}$ and $g'(0) = \frac{\pi^2}{6}$ . Hence $g(x) = \frac{x^3}{12} - \frac{\pi x^2}{4} + \frac{\pi^2 x}{6}$ .

2.5.14. The function $f$ defined in the solution to 2.5.12 is of bounded variation on $[-\pi, \pi]$ , but $b_n = 1/n$ is not $o(n^{-1})$ .

2.5.15. We have

$$
s _ {n} ^ {\prime} (x) = \sum_ {k = 1} ^ {n} \cos k x = \frac {\cos \frac {(n + 1) x}{2} \sin \frac {n x}{2}}{\sin \frac {x}{2}}.
$$

Thus $x_{n} = \frac{\pi}{n + 1}$ and

$$
s _ {n} \left(\frac {\pi}{n + 1}\right) = \sum_ {k = 1} ^ {n} \frac {\sin \frac {k \pi}{n + 1}}{\frac {k \pi}{n + 1}} \frac {\pi}{n + 1} \xrightarrow [ n \to \infty ]{} \int_ {0} ^ {\pi} \frac {\sin x}{x} d x.
$$

We note here that by the Dirichlet-Jordan test, $\lim_{n\to \infty}s_n(x) = f(x)$ for $x\in (0,2\pi)$ and $\lim_{n\to \infty}s_n(0) = 0 = \lim_{n\to \infty}s_n(2\pi)$ , but by the above the convergence of $\{s_n\}$ cannot be uniform on $[0,2\pi]$ .

2.5.16. We set $f(x) = e^{ax}$ for $0 < x < 2\pi$ , $f(0) = \frac{1 + e^{2\pi a}}{2}$ , and extend $f$ so that it is $2\pi$ -periodic. Applying the Dirichlet-Jordan test, we see that the Fourier series of $f$ converges to $f$ on $\mathbb{R}$ , and the first formula is obtained by a simple calculation. To get the second equality we reflect the graph of the function $x \mapsto e^{ax}$ , $x \in [0,\pi]$ , about the $y$ -axis and get the even function $g$ defined on $[-\pi,\pi]$ . If we reflect the graph of the function $x \mapsto e^{ax}$ , $x \in (0,\pi)$ , through the origin, we get the odd function $h$ on $(-\pi,0) \cup (0,\pi)$ . Moreover, we set $h(0) = h(-\pi) = h(\pi) = 0$ and get the last equality. We have also

$$
\begin{array}{l} f (0) = \frac {1 + e ^ {2 a \pi}}{2} = \frac {e ^ {2 a \pi} - 1}{\pi} \left(\frac {1}{2 a} + \sum_ {n = 1} ^ {\infty} \frac {a}{a ^ {2} + n ^ {2}}\right), \\ g (0) = 1 = \frac {e ^ {a \pi} - 1}{a \pi} + \frac {2}{\pi} \sum_ {n = 1} ^ {\infty} ((- 1) ^ {n} e ^ {a \pi} - 1) \frac {a}{a ^ {2} + n ^ {2}}. \\ \end{array}
$$

2.5.17. Using the first equality in 2.5.16, we get

$$
\frac {\pi}{e ^ {2 \pi a} - 1} e ^ {a x} + \frac {\pi}{e ^ {- 2 \pi a} - 1} e ^ {- a x} = - 2 \sum_ {n = 1} ^ {\infty} \frac {n \sin n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   2 \pi .
$$

This can be rewritten as

$$
\frac {\pi}{2} \cdot \frac {\sinh a (\pi - x)}{\sinh \pi a} = \sum_ {n = 1} ^ {\infty} \frac {n \sin n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   2 \pi .
$$

Likewise,

$$
\frac {\pi}{e ^ {2 \pi a} - 1} e ^ {a x} - \frac {\pi}{e ^ {- 2 \pi a} - 1} e ^ {- a x} = \frac {1}{a} + 2 \sum_ {n = 1} ^ {\infty} \frac {a \cos n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   2 \pi ,
$$

or equivalently,

$$
\frac {\pi}{2} \cdot \frac {\cosh a (\pi - x)}{\sinh \pi a} - \frac {1}{2 a} = \sum_ {n = 1} ^ {\infty} \frac {a \cos n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   2 \pi .
$$

2.5.18. We extend the function $f(x) = x^2, -\pi \leq x \leq \pi$ , onto $\mathbb{R}$ so that $f$ is $2\pi$ -periodic. Hence such a function satisfies the Dirichlet-Jordan test at any $x \in \mathbb{R}$ , and we easily arrive at

$$
x ^ {2} = \frac {\pi^ {2}}{3} + 4 \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} \frac {\cos n x}{n ^ {3}}, - \pi \leq x \leq \pi .
$$

Substituting $x = \pi$ and $x = 0$ gives the other equalities.

2.5.19. (a) We have

$$
\begin{array}{l} a _ {2 n - 1} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) \cos (2 n - 1) x d x \\ = \frac {1}{\pi} \int_ {- \pi} ^ {0} f (x + \pi) \cos (2 n - 1) x d x + \frac {1}{\pi} \int_ {0} ^ {\pi} f (x) \cos (2 n - 1) x d x \\ = - \frac {1}{\pi} \int_ {0} ^ {\pi} f (t) \cos (2 n - 1) t d t + \frac {1}{\pi} \int_ {0} ^ {\pi} f (x) \cos (2 n - 1) x d x = 0. \\ \end{array}
$$

Likewise, $b_{2n-1} = 0$ .

(b) The proof is analogous to that in (a).

2.5.20. We reflect the graph of $x \mapsto \cos x, 0 < x < \pi$ , through the origin and get an odd function $f$ on $(-\pi, \pi) \setminus \{0\}$ . Thus the Fourier series of $f$ is reduced to a sine series. Moreover, since $f(x + \pi) = f(x)$ for $x \in (-\pi, 0)$ , by (a) in the preceding problem, $b_{2n-1} = 0$ . A simple

calculation gives $b_{2n} = \frac{8n}{\pi(4n^2 - 1)}$ . To get the other formula, we reflect the graph of $x \mapsto \sin x, 0 \leq x < \pi$ , about the $y$ -axis and get an even function $g$ on $(-\pi, \pi)$ . The Fourier series of $g$ reduces to a cosine series, and by (a) in the previous problem $a_{2n - 1} = 0$ .

2.5.21. The function $f(x) = \ln \left| 2\sin \frac{x}{2} \right|, x \neq 2k\pi$ , is $2\pi$ -periodic and even. By 1.5.1(b), $\int_0^{\pi / 2} \ln \sin t dt = -\frac{\pi}{2} \ln 2$ , and consequently, $a_0 = 0$ . Moreover,

$$
\begin{array}{l} a _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} \ln \left(2 \sin \frac {x}{2}\right) \cos n x d x = \frac {2}{\pi} \ln \left(2 \sin \frac {x}{2}\right) \frac {\sin n x}{n} \Bigg | _ {0} ^ {\pi} \\ - \frac {1}{n \pi} \int_ {0} ^ {\pi} \frac {\sin n x \cos \frac {x}{2}}{\sin \frac {x}{2}} d x = - \frac {1}{n \pi} \int_ {0} ^ {\pi} \frac {\sin n x \cos \frac {x}{2}}{\sin \frac {x}{2}} d x. \\ \end{array}
$$

Since

$$
\begin{array}{l} \frac {\sin n x \cos \frac {x}{2}}{\sin \frac {x}{2}} = \frac {\sin (n + \frac {1}{2}) x}{2 \sin \frac {x}{2}} + \frac {\sin (n - \frac {1}{2}) x}{2 \sin \frac {x}{2}} \\ = \frac {1}{2} + \sum_ {k = 1} ^ {n} \cos k x + \frac {1}{2} + \sum_ {k = 1} ^ {n - 1} \cos k x, \\ \end{array}
$$

we get $a_n = -\frac{1}{n}$ . Similar reasoning can be applied to get the other formula.

2.5.22. By the periodicity, $f$ is integrable on $[0, 2\pi]$ . So, the function $F(x) = \int_{0}^{x} (f(t) - \frac{1}{2} a_0) dt$ is of bounded variation on $[0, 2\pi]$ . Moreover, $F(0) = F(2\pi) = 0$ and $F$ is $2\pi$ -periodic. Thus by the Dirichlet-Jordan test,

$$
F (x) = \frac {1}{2} A _ {0} + \sum_ {n = 1} ^ {\infty} \left(A _ {n} \cos n x + B _ {n} \sin n x\right),
$$

where, for $n = 1,2,\ldots$

$$
A _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} F (x) \cos n x d x = \frac {- 1}{n \pi} \int_ {- \pi} ^ {\pi} \left(f (x) - \frac {1}{2} a _ {0}\right) \sin n x d x = \frac {- b _ {n}}{n}
$$

and

$$
B _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} F (x) \sin n x d x = \frac {1}{n \pi} \int_ {- \pi} ^ {\pi} \left(f (x) - \frac {1}{2} a _ {0}\right) \cos n x d x = \frac {a _ {n}}{n}.
$$

Consequently,

$$
F (x) = \frac {1}{2} A _ {0} + \sum_ {n = 1} ^ {\infty} \frac {a _ {n} \sin n x - b _ {n} \cos n x}{n}.
$$

Putting $x = 0$ , we get

$$
\frac {1}{2} A _ {0} = \sum_ {n = 1} ^ {\infty} \frac {b _ {n}}{n}, \tag {1}
$$

which implies the desired formula.

2.5.23. The convergence of the series $\sum_{n=1}^{\infty} \frac{b_n}{n}$ follows immediately from (1) in the solution to the preceding problem. We now note that the series $\sum_{n=2}^{\infty} \frac{\sin nx}{\ln n}$ converges by the Dirichlet test (see, e.g., II, 3.2.13), but since the series $\sum_{n=2}^{\infty} \frac{1}{n \ln n}$ diverges, $\sum_{n=2}^{\infty} \frac{\sin nx}{\ln n}$ is not a Fourier series of any integrable function.

2.5.24. We have

$$
\int_ {- \pi} ^ {\pi} (f (x) - s _ {n} (x)) ^ {2} d x = \int_ {- \pi} ^ {\pi} f ^ {2} (x) d x - \pi \left(\frac {1}{2} a _ {0} ^ {2} + \sum_ {k = 1} ^ {n} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right)\right),
$$

because

$$
\int_ {- \pi} ^ {\pi} f (x) s _ {n} (x) d x = \int_ {- \pi} ^ {\pi} \left(s _ {n} (x)\right) ^ {2} d x - \pi \left(\frac {1}{2} a _ {0} ^ {2} + \sum_ {k = 1} ^ {n} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right)\right).
$$

Since $\int_{-\pi}^{\pi}(f(x) - s_n(x))^2 dx \geq 0$ , the series $\frac{1}{2} a_0^2 + \sum_{n=1}^{\infty}\left(a_n^2 + b_n^2\right)$ converges and its sum does not exceed $\frac{1}{\pi}\int_{-\pi}^{\pi}f^2(x)dx$ .

2.5.25. It follows from the solution of the last problem that there is a positive constant $C$ such that $\int_{-\pi}^{\pi}(f(x) - s_n(x))^2 dx \leq C$ . By the Schwarz inequality, for any measurable $B \subset [-\pi, \pi]$ ,

$$
\left| \int_ {\mathbf {B}} (f (x) - s _ {n} (x)) d x \right| \leq \sqrt {C} \sqrt {m (\mathbf {B})}. \tag {1}
$$

Without loss of generality we can assume that $\mathbf{A} \subset (-\pi, \pi)$ . Given $\varepsilon > 0$ , there is an open set $\mathbf{G}$ , such that $(- \pi, \pi) \supset \mathbf{G} \supset \mathbf{A}$ and $m(\mathbf{G} \setminus \mathbf{A}) < \varepsilon$ . Moreover, $\mathbf{G}$ is a union of countably many open pairwise disjoint intervals $(a_i, b_i)$ . We have

$$
\int_ {A} (f (x) - s _ {n} (x)) d x = \int_ {G} (f (x) - s _ {n} (x)) d x - \int_ {G \backslash A} (f (x) - s _ {n} (x)) d x.
$$

Furthermore, there is a positive integer $N$ such that

$$
m \left(\mathbf {G} \backslash \bigcup_ {n = 1} ^ {N} \left(a _ {n}, b _ {n}\right)\right) <   \varepsilon .
$$

If we set $\mathbf{G}_N = \bigcup_{n=1}^N (a_n, b_n)$ , then

$$
\int_ {\mathbf {G}} (f (x) - s _ {n} (x)) d x = \int_ {\mathbf {G} _ {N}} (f (x) - s _ {n} (x)) d x + \int_ {\mathbf {G} \backslash \mathbf {G} _ {N}} (f (x) - s _ {n} (x)) d x.
$$

It then follows from (1) that

$$
\left| \int_ {A} (f (x) - s _ {n} (x)) d x \right| \leq \left| \int_ {C _ {N}} (f (x) - s _ {n} (x)) d x \right| + 2 \sqrt {\varepsilon C}.
$$

Now we extend $f$ onto $\mathbb{R}$ periodically by putting $f(x + 2\pi) = f(x)$ and use the result in 2.5.22 to show that $\lim_{n \to \infty} \int_{a_i}^{\beta_i}(f(x) - s_n(x)) dx = 0$ for any $(\alpha_i, \beta_i) \subset [0, 2\pi]$ . Next, by the periodicity of the extended function $f$ we get $\lim_{n \to \infty} \int_{a_i}^{b_i}(f(x) - s_n(x)) dx = 0$ for any $(a_i, b_i) \subset [-\pi, \pi]$ . Thus $\lim_{n \to \infty} \int_{\mathbb{G}_N}(f(x) - s_n(x)) dx = 0$ , and the desired result follows.

2.5.26. By 2.3.25, given $\varepsilon >0$ , there is a simple function $\varphi$ such that

$$
\int_ {- \pi} ^ {\pi} (g (x) - \varphi (x)) ^ {2} d x <   \varepsilon .
$$

By the result in the previous problem,

$$
\lim  _ {n \rightarrow \infty} \int_ {- \pi} ^ {\pi} \varphi (x) (f (x) - s _ {n} (x)) d x = 0.
$$

Consequently,

$$
\begin{array}{l} \int_ {- \pi} ^ {\pi} g (x) (f (x) - s _ {n} (x)) d x = \int_ {- \pi} ^ {\pi} (g (x) - \varphi (x)) (f (x) - s _ {n} (x)) d x \\ \left| \int_ {- \pi} ^ {\pi} \varphi (x) (f (x) \quad s _ {n} (x)) d x \right. \\ <   \sqrt {\varepsilon} \left(\int_ {- \pi} ^ {\pi} (f (x) - s _ {n} (x)) ^ {2} d x\right) ^ {1 / 2} \\ + \int_ {- \pi} ^ {\pi} \varphi (x) (f (x) - s _ {n} (x)) d x. \\ \end{array}
$$

It follows from the solution of 2.5.25 that there is a constant $C$ such that $\int_{-\pi}^{\pi}(f(x) - s_n(x))^2 dx \leq C$ , which implies the desired result.

2.5.27. By the result in the preceding problem,

$$
\begin{array}{l} \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) g (x) d x = \lim  _ {n \rightarrow \infty} \frac {1}{\pi} \int_ {- \pi} ^ {\pi} s _ {n} (x) g (x) d x \\ = \lim  _ {n \rightarrow \infty} \left(\frac {1}{2} a _ {0} \alpha_ {0} + \sum_ {k = 1} ^ {n} \left(a _ {k} \alpha_ {k} + b _ {k} \beta_ {k}\right)\right). \\ \end{array}
$$

It is worth noting here that, in particular, if $f = g$ , we get the so-called Parseval formula:

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} f ^ {2} (x) d x = \frac {1}{2} a _ {0} ^ {2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right).
$$

2.5.28. The result follows immediately from 2.5.12 and from the identity proved in the preceding problem.

2.5.29. It follows from the result in 2.5.25 that for any measurable set $\mathbf{A} \subset [-\pi, \pi]$ ,

$$
\int_ {\Lambda} f (x) d x = \int_ {\Lambda} g (x) d x.
$$

Now it suffices to appeal to 2.3.7.

2.5.30. (a) By 2.5.18,

$$
\frac {2}{9} \pi^ {4} + 1 6 \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {4}} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} x ^ {4} d x = \frac {2}{5} \pi^ {4}.
$$

Hence $\sum_{n=1}^{\infty} \frac{1}{n^4} = \frac{\pi^4}{90}$ . Moreover, by 2.5.17,

$$
\frac {\pi}{2} \cdot \frac {\cosh a (\pi - x)}{\sinh \pi a} = \frac {1}{2 a} + \sum_ {n = 1} ^ {\infty} \frac {a \cos n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   2 \pi ,
$$

and

$$
\frac {\pi}{2} \cdot \frac {\sinh a (\pi - x)}{\sinh \pi a} = \sum_ {n = 1} ^ {\infty} \frac {n \sin n x}{a ^ {2} + n ^ {2}}, \quad 0 <   x <   2 \pi .
$$

Consequently,

$$
\begin{array}{l} \frac {1}{2 a ^ {2}} + \sum_ {n = 1} ^ {\infty} \frac {a ^ {2}}{(a ^ {2} + n ^ {2}) ^ {2}} = \frac {\pi}{4 \sinh^ {2} \pi a} \int_ {0} ^ {2 \pi} \cosh^ {2} a (\pi - x) d x \\ = \frac {\pi \cosh a \pi}{4 a \sinh a \pi} + \frac {\pi^ {2}}{4 \sinh^ {2} a \pi} \\ \end{array}
$$

and

$$
\sum_ {n = 1} ^ {\infty} \frac {n ^ {2}}{(a ^ {2} + n ^ {2}) ^ {2}} = \frac {\pi \cosh a \pi}{4 a \sinh a \pi} - \frac {\pi^ {2}}{4 \sinh^ {2} a \pi}.
$$

(b) Since

$$
\cos^ {3} x = \frac {3 \cos x}{4} + \frac {\cos 3 x}{4},
$$

we get

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} \cos^ {6} x d x = \frac {9}{1 6} + \frac {1}{1 6} = \frac {5}{8}.
$$

Likewise,

$$
\cos^ {4} x = \frac {3}{8} + \frac {\cos 2 x}{2} + \frac {\cos 4 x}{8},
$$

and, consequently,

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} \cos^ {8} x d x = \frac {9}{3 2} + \frac {1}{4} + \frac {1}{6 4} = \frac {3 5}{6 4}.
$$

2.5.31. By the Schwarz inequality and the Parseval formula,

$$
\sum_ {n = 1} ^ {\infty} \frac {| a _ {n} |}{n} \leq \left(\sum_ {n = 1} ^ {\infty} a _ {n} ^ {2}\right) ^ {1 / 2} \left(\sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}}\right) ^ {1 / 2} <   \infty .
$$

2.5.32. Integrating by parts gives

$$
a _ {m} = - \frac {1}{m} b _ {m} ^ {\prime} \quad \text {a n d} \quad b _ {m} = \frac {1}{m} a _ {m} ^ {\prime}, \quad m = 1, 2, \dots ,
$$

where $a_{m}^{\prime}$ and $b_{m}^{\prime}$ are the Fourier coefficients of $f^{\prime}$ . Moreover, since $f^{\prime}$ is continuous on $[-\pi, \pi]$ , $f^{\prime} \in L^{2}[-\pi, \pi]$ . So by the result in 2.5.27, the series $\sum_{n=1}^{\infty} ((a_{n}^{\prime})^{2} + (b_{n}^{\prime})^{2})$ converges. It then follows by the Schwarz

inequality that

$$
\begin{array}{l} \max  _ {x \in \mathbb {R}} | f (x) - s _ {n} (x) | = \max  _ {x \in \mathbb {R}} \left| \sum_ {m = n + 1} ^ {\infty} a _ {m} \cos m x + b _ {m} \sin m x \right| \\ \leq \sum_ {m = n + 1} ^ {\infty} \frac {\left| a _ {m} ^ {\prime} \right| + \left| b _ {m} ^ {\prime} \right|}{m} \\ \leq \left(\sum_ {m = n + 1} ^ {\infty} \frac {1}{m ^ {2}}\right) ^ {\frac {1}{2}} \left(\sum_ {m = n + 1} ^ {\infty} 2 \left(| a _ {m} ^ {\prime} | ^ {2} + | b _ {m} ^ {\prime} | ^ {2}\right)\right) ^ {\frac {1}{2}} \\ = \left(\sum_ {m = n + 1} ^ {\infty} \frac {1}{m ^ {2}}\right) ^ {\frac {1}{2}} o (1) \leq \frac {1}{\sqrt {n}} o (1). \\ \end{array}
$$

2.5.33. If $f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$ , then

(1) $f(x + h) - f(x - h)\sim 2\sum_{n = 1}^{\infty}\sin nh(b_n\cos nx - a_n\sin nx).$

By the Parseval formula,

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} (f (x + h) - f (x - h)) ^ {2} d x = 4 \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} n h.
$$

By assumption,

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} (f (x + h) - f (x - h)) ^ {2} d x \leq 2 L ^ {2} (2 h) ^ {2 \alpha}.
$$

Taking $h = \frac{\pi}{2^{k + 1}}$ gives

$$
\sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 ^ {k + 1}} \leq \frac {1}{2} L ^ {2} \left(\frac {\pi}{2 ^ {k}}\right) ^ {2 \alpha}.
$$

Hence

$$
\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 ^ {k + 1}} \leq \frac {1}{2} L ^ {2} \left(\frac {\pi}{2 ^ {k}}\right) ^ {2 \alpha}.
$$

Since $\sin^2\frac{n\pi}{2^{k + 1}}\geq \frac{1}{2}$ for $n = 2^{k - 1} + 1,\ldots ,2^k$ , we get

$$
\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \leq L ^ {2} \left(\frac {\pi}{2 ^ {k}}\right) ^ {2 \alpha}.
$$

By the Schwarz inequality,

$$
\begin{array}{l} \sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \sqrt {a _ {n} ^ {2} + b _ {n} ^ {2}} \leq \left(\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right)\right) ^ {1 / 2} \left(\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} 1\right) ^ {1 / 2} \\ \leq L \left(\frac {\pi}{2 ^ {k}}\right) ^ {\alpha} 2 ^ {(k - 1) / 2} <   L \left(\frac {\pi}{2 ^ {k}}\right) ^ {\alpha} 2 ^ {k / 2}. \\ \end{array}
$$

Finally, we get

$$
\sum_ {n = 2} ^ {\infty} \sqrt {a _ {n} ^ {2} + b _ {n} ^ {2}} = \sum_ {k = 1} ^ {\infty} \left(\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \sqrt {a _ {n} ^ {2} + b _ {n} ^ {2}}\right) \leq L \sum_ {k = 1} ^ {\infty} \left(\frac {\pi}{2 ^ {k}}\right) ^ {\alpha} 2 ^ {k / 2}.
$$

2.5.34. It follows from the solution to the previous problem that

$$
\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \leq L ^ {2} \left(\frac {\pi}{2 ^ {k}}\right) ^ {2 a}.
$$

We may suppose that $0 < \beta < 2$ . Then by the Hölder inequality,

$$
\begin{array}{l} \sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) ^ {\frac {9}{2}} \leq \left(\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right)\right) ^ {\frac {p}{2}} \left(\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} 1\right) ^ {1 - \frac {p}{2}} \\ \leq L ^ {\beta} \left(\frac {\pi}{2 ^ {k}}\right) ^ {\alpha \beta} 2 ^ {(k - 1) (1 - \beta / 2)} \\ = \frac {L ^ {\beta} \pi^ {\alpha \beta}}{2 ^ {1 - \frac {\beta}{2}}} 2 ^ {k (1 - \beta / 2 - \alpha \beta)}. \\ \end{array}
$$

Hence

$$
\begin{array}{l} \sum_ {n = 2} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) ^ {\frac {\beta}{2}} = \sum_ {k = 1} ^ {\infty} \left(\sum_ {n = 2 ^ {k - 1} + 1} ^ {2 ^ {k}} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) ^ {\frac {\beta}{2}}\right) \\ \leq \sum_ {k = 1} ^ {\infty} \frac {L ^ {\beta} \pi^ {\alpha \beta}}{2 ^ {1 - \frac {\beta}{2}}} 2 ^ {k (1 - \beta / 2 - \alpha \beta)}, \\ \end{array}
$$

and the desired result follows.

2.5.35. We have

$$
\begin{array}{l} \sum_ {i = 1} ^ {2 N} \left(f \left(x + \frac {i \pi}{N}\right) - f \left(x + \frac {(i - 1) \pi}{N}\right)\right) ^ {2} \\ \leq L \left(\frac {\pi}{N}\right) ^ {\alpha} \sum_ {i = 1} ^ {2 N} \left| f \left(x + \frac {i \pi}{N}\right) - f \left(x + \frac {(i - 1) \pi}{N}\right) \right| \leq L \left(\frac {\pi}{N}\right) ^ {\alpha} V, \\ \end{array}
$$

where $V$ is the total variation of $f$ over $[0,2\pi]$ . By (1) in the solution to 2.5.33 and by Parseval's formula,

$$
\begin{array}{l} 2 N \int_ {0} ^ {2 \pi} \left(f \left(x + \frac {i \pi}{N}\right) - f \left(x + \frac {(i - 1) \pi}{N}\right)\right) ^ {2} d x \\ = 8 N \pi \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 N} \\ \end{array}
$$

for $i = 1,2,\ldots ,2N$ .Hence

$$
\sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 N} \leq \frac {L}{4 N} \left(\frac {\pi}{N}\right) ^ {\alpha} V.
$$

Taking $N = 2^k$ , we get

$$
\sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 ^ {k + 1}} \leq \frac {L}{2 ^ {k + 2}} \left(\frac {\pi}{2 ^ {k}}\right) ^ {\alpha} V.
$$

Now it suffices to proceed as in the solution to 2.5.33.

2.5.36. The following example is due to Fejér. Let $G_{n}$ denote the group of $2n$ numbers

$$
\frac {1}{2 n - 1}, \frac {1}{2 n - 3}, \dots , \frac {1}{3}, 1, - 1, - \frac {1}{3}, \dots , - \frac {1}{2 n - 1}.
$$

We take a strictly increasing sequence of positive integers $\{\lambda_n\}$ and consider the groups $G_{\lambda_1}, G_{\lambda_2}, \ldots$ . We multiply each number of the group $G_{\lambda_n}$ by $n^{-2}$ and obtain the sequence

$$
\frac {1}{1 ^ {2} \left(2 \lambda_ {1} - 1\right)}, \dots , - \frac {1}{1 ^ {2} \left(2 \lambda_ {1} - 1\right)}, \frac {1}{2 ^ {2} \left(2 \lambda_ {2} - 1\right)}, \dots , - \frac {1}{2 ^ {2} \left(2 \lambda_ {2} - 1\right)}, \dots ,
$$

say, $\alpha_{1},\alpha_{2},\ldots$ . Our aim is to show that

$$
\sum_ {n = 1} ^ {\infty} \alpha_ {n} \cos n x
$$

is the Fourier series of a continuous function. We group the terms of this series in the following way:

$$
\sum_ {n = 1} ^ {2 \lambda_ {1}} \alpha_ {n} \cos n x + \sum_ {n = 2 \lambda_ {1} + 1} ^ {2 \lambda_ {1} + 2 \lambda_ {2}} \alpha_ {n} \cos n x + \sum_ {n = 2 \lambda_ {1} + 2 \lambda_ {2} + 1} ^ {2 \lambda_ {1} + 2 \lambda_ {2} + 2 \lambda_ {3}} \alpha_ {n} \cos n x + \dots .
$$

The last series can be written as

$$
\sum_ {n = 1} ^ {2 \lambda_ {1}} \alpha_ {n} \cos n x + \sum_ {n = 2} ^ {\infty} \frac {\varphi \left(\lambda_ {n} , 2 \lambda_ {1} + 2 \lambda_ {2} + \cdots + 2 \lambda_ {n - 1} , x\right)}{n ^ {2}},
$$

where

$$
\begin{array}{l} \varphi (n, r, x) = \frac {\cos (r + 1) x}{2 n - 1} + \frac {\cos (r + 2) x}{2 n - 3} + \dots + \frac {\cos (r + n) x}{1} \\ - \frac {\cos (r + n + 1) x}{1} - \frac {\cos (r + n + 2) x}{3} - \dots - \frac {\cos (r + 2 n) x}{2 n - 1}. \\ \end{array}
$$

Now we show that there is a constant $M$ (independent of $n, r,$ and $x$ ) such that $|\varphi(n, r, x)| \leq M$ . Indeed,

$$
\begin{array}{l} \varphi (n, r, x) = \sum_ {k = 1} ^ {n} \frac {\cos (r + n - k + 1) x}{2 k - 1} - \sum_ {k = 1} ^ {n} \frac {\cos (r + n + k) x}{2 k - 1} \\ = 2 \sin \left(r + n + \frac {1}{2}\right) x \sum_ {k = 1} ^ {n} \frac {\sin \left(k - \frac {1}{2}\right) x}{2 k - 1}. \\ \end{array}
$$

Since $\sum_{k=1}^{\infty} \frac{\sin(2k-1)\frac{\pi}{2}}{2k-1} = \frac{\pi}{4}$ for $x \in (0, 2\pi)$ (see 2.5.12), the sequence of its partial sums is bounded. It then follows that the grouped series

$$
\sum_ {n = 1} ^ {2 \lambda_ {1}} \alpha_ {n} \cos n x + \sum_ {n = 2} ^ {\infty} \frac {\varphi \left(\lambda_ {n} , 2 \lambda_ {1} + 2 \lambda_ {2} + \cdots + 2 \lambda_ {n - 1} , x\right)}{n ^ {2}} \tag {1}
$$

converges absolutely and uniformly on $\mathbb{R}$ , say to $f(x)$ , and $f$ is continuous on $\mathbb{R}$ . It is also easy to check that

$$
f (x) \sim \sum_ {n = 1} ^ {\infty} \alpha_ {n} \cos n x.
$$

We show finally that $\{\lambda_n\}$ can be chosen so that the above series diverges at zero, that is, $S_{n} = \alpha_{1} + \alpha_{2} + \dots +\alpha_{n}$ diverges to infinity. Since

$$
S _ {2 \lambda_ {1} + 2 \lambda_ {2} + \dots + 2 \lambda_ {n - 1} + \lambda_ {n}} = \frac {1}{n ^ {2}} \left(\frac {1}{2 \lambda_ {n} - 1} + \frac {1}{2 \lambda_ {n} - 3} + \dots + \frac {1}{3} + 1\right)
$$

behaves as $\frac{\ln\lambda_n}{2n^2}$ as $n \to \infty$ (that is, either both diverge or both converge to the same limit), it is enough to take, e.g., $\lambda_n = n^{n^2}$ . Then the Fourier series of $f$ does not converge to $f$ at $x = 2k\pi$ , $k \in \mathbb{Z}$ . It is worth noting here that if in the grouped series (1) we replace $x$ by $n!x$ , then the corresponding Fourier series fails to converge at every point $x = \frac{k\pi}{m}$ , $k \in \mathbb{Z}$ and $m \in \mathbb{N}$ . So, the Fourier series does not converge on a dense set. Indeed, if $x = \frac{k\pi}{m}$ , then for sufficiently large $n$ the part of the $n$ th group which has positive coefficients has the value

$$
\frac {1}{n ^ {2}} \left(\frac {1}{2 \lambda_ {n} - 1} + \frac {1}{2 \lambda_ {n} - 3} + \dots + \frac {1}{3} + 1\right),
$$

and taking $\lambda_{n}$ as above, we see that the series cannot converge at such points.

2.5.37. By the formula in 2.5.8,

$$
s _ {n} (x) = \frac {1}{\pi} \int_ {0} ^ {\pi} (f (x + t) + f (x - t)) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t,
$$

we get

$$
\begin{array}{l} \left| s _ {n} (x) \right| \leq \frac {2 M}{\pi} \int_ {0} ^ {\pi} \frac {\left| \sin \left(n + \frac {1}{2}\right) t \right|}{2 \sin \frac {1}{2} t} d t <   M \int_ {0} ^ {\pi} \frac {\left| \sin \left(n + \frac {1}{2}\right) t \right|}{t} d t \\ = M \int_ {0} ^ {\left(n + \frac {1}{2}\right) \pi} \frac {| \sin u |}{u} d u <   M \int_ {0} ^ {1} d u + M \int_ {1} ^ {\left(n + \frac {1}{2}\right) \pi} \frac {d u}{u} \\ = M \left(1 + \ln \left(n + \frac {1}{2}\right) \pi\right). \\ \end{array}
$$

It is worth noting here that the estimate is uniform on $\mathbb{R}$ .

2.5.38. We have

$$
\begin{array}{l} L _ {n} = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) x}{\sin \frac {x}{2}} \right| d x = \frac {1}{\pi} \int_ {0} ^ {\pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) x}{\sin \frac {x}{2}} \right| d x \\ = \frac {2}{\pi} \int_ {0} ^ {\pi / 2} \left| \frac {\sin \left(n + \frac {1}{2}\right) 2 t}{\sin t} \right| d t > \frac {2}{\pi} \int_ {0} ^ {\pi / 2} \frac {\left| \sin \left(n + \frac {1}{2}\right) 2 t \right|}{t} d t \\ \end{array}
$$

$$
\begin{array}{l} = \frac {2}{\pi} \int_ {0} ^ {(2 n + 1) \pi / 2} \frac {| \sin u |}{u} d u > \frac {2}{\pi} \sum_ {k = 0} ^ {n - 1} \int_ {k \pi} ^ {(k + 1) \pi} \frac {| \sin u |}{u} d u \\ = \frac {2}{\pi} \sum_ {k = 0} ^ {n - 1} \int_ {0} ^ {\pi} \frac {\sin u}{u + k \pi} d u > \frac {2}{\pi} \sum_ {k = 0} ^ {n - 1} \frac {1}{(k + 1) \pi} \int_ {0} ^ {\pi} \sin u d u \\ = \frac {4}{\pi^ {2}} \sum_ {k = 0} ^ {n - 1} \frac {1}{k + 1}. \\ \end{array}
$$

We know, see, e.g., I, 2.1.41, that the sequence

$$
b _ {n} = \sum_ {k = 0} ^ {n - 1} \frac {1}{k + 1} - \ln n
$$

monotonically decreases to Euler's constant $\gamma = 0.5772\ldots$ . Thus $L_{n} > \frac{4}{\pi^{2}} \ln n + \frac{4}{\pi^{2}} \gamma$ . To prove the opposite inequality, we first observe that

$$
\left| \frac {\sin \left(n + \frac {1}{2}\right) t}{\sin \frac {t}{2}} - \frac {\sin n t}{\tan \frac {t}{2}} \right| \leq 1.
$$

Thus

$$
\begin{array}{l} L _ {n} \leq 1 + \frac {1}{\pi} \int_ {0} ^ {\pi} \left| \frac {\sin n t}{\tan \frac {t}{2}} \right| d t = 1 + \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} \left| \frac {\sin 2 n t}{\tan t} \right| d t \\ <   1 + \frac {2}{\pi} \int_ {0} ^ {\frac {\pi}{2}} \frac {| \sin 2 n t |}{t} d t = 1 + \frac {2}{\pi} \int_ {0} ^ {n \pi} \frac {| \sin u |}{u} d u \\ = 1 + \frac {2}{\pi} \sum_ {k = 1} ^ {n} \int_ {(k - 1) \pi} ^ {k \pi} \frac {| \sin u |}{u} d u = 1 + \frac {2}{\pi} \sum_ {k = 1} ^ {n} \int_ {0} ^ {\pi} \frac {\sin t}{t + (k - 1) \pi} d t \\ <   1 + \frac {2}{\pi} \int_ {0} ^ {\pi} \frac {\sin t}{t} d t + \frac {4}{\pi^ {2}} \sum_ {k = 2} ^ {n} \frac {1}{k - 1} <   C + \frac {4}{\pi^ {2}} \ln n + \frac {4}{\pi^ {2}} \gamma . \\ \end{array}
$$

It is worth noting here that the result in the previous problem is an immediate consequence of this result.

2.5.39. We know from the solution to 2.5.8 that

$$
s _ {n} (x) - f (x) = \frac {1}{\pi} \int_ {0} ^ {\pi} (f (x + t) + f (x - t) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} d t.
$$

Thus it is enough to show that

$$
I _ {n} = \int_ {0} ^ {\pi} \left| (f (x + t) + f (x - t) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) t}{2 \sin \frac {1}{2} t} \right| d t = o (\ln n).
$$

Consequently,

$$
\left| B _ {n} (f, x) - f (x) \right| \leq \sum_ {k = 0} ^ {n} \left| f \left(\frac {k}{n}\right) - f (x) \right| \binom {n} {k} x ^ {k} (1 - x) ^ {n - k}. \tag {1}
$$

By the uniform continuity of $f$ on $[0,1]$ , given $\varepsilon > 0$ there is $\delta > 0$ such that

$$
| f (x) - f \left(x ^ {\prime}\right) | <   \varepsilon
$$

whenever $|x - x'| < \delta$ , $x, x' \in [0,1]$ . Clearly, there is $M > 0$ such that $|f(x)| \leq M$ for $x \in [0,1]$ . Let $x$ be arbitrarily chosen in $[0,1]$ . Then the set $\{0,1,2,\ldots,n\}$ can be decomposed into the two sets

$$
A = \left\{k: \left| \frac {k}{n} - x \right| <   \delta \right\} \quad a n d \quad B = \left\{k: \left| \frac {k}{n} - x \right| \geq \delta \right\}.
$$

If $k \in \mathbf{A}$ , then

$$
\left| f \left(\frac {k}{n}\right) - f (x) \right| <   \varepsilon ,
$$

and so

$$
\sum_ {k \in A} \left| f \left(\frac {k}{n}\right) - f (x) \right| <   \varepsilon \sum_ {k \in A} \binom {n} {k} x ^ {k} (1 - x) ^ {n - k} \leq \varepsilon . \tag {2}
$$

If $k\in \mathbf{B}$ , then

$$
\frac {(k - n x) ^ {2}}{n ^ {2} \delta^ {2}} \geq 1,
$$

and by the inequality given in 2.5.52 we get

$$
\begin{array}{l} \sum_ {k \in \mathbf {B}} \left| f \left(\frac {k}{n}\right) - f (x) \right| \binom {n} {k} x ^ {k} (1 - x) ^ {n - k} \\ \leq \frac {2 M}{n ^ {2} \delta^ {2}} \sum_ {k \in \mathbf {B}} (k - n x) ^ {2} \binom {n} {k} x ^ {k} (1 - x) ^ {n - k} \leq \frac {M}{2 n \delta^ {2}}. \\ \end{array}
$$

This combined with (1) and (2) yields

$$
\left| B _ {n} (f, x) - f (x) \right| \leq \varepsilon + \frac {M}{2 n \delta^ {2}}, \quad x \in [ 0, 1 ].
$$

Thus the first claim follows from the fact that the Fejer kernel $\frac{\sin^2\frac{1}{2}nt}{\sin^2\frac{1}{2}t}$ is nonnegative. If for some $n$ and $x$ we have $\sigma_n(x) = M$ , then

$$
\frac {1}{n \pi} \int_ {- \pi} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} (M - f (x + t)) d t = 0,
$$

and the integrand is nonnegative. Thus the second claim follows from 2.3.6.

2.5.42. One can easily check that if $S_{n} = c_{0} + c_{1} + \dots + c_{n-1}$ and $\sigma_{n} = \frac{S_{1} + S_{2} + \cdots + S_{n}}{n}$ , then

$$
S _ {n} - \sigma_ {n} = \frac {c _ {1} + 2 c _ {2} + \cdots + (n - 1) c _ {n - 1}}{n}.
$$

Consequently,

$$
s _ {n} (x) = \sigma_ {n + 1} (x) + \frac {\sum_ {k = 1} ^ {n} k \left(a _ {k} \cos k x + b _ {k} \sin k x\right)}{n + 1}, \tag {1}
$$

where $s_n(x)$ and $\sigma_n(x)$ denote the $n$ th partial sum and the $n$ th Cesàro mean of the Fourier series of $f$ , respectively. Thus, by assumption,

$$
\left| s _ {n} (x) - \sigma_ {n + 1} (x) \right| \leq A + B,
$$

and the first statement follows from the previous problem. Now, the second statement is an immediate consequence of the formula

$$
\frac {\pi - x}{2} = \sum_ {n = 1} ^ {\infty} \frac {\sin n x}{n}, \quad 0 <   x <   2 \pi .
$$

It is also worth noting here that, in view of the result in 2.5.4, if $f$ is of bounded variation on $[-\pi, \pi]$ , then the partial sums of the Fourier series of $f$ are uniformly bounded.

2.5.43. We may assume that $0 < x < \pi$ . Put $m = [\pi / x]$ and write

$$
\sum_ {k = 1} ^ {n} c _ {k} \sin k x = \sum_ {k = 1} ^ {m} c _ {k} \sin k x + \sum_ {k = m + 1} ^ {n} c _ {k} \sin k x,
$$

an empty sum being counted zero. Then

$$
0 \leq \sum_ {k = 1} ^ {m} c _ {k} \sin k x \leq \sum_ {k = 1} ^ {m} \frac {A}{k} \sin k x \leq \sum_ {k = 1} ^ {m} \frac {A}{k} k x = m A x \leq A \pi .
$$

To estimate the second sum, the following formula for summation by parts will be used:

$$
\sum_ {k = m + 1} ^ {n} c _ {k} \sin k x = \sum_ {k = m + 1} ^ {n - 1} (c _ {k} - c _ {k + 1}) (S _ {k} (x) - S _ {m} (x)) + c _ {n} (S _ {n} (x) - S _ {m} (x)),
$$

where

$$
S _ {k} (x) = \sum_ {j = 1} ^ {k} \sin j x = \frac {\sin \frac {n x}{2} \sin \frac {(n + 1) x}{2}}{\sin \frac {x}{2}}.
$$

Note also that

$$
\begin{array}{l} | S _ {k} (x) - S _ {m} (x) | = \left| \frac {\sin \frac {k x}{2} \sin \frac {(k + 1) x}{2} - \sin \frac {m x}{2} \sin \frac {(m + 1) x}{2}}{\sin \frac {x}{2}} \right| \\ = \left| \frac {\cos \frac {(2 k + 1) x}{4} - \cos \frac {(2 m + 1) x}{4}}{2 \sin \frac {x}{2}} \right| \leq \frac {1}{\left| \sin \frac {x}{2} \right|}. \\ \end{array}
$$

Consequently,

$$
\begin{array}{l} \left| \sum_ {k = m + 1} ^ {n} c _ {k} \sin k x \right| \leq \sum_ {k = m + 1} ^ {n - 1} \left(c _ {k} - c _ {k + 1}\right) \frac {1}{\sin \frac {x}{2}} + c _ {n} \frac {1}{\sin \frac {x}{2}} \\ = \frac {c _ {m + 1}}{\sin \frac {x}{2}} \leq \frac {A}{(m + 1) \sin \frac {x}{2}} <   A. \\ \end{array}
$$

2.5.44. It follows from 2.5.41 that $|\sigma_n(x)| \leq M$ for all $n$ and $x$ . Moreover, by (1) in the solution to 2.5.42,

$$
\sigma_ {n + 1} (x) = \sum_ {k = 1} ^ {n} \left(1 - \frac {k}{n + 1}\right) b _ {k} \sin k x.
$$

Taking $x = \frac{\pi}{4m}$ , we get

$$
M \geq \sigma_ {2 m + 1} \left(\frac {\pi}{4 m}\right) \geq \sum_ {k = 1} ^ {2 m} \left(1 - \frac {k}{2 m + 1}\right) b _ {k} \frac {k}{2 m} \geq \frac {1}{2} \sum_ {k = 1} ^ {m} b _ {k} \frac {k}{2 m}.
$$

Hence

$$
\sum_ {k = 1} ^ {m} k b _ {k} \leq 4 m M.
$$

This together with (1) in the solution to 2.5.42 gives $|s_n(x)| \leq 5M$ .

2.5.45. We know, by 2.5.41, that $|\sigma_n(x)| \leq M$ . Consequently, since $a_n \geq 0$ ,

$$
\begin{array}{l} M \geq \sigma_ {2 n + 1} (0) = \frac {1}{2 n + 1} \sum_ {k = 0} ^ {2 n} s _ {k} (0) \geq \frac {1}{2 n + 1} \sum_ {k = n} ^ {2 n} s _ {k} (0) \\ \geq \frac {n + 1}{2 n + 1} s _ {n} (0) \geq \frac {1}{2} s _ {n} (0). \\ \end{array}
$$

2.5.46. We have

$$
f (x) = \sum_ {n = 1} ^ {\infty} \frac {n ^ {3}}{n ^ {4} + 1} \sin n x = \sum_ {n = 1} ^ {\infty} \frac {\sin n x}{n} - \sum_ {n = 1} ^ {\infty} \frac {1}{n \left(n ^ {4} + 1\right)} \sin n x.
$$

Thus

$$
f (x) = \frac {\pi - x}{2} + g (x)
$$

and

$$
g ^ {(4)} (x) = - f (x).
$$

2.5.47. Since

$$
1 = \frac {1}{2 \pi n} \int_ {0} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} 2 d t,
$$

we have

$$
\sigma_ {n} (x) - s = \frac {1}{2 \pi n} \int_ {0} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} (f (x + t) + f (x - t) - 2 s) d t
$$

for any real $s$ . We now put $s = \frac{f(x^{-}) + f(x^{+})}{2}$ . To prove that the sequence $\{\sigma_n(x)\}$ converges to $s$ , we set $\varphi(t) = f(x + t) + f(x - t) - 2s$ , and note that it suffices to show that

$$
\lim  _ {n \rightarrow \infty} \frac {1}{n} \int_ {0} ^ {\delta} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t = 0
$$

for some $0 < \delta < \pi$ , because

$$
\left| \frac {1}{n} \int_ {\delta} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t \right| \leq \frac {1}{n} \int_ {\delta} ^ {\pi} \frac {| \varphi (t) |}{\sin^ {2} \frac {1}{2} t} d t.
$$

By assumption, given $\varepsilon > 0$ , there is $0 < \eta < \delta$ such that $|\varphi(t)| < \varepsilon$ for $|t| < \eta$ . Then

$$
\begin{array}{l} \left| \frac {1}{n} \int_ {0} ^ {\delta} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t \right| \leq \frac {\pi^ {2}}{n} \int_ {0} ^ {\delta} \frac {\sin^ {2} \frac {1}{2} n t}{t ^ {2}} | \varphi (t) | d t \\ \leq \frac {\pi^ {2}}{n} \int_ {0} ^ {\eta} \frac {\sin^ {2} \frac {1}{2} n t}{t ^ {2}} \varepsilon d t + \frac {\pi^ {2}}{n} \int_ {\eta} ^ {\delta} \frac {1}{t ^ {2}} | \varphi (t) | d t \\ = \frac {\pi^ {2} \varepsilon}{n} \int_ {0} ^ {\eta} \frac {\sin^ {2} \frac {1}{2} n t}{t ^ {2}} d t + \frac {\pi^ {2}}{n} \int_ {\pi} ^ {\delta} \frac {| \varphi (t) |}{t ^ {2}} d t. \\ \end{array}
$$

Moreover, by 1.5.55,

$$
\begin{array}{l} \frac {\pi^ {2} \varepsilon}{n} \int_ {0} ^ {\eta} \frac {\sin^ {2} \frac {1}{2} n t}{t ^ {2}} d t = \frac {\pi^ {2} \varepsilon}{2} \int_ {0} ^ {\frac {1}{2} n \eta} \frac {\sin^ {2} u}{u ^ {2}} d u \\ <   \frac {\pi^ {2} \varepsilon}{2} \int_ {0} ^ {\infty} \frac {\sin^ {2} u}{u ^ {2}} d u = \frac {\pi^ {3} \varepsilon}{4}. \\ \end{array}
$$

2.5.48. Note that if $\pmb{x}$ is a Lebesgue point for $f$ (see 2.4.22 for the definition), then

$$
\Phi (t) = \int_ {0} ^ {t} | f (x + u) + f (x - u) - 2 f (x) | d u = o (t).
$$

We put $\varphi(t) = f(x + t) + f(x - t) - 2f(x)$ . As in the solution to the preceding problem,

$$
\sigma_ {n} (x) - f (x) = \frac {1}{2 \pi n} \int_ {0} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t,
$$

and it suffices to show that

$$
\lim  _ {n \rightarrow \infty} \frac {1}{2 \pi n} \int_ {0} ^ {\delta} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t = 0
$$

for some $0 < \delta < \pi$ . Let $\varepsilon > 0$ be given. Then there is $0 < \eta < \delta$ such that $\Phi(t) < \varepsilon t$ for $t < \eta$ . We now take $n$ such that $\sqrt[n]{n} > 1 / \eta$ , and

write

$$
\begin{array}{l} \frac {1}{2 \pi n} \int_ {0} ^ {\delta} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t \\ = \frac {1}{2 \pi n} \int_ {0} ^ {\frac {1}{n}} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t + \frac {1}{2 \pi n} \int_ {\frac {1}{n}} ^ {\eta} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t \\ + \frac {1}{2 \pi n} \int_ {\eta} ^ {\delta} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} \varphi (t) d t = I _ {1} + I _ {2} + I _ {3}. \\ \end{array}
$$

Then

$$
\left| I _ {1} \right| \leq \frac {1}{2 \pi n} \int_ {0} ^ {\frac {1}{n}} \frac {\frac {n ^ {2} t ^ {2}}{4}}{\frac {t ^ {2}}{\pi^ {2}}} | \varphi (t) | d t = \frac {n \pi}{8} \int_ {0} ^ {\frac {1}{n}} | \varphi (t) | d t <   \frac {\pi}{8} \varepsilon .
$$

Integrating by parts, we get

$$
\begin{array}{l} \left| I _ {2} \right| \leq \frac {\pi}{2 n} \int_ {\frac {1}{n}} ^ {\eta} \frac {| \varphi (t) |}{t ^ {2}} d t = \frac {\pi}{2 n} \left(\frac {\Phi (\eta)}{\eta^ {2}} - n ^ {2} \Phi \left(\frac {1}{n}\right) + 2 \int_ {\frac {1}{n}} ^ {\eta} \frac {\Phi (t)}{t ^ {3}} d t\right) \\ <   \frac {\pi}{2 n} \left(\frac {\varepsilon}{\eta} + 2 \varepsilon \int_ {\frac {1}{n}} ^ {\eta} \frac {1}{t ^ {2}} d t\right) = \frac {\pi}{2 n} \left(\frac {\varepsilon}{\eta} + 2 \varepsilon n - \frac {2 \varepsilon}{\eta}\right) <   \pi \varepsilon . \\ \end{array}
$$

Finally,

$$
\left| I _ {3} \right| \leq \frac {\pi}{2 n \eta^ {2}} \int_ {\eta} ^ {\delta} | \varphi (t) | d t \leq \frac {\pi C}{2 n \eta^ {2}} \leq \frac {\pi C}{2 \sqrt {n}},
$$

where $C = \int_0^\pi |\varphi (t)|dt.$

It is worth noting here that in view of the result in 2.4.24, $\{\sigma_n(x)\}$ converges to $f(x)$ almost everywhere on $\mathbb{R}$ .

2.5.49. We start by showing that if $f$ is $2\pi$ -periodic on $\mathbb{R}$ and $f \in L^{p}[-\pi, \pi]$ , $1 \leq p < \infty$ , and $f_{t}(x) = f(x - t)$ , then

$$
\lim  _ {t \rightarrow 0} \| f _ {t} - f \| _ {p} = 0,
$$

which means that the translate is continuous in the $L^p$ norm. We assume that $|t| < \pi$ . Note also that $\int_{-2\pi}^{2\pi}|f(x)|^p dx < \infty$ . It follows from 2.3.30 that, given $\varepsilon > 0$ , there is a function $g$ , continuous on

$[-2\pi, 2\pi]$ , such that $\int_{-2\pi}^{2\pi} |f(x) - g(x)|^p dx < \varepsilon$ . Hence

$$
\begin{array}{l} \int_ {- \pi} ^ {\pi} | f (x - t) - f (x) | ^ {p} d x \leq \int_ {- \pi} ^ {\pi} | f (x - t) - g (x - t) | ^ {p} d x \\ + \int_ {- \pi} ^ {\pi} | g (x - t) - g (x) | ^ {p} d x + \int_ {- \pi} ^ {\pi} | g (x) - f (x) | ^ {p} d x \\ \leq \int_ {- \pi - t} ^ {\pi - t} | g (x) - f (x) | ^ {p} d x + \int_ {- \pi} ^ {\pi} | g (x - t) - g (x) | ^ {p} d x + \varepsilon \\ \leq 2 \varepsilon + \int_ {- \pi} ^ {\pi} | g (x - t) - g (x) | ^ {p} d x. \\ \end{array}
$$

Since $g$ is uniformly continuous on $[-2\pi, 2\pi]$ , there is $\delta > 0$ such that $|g(x - t) - g(x)|^p < \frac{\varepsilon}{2\pi}$ for $|t| < \delta$ and $x \in [-\pi, \pi]$ . Hence $\int_{-\pi}^{\pi} |f(x - t) - f(x)|^p dx \leq 3\varepsilon$ , which proves the claim stated above.

Suppose now that $f$ is $2\pi$ -periodic on $\mathbb{R}$ , $f \in L^{2}[-\pi, \pi]$ and $g$ is the function defined in the problem. Then, using consecutively the Schwarz inequality, the change of variable formula (2.4.13) and the periodicity of $f$ , we get

$$
\begin{array}{l} \left| g \left(x _ {1}\right) - g \left(x _ {2}\right) \right| \leq \| f \| _ {2} \left(\int_ {- \pi} ^ {\pi} | f \left(x _ {1} + t\right) - f \left(x _ {2} + t\right) | ^ {2} d t\right) ^ {\frac {1}{2}} \\ = \| f \| _ {2} \left(\int_ {- \pi + x _ {1}} ^ {\pi + x _ {1}} | f (s) - f (s - (x _ {1} - x _ {2}) | ^ {2} d s\right) ^ {\frac {1}{2}} \\ = \| f \| _ {2} \left(\int_ {- \pi} ^ {\pi} | f (s) - f (s - (x _ {1} - x _ {2}) | ^ {2} d s\right) ^ {\frac {1}{2}} \\ = \| f \| _ {2} \| f _ {x _ {1} - x _ {2}} - f \| _ {2}. \\ \end{array}
$$

So the result follows from the continuity of $f_{t}$ in the $L^2$ norm.

2.5.50. We have

$$
\sigma_ {n} (x) - f (x) = \frac {1}{2 \pi n} \int_ {0} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} (f (x + t) + f (x - t) - 2 f (x)) d t.
$$

Since $f$ is uniformly continuous on $\mathbb{R}$ , given $\varepsilon > 0$ , there is $\delta > 0$ such that $|f(x) - f(t)| < \varepsilon$ whenever $|t - x| < \delta$ . Hence

$$
| \sigma_ {n} (x) - f (x) | \leq \frac {\varepsilon}{\pi n} \int_ {0} ^ {\delta} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} d t + \frac {2 M}{\pi n} \int_ {\delta} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} d t,
$$

where $M = \sup \{|f(x)| : x \in \mathbb{R}\}$ . We know that

$$
\frac {1}{\pi n} \int_ {0} ^ {\pi} \frac {\sin^ {2} \frac {1}{2} n t}{\sin^ {2} \frac {1}{2} t} d t = 1.
$$

So, if $n > \frac{1}{\delta^4}$ , then

$$
\left| \sigma_ {n} (x) - f (x) \right| \leq \varepsilon + \frac {\pi}{n \delta^ {2}} 2 M \pi <   \varepsilon + \frac {2 \pi^ {2} M}{\sqrt {n}}.
$$

2.5.51. We know, by the result in the preceding problem, that the sequence $\{\sigma_n(x)\}$ converges to $f(x)$ uniformly on $\mathbb{R}$ . Hence, given $\varepsilon > 0$ , there is $n_0$ such that $|g_n(x)| = |\dot{f}(x) - \sigma_n(x)| < \varepsilon$ for all $x$ and $n \geq n_0$ . In what follows $S_n(y(x))$ denotes the $n$ th partial sum of the Fourier series of an integrable function $g$ . First we note that if $p, q > n \geq n_0$ , then $S_p(\sigma_n(x)) = S_q(\sigma_n(x)) = \sigma_n(x)$ . Thus

$$
\begin{array}{l} \left| S _ {p} (f (x)) - S _ {q} (f (x)) \right| \\ \leq \left| S _ {p} \left(\sigma_ {n} (x)\right) \quad S _ {q} \left(\sigma_ {n} (x)\right) \right| \mid \left| S _ {p} \left(g _ {n} (x)\right) \right| \mid \left| S _ {q} \left(g _ {n} (x)\right) \right| \\ = \left| S _ {p} \left(g _ {n} (x)\right) \right| + \left| S _ {q} \left(g _ {n} (x)\right) \right|. \\ \end{array}
$$

We now note that the Fourier coefficients of $g_{n}$ are nonnegative. Moreover, $g_{n}$ can be represented as a sum of an even function and an odd function; that is,

$$
g _ {n} (x) = \frac {g _ {n} (x) + g _ {n} (- x)}{2} + \frac {g _ {n} (x) - g _ {n} (- x)}{2}.
$$

Both terms are bounded (by $-\varepsilon$ from below and by $\varepsilon$ from above) and their Fourier series are the cosine and sine parts of the Fourier series of $g_{n}$ , respectively. It then follows from the result in 2.5.44 and from the solution to 2.5.45 that

$$
\left| S _ {p} (f (x)) - S _ {q} (f (x)) \right| \leq \left| S _ {p} \left(g _ {n} (x)\right) \right| + \left| S _ {q} \left(g _ {n} (x)\right) \right| \leq 1 0 \varepsilon + 4 \varepsilon .
$$

2.5.52. It follows from the Fejer-Lebesgue theorem (see 2.5.48) that $\lim_{n\to \infty}\sigma_n(x) = f(x)$ a.e. Thus the first claim will be proved if we show that $\lim_{n\to \infty}(s_n(x) - \sigma_n(x)) = 0$ for all $x$ . By (1) in the solution to 2.5.42,

$$
\left| s _ {n} (x) - \sigma_ {n + 1} (x) \right| = \frac {\left| \sum_ {k = 1} ^ {n} k \left(a _ {k} \cos k x + b _ {k} \sin k x\right) \right|}{n + 1} \leq \frac {\sum_ {k = 1} ^ {n} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}}}{n + 1}.
$$

Furthermore, in view of the result in 2.5.50, the other claim follows.

2.5.53. We start with the following formula, proved in the solution to 2.5.33:

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} (f (x + h) - f (x - h)) ^ {2} d x = 4 \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} n h,
$$

and get

$$
\frac {1}{\pi} \int_ {- \pi} ^ {\pi} \left(f \left(x + \frac {k \pi}{r}\right) - f \left(x + \frac {(k - 1) \pi}{r}\right)\right) ^ {2} d x = 4 \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 r}.
$$

Consequently,

$$
\begin{array}{l} \frac {1}{\pi} \int_ {- \pi} ^ {\pi} \sum_ {k = 1} ^ {2 r} \left(f \left(x + \frac {k \pi}{r}\right) - f \left(x + \frac {(k - 1) \pi}{r}\right)\right) ^ {2} d x \\ = 8 r \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 r}. \\ \end{array}
$$

Since

$$
\begin{array}{l} \frac {1}{\pi} \int_ {- \pi} ^ {\pi} \sum_ {k = 1} ^ {2 r} \left(f \left(x + \frac {k \pi}{r}\right) - f \left(x + \frac {(k - 1) \pi}{r}\right)\right) ^ {2} d x \\ \leq 2 \omega \left(\frac {\pi}{r}\right) V (f; 0, 2 \pi), \\ \end{array}
$$

where $\omega(h) = \sup \{|f(x + h) - f(x)| : x \in \mathbb{R}\}$ , we see that if $f$ is continuous, then

$$
\lim  _ {r \rightarrow \infty} r \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \sin^ {2} \frac {n \pi}{2 r} = 0. \tag {1}
$$

Now we show that (1) implies the continuity of $f$ . Indeed, if $x_0$ were a point of discontinuity of $f$ , then $|f(x_0^+) - f(x_0^-)| = d > 0$ , which would imply that at least one term in the sum

$$
\sum_ {k = 1} ^ {2 r} \left(f \left(x + \frac {k \pi}{r}\right) - f \left(x + \frac {(k - 1) \pi}{r}\right)\right) ^ {2}
$$

would contribute an amount not less than $\frac{d^2}{4}$ . This would contradict (1). Thus we have proved that $f$ is continuous if and only if condition (1) is fulfilled. Our task is to show that (1) is equivalent to

$$
\lim  _ {n \rightarrow \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}} = 0. \tag {2}
$$

Put

$$
P _ {n} = n \sum_ {k = 1} ^ {\infty} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) \sin^ {2} \frac {k \pi}{2 n} \quad \text {a n d} \quad T _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}}.
$$

If $\lim_{n\to \infty}P_n = 0$ , then

$$
P _ {n} \geq n \sum_ {k = 1} ^ {n} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) \sin^ {2} \frac {k \pi}{2 n} \geq \frac {1}{n} \sum_ {k = 1} ^ {n} k ^ {2} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) \geq T _ {n} ^ {2},
$$

where the last inequality follows from the Cauchy inequality. This shows that $\lim_{n\to \infty}T_n = 0$ . Conversely, if $\lim_{n\to \infty}T_n = 0$ , then we have

$$
\begin{array}{l} P _ {n} = n \sum_ {k = 1} ^ {N n} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) \sin^ {2} \frac {k \pi}{2 n} + n \sum_ {k = N n + 1} ^ {\infty} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) \sin^ {2} \frac {k \pi}{2 n} \\ \leq n \sum_ {k = 1} ^ {N n} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) \frac {k ^ {2} \pi^ {2}}{4 n ^ {2}} + n \sum_ {k = N n + 1} ^ {\infty} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) \\ \leq \frac {\pi^ {2}}{4 n} \sum_ {k = 1} ^ {N n} k ^ {2} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) + n C \sum_ {k = N n + 1} ^ {\infty} \frac {1}{k ^ {2}}, \\ \end{array}
$$

because, by the result in 2.5.4, the coefficients $a_{n}$ and $b_{n}$ are $O(n^{-1})$ . Moreover, since

$$
\sum_ {k = N n + 1} ^ {\infty} \frac {1}{k ^ {2}} <   \frac {1}{N n},
$$

given $\varepsilon > 0$ , there is $N$ such that

$$
n C \sum_ {k = N n + 1} ^ {\infty} \frac {1}{k ^ {2}} <   \varepsilon .
$$

Thus

$$
P _ {n} \leq \frac {\pi^ {2}}{4 n} \sum_ {k = 1} ^ {N n} k ^ {2} \left(a _ {k} ^ {2} + b _ {k} ^ {2}\right) + \varepsilon \leq \frac {\sqrt {C} \pi^ {2}}{4 n} \sum_ {k = 1} ^ {N n} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}} + \varepsilon .
$$

2.5.54. We will show that the assumption of the Fatou theorem is satisfied. We have

$$
n _ {k} \leq \frac {1}{q} n _ {k + 1} \leq \dots \leq \frac {1}{q ^ {m - k}} n _ {m}.
$$

Moreover, we know, by 2.5.2, that $\lim_{n\to \infty}\sqrt{a_n^2 + b_n^2} = 0$ . Thus, given $\varepsilon > 0$ , there is $n^*$ such that $\sqrt{a_n^2 + b_n^2} < \varepsilon$ for $n > n^*$ . If $n^* \leq n_m \leq N < n_{m+1}$ , then

$$
\frac {1}{N} \sum_ {k = 1} ^ {N} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}} = \frac {1}{N} \sum_ {k = 1} ^ {n ^ {\bullet}} k \sqrt {a _ {k} ^ {2} + b _ {k} ^ {2}} + \frac {1}{N} \sum_ {k = j} ^ {m} n _ {k} \sqrt {a _ {n _ {k}} ^ {2} + b _ {n _ {k}} ^ {2}},
$$

where $n_{j-1} \leq n^{*} < n_{j}$ . Since the first term tends to zero as $N \to \infty$ , it suffices to show that the second term also tends to zero as $N \to \infty$ . To this end, observe that

$$
\frac {1}{N} \sum_ {k = j} ^ {m} n _ {k} \sqrt {a _ {n _ {k}} ^ {2} + b _ {n _ {k}} ^ {2}} \leq \frac {\varepsilon}{n _ {m}} \sum_ {k = j} ^ {m} q ^ {k - m} n _ {m} <   \varepsilon \sum_ {l = 0} ^ {\infty} q ^ {- l} = \varepsilon \frac {q}{q - 1}.
$$

2.5.55. Let $g$ be any function in $L^q[-\pi, \pi]$ , where $\frac{1}{p} + \frac{1}{q} = 1$ . Then

$$
\begin{array}{l} \int_ {- \pi} ^ {\pi} (\sigma_ {n} (x) - f (x)) g (x) d x \\ = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \left(\int_ {- \pi} ^ {\pi} (f (x - t) - f (x)) g (x) \frac {\sin^ {2} \frac {n t}{2}}{n \sin^ {2} \frac {t}{2}} d t\right) d x, \\ \end{array}
$$

and by Fubini's theorem and the Hölder inequality we get

$$
\begin{array}{l} \left| \int_ {- \pi} ^ {n} \left(\sigma_ {n} (x) - f (x)\right) g (x) d x \right| \\ \leq \int_ {- \pi} ^ {\pi} \left| \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} (f (x - t) - f (x)) g (x) d x \right| \frac {\sin^ {2} \frac {n t}{2}}{n \sin^ {2} \frac {t}{2}} d t \\ \leq \| g \| _ {q} \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \| f _ {t} - f \| _ {p} \frac {\sin^ {2} \frac {n t}{2}}{n \sin^ {2} \frac {t}{2}} d t, \\ \end{array}
$$

where $f_{t}(x) = f(x - t)$ is the translate of $f$ by $-t$ . Since the inequality

$$
\left| \int_ {- \pi} ^ {\pi} \left(\sigma_ {n} (x) - f (x)\right) g (x) d x \right| \leq \| g \| _ {q} \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \| f _ {t} - f \| _ {p} \frac {\sin^ {2} \frac {n t}{2}}{n \sin^ {2} \frac {t}{2}} d t
$$

holds for every $g \in L^{q}[-\pi, \pi]$ and

$$
\| \sigma_ {n} - f \| _ {p} = \sup  _ {\| g \| _ {q} = 1} \left| \int_ {- \pi} ^ {\pi} (\sigma_ {n} (x) - f (x)) g (x) d x \right|,
$$

we get

$$
\left\| \sigma_ {n} - f \right\| _ {p} \leq \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \left\| f _ {t} - f \right\| _ {p} \frac {\sin^ {2} \frac {n t}{2}}{n \sin^ {2} \frac {t}{2}} d t.
$$

Now for $0 < \delta < \pi$ we have

$$
\begin{array}{l} \left\| \sigma_ {n} - f \right\| _ {p} \leq \frac {1}{2 \pi} \int_ {- \delta} ^ {\delta} \left\| f _ {t} - f \right\| _ {p} \frac {\sin^ {2} \frac {n t}{2}}{n \sin^ {2} \frac {t}{2}} d t \\ + \frac {1}{2 \pi} \int_ {\delta \leq | t | \leq \pi} \| f _ {t} - f \| _ {p} \frac {\sin^ {2} \frac {n t}{2}}{n \sin^ {2} \frac {t}{2}} d t \\ \leq \sup  _ {| t | <   \delta} \| f _ {t} - f \| _ {p} + 2 \| f \| _ {p} \frac {1}{n \sin^ {2} \frac {\delta}{2}}, \\ \end{array}
$$

and the desired result follows from the fact that the translate $f_{t}$ is continuous in the $L^{p}$ norm (see the solution to 2.5.49).

2.5.56. We first prove that the condition $\lim_{n\to \infty}nb_n = 0$ is sufficient for the uniform convergence of $\sum_{n = 1}^{\infty}b_n\sin nx$ on $[0,2\pi ]$ . Since $\{b_n\}$ is a monotonically decreasing sequence converging to zero, by the Dirichlet test for uniform convergence (see, e.g., II 3.2.13), the series is uniformly convergent on $[\delta ,2\pi -\delta ]$ , where $0 < \delta < \pi$ . Thus it suffices to show that the series converges uniformly on $[0,\pi /4]$ . It follows from the summation by parts formula (Abel transformation) that

$$
\sum_ {k = n} ^ {m} b _ {k} \sin k x = \sum_ {k = n} ^ {m - 1} (b _ {k} - b _ {k + 1}) D _ {k} (x) - b _ {n} D _ {n - 1} (x) + b _ {m} D _ {m} (x),
$$

where $D_{k}(x) = \sin x + \sin 2x + \dots +\sin kx$ . Now putting

$$
r _ {n} (x) = \sum_ {k = n} ^ {\infty} b _ {k} \sin k x,
$$

we get

$$
\left| r _ {n} (x) \right| \leq \sum_ {k = n} ^ {\infty} \left(b _ {k} - b _ {k + 1}\right) \left| D _ {k} (x) \right| + b _ {n} \left| D _ {n - 1} (x) \right|. \tag {1}
$$

Let $\varepsilon > 0$ be chosen arbitrarily. Then there is $n_0 \in \mathbb{N}$ such that $0 \leq nb_n < \varepsilon$ whenever $n \geq n_0$ . We have $r_n(0) = 0$ , and if $x \in (0, \pi/4]$ , then there is $N$ such that $\frac{1}{N} < x \leq \frac{1}{N-1}$ . If $n \geq n_0$ , then two cases are possible: either $n \geq N$ or $n < N$ . In the first case, by (1) and by the inequality $|D_k(x)| \leq \frac{\pi}{x}$ , we get

$$
\left| r _ {n} (x) \right| \leq b _ {n} \frac {\pi}{x} + b _ {n} \frac {\pi_ {i}}{x} <   2 \pi N b _ {n} \leq 2 \pi n b _ {n} <   2 \pi \varepsilon ,
$$

and, in the second case,

$$
\begin{array}{l} \left| r _ {n} (x) \right| \leq \left| \sum_ {k = n} ^ {N - 1} b _ {k} \sin k x \right| + \left| \sum_ {k = N} ^ {\infty} b _ {k} \sin k x \right| \\ \leq \sum_ {k = n} ^ {N - 1} k b _ {k} x + 2 \pi \varepsilon \leq \frac {N - n}{N - 1} \varepsilon + 2 \pi \varepsilon \leq (2 \pi + 1) \varepsilon . \\ \end{array}
$$

This shows that $r_n(x)$ converges uniformly to zero on $[0, \pi/4]$ .

To prove the necessity of the condition, assume that the series $\sum_{n=1}^{\infty} b_n \sin nx$ converges uniformly on $[0, 2\pi]$ . Then, by the Cauchy criterion for uniform convergence, given $\varepsilon > 0$ , there is $n_0$ such that

$$
\left| \sum_ {k = n + 1} ^ {2 n} b _ {k} \sin k x \right| <   \varepsilon
$$

for all $n \geq n_0$ and $x \in [0, 2\pi]$ . Putting $x = \frac{\pi}{4n}$ , we get $\frac{\pi}{4} \leq kx \leq \frac{\pi}{2}$ for $k = n + 1, \ldots, 2n$ , and therefore,

$$
\varepsilon > \frac {1}{\sqrt {2}} \sum_ {k = n + 1} ^ {2 n} b _ {k} \geq \frac {1}{\sqrt {2}} n b _ {2 n},
$$

which gives $2nb_{2n} < 2\sqrt{2}\varepsilon$ . It then follows that $\lim_{n\to \infty}nb_n = 0$

2.5.57. It follows from the preceding that if $\lim_{n\to \infty}nb_n = 0$ , then the series $\sum_{n = 1}^{\infty}b_n\sin nx$ converges uniformly to a continuous function. Assume now that $\sum_{n = 1}^{\infty}b_n\sin nx$ is the Fourier series of a continuous function $f$ . By the result in 2.5.50 the sequence $\{\sigma_n(x)\}$ of the Cesàro means of $\sum_{n = 1}^{\infty}b_n\sin nx$ converges uniformly to $f$ . Hence $f(0) = 0$ , and $\sigma_n\left(\frac{\pi}{n}\right)$ converges to zero as $n\to \infty$ . Since $\sin x > \frac{2x}{\pi}$ for $0 < x < \frac{\pi}{2}$ , we see that

$$
\begin{array}{l} \sigma_ {n} \left(\frac {\pi}{n}\right) \geq \frac {1}{n} \sum_ {k = 1} ^ {[ n / 2 ]} (n - k) b _ {k} \sin \frac {k \pi}{n} \\ \geq \frac {1}{n} \sum_ {k = 1} ^ {[ n / 2 ]} 2 k b _ {k} \left(1 - \frac {k}{n}\right) \geq \frac {1}{n} \sum_ {k = 1} ^ {[ n / 2 ]} 2 k b _ {k} \left(1 - \frac {[ n / 2 ]}{n}\right) \\ \end{array}
$$

$$
\geq \frac {1}{n} \sum_ {k = 1} ^ {[ n / 2 ]} k b _ {k} \geq \frac {1}{n} b _ {[ n / 2 ]} \frac {[ n / 2 ] ([ n / 2 ] + 1)}{2},
$$

which implies that $[n / 2]b_{[n / 2]}$ tends to zero as $n\to \infty$

2.5.58. If $\sum_{n=1}^{\infty} b_n \sin nx$ is the Fourier series of a bounded function, then the sequence $\{\sigma_n(x)\}$ of the Cesàro means of $\sum_{n=1}^{\infty} b_n \sin nx$ is bounded (see 2.5.41). In particular, $\{\sigma_n(\pi/n)\}$ is bounded, and one can proceed as in the solution of the previous problem to show that $nb_n = O(1)$ . Now assume that $nb_n = O(1)$ ; that is, there is $C > 0$ such that $nb_n \leq C$ , for $n \in \mathbb{N}$ . Our aim is to show that there is a constant $M$ such that for all $x$ and $n$ ,

$$
| s _ {n} (x) | = \left| \sum_ {k = 1} ^ {n} b _ {k} \sin k x \right| \leq M.
$$

Without loss of generality we can assume that $0 < x < \pi$ . Then for $\frac{\pi}{N + 1} < x \leq \frac{\pi}{N}$ we have

$$
| \sigma_ {n} (x) | \leq \sum_ {k = 1} ^ {N} b _ {k} \sin k x + \left| \sum_ {k = N + 1} ^ {n} b _ {k} \sin k x \right|
$$

(an empty sum being counted as zero) and

$$
\sum_ {k = 1} ^ {N} h _ {k} \sin k x \leq x \sum_ {k = 1} ^ {N} k b _ {k} \leq \pi C.
$$

Moreover, summation by parts gives

$$
\begin{array}{l} \left| \sum_ {k = N + 1} ^ {n} b _ {k} \sin k x \right| \\ = \left| \sum_ {k = N + 1} ^ {n - 1} \left(b _ {k} - b _ {k + 1}\right) \left(D _ {k} (x) - D _ {N} (x)\right) + b _ {n} \left(D _ {n} (x) - D _ {N} (x)\right) \right|, \\ \end{array}
$$

where

$$
| D _ {k} (x) | = \left| \sum_ {j = 1} ^ {k} \sin j x \right| \leq \frac {1}{\sin \frac {x}{2}} \leq \frac {\pi}{x} <   N + 1.
$$

So,

$$
\left| \sum_ {k = N + 1} ^ {n} b _ {k} \sin k x \right| \leq 2 (N + 1) b _ {N + 1} \leq 2 C.
$$

Thus our claim is proved. It then follows that the pointwise limit of $s_n(x)$ is a bounded function, say $f(x)$ , and Lebesgue's dominated convergence theorem can be used to show that $\sum_{n=1}^{\infty} b_n \sin nx$ is the Fourier series for $f$ .

2.5.59. It follows from the Dirichlet test that $\frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos nx$ is pointwise convergent, say to $f(x)$ , for $x \neq 2k\pi$ , $k \in \mathbb{Z}$ . We now show that $f$ is nonnegative. Set

$$
s _ {n} (x) = \frac {a _ {0}}{2} + \sum_ {k = 1} ^ {n} a _ {k} \cos k x.
$$

Then, by the Abel transformation,

$$
s _ {n} (x) = \sum_ {k = 0} ^ {n - 1} \left(a _ {k} - a _ {k + 1}\right) K _ {k} (x) + a _ {n} K _ {n} (x) = \sum_ {k = 0} ^ {n - 1} \Delta a _ {k} K _ {k} (x) + a _ {n} K _ {n} (x),
$$

where

$$
K _ {n} (x) = \frac {1}{2} + \cos x + \cos 2 x + \dots + \cos n x = \frac {\sin \left(n + \frac {1}{2}\right) x}{2 \sin \frac {x}{2}}.
$$

By the Abel transformation, again,

$$
s _ {n} (x) = \sum_ {k = 0} ^ {n - 2} (\Delta a _ {k} - \Delta a _ {k + 1}) \sum_ {j = 0} ^ {k} K _ {j} (x) + \Delta a _ {n - 1} \sum_ {j = 0} ^ {n - 1} K _ {j} (x) + a _ {n} K _ {n} (x).
$$

Since

$$
\sum_ {j = 0} ^ {k} K _ {j} (x) = \frac {\sin^ {2} \frac {(k + 1) x}{2}}{2 \sin^ {2} \frac {x}{2}}
$$

and, by assumption, $\Delta a_{k} - \Delta a_{k + 1} = a_{k} - 2a_{k + 1} + a_{k + 2}\geq 0$ we see that

$$
f (x) = \lim  _ {n \rightarrow \infty} s _ {n} (x) = \sum_ {k = 0} ^ {\infty} \left(\Delta a _ {k} - \Delta a _ {k + 1}\right) \sum_ {j = 0} ^ {k} K _ {j} (x) \geq 0.
$$

We know that the series $\frac{a_n}{2} + \sum_{n=1}^{\infty} a_n \cos nx$ converges uniformly on $[\varepsilon, \pi]$ . Thus

$$
\begin{array}{l} \int_ {c} ^ {\pi} f (x) d x = \frac {a _ {0}}{2} (\pi - \varepsilon) + \sum_ {n = 1} ^ {\infty} a _ {n} \int_ {c} ^ {\pi} \cos n x d x \\ = \frac {a _ {0}}{2} (\pi - \varepsilon) - \sum_ {n = 1} ^ {\infty} a _ {n} \frac {\sin n \varepsilon}{n}. \\ \end{array}
$$

By the solution to 2.5.57 the last series converges uniformly on $[0, \pi]$ , so, letting $\varepsilon$ go to zero, we get

$$
\int_ {0} ^ {\pi} f (x) d x = \lim  _ {\varepsilon \rightarrow 0} \int_ {\varepsilon} ^ {\pi} f (x) d x = \frac {a _ {0}}{2} \pi .
$$

Since $f$ is even, we see that

$$
a _ {0} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (x) d x.
$$

Likewise,

$$
\begin{array}{l} \int_ {x} ^ {\pi} f (x) \cos k x d x \\ = \frac {a _ {0}}{2} \int_ {\epsilon} ^ {\pi} \cos k x d x + \sum_ {n = 1} ^ {k - 1} a _ {n} \int_ {\epsilon} ^ {\pi} \cos k x \cos n x d x \\ + a _ {k} \int_ {\epsilon} ^ {\pi} \cos^ {2} k x d x + \sum_ {n = k + 1} ^ {\infty} a _ {n} \int_ {\epsilon} ^ {\pi} \cos k x \cos n x d x, \\ \end{array}
$$

and letting $\varepsilon$ to zero, we obtain

$$
\begin{array}{l} \lim  _ {\epsilon \rightarrow 0} \int_ {\epsilon} ^ {\pi} f (x) \cos k x d x \\ = a _ {k} \frac {\pi}{2} + \lim  _ {\epsilon \rightarrow 0} \sum_ {n = k + 1} ^ {\infty} a _ {n} \int_ {\epsilon} ^ {\pi} \cos k x \cos n x d x \\ = a _ {k} \frac {\pi}{2} + \lim  _ {\varepsilon \rightarrow 0} \sum_ {n = k + 1} ^ {\infty} a _ {n} \left(\frac {\sin (k + n) \varepsilon}{2 (k + n)} + \frac {\sin (n - k) \varepsilon}{2 (n - k)}\right) = a _ {k} \frac {\pi}{2}, \\ \end{array}
$$

where the last equality can be derived as above.

# Bibliography - Books

[1] T. M. Apostol, Mathematical Analysis, Addison-Wesley Publishing Company, Inc., Reading, Mass., 1957.   
[2] N. K. Bari, A treatise on trigonometric series. Vols. I, II, Pergamon Press, Oxford, and Macmillan, New York, 1964.   
[3] P. Biler, A. Witkowski, *Problems in Mathematical Analysis*, Marcel Dekker, Inc., New York and Basel, 1990.   
[4] F. Burk, Lebesgue Measure and Integration, A Wiley-Interscience Publication. John Wiley & Sons, Inc., New York, 1998.   
[5] D. L. Cohn, Measure Theory, Birkhäuser, Boston, Basel, Berlin, 1993.   
[6] A. J. Dorogovcev, Matematicheskij analitz. Spravočnoe posobe, Vysshaja Skola, Kiev, 1985.   
[7] A. J. Dorogovcev, Matematicheskij analiz. Sbornik zadač, Vyšcaja Škola, Kiev, 1987.   
[8] R. E. Edwards, Fourier series. Vol. I., Holt, Rinehart and Winston, Inc., New York, Montreal, London, 1967.   
[9] L. C. Evans, R. E. Gariepy, Measure Theory and Fine Properties of Functions, RCC Press, Boca Raton Fla., New York, London, Tokyo, 1999.   
[10] G. M. Fichtenholz, Differential-und Integralrechnung, I, II, III, V.E.B. Deutscher Verlag Wiss., Berlin, 1966-1968.   
[11] B. R. Gelbaum, J. M. H. Olmsted, Theorems and Counterexamples in Mathematics, Springer-Verlag, New York, Berlin, Heidelberg, 1990.   
[12] G. H. Hardy, J. E. Littlewood, G. Polya, Inequalities, Cambridge University Press, 1963.

[13] E. Hewitt, K. Stromberg, Real and Abstract Analysis, Springer-Verlag, New York, Berlin, Heidelberg, 1965.   
[14] E. W. Hobson, The Theory of Functions of a Real Variable. Vols. I, II, Dover Publications, Inc., New York, 1958.   
[15] W. J. Kaczor, M. T. Nowak, Problems in Mathematical Analysis I. Real Numbers, Sequences and Series, American Mathematical Society, Providence, RI, 2000.   
[16] W. J. Kaczor, M. T. Nowak, Problems in Mathematical Analysis II. Continuity and Differentiation, American Mathematical Society, Providence, RI, 2001.   
[17] G. Klambauer, Mathematical Analysis, Marcel Dekker, Inc., New York, 1975.   
[18] G. Klambauer, Real Analysis, American Elsevier Publishing Company, Inc., New York London Amsterdam, 1973.   
[19] S. Lojasiewicz, An Introduction to the Theory of Real Functions, A Wiley-Interscience Publication, John Wiley & Sons, Ltd., Chichester, 1988.   
[20] D. S. Mitrinovic, Analytic Inequalities, Springer-Verlag, New York, Berlin, Heidelberg, 1970.   
[21] M. E. Munroe, Introduction to Measure and Integration, Addison-Wesley Publishing Company, Inc., Cambridge, Mass., 1953.   
[22] I. P. Natanson, Teoria funkcjij vescestvennoj peremennoj. (Russian), Gosudarstv. Izdat. Tehn.-Teoret. Lit., Moscow, 1950; English trans., Vols. 1,2, Ungar, New York, 1955, 1961.   
[23] J. Niewiarowski, Zadania z teori miary, (Polish), Wydawnictwo Uni- wersytetu Łódzkiego, Łódź, 1999.   
[24] Yu. S. Očan, Sbornik zadač po matematíceskomu analizu, (Russian), Prosveženie, Moskva, 1981.   
[25] G. Pólya, G. Szegö, Problems and Theorems in Analysis I, Springer-Verlag, Berlin Heidelberg New York, 1978.   
[26] W. W. Rogosinski, Volume and Integral, Oliver and Boyd, Edinburgh and London; Interscience Publishers, Inc., New York, 1952.   
[27] H. L. Royden, Real Analysis, The Macmillan Company, New York, and Collier-Macmillan Limited, London, 1968.   
[28] W. Rudin, Principles of Mathematical Analysis, McGraw-Hill Book Company, New York, 1964.   
[29] R. Sikorski, Funkcje rzechywiste, (Polish), PWN, Warszawa, 1958.   
[30] P. N. de Souza, J.-N. Silva, Berkeley Problems in Mathematics, Springer-Verlag, New York, 1998.

[31] E. C. Titchmarsh, The Theory of Functions, Oxford University Press, 1939.   
[32] E. T. Whittaker, G. N. Watson, A Course of Modern Analysis, Cambridge University Press, 1963.   
[33] A. Zygmund, Trigonometric series. Vols. I, II, Cambridge University Press, 1959.

# Index

Abel test for convergence of improper integrals, 33  
absolutely continuous function, 77  
almost everywhere, 65  
approximation theorem for measurable functions, 65  
Arzelà theorem, 20

Banach indicatrix, 78  
Banach-Zarecki theorem, 78  
Bernstein theorem, 87  
Bessel's inequality, 86  
Bonnet form of second mean value theorem, 18

Cantor function, 66  
Carathéodory condition, 57  
Cauchy theorem, 31  
Cesàro mean of the Fourier series, 88  
change of variable formula, 15  
for Lebesgue integrals, 79  
Chebyshev inequality, 44  
convergence in measure, 68

Dinl-Lipschitz test for convergence of Fourier series, 84  
Dirichlet test for convergence of improper integrals, 33  
Dirichlet-Jordan test for convergence of Fourier series, 84  
duplication formula, 41

Egorov theorem, 67  
elementary set, 52  
equi-integrable functions, 74  
essential supremum, 70

essentially bounded function, 70 Euler's beta function, 41 Euler's gamma function, 35

Fatou lemma for Riemann integrals, 20   
Fatou theorem, 90   
Fejer kernel, 334   
Fejer theorem, 89   
Fejer-Lebesgue theorem, 89   
first mean value theorem, 9   
Fourier coefficients, 82   
Fourier series, 82   
Frechet theorem, 69   
Fresnel's integrals, 39   
function Lobesgue measurable, 64 of bounded variation, 10 of negative variation, 10 of positive variation, 10 simple, 65 singular, 80

Holly selection theorem, 18  
Helly theorem, 18  
Holder condition, 12  
Holder Inequality, 46

integration by parts for Lobesgue Integrals and absolutely continuous functions, 80

Jensen inequality, 47 for Lebesgue integral, 76

Lebesgue constants. 88

Lebesgue criterion for Riemann integrability, 64

Lebesgue inner measure, 59

Lebesgue point, 80

Lebesgue theorem, 69

Lipschitz condition, 114

Lipschitz condition of order $\alpha$ , 12

Lipschitz constant, 114

Lusin theorem, 68

mesh, 3

Minkowski inequality, 48

monotone convergence theorem for the

Riemann integral, 20

Opial inequality, 51

pairwise separate sets, 52

Parseval formula, 325

partial integration formula, 15

point

of approximate continuity, 81

of density, 62

of dispersion, 62

of outer density, 81

of outer dispersion, 81

Riesz theorem, 69

saltus function, 14

Schwarz inequality, 42

second mean value theorem, 18

separate intervals, 52

Steffensen inequality, 49

step function, 6

Stirling formula, 42

total variation, 10

translate of a function by t, 76

uniform convergence of an improper integral, 35

Vitali sat, 63

Vitali theorem, 69

Wionar theorem, 90

Young inequality, 45

We learn by doing. We learn mathematics by doing problems. This is the third volume of Problems in Mathematical Analysis. The topic here is integration for real functions of one real variable. The first chapter is devoted to the Riemann and the Riemann-Stieltjes integrals. Chapter 2 deals with Lebesgue measure and integration.

The authors include some famous, and some not so famous, integral inequalities related to Riemann integration. Many of the problems for Lebesgue integration concern convergence theorems and the interchange of limits and integrals. The book closes with a section on Fourier series, with a concentration on Fourier coefficients of functions from particular classes and on basic theorems for convergence of Fourier series.

The book is primarily geared toward students in analysis, as a study aid, for problem-solving seminars, or for tutorials. It is also an excellent resource for instructors who wish to incorporate problems into their lectures. Solutions for the problems are provided in the book.

![](images/4b7cd9a25c770f52e4476d3207bceb623762515c87019b850046ae3ae21227ab.jpg)

For additional information and updates on this book, visit

www.ams.org/bookpages/std-21

![](images/11db9e8d4ad863cbdcddec6007d923cac222ff2ea0eb50d81aba108bfff89159.jpg)