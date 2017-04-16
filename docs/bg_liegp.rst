Basics of Lie Group Theory
--------------------------

This section is a very basic introduction of Lie Group & Lie Algebra theory. Again, we would like to mention that there Lie Group & Lie Algebra is a tremendously abundant, and this section concerns only tips of the tips. The aim of this introduction is simply to provide you with an overall view of how Lie Group & Lie Algebra is implemented into physical theories. Therefore, we strongly recommend a more detailed investigation on this branch of Mathematics if possible.

Group and Lie Group
~~~~~~~~~~~~~~~~~~~

Group structure is an algebraic structure on a set, namely

    **Definition.** Group :math:`G` is a set equipped with a binary operation **multiplication**: :math:`\cdot: G\times G\rightarrow G` satisfying

    1. Associativity: :math:`(gh)k = g(hk)`

    2. Identity Element: :math:`\exists e, eg = ge = g`

    3. Inverse Element: :math:`\forall g, \exists g^{-1}, gg^{-1} = g^{-1}g =e`

Translate to human language: group is a set; you can perform multiplication of any two element of the set, and the multiplication satisfies three conditions.

The reason to invoke group into Physics lies on its similarity to the symmetry. Take translational symmetry for instance. The three translation operation clearly satisfies the associativity. There exists an identity translation (no translation). And for every translation there exists an inverse operation that transforms everything back. Similar argument also holds for rotation and other symmetries.

But a simple group structure does not provide enough tools for our analysis. We clearly are not satisfied with description as "translation :math:`a`\ ” and "translation :math:`b`\ ”. We hope that we can say "translation of :math:`5` units". How can we do that? You got it! We need a manifold.

Now, **Lie group** debuts. Lie group is nothing more complex than a set that is both a group and a manifold. The manifold provides the coordinates for each of the group element, and we can use a variety of tools provided by Differential Geometry.

Generator and Exponential Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of a very important tool provided by the Differential Geometry is the possibility to analyse the group element through generators. Take the 3D translation as an example. With a differential structure in hand, we can express some group element like "translation of 5 units along x axis". Here, the group element is designated by a parameter "5 units" and a *direction* "x axis". The generator is nothing other than the *direction* here. Therefore, every group element can be written as a parameter with a *direction*.

    Mathematically speaking, the generator is the element of the vector space at identity element of the Lie group. If you can not understand the previous statement, a review of linear structure on manifolds will be beneficial. There is no intention to expand here.

Next, we are going to explicitly illustrate how to the generator *generate* the group element. Suppose we now have a infinitesimal transformation

.. math::


   1+\epsilon A

where :math:`1` means the identity element, :math:`\epsilon` is a first order infinitesimal parameter and :math:`A` is the generator. To generate the element :math:`g` with *direction* :math:`A` and parameter :math:`t`, divide :math:`t` by :math:`n` and ask :math:`n\rightarrow\infty`. Therefore, the infinitesimal parameter :math:`\epsilon=t/n`. Then, apply the transformation :math:`n` times to get

.. math::


   g = \lim_{n\rightarrow\infty}(1+\frac{t}{n}A)^n\equiv\exp\{tA\}

Symbol :math:`\equiv` means "denoted by". The expression :math:`\exp\{tA\}` is called the **exponential map** of element :math:`g`. The reason for this denotation will be apparent if you notice a conclusion in Calculus

.. math::


   \exp\{x\} = (1 + \frac{x}{n})^n

It seems that we have got nothing but a denotation. However, the following theorem will show the power of the exponential map

    **Theorem.** For matrix group, thre is :math:`\exp = \mathrm{Exp}`.

In the above theorem, map :math:`\mathrm{Exp}` is defined as

.. math::


   \mathrm{Exp}(tA) = 1 + tA + \frac{t^2A^2}{2!} + \ldots = \sum_{k=0}^{\infty}\frac{t^kA^k}{k!}

and the matrix group means the group with all elements being square matrix. Notice that most group that are of great concern is the matrix group. There is no doubt that this theorem will provide great convenience.

    The trick of expanding the definition of function of real number to function of other object using the Taylor expansion is widely used in Mathematics. Thus, if you see some function that is originally only defined on numbers but actually acts on something else, you should then regard the definition of the function as the corresponding Taylor expansion.

Special Lie Groups
~~~~~~~~~~~~~~~~~~

This section will introduce several crucial matrix Lie groups that are widely used in physical theories. In fact, in frontier research, there are numerous kinds of Lie groups that frequently appear in the theories. This section will only introduce two of them --- **orthogonal group** (including **Lorentz group**) and **unitary group**.

**General Linear Group** :math:`\mathrm{GL}(n)`

We start from the most basic matrix Lie group --- :math:`n`-dim General Linear Group, or :math:`\mathrm{GL}(n)`, which consists of all bijective linear map from an :math:`n`-dim vector space :math:`V` to itself, with group multiplication defined as the map composition. If we select a basis of space :math:`V`, then the map will become an invertible square matrix of order :math:`n`, or square matrix :math:`A` of order :math:`n` with :math:`\det(A)\neq0`.

There is something "general", then there must be something "special". Yes, if we ask :math:`\det(A)=1`, then the matrices form the :math:`n`-dim **Special Linear Group**, or :math:`\mathrm{SL}(n)`. Moreover, this definition is not only suitable for General Linear Group only. Actually, when we say "special ... group", it just means "... group" with the determinant of the group element being :math:`1` specifically.

**Orthogonal Group** :math:`\mathrm{O}(n)` and :math:`\mathrm{O}(m,n)`

When defining :math:`\mathrm{GL}(n)`, we have no restriction on the vector space :math:`V`. Now, if there is also a metric defined on :math:`V`, then we can add more restriction to the transformation --- preserve the "length". More specifically, suppose space :math:`V` has a Euclidean metric :math:`\delta_{\mu\nu}`. Thus, the preservation of "length" can be expressed as

.. math::


   \delta_{\mu\nu}Z^\mu_\rho Z^\nu_\sigma v^\rho v^\sigma = \delta_{\mu\nu}v^\mu v^\nu

or written in matrix form

.. math::


   v^{\mathrm{T}}Z^{\mathrm{T}}Zv = v^{\mathrm{T}} v = v^{\mathrm{T}}Iv

where :math:`I` is the identity matrix. Thus, the preservation of "length" will be equivalent to

.. math::


   Z^{\mathrm{T}}Z = I

All this kind of matrices form the :math:`n`-dim Orthogonal Group, or :math:`\mathrm{O}(n)`. And from the illustration of the previous section, you should be able to understand what is **Special Orthogonal Group**, or :math:`\mathrm{SO}(n)`.

The story does not end here. Just now we ask the space :math:`V` to have a Euclidean metric. Now we want to ask the metric to be more general --- not necessary to be positively definite. More specifically, the diagonal elements of the metric can have :math:`m` occurrences as :math:`-1` and :math:`n` occurrences as :math:`1`. Also ask the matrix to preserve the "length". This kind of matrices form group :math:`\mathrm{O}(m,n)`. A famous example of this kind of group is :math:`\mathrm{O}(1,3)`. It has a dedicated name **Lorentz Group**, and it can be so vital that we decide to open a new section for it.

**Lorentz Group** :math:`\mathrm{L}` or :math:`\mathrm{O}(1,3)`

As is introduced in the previous section, the Lorentz Group is the linear group whose vector space :math:`V` has a Minkowski metric :math:`\eta_{\mu\nu}`. Yes, it is the Minkowski metric that makes it so significant in the physical theories.

The Lorentz Group has quite a complicated structure which we have no intention to address. But we would like to mention one important thing: the Lorentz Group can be divided into four branches, using the :math:`\varLambda^0_0` element (the leftmost and uppermost element) and determinant (either :math:`+1` or :math:`-1`). We use :math:`+/-` and :math:`\uparrow/\downarrow` to denote the four branches, e.g. :math:`\mathrm{L}^\uparrow_+` means :math:`\varLambda^0_0\geqslant1` and :math:`\det(\varLambda)=+1`.

Although there are a massive amount of properties revealed, we stop here --- many interesting facts about the Lorentz Group and its representation will be discussed in the introduction of representation theory.

**Unitary Group** :math:`\mathrm{U}(n)`

All our previous groups are based on the vector space :math:`V` which is *real*. Now we ask it to be complex. Then we get the complex General Linear Group :math:`\mathrm{GL}(n,\mathbb{C})`. Similarly, if there is an inner product (just like the metric in real space) defined on the complex vector space, we can ask the transformation to preserve "length". Thus, we get the unitary group :math:`\mathrm{U}(n)`. Again, we stop here. If you want to know more about the Unitary Group and its similarity or distinction with Orthogonal Group, please refer to the references concerning Lie Group & Lie Algebra.
