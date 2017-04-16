Basic Linear Algebra
--------------------

    There is no intention to introduce Linear Algebra in this section. We have assumed that you have already accomplished training on Linear Algebra. This section serves just as a brief review of the vector space.

The following is the definition of a vector space, or linear space in some references.

    **Definition.** The vector space :math:`V` over field :math:`F` is a set with two binary operation: **addition** :math:`+:V\times V\rightarrow V` and **scalar multiplication** :math:`\cdot:F\times V\rightarrow V` satisfying

    1. Commutativity: :math:`v+u=u+v`

    2. Associativity of addition: :math:`(v+u)+w = v+(u+w)`

    3. Additive identity: :math:`\exists 0, \forall v\in V, 0+v=v+0=v`

    4. Additive inverse: :math:`\exists (-v), v + (-v) = 0`

    5. Associativity of scalar multiplication: :math:`\beta(\alpha v) = (\beta\alpha)v`

    6. Compatibility of addition and scalar multiplication: :math:`(\alpha+\beta)v = \alpha v + \beta v`, :math:`\alpha(v+u) = \alpha v + \alpha u`

    7. Scalar multiplicative identity: :math:`\exists 1, 1\cdot v = v`

There is no need to be so keen on the definition of vector space, but there does exist some important facts worth noticing. From the definition can we discover that the vector space is actually a very general concept --- it would be more appropriate to call it a paradigm. Thus, when facing vector space, one should be very careful to distinguish the general vector space and some specific vector spaces.

As an example, the real number set over real number field with addition and scalar multiplication as the ordinary addition and multiplication of real numbers forms a vector space. In this case, all real numbers are vectors of real number set --- this is somehow different from our previous intuition, since a real number is widely referred as "scalar" instead of a vector.

As another example, the tensor space of any type is a vector space. But in many applicative contexts, the tensor of order one is specifically referred as vector.

The reason for this section is to remind you that there might be multiple meanings corresponding to the term "vector". Thus, sometimes if you find the argument containing "vector" incomprehensible, please remember that there might be the problem of the ambiguity of the term "vector".

