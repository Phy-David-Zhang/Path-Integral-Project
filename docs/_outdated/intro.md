## Introduction to Path Integral Project

### What is Path Integral Project?

I promise, this might be the most comprehensible introduction of Quantum Field Theory existed, ever. Indeed, the Quantum Field Theory can be one of the most powerful but complicated advanced physical theory ever existed. And, I was one of the many victims of this complication. 

However, we want to put this situation to an end. Instead of directly throwing piles of academic illustration, we hope to clarify all the logic during the construction of Quantum Field Theory. Moreover, it is also expected that a mathematically acceptable Quantum Field Theory to be established if possible. 

Accordingly, the Path Integral Project emerges. This project will do a profound investigation towards the construction of a mathematically rigorous Quantum Field Theory, and to see if any amendments during this process will provide hint towards a valid quantised gravitational theory.

Excited? Then just follow my pace to the next section. Welcome to the world of quantum field theory.

### A Brief History

Unlike other Quantum Field Theory textbook, our introduction to the history will not be so long. In this section, we only plan to introduce the part that has direct  connection to the motivation of Quantum Field Theory.

!! The following context will call [Geometric Unit System](../../background/geometric-unit-system) and [Einstein Summation Convention](../../background/einstein-summation-convention). Review the link if you have never heard of them — they are important!

Assuming that you already have the knowledge of Quantum Mechanics. At least you are able to recognise the most famous equation shown below

$$
\mathrm{i}\frac{\partial}{\partial t}\psi = -\frac{1}{2m}\nabla^2\psi + V\psi
$$

It is called a wave equation. Why? If you take 

$$
\psi = A\exp\{-\mathrm{i}\omega t + \mathrm{i}k\cdot x\}
$$

into the equation, you will find that it is a solution of the Schrödinger equation as long as the following holds

$$
\omega = \frac{k^2}{m} + V \label{difrel}
$$

Recall that we have the following relationship in Quantum Mechanics

$$
\omega = E,\ \ \ \ \  k^i = p^i
$$

where $E$ is the energy and $p^i$ is the momentum with $i=1,2,3$. Now, we immediately find that the previous equation becomes

$$
E = \frac{p^2}{m} + V
$$

which is nothing but the energy-momentum relationship in Newtonian classical mechanics.

! Now we release symbol $\psi$. This indicates that $\psi$ in the following context will have a different meaning.

So now we are going to think: what if we want it to be relativistic? Assuming that you already have the knowledge of Relativity. In Special Theory of Relativity, the energy-momentum relationship becomes

$$
E^2 = p^2 + m^2
$$

To achieve this result, simply reverse the previous steps. The above relationship should require 

$$
\omega^2 = k^2 + m^2 
$$

And this requires

$$
(\partial_\mu\partial^\mu - m^2)\varphi = 0
$$

where the [signature of metric](@waiting) here is $+2$. This is the famous “Klein-Gordon equation” — the relativistic version of Schrödinger equation. The quotes here indicates that it still has some subtle difference with the *real* Klein-Gordon equation, as we are going to see next.

It seems that it is so easy to combine Quantum Mechanics and Special Theory of Relativity. Nonetheless, things are not so trivial. The Newtonian energy-momentum relation can guarantee that the energy of a free ($V=0$) particle is always positive. However, the relativistic version can not. The relativistic energy-momentum relation reveals that

$$
E = \pm\sqrt{p^2+m^2}
$$

where we discover that there are both positive and negative solutions are possible. This issue is not paramount in classical theory, since the energy of a classical particle can only varies continuously, and there is a gap of $2m$ between the lowest positive energy $E=m$ (where $p=0$) and the greatest negative value $E=-m$ (where $p=0$). Thus, a classical particle can have either positive or negative energy — the only matter is to set an initial sign.

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

### Why Path Integral?

If you have any previous touch with Quantum Field Theory, you may know that there is a much more popular way to quantise the classical fields — canonical quantisation. However, in this introduction, we will not mention a word about it. If you are curious about the reason, this section will tell you why. However, if you are just a new learner, you can well skip this, it won’t affect.

#### Canonical Quantisation

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

#### Comments on Delta Function

The delta function is always a subtle object in Physics. First invented by Dirac in early 20th century, it has showed it magic in Quantum Mechanics for a countless of times. Hence, although the expression of Dirac delta function had been repeatedly refused, mathematicians were eventually forced to investigate this strange “function” seriously. 

Indeed, there has been several successful interpretation of delta function, such as generalized function theory and Dirac delta measure in measure theory. However, these implementation can only hold if the delta function is inside the integral, no matter what the integral means.

This condition can be fully comply in Quantum Mechanics, which explains why the delta function achieves that much. However, in canonical quantisation, the commutation relation will require delta function to appear barely outside. A [further investigation](@waiting) reveals that finally it is this carelessness that finally leads to the annoying infinities in S-matrix, and hence brings difficulties in quantising gravity.

Finally, we want to emphasise that the success of delta function in Quantum Mechanics does not mean that it will succeed in Quantum Field Theory too. The fact is: it fails. Therefore, in our introduction to Quantum Field Theory, canonical quantisation is avoided and any further usage of delta function will be carefully treated.