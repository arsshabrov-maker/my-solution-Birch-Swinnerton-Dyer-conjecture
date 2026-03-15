Inspiration and Logic for the Activation Formula

"I was inspired by one of the Millennium Prize Problems—the Birch and Swinnerton-Dyer conjecture, which uses the formula y^2=z^3 + wz + b. From this, 
I derived my own formula: y=z^2 (1 - z) + b. I replaced y^2=>y because if y^2 is complex, it can result in positive or negative values, so it can be substituted with y. Next,
I transformed z^3 + wz + b=>z^2 (1 - z) + b. Let’s prove the transition z^3 + wz =>z^2 (1 - z). In the equation z^3 + wz = y, if y is positive, then at least one term (z^3 or wz) must be positive.
If both are positive, it becomes a completely different function. If we use z^2 (w + z) + b, the term (w - z) could be positive, so it is necessary to make them opposite for a simpler implementation. 
Specifically: z^3 + wz =>z^3 -z^2=> z^2 -z^3=>z^2 (1 - z).
I kept +b because it does not change during the transformation and retains its mathematical meaning as a bias. Consequently, the final formula is y=z^2 (1 - z) + b."
