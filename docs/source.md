
## What is Path Integral Project?

I promise, this might be the most comprehensible introduction of Quantum Field Theory existed, ever. Indeed, the Quantum Field Theory can be one of the most powerful but complicated advanced physical theories ever created. And, I was one of the many victims of this complication. 

However, we want to put this situation to an end. Instead of directly throwing piles of academic illustration, we hope to clarify all the logic during the construction of Quantum Field Theory. Moreover, it is also expected that a mathematically acceptable Quantum Field Theory to be established if possible. 

Accordingly, the Path Integral Project emerges. This project will do a profound investigation towards the construction of a mathematically rigorous Quantum Field Theory, and to see if any amendments during this process will provide hint towards a valid quantised gravitational theory.

Excited? Then just follow my pace to the next section. Welcome to the world of quantum field theory.

## A Brief History

Unlike other Quantum Field Theory textbook, our introduction to the history will not be so long. In this section, we only plan to introduce the part that has direct  connection to the motivation of Quantum Field Theory.

.. note:: The following context will call [Geometric Unit System](../../background/geometric-unit-system) and [Einstein Summation Convention](../../background/einstein-summation-convention). Review the link if you have never heard of them — they are important!

Assuming that you already have the knowledge of Quantum Mechanics. At least you are able to recognise the most famous equation shown below

$$
\mathrm{i}\frac{\partial}{\partial t}\psi = -\frac{1}{2m}\nabla^2\psi + V\psi
$$

It is called a wave equation. Why? If you take 

$$
\psi = A\exp\{-\mathrm{i}\omega t + \mathrm{i}\vec k\cdot \vec x\}
$$

into the equation, you will find that it is a solution of the Schrödinger equation as long as the following holds

\begin{equation} 
\omega = \frac{\vec k^2}{m} + V \label{difrel}
\end{equation}

Recall that we have the following relationship in Quantum Mechanics

$$
\omega = E,\ \ \ \ \  k^i = p^i
$$

where $E$ is the energy and $p^i$ is the momentum with $i=1,2,3$. Now, we immediately find that the previous equation becomes

$$
E = \frac{\vec p^2}{m} + V
$$

which is nothing but the energy-momentum relationship in Newtonian classical mechanics.

.. warning:: Now we release symbol $\psi$. This indicates that $\psi$ in the following context will have a different meaning.

So now we are going to think: what if we want it to be relativistic? Assuming that you already have the knowledge of Relativity. In Special Theory of Relativity, the energy-momentum relationship becomes

$$
E^2 = \vec p^2 + m^2
$$

To achieve this result, simply reverse the previous steps. The above relationship should require 

\begin{equation} 
\omega^2 = \vec k^2 + m^2 
\end{equation}

And this requires

$$
(\partial_\mu\partial^\mu - m^2)\varphi = 0
$$

where the [signature of metric](@waiting) here is $+2$. This is the famous “Klein-Gordon equation” — the relativistic version of Schrödinger equation. The quotes here indicates that it still has some subtle difference with the *real* Klein-Gordon equation, as we are going to see next.

It seems that it is so easy to combine Quantum Mechanics and Special Theory of Relativity. Nonetheless, things are not so trivial. The Newtonian energy-momentum relation can guarantee that the energy of a free ($V=0$) particle is always positive. However, the relativistic version can not. The relativistic energy-momentum relation reveals that

$$
E = \pm\sqrt{\vec p^2+m^2}
$$

where we discover that there are both positive and negative solutions are possible. This issue is not paramount in classical theory, since the energy of a classical particle can only varies continuously, and there is a gap of $2m$ between the lowest positive energy $E=m$ (where $\vec p=0$) and the greatest negative value $E=-m$ (where $\vec p=0$). Thus, a classical particle can have either positive or negative energy — the only matter is to set an initial sign.

However, recall that quantised particles can jump between discrete energy levels. Hence, it is just a matter of probability for them to jump from a positive energy to a negative one and … fall all the way down to minus infinity. This then becomes a major difficulty of “Klein-Gordon equation”.

Also, let’s investigate the continuity equation. In Quantum Mechanics, there is

$$
\mathrm{i}\frac{\partial}{\partial t}\varphi = -\frac{1}{2m}\nabla^2\varphi + V\varphi\\
-\mathrm{i}\frac{\partial}{\partial t}\varphi^* = -\frac{1}{2m}\nabla^2\varphi^* + V\varphi^*
$$

The first equation is the Schrödinger equation and the second equation is nothing other than the complex conjugate of the first one.

Now, we apply $\varphi^*$ to the first equation and $\varphi$ to the second one, and let the first one subtract the second
$$
\varphi^*\mathrm{i}\frac{\partial}{\partial t}\varphi + \varphi\mathrm{i}\frac{\partial}{\partial t}\varphi^* = \varphi\frac{1}{2m}\nabla^2\varphi^* - \varphi^*\frac{1}{2m}\nabla^2\varphi
$$

which, after a transform, becomes

$$
\mathrm{i}\frac{\partial}{\partial t}\varphi\varphi^* = \frac{1}{2m}\nabla(\varphi\nabla\varphi^* - \varphi^*\nabla\varphi)
$$

To gain the continuity equation, the only thing to do is to identify the probability density and probability current as

$$
\rho = \varphi\varphi^*,\ \ \ \ \ \vec{j} = {1\over2m\mathrm i}(\varphi\nabla\varphi^* - \varphi^*\nabla\varphi)
$$

The probability density is the square of the wave function, and will always be positive due to the property of square. Everything works fine here.

However, if you derive the continuity equation corresponding to the “Klein-Gordon equation”, you will find that the “probability density” now becomes

$$
\rho \sim \varphi^*\frac{\partial}{\partial t}\varphi - \varphi\frac{\partial}{\partial t}\varphi^*
$$

The minus sign indicates that it might be negative(!), which destroys the probabilistic interpretation of quantum theory. This is another major difficulty of “Klein-Gordon equation”.

To solve the difficulties, physicists decided to reinterpret symbol $\varphi$ here as **classical field**, instead of wave function. Then, similar to the Quantum Mechanics, path integral is used to quantise the classical field.

Now, if you can follow the pace, welcome to the next section.

## Why Path Integral?

If you have any previous touch with Quantum Field Theory, you may know that there is a much more popular way to quantise the classical fields — canonical quantisation. However, in this introduction, we will not mention a word about it. If you are curious about the reason, this section will tell you why. However, if you are just a new learner, you can well skip this, it won’t affect.

### Canonical Quantisation

Take the scalar field for example. The canonical quantisation claims the following “quantisation condition”

$$
[\varphi(\vec x, t), \pi(\vec x', t)] = \mathrm i\delta(\vec x-\vec x')
$$

This is convenient since similar commutation relation has been studied thoroughly in Quantum Mechanics. However, it is this very first assumption that ruins the whole field theory. 

To see this, let’s first review what the Quantum Mechanics claims. In Quantum Mechanics, we have the following commutation relation

$$
[x_i, p_j] = \mathrm i\delta_{ij}
$$

There is nothing wrong here if both $x_i$ and $p_i$ are operators, and the product refers to operator composition. As an example, explicitly write an representation as $p_i = -\mathrm i\partial_i$ will satisfy the above relation.

However, although many physicists claim that the commutation relation of fields is nothing but a continuous version of the point particle one, it is still mathematically impossible for such a “continuous” commutation relation to hold. 

This can be seen through the following argument: field $\varphi$ and $\pi$ are both scalar field; according to the definition of scalar field product and subtraction, $\varphi\pi$ and $\pi\varphi$ will both be scalar field, so will their commutator $[\varphi, \pi]$. Thus, the left hand side of the commutation relation will be a scalar field (or more specifically, operator valued scalar field).

However, the right hand side is not a scalar field. Instead, according to the most moderate point of view, $\delta(\vec x - \vec x')$ should be at most a generalized function. Therefore, the two sides of the equation can never be equal.

### Comments on Delta Function

The delta function is always a subtle object in Physics. First invented by Dirac in early 20th century, it has showed it magic in Quantum Mechanics for a countless of times. Hence, although the expression of Dirac delta function had been repeatedly refused, mathematicians were eventually forced to investigate this strange “function” seriously. 

Indeed, there has been several successful interpretation of delta function, such as generalized function theory and Dirac delta measure in measure theory. However, these implementation can only hold if the delta function is inside the integral, no matter what the integral means.

This condition can be fully comply in Quantum Mechanics, which explains why the delta function achieves that much. However, in canonical quantisation, the commutation relation will require delta function to appear barely outside. A [further investigation](@waiting) reveals that finally it is this carelessness that finally leads to the annoying infinities in S-matrix, and hence brings difficulties in quantising gravity.

Finally, we want to emphasise that the success of delta function in Quantum Mechanics does not mean that it will succeed in Quantum Field Theory too. The fact is: it fails. Therefore, in our introduction to Quantum Field Theory, canonical quantisation is avoided and any further usage of delta function will be  carefully treated.


## Classical Theory: Scalar Field

.. note:: This context will require knowledge on Lagrangian dynamics of fields. If you have not yet cover that in your previous learning, you will find [Lagrangian Form of Fields](@waiting) helpful.

The Lagrangian of a scalar field is usually written as

$$
\mathcal L = -\partial_\mu\varphi^*\partial^\mu\varphi - m^2\varphi^*\varphi
$$

Alternatively, we can write

$$
\mathcal L = \varphi^*(\partial^\mu\partial_\mu - m^2)\varphi
$$

The equivalence between the two expression can be manifest once notice

$$
\partial_\mu(\varphi^*\partial^\mu\varphi) = \varphi^*\partial^\mu\partial_\mu \varphi + \partial_\mu\varphi^*\partial^\mu\varphi = 0
$$

The last equality is due to the fact that the left hand side is a surface term in the action integral.

Using the Lagrange equation, we get the equations of motion of scalar field

$$
(\partial^\mu\partial_\mu - m^2)\varphi = 0\\
(\partial^\mu\partial_\mu - m^2)\varphi^* = 0
$$

This is the “real” **Klein-Gordon equation** — the equation of scalar field.

## Solution of Klein-Gordon Equation

.. note:: This section is important to the canonical quantisation method, and will not influence the overall logic. You may skip this if you wish.

In this section, we look at the general solution of the Klein-Gordon equation. We do this for $\varphi$, and similar procedure can be easily carried out for $\varphi^*$. 

For any possible field $\varphi$, we can perform Fourier expansion as 

$$
\varphi = \int{\mathrm d^4k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}
$$

.. note:: Well, you may notice that here we do not take the symmetric form of the Fourier transformation. Although personally I prefer the symmetric form, but trust me, it can make all the successive discussions awful. 

Take the above expression back into the equation, we get the dispersion relation

$$
k^2 + m^2 = 0
$$

This relation serves as a constraint to the wave number $k^\mu$. Thus, to gain the solution, all we need to do is to switch the integral measure to [delta measure](@waiting)

$$
\varphi(x) = \int{\mathrm d^4k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot2\pi\delta(k^2+m^2)
$$

Factor $2\pi$ is necessary since we are going to perform the integral once, like

$$
\varphi(x) &= \int{\mathrm d\omega \mathrm d^3k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot2\pi\delta(-\omega^2 + \vec k^2 + m^2)\\
&= \int{\mathrm d\omega^2 \mathrm d^3k\over2\omega(2\pi)^3}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot\delta(-\omega^2 + \vec k^2 + m^2)\\
&= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}a(k)\exp\{\mathrm i(\omega_k t - \vec k \vec x\} + \int{\mathrm d^3k\over(-2\omega_k)(2\pi)^3}a(k)\exp\{\mathrm i(-\omega_k t - \vec k \vec x\}\\
&= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}a(k)\exp\{\mathrm i(\omega_k t - \vec k \vec x\} + \int{\mathrm d^3k\over(2\omega_k)(2\pi)^3}a(-k)\exp\{\mathrm i(-\omega_k t + \vec k \vec x\}\\
&= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}\left[a(k)\exp\{-\mathrm i(k^\mu x_\mu\} + a(-k)\exp\{\mathrm i(k^\mu x_\mu\} \right]
$$

where $\omega_k = \sqrt{\vec k^2 + m^2}$. The fourth equality is nothing other than reversing the direction of $\vec k$. Hence, we get the general form of the solution of Klein-Gordon equation.

## The Symmetry of Fields

To extend our investigation towards spinor field and vector field, it is inevitable to introduce the change of components of fields under Lorentz transformation. This context, however, can be as complicated as a combination of Differential Geometry, Lie Group and Lie Algebra theory and Fibre Bundle theory. It would be much better if you are able to fully review these contexts. But anyway, we still try to provide a very basic introduction either to make our logic coherent or to provide motivation as you are studying those enigmatic mathematical theories.

.. note:: To understand this section, you at least need to know [some very basic Differential Geometry](../../Background/Basic%20Differential%20Geometry) and [basic Linear Algebra](../../Background/Basic%20Linear%20Algebra).

Currently, we are talking about classical fields. The classical field is a kind of physical object. Therefore, despite that we can develop some tools (e.g. coordinate system or basis) to describe it, it should in a whole remain unchanged after certain manual transformation (e.g. re-selection of the basis). 

However, this does not mean that the components of the field will remain invariant. In fact, except for the scalar field (we will analyse this later), many other types of fields will encounter a component change after the change of basis or coordinate system. Hence, based on the behaviour of the variation of components, we can classify the physical fields.

A conclusion is needed: it is possible to naturally set up an $n$-dim vector space associated to every point in an $n$-dim manifold. The basis of this specific vector space is called **tetrad** (or $n$-**frame**, **veirbein** in some references). 

> We are not going to elucidate this conclusion since it would be a harangue. If you are interested, please referred to textbooks on Differential Geometry for further details.

In Quantum Field Theory, we care about three types of fields ---  scalar field, spinor field and vector field. Please notice that the term "scalar" and "vector" here are domain specific, which means that they might have a similar but essentially different meaning in other contexts.

**Scalar field** is a kind of field which does not change under any transformation of tetrad; **spinor field** transforms according to spinor representation of the Lorentz group, and **vector field** transforms according to the vector representation.

I know you don't understand. But don't worry, it is going to be illustrated next.

## Geometric Unit System

This is an introduction to the geometric unit used widely in the theoretical contexts of Physics.

In Physics, there are many important constants, such as light speed in vacuum $c$, (reduced) Plank constant $\hbar$, absolute permittivity $\varepsilon_0$, etc. If we include all these constants in an equation, the expression can be cumbersome. To solve this problem, the simplest way is to introduce the following convention

$$
c=1,\ \ \ \ \ \hbar=1
$$

Therefore, all multiplication of these constants in the equation will disappear. But wait! You may immediately notice a problem: the dimension! Yes, it seems that the above equation violates a fundamental requirement — balance of dimension. The left hand side is a physical constant with dimension, but the right hand side is a pure number. 

Well, this in fact does not matter so much. You can view it as a redefinition of units. For example, to make light speed $c=1$, all we need to do is to redefine the time unit as the time within which light travels a unit length. This is called **Geometric Unit System**. As a result, the convention $c=1$ will be equivalent to $[L]=[T]$, where $[L]$ stands for the length dimension and $[T]$ for time dimension. Similarly, it is easy to figure out that $\hbar=1$ leads to $[L]=[M]^{-1}$. 

Hope you get the point. Now you should not feel unfamiliar with sentences like “momentum has a dimension of $[L]^{-1}$”. The theory of dimension analysis guarantees that there will not be a problem with this convention as long as you do a correct calculation.

## Einstein Summation Convention

This is an introduction to the Einstein summation convention used widely in the theoretical contexts in Physics.

The definition of the convention is simple: repeating upper and lower indices implies summation, unless stated otherwise, i.e.

$$
x^iy_i = \sum_{i\in I}x^iy_i
$$

where set $I$ is the set of possible values of the indices. 

Please notice that there are other versions of Einstein summation convention. One version may consider all the dummy indices as summation. However, in this context, only the repeated upper and lower indices should be interpreted as summation, expression as $x_iy_i$ does not apply to the summation convention.

## Basic Differential Geometry

Differential Geometry can be one of the most crucial foundations of theoretical Physics. Thus, we suggest everyone who aims at fundamental theoretical Physics to have a detailed review of Differential Geometry. We are not going to introduce thoroughly here, since that would make up another book. You can rely on this if you just want to understand our main context, nevertheless, you are strongly suggested to look for other Differential Geometry introductory for  many other important details.

### Get Started: Motivation

In Calculus, we have studied many properties of functions, like continuity, differentiability and so on. However, these properties only apply to functions — whose domain is a number set (such as $\mathbb R^n$). However, pragmatically we are dealing with ordinary maps — whose domain is an ordinary set (ranging from all particles of the desk in front of you to the spacetime of the universe). At this time, we find that we are lack of the structure (just like a kind of property) on that ordinary set. For example, you can not judge whether a map from the phone to its number is differentiable or not. Hence, extra structures are needed.

How does this related to Physics? You may consider the electric potential $\phi$ which is a vector field in spacetime. The vector field is nothing but a map from the set of all points in spacetime to the real number set. And the set of all points in spacetime can be an example of the *ordinary set* in our previous illustration.

### Prerequisites: Topology

The first structure we need is the topology. The topology of a set will help us define the continuity of the map. In Calculus, a function is continuous if the inverse image of any of the open interval in the image will be an open interval (You can prove that this is equivalent to the $\varepsilon$-$\delta$ form in Calculus). Thus, if we want to define continuity of any map, the only structure we need is to define the “open interval” of the set.

This inspires us to manually designate some subsets of the set to be **open** (plus some conditions). And the continuity of the map can be defined in similar way. We are not going to expand here — it can be a long story. The only thing you need to remember is that we can now talk about the openness of the subset and the continuity of a map. 

### Set up a Coordinate System

Next we move on to the differentiability of a map. To do this, we equip every open subset with an open subset of a number set. To be more specific, construct a continuous bijection $\psi_\alpha$ for each subset $U_\alpha$ of set $M$ to an open subset of $\mathbb R^n$. 

To see how this works, let’s look at map $\psi_\alpha$. It maps the point $p$ of set $M$ into $n$ numbers in $\mathbb R^n$. Or equivalently, it assigns $n$ numbers to point $p$. Yes! Those numbers are nothing other than the **coordinates** of point $p$. And, map $\psi_\alpha$ will then be the **coordinate system** on subset $U_\alpha$. Set equipped with the coordinate system is called manifold.

Now, we can define the differentiability of the map between manifolds. Since every point has its coordinates, the map between points becomes functions between coordinates. Thus, the differentiability of the map can be defined as that of those functions, which is well-defined in Calculus.

Another thing that we would like to mention is the separation of point and its coordinates. In many elementary Physics textbooks, point and coordinates are the *same thing*. But now, we strongly suggest to distinguish these two entities — you will benefit a lot if you take this seriously in the future.

### Spacetime Geometry

Here, we introduce briefly (*extremely briefly*) about the spacetime geometry. In fact, there is a spectacular construction of spacetime geometry in Differential Geometry theory. So if you are able, try to learn something about it. You will never regret.

In 3 dimensional Euclidean space, we have Gougu Theorem

$$
\Delta s^2 = \Delta x^2 + \Delta y^2 + \Delta z^2
$$

In differential form, it is

$$
\mathrm d s^2 = \mathrm d x^2 + \mathrm d y^2 + \mathrm d z^2
$$

Symbol $\mathrm d s^2$ here is called **line element**. You may notice that the coefficients of the three terms in right hand side are all $1$. This is a typical characteristic of flat 3D Euclidean space. Now we think: what if the coefficients are not $1$? In fact, the configuration of those coefficients labels a kind of *geometry*. As an important example, look at

$$
\mathrm d s^2 = -\mathrm d t^2 + \mathrm d x^2 + \mathrm d y^2 + \mathrm d z^2
$$

Clearly this is not the 4D Euclidean space, since there is a $-1$ here. Actually, this is **Minkowski spacetime**  widely used in Special Relativity and Quantum Field Theory. You can also write other numbers or even functions for those coefficients. Certain functions will even let the spacetime to curve. But these are the content of General Relativity which we do not aim at here. (Again if you have time, take a look at it. It’s wonderful.)

We can write the Minkowski line element formally as

$$
\mathrm d s^2 = [\mathrm d t\ \mathrm d x\ \mathrm d y\ \mathrm d z]
\left[
\begin{matrix}
-1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1
\end{matrix}
\right]
\left[
\begin{matrix}
\mathrm d t\\
\mathrm d x\\
\mathrm d y\\
\mathrm d z\\
\end{matrix}
\right]
$$

The $4\times 4$ matrix in the above equation, usually denoted by $\eta_{\mu\nu}$, is called the **metric** of the spacetime. The sum of all the diagonal element ($+2$ in this case) is called the **signature** of the metric. Many textbooks of Quantum Field Theory uses Minkowski metric as $\eta = \mathrm{diag}(1,-1,-1,-1)$, whose signature is $-2$. However, to comply with the convention in the Theory of Relativity, we use the $+2$ metric.

## Lagrangian Dynamics of Fields

.. note:: Before step into this section, we suggest you review the Lagrangian dynamics of classical point particles, as we are not going to go through that.

The Lagrangian density of a field $\phi(x)$ is a map $\mathcal L(\phi,\partial_\mu\phi)$ of field $\phi$ and its derivative $\partial_\mu\phi$. Thus, the action can be constructed as

$$
\mathcal S = \int \mathcal L(\phi,\partial_\mu\phi)\,\mathrm d^4x
$$

Now, perform the variation of the action

$$
\delta S &= \int \delta\mathcal L \,\mathrm d^4x\\
&= \int \left({\partial\mathcal L\over \partial \phi}\delta\phi + {\partial\mathcal L\over\partial\partial_\mu\phi}\delta\partial_\mu\phi\right)\,\mathrm d^4x\\
&= \int \left({\partial\mathcal L\over \partial \phi}\delta\phi + {\partial\mathcal L\over\partial\partial_\mu\phi}\partial_\mu\delta\phi\right)\,\mathrm d^4x\\
&= \int \left({\partial\mathcal L\over \partial \phi} - \partial_\mu {\partial\mathcal L\over\partial\partial_\mu\phi}\right)\delta\phi\,\mathrm d^4x + \int \partial_\mu \left({\partial\mathcal L\over\partial\partial_\mu\phi}\delta\phi\right)\,\mathrm d^4x\\
&= \int \left({\partial\mathcal L\over \partial \phi} - \partial_\mu {\partial\mathcal L\over\partial\partial_\mu\phi}\right)\delta\phi\,\mathrm d^4x = 0
$$

The second equality is due to the fact that the variation of $\phi$ does not change the coordinate system; the fourth equality is because the second integral is a surface term under Stokes theorem, and the variation on the surface is zero.

Thus, to make the equality hold, the only possible way is
$$
{\partial\mathcal L\over \partial \phi} - \partial_\mu {\partial\mathcal L\over\partial\partial_\mu\phi} = 0
$$

This is the Lagrangian equation for fields.


## Basic Linear Algebra

> There is no intention to introduce Linear Algebra in this section. We have assumed that you have already accomplished training on Linear Algebra. This section serves just as a brief review of the vector space.

The following is the definition of a vector space, or linear space in some references.

> **Definition.** The vector space $V$ over field $F$ is a set with two binary operation: **addition** $+:V\times V\rightarrow V$ and **scalar multiplication** $\cdot:F\times V\rightarrow V$ satisfying
>
> 1. Commutativity: $v+u=u+v$
>
> 2. Associativity of addition: $(v+u)+w = v+(u+w)$
>
> 3. Additive identity: $\exists 0, \forall v\in V, 0+v=v+0=v$
>
> 4. Additive inverse: $\exists (-v), v + (-v) = 0$
>
> 5. Associativity of scalar multiplication: $\beta(\alpha v) = (\beta\alpha)v$
>
> 6. Compatibility of addition and scalar multiplication: $(\alpha+\beta)v = \alpha v + \beta v$, $\alpha(v+u) = \alpha v + \alpha u$
>
> 7. Scalar multiplicative identity: $\exists 1, 1\cdot v = v$

There is no need to be so keen on the definition of vector space, but there does exist some important facts worth noticing. From the definition can we discover that the vector space is actually a very general concept --- it would be more appropriate to call it a paradigm. Thus, when facing vector space, one should be very careful to distinguish the general vector space and some specific vector spaces. 

As an example, the real number set over real number field with addition and scalar multiplication as the ordinary addition and multiplication of real numbers forms a vector space. In this case, all real numbers are vectors of real number set --- this is somehow different from our previous intuition, since a real number is widely referred as "scalar" instead of a vector. 

As another example, the tensor space of any type is a vector space. But in many applicative contexts, the tensor of order one is specifically referred as vector.

The reason for this section is to remind you that there might be multiple meanings corresponding to the term "vector". Thus, sometimes if you find the argument containing "vector" incomprehensible, please remember that there might be the problem of the ambiguity of the term "vector".


## Basics of Lie Group Theory

This section is a very basic introduction of Lie Group & Lie Algebra theory. Again, we would like to mention that there Lie Group & Lie Algebra is a tremendously abundant, and this section concerns only tips of the tips. The aim of this introduction is simply to provide you with an overall view of how Lie Group & Lie Algebra is implemented into physical theories. Therefore, we strongly recommend a more detailed investigation on this branch of Mathematics if possible.

### Group and Lie Group

Group structure is an algebraic structure on a set, namely

> **Definition.** Group $G$ is a set equipped with a binary operation **multiplication**: $\cdot: G\times G\rightarrow G$ satisfying
>
> 1. Associativity: $(gh)k = g(hk)$
>
> 2. Identity Element: $\exists e, eg = ge = g$
>
> 3. Inverse Element: $\forall g, \exists g^{-1}, gg^{-1} = g^{-1}g =e$

Translate to human language: group is a set; you can perform multiplication of any two element of the set, and the multiplication satisfies three conditions.

The reason to invoke group into Physics lies on its similarity to the symmetry. Take translational symmetry for instance. The three translation operation clearly satisfies the associativity. There exists an identity translation (no translation). And for every translation there exists an inverse operation that transforms everything back. Similar argument also holds for rotation and other symmetries. 

But a simple group structure does not provide enough tools for our analysis. We clearly are not satisfied with description as "translation $a$” and "translation $b$”. We hope that we can say "translation of $5$ units". How can we do that? You got it! We need a manifold.

Now, **Lie group** debuts. Lie group is nothing more complex than a set that is both a group and a manifold. The manifold provides the coordinates for each of the group element, and we can use a variety of tools provided by Differential Geometry.

### Generator and Exponential Map

One of a very important tool provided by the Differential Geometry is the possibility to analyse the group element through generators. Take the 3D translation as an example. With a differential structure in hand, we can express some group element like "translation of 5 units along x axis". Here, the group element is designated by a parameter "5 units" and a *direction* "x axis". The generator is nothing other than the *direction* here. Therefore, every group element can be written as a parameter with a *direction*.

> Mathematically speaking, the generator is the element of the vector space at identity element of the Lie group. If you can not understand the previous statement, a review of linear structure on manifolds will be beneficial. There is no intention to expand here.

Next, we are going to explicitly illustrate how to the generator *generate* the group element. Suppose we now have a infinitesimal transformation

$$
1+\epsilon A
$$

where $1$ means the identity element, $\epsilon$ is a first order infinitesimal parameter and $A$ is the generator. To generate the element $g$ with *direction* $A$ and parameter $t$, divide $t$ by $n$ and ask $n\rightarrow\infty$. Therefore, the infinitesimal parameter $\epsilon=t/n$. Then, apply the transformation $n$ times to get

$$
g = \lim_{n\rightarrow\infty}(1+\frac{t}{n}A)^n\equiv\exp\{tA\}
$$

Symbol $\equiv$ means "denoted by". The expression $\exp\{tA\}$ is called the **exponential map** of element $g$. The reason for this denotation will be apparent if you notice a conclusion in Calculus

$$
\exp\{x\} = (1 + \frac{x}{n})^n
$$

It seems that we have got nothing but a denotation. However, the following theorem will show the power of the exponential map

> **Theorem.** For matrix group,  thre is $\exp = \mathrm{Exp}$.

In the above theorem, map $\mathrm{Exp}$ is defined as

$$
\mathrm{Exp}(tA) = 1 + tA + \frac{t^2A^2}{2!} + \ldots = \sum_{k=0}^{\infty}\frac{t^kA^k}{k!}
$$

and the matrix group means the group with all elements being square matrix. Notice that most group that are of great concern is the matrix group. There is no doubt that this theorem will provide great convenience.

> The trick of expanding the definition of function of real number to function of other object using the Taylor expansion is widely used in Mathematics. Thus, if you see some function that is originally only defined on numbers but actually acts on something else, you should then regard the definition of the function as the corresponding Taylor expansion.

### Special Lie Groups

This section will introduce several crucial matrix Lie groups that are widely used in physical theories. In fact, in frontier research, there are numerous kinds of Lie groups that frequently appear in the theories. This section will only introduce two of them --- **orthogonal group** (including **Lorentz group**) and **unitary group**.

**General Linear Group** $\mathrm{GL}(n)$

We start from the most basic matrix Lie group --- $n$-dim General Linear Group, or $\mathrm{GL}(n)$, which consists of all bijective linear map from an $n$-dim vector space $V$ to itself, with group multiplication defined as the map composition. If we select a basis of space $V$, then the map will become an invertible square matrix of order $n$, or square matrix $A$ of order $n$ with $\det(A)\neq0$. 

There is something "general", then there must be something "special". Yes, if we ask $\det(A)=1$, then the matrices form the $n$-dim **Special Linear Group**, or $\mathrm{SL}(n)$. Moreover, this definition is not only suitable for General Linear Group only. Actually, when we say "special ... group", it just means "... group" with the determinant of the group element being $1$ specifically.

**Orthogonal Group** $\mathrm{O}(n)$ and $\mathrm{O}(m,n)$

When defining $\mathrm{GL}(n)$, we have no restriction on the vector space $V$. Now, if there is also a metric defined on $V$, then we can add more restriction to the transformation --- preserve the "length". More specifically, suppose space $V$ has a Euclidean metric $\delta_{\mu\nu}$. Thus, the preservation of "length" can be expressed as

$$
\delta_{\mu\nu}Z^\mu_\rho Z^\nu_\sigma v^\rho v^\sigma = \delta_{\mu\nu}v^\mu v^\nu
$$

or written in matrix form

$$
v^{\mathrm{T}}Z^{\mathrm{T}}Zv = v^{\mathrm{T}} v = v^{\mathrm{T}}Iv
$$

where $I$ is the identity matrix. Thus, the preservation of "length" will be equivalent to

$$
Z^{\mathrm{T}}Z = I
$$

All this kind of matrices form the $n$-dim Orthogonal Group, or $\mathrm{O}(n)$. And from the illustration of the previous section, you should be able to understand what is **Special Orthogonal Group**, or $\mathrm{SO}(n)$.

The story does not end here. Just now we ask the space $V$ to have a Euclidean metric. Now we want to ask the metric to be more general --- not necessary to be positively definite. More specifically, the diagonal elements of the metric can have $m$ occurrences as $-1$ and $n$ occurrences as $1$. Also ask the matrix to preserve the "length". This kind of matrices form group $\mathrm{O}(m,n)$. A famous example of this kind of group is $\mathrm{O}(1,3)$. It has a dedicated name **Lorentz Group**, and it can be so vital that we decide to open a new section for it.

**Lorentz Group** $\mathrm{L}$ or $\mathrm{O}(1,3)$

As is introduced in the previous section, the Lorentz Group is the linear group whose vector space $V$ has a Minkowski metric $\eta_{\mu\nu}$. Yes, it is the Minkowski metric that makes it so significant in the physical theories. 

The Lorentz Group has quite a complicated structure which we have no intention to address. But we would like to mention one important thing: the Lorentz Group can be divided into four branches, using the $\varLambda^0_0$ element (the leftmost and uppermost element) and determinant (either $+1$ or $-1$). We use $+/-$ and $\uparrow/\downarrow$ to denote the four branches, e.g. $\mathrm{L}^\uparrow_+$ means $\varLambda^0_0\geqslant1$ and $\det(\varLambda)=+1$.

Although there are a massive amount of properties revealed, we stop here ---  many interesting facts about the Lorentz Group and its representation will be discussed in the introduction of representation theory.

**Unitary Group** $\mathrm{U}(n)$

All our previous groups are based on the vector space $V$ which is *real*. Now we ask it to be complex. Then we get the complex General Linear Group $\mathrm{GL}(n,\mathbb{C})$. Similarly, if there is an inner product (just like the metric in real space) defined on the complex vector space, we can ask the transformation to preserve "length". Thus, we get the unitary group $\mathrm{U}(n)$. Again, we stop here. If you want to know more about the Unitary Group and its similarity or distinction with Orthogonal Group, please refer to the references concerning Lie Group & Lie Algebra. 

