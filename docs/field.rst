Scalar, Spinor and Vector (Tensor) Field
----------------------------------------

.. note:: Please make sure you have covered the previous section `Representation of Lorentz Group <./repr_lg.html>`__.

This section will tell you how to define the scalar, spinor and vector (tensor) field. But before that, it is suggested to cover `Basic Linear Algebra <./bg_linalg.html>`__ for clarification of possible ambiguity of "vector". To avoid this ambiguity, we use term **linear space** for the *vector space* in `Linear Algebra <./bg_linalg.html>`__.

Physical Field
~~~~~~~~~~~~~~

In Quantum Field Theory, **field** is a central concept. In general, field is a map from the spacetime point to some object (numbers, arrows, etc.). All fields can form a linear space if the *object* also forms a linear space (as a practice, think about how to define that space). Although looked trivial, there is one thing that makes this concept intriguing --- spacetime point. Spacetime point can be too abstract for analysis such that, like what we do in Group Theory, we should set up a manifold for it. With a manifold, every spacetime point has its unique coordinates, which is a powerful tool for analysis.

However, the choice of coordinate system is artificial, and a law of nature should never depend on such an artificial object. Thus, it is crucial that the field should not vary after a change of coordinate system (and anything possibly related, basis of the field for example).

But that does not mean that the components of the field will also be invariant. In fact, **based on the different behaviour of the field components under transformations, we divide the physical field into several types** --- scalar field, spinor field and vector (tensor) field. Specifically, any field (as an element of a linear space) can be written as

.. math::


   \phi = \phi_i \cdot e^i

where :math:`\phi_i` is the components of the field and :math:`e^i` is a basis for the linear space. Now, if we perform a transformation :math:`g` to the basis, the components should transform inversely in order to make the combination invariant, i.e.

.. math::


   \phi = g^{-1}(\phi_i)\cdot g(e^i)

Nonetheless, the above expression is meaningless. As we have pointed out, the transformation is usually constructed using Lie group. And in Quantum Field Theory, it is Lorentz Group. However, we find that the expression :math:`g^{-1}(\phi_i)` and :math:`g(e^i)` undefined, since there is no definition indicating how to apply an element of Lie group to the components and basis of the field. Thus, to let the expression make sense, we need additional information of how the group element acts on the components and the basis. This designation is called **representation** of Lie group.

.. warning:: Important Notice: the dot in the previous two equations may not have the significance of certain "product". You will see this later.

A simple example is when the Lie group is :math:`\mathrm{GL}(n)`. Then a trivial representation is just to define the action as the matrix multiplication. In Quantum Field Theory, the representation of Lorentz Group on the basis is always this trivial one, but that on the components can be various. Therefore, we give this representation a name: **field representation**.

.. note:: Just a reminder, although you might not notice, you are actually using the idea of Fibre Bundle. If you would like, try to find some basic tutorial on principal bundle and fibre bundle associated to a principal bundle. And you will then be able to feel the elegance.

Scalar Field
~~~~~~~~~~~~

The scalar field is the field whose field representation is scalar representation. The **scalar representation** is defined as

.. math::


   \varLambda(\phi_i) = \phi_i

which means the components of the field does not change at all under the transformation.

Vector Field
~~~~~~~~~~~~

The vector field is the field whose field representation is vector representation. Thus, the components transform as

.. math::


   \varLambda(A_i) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_i}^jA_j

.. note:: To understand the above equation, you need `Basic Group Theory <./bg_liegp.html>`__ and `Representation of Lorentz Group <./repr_lg.html>`__.

First let's examine the above expression. First, you have to recall what is the exponential map. Remember that the result of the exponential map (:math:`\exp\{...\}`) is a matrix, and thus :math:`\exp\{...{\}_i}^j\phi_j` is nothing but a matrix multiply a column vector.

Next, remember that we have said the transformation of the basis follows the trivial representation which is defined just as the matrix product

.. math::


   \varLambda(e_i) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_i}^je_j

Therefore we have

.. math::


   A = \varLambda^{-1}(A^i)\cdot\varLambda(e_i) = A^i \exp\{\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_i}^j \cdot \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_j}^k e_k = A^j\cdot e_j

Now you can see why we write a dot :math:`\cdot` between the components and the basis --- under vector representation (where some triviality applies), the :math:`\cdot` in the above derivation can be "viewed" as the matrix product. However, this "view" will fail in some other non-trivial situations --- as described any minute next.

Spinor Field
~~~~~~~~~~~~

The spinor field is the field whose field representation is spinor representation. The **spinor representation** is define as

.. math::


   \varLambda(\psi_i) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}S_{ab}{\}_i}^j\psi_j, \ \ \text{where}\ \ \varLambda = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}\}

Just like what we have done in the previous section, write down explicitly

.. math::


   A^i \exp\{\frac{1}{2}\mathrm{i}\epsilon^{ab}S_{ab}{\}_i}^j \cdot \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_j}^k e_k =  A^j\cdot e_j ???

We see that the parameters :math:`\epsilon^{ab}` are the same in the two sides of “\ :math:`\cdot`\ ”, but the "basis" is different. Thus, if we still view :math:`\cdot` as the matrix product, the equality will no longer hold.

Hence, we need a new definition in this case, which means under the new product, there is

.. math::


   \exp\{\frac{1}{2}\mathrm{i}\epsilon^{ab}S_{ab}\} \cdot \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}\} \rightarrow \text{identity matrix}

In Fibre Bundle theory, we achieve this by introducing an equivalence class. Yes, it looks like that we are "brute-forcely" identify the the above result as an identity matrix. But as a matter of fact, there is no preliminary intentions to make :math:`\cdot` here as a product --- it just looks like that in vector field. In Fibre Bundle theory, fields of all kinds are described universally using the equivalence class.

Tensor Field
~~~~~~~~~~~~

The tensor of order :math:`n` is nothing but a quantity :math:`T_{\mu_1\cdots \mu_n}` of :math:`n` indices with each of them transforming like the vector. For instance, if you put two vectors :math:`A_\mu` and :math:`B_\nu` together, i.e. :math:`A_\mu B_\nu`, the result will be a tensor.

.. note:: Actually it is a tough decision for me to write down the above "non-sense". Yes, rigorously speaking, the above descriptions are total non-sense --- but they appear in many textbooks. In fact, there is no indices which are able to "transform like vector", and there is no way to "put vectors together" (It has its name --- tensor product!). Unfortunately it will make our introduction to QFT too cumbersome so we decide not to cover Tensor Analysis. However! You are strongly suggested to try your best to cover that --- it is as essential, and beautiful, and powerful as any other wonderful theories you met before.

Although we do not cover Tensor Analysis, we will provide a list for you to determine whether you have mastered it.

    -  Tensor of type :math:`(k, l)` is a multi-linear map from the Cartesian product of :math:`k` dual vector spaces and :math:`l` vector spaces.
    -  The tensor product of a tensor of type :math:`(k, l)` and a tensor of type :math:`(k', l')` is a tensor of type :math:`(k+k', l+l')`.
    -  The dimension of the space of tensor of type :math:`(k, l)` is :math:`n^{(k+l)}`, where :math:`n` is the dimension of the vector space in the definition of the tensor.
    -  The act of the tensor on a vector (or dual vector) is equivalent to the composite of tensor product and tensor contraction.

You should be able to understand in detail the above statements before you can say you have mastered Tensor Analysis.

