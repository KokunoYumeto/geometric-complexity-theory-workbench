# The hypotheses of Mulmuley's flip for permanent and determinant, after Kumar and Bürgisser–Ikenmeyer–Panova

Research note WB-0002, version 0.1 of 22 November 2026. It is a note for checking and reuse; a paper is in preparation.

K. Mulmuley's *Geometric Complexity Theory VI* proposes to construct explicit obstructions to the determinant containing
the padded permanent, from three hypotheses: rational singularities (RH), positivity (PH1) and the existence of short
robust obstructions (OH). We show that RH is false for every m > n ≥ 2, that PH1 on the determinant's side is false as
stated, and that OH contradicts the counting clauses of PH1 for m ≥ (n+1)^25. The first result extends a theorem of
S. Kumar, and the third rests on the theorem of P. Bürgisser, C. Ikenmeyer and G. Panova that occurrence obstructions
don't exist in that range. The text and proofs are AI-produced (Claude Opus 5.5 at effort max, with an independent
re-proof by Claude Opus 5.5 at effort high). No human has checked them.

## Why it matters

Geometric complexity theory, begun by Mulmuley and Sohoni, is a programme to prove that the permanent is not a small
determinant, the algebraic analogue of separating NP from P, by finding representations that occur for one orbit closure
and not for the other. The *flip* of GCT VI is its proposal for how such representations could be found explicitly:
positivity would turn their existence into questions about polytopes, which algorithms can answer. Theorem
`texplicitperm` of that paper makes this exact for permanent and determinant. These are that theorem's hypotheses.

## What GCT VI assumes

References are to arXiv:0704.0229v4, the chapter on verification and discovery of obstructions, in the setting of
permanent and determinant. Let n be the size of the permanent and m > n that of the determinant, g = det\_m, and
G = GL(m²). Let X′ consist of the n² variables of the permanent and a further variable y, H = GL(X′),
f′ = y^(m−n) per\_n in W′ = Sym^m(X′), and Z the closure of the cone over the orbit of f′, with coordinate ring
R = R\_W′[f′]. Put s^λ\_d for the multiplicity of V\_λ(H) in the dual of R\_d, and m^d\_λ for the multiplicity of the
G\_g-module (Cg)^d in V\_λ(G). The bit length of a number is written ⟨·⟩.

- **RH:** Spec R has rational singularities.
- **PH1** (`hph1det`, `phph1Z`): there are polytopes Q for m^d\_λ and P for s^λ\_d whose numbers of integer points are
  these multiplicities, whose Ehrhart quasi-polynomials are the stretching functions k ↦ m^(kd)\_(kλ) and
  k ↦ s^(kλ)\_(kd), and which have short encodings: for Q, ⟨Q⟩ is polynomial in n, ⟨m⟩, ⟨d⟩ and ⟨λ⟩. The encoding
  length of a polytope in R^N is N plus the bit length of an inequality.
- **OH:** for every large n there is λ of bit length polynomial in n, m dividing |λ| and d = |λ|/m, such that either Q
  is empty and P isn't, or both are nonempty and the affine span of P has an integer point while that of Q has none.

The theorem takes m = poly(n), or even 2^polylog(n). The paper stresses that the bounds must be uniform in m.

## The results

**Theorem 1** (WB-0002.001). For every m > n ≥ 2, Spec R is not normal. So RH is false.

**Theorem 2** (WB-0002.002). `hph1det` is false. For λ = (m−1, 1) and d = 1 a polytope with the required count needs
at least m − 2 coordinates, while the required encoding length is polynomial in n and log m.

**Theorem 3** (WB-0002.003). Let n ≥ 2 and m ≥ (n+1)^25, and suppose that polytopes P and Q have only the counting
property of PH1, for all large k. Then no λ, of any bit length, satisfies either condition of OH.

In words: the first hypothesis fails for every pair of sizes to which the theorem applies, so its premises never hold.
The second fails for a representation with two rows in degree one. In the range of the third such polytopes give no
robust obstruction at all.

**What is supplied here, and what isn't ours.** Kumar proved that this variety isn't normal for n ≥ 3 and m ≥ 2n (Comment. Math. Helv. 88
(2013), Corollary 8.3); Theorem 1 covers every m > n ≥ 2, by a different and short argument. The absence of occurrence
obstructions for m ≥ n^25, with a variable of the permanent as padding, is the theorem of Bürgisser–Ikenmeyer–Panova
(J. Amer. Math. Soc. 32 (2019)). What is supplied for Theorem 3 is the passage to GCT VI's separate padding variable,
and from occurrence to both conditions of OH. A search of the literature hasn't been completed, and we claim no
priority for any statement.

**The neighbouring work.** E. Briand, R. Orellana and M. Rosas showed by examples that stretched Kronecker coefficients
violate the saturation conjecture of the first versions of GCT VI (arXiv:0810.3163); Mulmuley relaxed it in an appendix to their paper. T. Kahle and
M. Michałek found plethysm rays whose stretching function is the Ehrhart function of no polytope (arXiv:1507.07131). J. Dörfler, C. Ikenmeyer and G. Panova showed that
multiplicity obstructions can be stronger than occurrence obstructions (arXiv:1901.04576); Theorem 3 concerns the
robust obstructions of OH, and these lead to occurrence obstructions.

## Why the proofs work

The padded permanent remembers its padding: a point ℓ^(m−n) q determines the line of ℓ by unique factorization. So the
cone of the tensors ℓ^(m−n) ⊗ q maps finitely and birationally onto Z, and it has more functions of degree one. For a
normal Z such a map would be an isomorphism. For PH1, two-row representations see only binary forms, and every binary form is a
determinant, so that the multiplicities are partition numbers. Along one ray their growth has degree m − 2, and a
polytope needs at least that many coordinates to count them. For OH, stretching turns either condition into an
occurrence obstruction at some degree, and Bürgisser–Ikenmeyer–Panova exclude those.

## Proof of Theorem 1

Put p = m − n ≥ 1, let U be the span of X′, and let E ⊂ Sym^n U be the closure of the GL(U)-orbit of per\_n. It is an
irreducible GL(U)-stable cone, so it spans Sym^n U. Every point of the orbit of f′ is ℓ^p q with ℓ in U and q in E,
and the set of these products is closed and irreducible, the image of a projective variety under a morphism. Hence
Z = {ℓ^p q}.

Let S = ⊕\_d Sym^(pd)(U*) ⊗ C[E]\_d, the coordinate ring of the cone of the tensors ℓ^p ⊗ q. It is a domain. The
multiplication map π: Spec S → Z is dominant, so R ⊂ S. It is finite, since it is linear and kills no nonzero point
of that cone. It is birational: for general q the form is irreducible of degree n ≥ 2, so ℓ^p q determines the line of
ℓ, and then the tensor.

The space S\_1 is dual to Sym^p U ⊗ Sym^n U, while R\_1 is a quotient of the dual of Sym^m U. The multiplication
Sym^p U ⊗ Sym^n U → Sym^m U is surjective and not injective, as dim U ≥ 2. So dim R\_1 < dim S\_1 and R ≠ S. If R were
normal, the finite extension S inside its field of fractions would equal R. So R isn't normal, and a rational
singularity is normal by definition. ∎

## Proof of Theorem 2

Let β = (dm−b, b) with 2b ≤ dm, and let B(b) be the number of partitions of b in an m × d box, B(−1) = 0. For a partition α
of em write K(α,e) for the multiplicity of α in degree e of the coordinate ring of the closure of G·g. The dual labelling gives
the same numbers here. We claim that

  K(β,d) = m^d\_β = B(b) − B(b−1).

*Lower bound for K.* By Cayley–Sylvester the highest-weight vectors of weight β in Sym^d Sym^m(C²) form a space of
dimension B(b) − B(b−1). They involve only the coefficients of binary forms. A binary form of degree m is a product
of m linear forms, the determinant of a diagonal pencil, and so lies in the closure of G·g. Therefore none of these
vectors vanishes there, and K(β,d) is at least that number.

*K(α,e) ≤ m^e\_α for every α.* Evaluation at g sends an equivariant map from V\_α to that coordinate ring in degree e
injectively to a functional on V\_α on which the stabilizer of g
acts by the e-th power of its character: if the functional is zero, the map vanishes on the orbit and on its closure.

*Upper bound for m^d\_β.* The connected stabilizer gives m^d\_β ≤ g(β, μ, μ), the Kronecker coefficient with μ = (d^m).
For N = dm the inner product of [μ]⊗[μ] with the character induced from the trivial one of S\_(N−b) × S\_b is the sum of
the squares of the Littlewood–Richardson numbers c^μ\_(ρν), ν a partition of b. In a rectangle ρ is determined by
ν ⊂ μ and the number is 1, so the sum is B(b). Subtracting the same for b − 1 gives
g(β, μ, μ) = B(b) − B(b−1), and the claim follows.

Now let λ = (m−1, 1), d = 1 and m ≥ 3. At β = kλ the box is m × k, and B(k) counts the partitions of k into parts at
most m. Hence

  m^k\_(kλ) = [z^k] ∏\_(i=2)^m (1 − z^i)^(−1),

a quasi-polynomial of degree m − 2 on every residue class, as both 2 and 3 are parts. A polytope in R^N has O(k^N)
integer points in its k-th dilation, so N ≥ m − 2, and the encoding length is at least N. The hypothesis gives a fixed
bound C(n + log m)^e on it, since ⟨d⟩ and ⟨λ⟩ are O(log m). For m = n^(e+2), or m = 2^(⌈log n⌉²), and n large this is
less than m − 2. The height of λ is 2 ≤ n²+1, so the hypothesis is false. ∎

If a new polynomial were allowed for each family m = n^c, the first choice of m wouldn't contradict it, and the second
still would. GCT VI doesn't allow that reading.

## Proof of Theorem 3

*No occurrence obstructions with the separate variable.* Substituting diag(y, X) in per\_(n+1) gives y·per\_n(X). So
y^(m−n) per\_n(X) is a substitution of X\_11^(m−n−1) per\_(n+1), and its orbit closure lies in that of the latter. By the
theorem of Bürgisser–Ikenmeyer–Panova for the permanent of size n+1, every representation that occurs in the
coordinate ring of the latter, in degree e, occurs in that of det\_m, as m ≥ (n+1)^25. The same then holds for the
former, since restriction to a closed stable subvariety is surjective. GCT VI records (from GCT II, Theorem 8.2) that
V\_α(G) occurs for the orbit closure of y^(m−n) per\_n if and only if V\_α(H) occurs for Z. So

  s^α\_e > 0 implies K(α,e) > 0, hence m^e\_α > 0

(the labellings being the same on both sides).

*The two conditions.* Let s(k) = s^(kλ)\_(kd) and t(k) = m^(kd)\_(kλ). For all large k these are the numbers of integer
points of kP and kQ, and s(k) > 0 implies t(k) > 0. If Q is empty and P isn't, take k a large multiple of the
denominators of a rational point of P: then s(k) > 0 and t(k) = 0, a contradiction. If both are nonempty and the
affine span of P has an integer point, the integer points have full rank in that span, so kP has one for every large
k. Hence so does kQ. Take integer points x in kQ and x′ in (k+1)Q: then x′ − x is an integer point of the affine span
of Q. So the second condition fails too. ∎

## What is not decided here

- PH1 for s^λ\_d (`phph1Z`).
- OH in the range m < (n+1)^25. The check record extends Theorem 3 to m ≥ n^25 for n ≥ 5, from that paper's
  propositions.
- SH(a) and PH2 for m^d\_λ itself.
- The corresponding hypotheses for the class varieties that GCT VI uses for P against NP.

## Method and checks

The statements were found and first proved by Claude Opus 5.5 at effort max on 22 November 2026. Claude Opus 5.5 at
effort high then proved them again from the statements, without opening that proof, sharpened the first two and found
and repaired a wrong citation in the third. This note follows the second proof: `checks/INDEPENDENT_CHECK.md`. The
definitions were read in GCT VI's source and the theorem of Bürgisser–Ikenmeyer–Panova in theirs; their proof wasn't
re-proved. `checks/check.py` verifies small cases and inequalities (`python -I -B checks/check.py`, expected output in
`checks/check_output.txt`). No human has checked this note.

Where we hold rights in this text, they are dedicated to the public domain under CC0 1.0.

## References

- P. Bürgisser, C. Ikenmeyer, G. Panova, No occurrence obstructions in geometric complexity theory, J. Amer. Math.
  Soc. 32 (2019), 163–193; https://arxiv.org/abs/1604.06431.
- E. Briand, R. Orellana, M. Rosas, Reduced Kronecker coefficients and counter-examples to Mulmuley's strong
  saturation conjecture SH, Computational Complexity 18 (2009); https://arxiv.org/abs/0810.3163.
- J. Dörfler, C. Ikenmeyer, G. Panova, On geometric complexity theory: multiplicity obstructions are stronger than
  occurrence obstructions, https://arxiv.org/abs/1901.04576.
- T. Kahle, M. Michałek, Obstructions to combinatorial formulas for plethysm, https://arxiv.org/abs/1507.07131.
- S. Kumar, Geometry of orbits of permanents and determinants, Comment. Math. Helv. 88 (2013);
  https://arxiv.org/abs/1007.1695.
- K. Mulmuley, Geometric complexity theory VI: the flip via saturated and positive integer programming in
  representation theory and algebraic geometry, https://arxiv.org/abs/0704.0229v4.
- K. Mulmuley, M. Sohoni, Geometric complexity theory I and II, SIAM J. Comput. 31 (2001) and 38 (2008).
