# Independent check of two statements on GCT VI's explicit-obstruction theorem

Claude Opus 5.5 at effort high (agent a17221e5), 22 November 2026, for the main session (Claude Opus 5.5 at effort max).
`THE_THREE_HYPOTHESES_20261122.md` and `ph1det_check.py` in this folder were not opened. The proofs below are my own.
Where a published theorem or proposition is used, it is named.

Notation is GCT VI's: n is the size of the permanent, m > n that of the determinant, X′ the n² + 1 variables (those
of X and the padding variable y, which is **not** an entry of X), f′ = y^{m−n} perm_n, Z = the closure of GL(X′)·f′,
g = det_m. Bürgisser-Ikenmeyer-Panova (BIP) use n and m the other way round. Their statements are rewritten here in
GCT VI's letters.

## Verdicts

| statement | verdict |
|---|---|
| **A** | **Proved**, for `hph1det` as written: one polynomial in n, ⟨m⟩, ⟨d⟩, ⟨λ⟩. The degree m − 3 for (2m,2m) is right for m ≥ 3. A simpler witness also works, and it survives restricting the hypothesis to λ that can occur for the padded permanent. The limit of the proof is in A.5. |
| **B, RH** | **Proved, and more:** Spec R_{W′}[f′] is non-normal for **every** m > n ≥ 2. Neither m ≥ 2n nor n ≥ 3 is needed. Kumar's Corollary 8.3 concerns the same variety and agrees in its range. |
| **B, PH1** | **Proved for `hph1det`**, as in A. `phph1Z`, the other half of the theorem's PH1, is not refuted here. |
| **B, OH with PH1** | **Proved for m ≥ n^25, n ≥ 5** (so for every large n, which is what OH asks). BIP's theorem **cannot be cited as it stands**: it is about internal padding. The transfer is in B.3. The contradiction needs only the counting clauses of PH1, with no bound on bit length. |
| **B as one sentence** ("all three fail") | True with these scopes. For a fixed family m = n^c with c < 25, only the failure of RH is proved: A needs uniformity there, and OH is untouched. Since RH fails for every m > n ≥ 2, the theorem's premises are never satisfied there either. |

## 0. A lemma used twice

Let K_m(λ,d) be the multiplicity of V_λ(G) in the degree-d part of the coordinate ring of the closure of G·g, in
either of the two dual labellings. **Then K_m(λ,d) ≤ m^d_λ.**

*Proof.* Send a G-map φ: V_λ → R_V[g]_d to the functional v ↦ φ(v)(g). For σ ∈ G_g one has σg = χ(σ)g, so homogeneity
makes the functional transform by the d-th power of χ: it is an element of the space whose dimension is m^d_λ. If it is
zero, then φ(v)(σg) = φ(σ^{-1}v)(g) = 0 for all σ, so φ = 0 on the orbit and hence on its closure. The map is
injective. ∎

Here G_g is the whole stabilizer, transposition included. Its connected component gives the ordinary Kronecker
coefficient g(λ,(d^m),(d^m)), so m^d_λ ≤ g(λ,(d^m),(d^m)).

## A. `hph1det`

### A.1 The two-row multiplicities, whatever the convention

Let β = (dm−b, b) with 2b ≤ dm, and let B(b) be the number of partitions of b in an m × d box, with B(−1) = 0. Then

> K_m(β,d) = m^d_β = g(β,(d^m),(d^m)) = B(b) − B(b−1).

*Proof.*
- *Lower bound.* By Cayley-Sylvester the space of highest-weight vectors of weight β in Sym^d Sym^m C² has dimension
  B(b) − B(b−1). Such a vector uses only binary coefficients. Every binary form of degree m is a product of m linear
  forms, so it is the determinant of a diagonal pencil and lies in the closure of G·g. A nonzero vector therefore does
  not vanish there: K_m(β,d) ≥ B(b) − B(b−1).
- *Upper bound.* For μ = (d^m) and N = dm, the inner product ⟨[μ]⊗[μ], Ind_{S_{N−b}×S_b}^{S_N} 1⟩ is the sum of the
  squared Littlewood-Richardson numbers c^μ_{ρν} over ν ⊢ b. In a rectangle the complement ρ of each ν ⊂ μ is unique
  and the number is 1, so the sum is B(b). Subtracting the same for b − 1 gives g = B(b) − B(b−1).
- Lemma 0 and m^d_β ≤ g close the chain. ∎

So the symmetric and the ordinary coefficient agree here. Taking duals changes neither. Padding does not enter m^d_λ.

### A.2 The witness (2m,2m)

Here d = 4, the height is 2 ≤ n²+1, and for m ≥ 3

> F(s) := m^{4s}_{s(2m,2m)} = dim C[V_m]^{SL_2}_{4s}, with V_m the space of binary forms of degree m.

Let R = C[V_m]^{SL_2}.
- *Its dimension is m − 2.* The generic stabilizer is finite. SL_2 has no nontrivial character and C[V_m] is
  factorial, so the field of invariants is Frac R and has transcendence degree (m+1) − 3.
- *The Veronese subring R^{(4)}* has the same dimension, so some residue class of its Hilbert quasi-polynomial has
  degree m − 3.
- *All residue classes have that degree.* R_4 ≠ 0: by Hermite reciprocity its dimension is the number of (a,b) with
  2a + 3b = m. Multiplication by a nonzero element of R_4 is injective in the domain R, so F is nondecreasing.

**So F has degree exactly m − 3 in s.**

### A.3 A simpler witness: λ = (m−1, 1), d = 1

By A.1,

> m^{k}_{k(m−1,1)} = B(k) − B(k−1) = [z^k] ∏_{i=2}^{m} (1 − z^i)^{-1},

a quasi-polynomial of degree m − 2 on every residue class (parts 2 and 3 are present). This λ has λ_1 ≥ (m−n)d, so it
also refutes the repair "only for λ that satisfy the first-row condition of padded permanents".

### A.4 The contradiction

Suppose Q ⊂ R^N has #(kQ ∩ Z^N) equal to this stretching function (clauses 1 and 2; agreement for large k is enough).
Q is bounded, so kQ lies in a cube of side O(k) and the count is O(k^N). Hence N ≥ m − 2, respectively N ≥ m − 3. GCT
VI's section "Separation oracle" defines ⟨Q⟩ = N + φ, where N is the number of coordinates of the space containing Q,
so ⟨Q⟩ ≥ N.

Clause 3 gives one polynomial p with ⟨Q⟩ ≤ p(n, ⟨m⟩, ⟨d⟩, ⟨λ⟩). For either witness the last three arguments are
O(log m), so the right side is at most C(n + log m)^e for fixed C and e. Choose:
- m = n^{e+2}, a family with m = poly(n); or
- m = 2^{⌈log n⌉²}, which is 2^{polylog n}.

For large n both exceed C(n + log m)^e + 3. **So `hph1det` is false.** ∎

No complexity assumption is used.

### A.5 Attempts to refute A, and what remains

- **Symmetric against ordinary coefficient:** equal, by A.1.
- **Bit length:** the lower bound uses only the dimension N, which the definition includes. An extended formulation in
  more variables only increases N.
- **Height of λ:** it is 2.
- **The case m = 2:** outside A. The formula m − 3 needs m ≥ 3, and here m > n.
- **Order of quantifiers. This is the one real limit.**
  - If one allowed a new polynomial for each fixed family m = n^c, then m − 2 = poly(n) and neither witness
    contradicts the hypothesis on that family.
  - The family m = 2^{⌈log n⌉²} still does.
  - The text does not allow that reading. It asks for dependence on n and ⟨m⟩ "rather than m", and its remark after
    the theorem asks for polynomial bounds "independent of m, as long as m<< 2^n".

## B. The three assumptions of `texplicitperm`

### B.1 RH fails for every m > n ≥ 2

Put p = m − n ≥ 1, U = (X′)^*, and Ĥ ⊂ Sym^n U the closure of the GL(U)-orbit of perm_n, regarded as a form on X′ by
forgetting y. It is an irreducible GL(U)-stable cone, so it spans Sym^n U.
- *The variety.* An element of the orbit of f′ is ℓ^p h(L), with h = perm_n and (ℓ, L) a basis of U. The map
  (ℓ, q) ↦ ℓ^p q on U × Ĥ has closed image, because it is projective after projectivization (the product vanishes
  only if a factor does). Thus Z = {ℓ^p q : ℓ ∈ U, q ∈ Ĥ}.
- *A second ring.* Let R = C[Z], the ring R_{W′}[f′], and S = ⊕_d Sym^{pd}(U^*) ⊗ C[Ĥ]_d. Then S is a domain generated
  in degree one, and Spec S is the cone of the tensors ℓ^p ⊗ q. Multiplication induces π: Spec S → Z, with R ⊂ S.
- *π is finite.* It is a linear projection and kills no nonzero point of that cone, since ℓ^p q = 0 forces ℓ = 0 or
  q = 0.
- *π is birational.* For generic q the form is irreducible of degree n ≥ 2. So the product determines the line of ℓ
  by unique factorization, and then the tensor ℓ^p ⊗ q.
- *π is not an isomorphism.* S_1 is the dual of Sym^p U ⊗ Sym^n U, since the powers span the first factor and Ĥ the
  second. R_1 is a quotient of the dual of Sym^m U. As
  C(n²+p, p)·C(n²+n, n) > C(n²+m, m), we have R_1 ≠ S_1.

If R were normal, the integral extension S ⊂ Frac R would equal R. **So Spec R is not normal. A rational singularity
is by definition normal, so RH is false.** ∎

*Against Kumar, arXiv:1007.1695.* His section 5 takes 3 ≤ n < m, the variable x_{11} outside the lower right
n × n block as padding, and S spanned by that variable and the block, of dimension n²+1. The variety of his Corollary
8.3 is the closure of GL(S)·p, which is exactly Z. He proves it non-normal for m ≥ 2n. The identification asked for
in the brief holds. The proof above does not use his result.

### B.2 OH contradicts PH1 wherever occurrence obstructions are absent

Assume:

> **(NO)** whenever V_μ(H) occurs in R_{W′}[f′]_e, also K_m(μ,e) > 0.

Let P and Q be any rational polytopes whose lattice-point counts in kP and kQ equal s(k) := s^{kλ}_{kd} and
μ(k) := m^{kd}_{kλ} for all large k. This is weaker than clauses 1 and 2. It does not need s to be a quasi-polynomial
for small k, which GCT VI derives from RH. By (NO) and Lemma 0, **s(k) > 0 ⇒ μ(k) > 0.**
- *OH (a): Q empty, P nonempty.* For a large multiple k of the denominators of a rational point of P, kP has a
  lattice point. So s(k) > 0, hence μ(k) > 0 and kQ is nonempty. This is absurd.
- *OH (b): both nonempty, aff P has an integer point a, aff Q has none.* The lattice in the direction space of aff P
  has full rank there, and k(P − a) eventually contains a ball in that space larger than a covering radius. So kP has
  a lattice point for all large k. Then so does kQ: take x ∈ kQ and x′ ∈ (k+1)Q integral. The point x′ − x is
  integral and is an affine combination, with coefficients k+1 and −k, of two points of Q. So it lies in aff Q. This
  is absurd.

**So no λ, of any bit length, satisfies OH.** The same argument shows that there is no robust obstruction at all. ∎

The conjunction "OH and PH1" would be false by A alone. B.2 says more: it stays false after clause 3 is deleted.

### B.3 (NO) for m ≥ n^25 with GCT VI's padding

**The point at which the direct citation fails.** BIP's Theorem `th:main` is for X_11^{m−n} perm_n, with X_11 an entry
of the permanent, and its proof starts from ℓ(λ) ≤ n². Here ℓ(λ) can be n²+1. BIP say the choice of padding "is
irrelevant" and cite Ikenmeyer-Panova's appendix. That appendix proves only that **containment** in the determinant
closure passes from one padding to the other, with a polynomial enlargement of m. It does not transfer occurrence of
representations at the same m.

**Reduction to ≤ n²+1 rows, proved.** Let μ ⊢ me occur for GCT VI's padded permanent.
- Highest-weight vectors with at most n²+1 rows use only the coefficients in X′, and the projection of the closure of
  G·f to those coefficients is Z. This gives the passage to the reduced variety and ℓ(μ) ≤ n²+1.
- Such a vector P is nonzero at some ℓ^p q with ℓ(e_1) ≠ 0. A unipotent substitution fixing P carries ℓ to a multiple
  of the first coordinate. Every coefficient occurring in a monomial of P that is nonzero at that point then has
  first exponent ≥ p. Hence μ_1 ≥ ep and |μ̄| ≤ ne.
- μ occurs in Sym^e Sym^m.

**BIP's argument with one more row, n ≥ 5, m ≥ n^25.** I use as published Propositions `pro:I-degreebound`,
`thm:newoccurrence`, `pro:lifting`(2), `le:newlift`(2), `cor:nonvanishing` and Theorem `eq:I-containlinforms`.
1. *m ≥ ne².* `pro:I-degreebound` has no row hypothesis and gives occurrence on the determinant closure.
2. *Otherwise e > √(m/n) ≥ n^{12}. Suppose first |μ̄| < (n+1)^{10}.* If μ̄ = ∅, the power of a linear form settles
   it. Otherwise put t = μ_2 and k = μ_2 + |μ̄|. Then k < 2(n+1)^{10} ≤ n^{12} < e and tk < 2(n+1)^{20} ≤ n^{25} ≤ m.
   - The two lifting propositions write the highest-weight vector through a nonzero g ∈ Sym^k Sym^t.
   - `cor:nonvanishing` makes g nonzero on sums of k t-th powers, and `eq:I-containlinforms` puts their paddings in
     the determinant closure, since m ≥ tk.
   - This is BIP's proof of `thm:verylongfirstrow`, with k chosen directly, so that no row bound enters.
3. *Otherwise |μ̄| ≥ (n+1)^{10}.* Apply `thm:newoccurrence` with the parameter n+1:
   - ℓ(μ) ≤ n²+1 ≤ (n+1)²;
   - |μ̄| ≤ ne ≤ (n+1)e;
   - m ≥ 24(n+1)^6 and e > 4(n+1)^6.

   It gives occurrence.

The numerical inequalities hold at n = 5. After division by the right-hand powers of n their left sides decrease in n,
so they hold for all n ≥ 5. This proves (NO). ∎

**A second route, for m ≥ (n+1)^25 and any n ≥ 2.** per_{n+1} restricted to diag(y, X) is y·perm_n. So
y^{m−n} perm_n is a substitution of X_11^{m−n−1} per_{n+1}, its orbit closure lies in BIP's variety for permanent size
n+1, and their theorem applies as stated.

### B.4 What is not shown

- `phph1Z` is not refuted.
- OH is not refuted for m < n^25, nor for n = 3, 4 with n^25 ≤ m < (n+1)^25.
- I did not re-prove BIP's propositions. I read their statements, the proof of their main theorem, the proof of
  `thm:verylongfirstrow` and parts of the proof of `thm:newoccurrence`.
- Nothing here says that the conclusion of `texplicitperm` is false for m < n^25. For m ≥ n^25, B.2 shows it is
  false, whenever polytopes satisfying the counting clauses exist to define it.
- No novelty search was made.

## What I read

- The brief.
- GCT VI v4 `main.tex`, lines 2198-2243 and 5931-6378.
- BIP `main.tex` from the same supplied-sources folder: lines 279-340, 378-386, 540-690, 1038-1048, 1898-1916,
  2026-2042, 2146-2222, 2283-2330, 2396-2530, with a grep of the theorem labels.
- Ikenmeyer-Panova's appendix "padding with the first variable" in the same folder.
- Kumar, arXiv:1007.1695, fetched as a PDF by its identifier. The prompt to the fetch tool asked only for the
  statement of Corollary 8.3 and its definitions. From the extracted text: the opening of section 5 through part of
  the proof of Lemma 5.1; Proposition 8.1 with part of its proof; Corollary 8.3 with its proof; the statement of
  Theorem 8.4; a grep for "normal".
- No statement of ours went to any search.

## Check events

| statement id | date | who | type | outcome |
|---|---|---|---|---|
| A | 2026-11-22 | Claude Opus 5.5 at effort high, agent a17221e5 | independent re-proof | proved for the hypothesis as written (A.1-A.4); limit of a per-family polynomial reading in A.5 |
| A | 2026-11-22 | same | computation or formal certificate | `independent_a17221e5_checks/check.py`: g = sk = box difference at s(2m,2m) for (s=1, m=3..8), (s=2, m=3,4); at k(m−1,1) for m=3..6, k≤6 with km≤30 |
| B, RH | 2026-11-22 | same | independent re-proof | proved for every m > n ≥ 2 without Kumar; his Corollary 8.3 identified as the same variety |
| B, RH | 2026-11-22 | same | computation or formal certificate | the degree-one dimension inequality, n = 2..8, m−n = 1..39 |
| B, PH1 | 2026-11-22 | same | independent re-proof | `hph1det` false, as A; `phph1Z` not decided |
| B, OH with PH1 | 2026-11-22 | same | independent re-proof | proved for m ≥ n^25, n ≥ 5, given BIP's named propositions; and for m ≥ (n+1)^25, n ≥ 2, from their theorem |
| B, OH with PH1 | 2026-11-22 | same | computation or formal certificate | transfer inequalities, n = 5..2000 |
| BIP, no occurrence obstructions | 2026-11-22 | same | used and rechecked in this run | padding mismatch found and repaired (B.3); cited propositions not re-proved |
| Kumar, Corollary 8.3 | 2026-11-22 | same | carried as background without fault found | statement, setting and short proof read; not needed |
