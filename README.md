---
typora-root-url: ./
---

# Motion of a Satellite using the Three Body Problem 

This small simulation consists in predicting the motion of a Satellite, which is influenced by the gravity of the Moon and Earth. The programming language used is Python and the libraries used are Pandas and Scipy.

### Definitions and Physics

**The Two Body Problem** consists in predicting the motion of two celestial bodies, which only interact with each other without the influence of a third body. In general, this kind of problem is known as " **the n-Body Problem**".  First is important to calculate the motion of the Moon and the Earth.

Is commonly known that the Earth orbits around the Sun, but actually the Earth and Sun orbit around his common **center of mass**, this center of mass is called **barycenter**. This not only applies for the system Earth-Sun, it applies for all celestial bodies. That means, the Earth and Moon have they own **barycenter**. 

Let the orbit of the Earth be **1** and Moon **2**. The semi-major axis of the Orbit 1 <a><img src="https://latex.codecogs.com/svg.latex?d_1"/></a>  is actually the distance to the barycenter and <a><img src="https://latex.codecogs.com/svg.latex?d_2"/></a> is the semi-major axis of the Orbit 2 and the distance to the barycenter. If <a><img src="https://latex.codecogs.com/svg.latex?d_1"/></a> and <a><img src="https://latex.codecogs.com/svg.latex?d_2"/></a> are the distances to the barycenter, that means the sum of both is the distance from the Earth and Moon,  in other words <a><img src="https://latex.codecogs.com/svg.latex?a&space;=&space;d_1&space;&plus;&space;d_2"/></a>, where <a><img src="https://latex.codecogs.com/svg.latex?a"/></a> is the  distance between Earth and Moon and the semi-major axis of the whole system. From the concept of **center of mass**, the two bodies follow the relation between mass <a><img src="https://latex.codecogs.com/svg.latex?m"/></a> and distance to the center of mass (barycenter) <a><img src="https://latex.codecogs.com/svg.latex?r"/></a> which is defined as<a><img src="https://latex.codecogs.com/svg.latex?m_1&space;d_1&space;=&space;m_2&space;d_2"/></a>. 

If <img src="https://latex.codecogs.com/svg.latex?a&space;=&space;d_1&space;&plus;&space;d_2"/>, then:

<a><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;m_1&space;d_1&space;&=&space;m_2(a-d_1)\\&space;d_1&space;&=&space;\frac{m_2}{m_1&plus;m_2}&space;a&space;\end{align*}" title="\begin{align*} m_1 d_1 &= m_2(a-d_1)\\ d_1 &= \frac{m_2}{m_1+m_2} a \end{align*}" /></a> 

Analog: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;m_1&space;r_1&space;&=&space;m_2(a-r_1)\\&space;r_1&space;&=&space;\frac{m_2}{m_1&plus;m_2}&space;a&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;&space;d_2&space;&=&space;\frac{m_1}{m_1&plus;m_2}&space;a&space;\end{align*}" title="\begin{align*} m_1 r_1 &= m_2(a-r_1)\\ d_1 &= \frac{m_2}{m_1+m_2} a \end{align*}" /></a>

Now it is important to know the position of the Earth and Moon in a cartesian plane. The bodies have a motion almost circular, with an amplitude and frequency.  From the harmonic motion, the position in <a><img src="https://latex.codecogs.com/svg.latex?x"/></a> is <a href="https://www.codecogs.com/eqnedit.php?latex=x(t)&space;=&space;A\cos(\omega&space;t)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?x(t)&space;=&space;A\cos(\omega&space;t)" title="x(t) = A\cos(\omega t)" /></a>, where <a><img src="https://latex.codecogs.com/svg.latex?A"/></a> is the **amplitude**, <a><img src="https://latex.codecogs.com/svg.latex?\omega"/></a>  the **angular frequency** and <img src="https://latex.codecogs.com/svg.latex?t"/>/a> time.  The angular frequency <a><img src="https://latex.codecogs.com/svg.latex?\omega"/></a> is defined as <a href="https://www.codecogs.com/eqnedit.php?latex=\omega&space;=&space;\frac{2\pi}{T}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\omega&space;=&space;2\pi/T" title="\omega = 2\pi/T" /></a>, with <a><img src="https://latex.codecogs.com/svg.latex?T"/></a> as **period**. Using the **polar coordinates**, the position of a body with orbital period <a><img src="https://latex.codecogs.com/svg.latex?T"/></a> in relation to time is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;x(t)&space;&=&space;rcos(\omega&space;t)\\&space;y(t)&space;&=&space;rsin(\omega&space;t)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;x(t)&space;&=&space;rcos(\omega&space;t)\\&space;y(t)&space;&=&space;rsin(\omega&space;t)&space;\end{align*}" title="\begin{align*} x(t) &= rcos(\omega t)\\ y(t) &= rsin(\omega t) \end{align*}" /></a>

Both terms resemble harmonic motion's equation.  The Earth and Moon have a common orbit because of the **barycenter**, that means they both have the same period in **this** orbit (Earth-Moon), this period  <a><img src="https://latex.codecogs.com/svg.latex?T"/></a> is the period which the moon makes a whole cycle (~29.53 days).  With that, the position of the Earth and Moon are:

Earth:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;x(t)&space;&=&space;rcos(\omega&space;t)\\&space;y(t)&space;&=&space;rsin(\omega&space;t)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;x_1(t)&space;&=&space;d_1\cos(\omega&space;t)\\&space;y_1(t)&space;&=&space;d_1\sin(\omega&space;t)&space;\end{align*}" title="\begin{align*} x(t) &= rcos(\omega t)\\ y(t) &= rsin(\omega t) \end{align*}" /></a>

Moon:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;x_2(t)&space;&=&space;r_2\cos(\omega&space;t)\\&space;y_2(t)&space;&=&space;r_2\sin(\omega&space;t)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;x_2(t)&space;&=&space;d_2\cos(\omega&space;t)\\&space;y_2(t)&space;&=&space;d_2\sin(\omega&space;t)&space;\end{align*}" title="\begin{align*} x_2(t) &= d_2\cos(\omega t)\\ y_2(t) &= d_2\sin(\omega t) \end{align*}" /></a>

### Three Body Problem

The position of the Moon and Earth are finally defined, now it's time to add a third body to the system, a **satellite**. In this case, the satellite will have an **initial velocity**, which it will escape from the Earth's atmosphere and an **initial position** when it is outside of the atmosphere. Newton's law of universal gravitation says that all bodies attract each other with a gravitational force. The gravitational force from object 1 to 2 is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\vec{F}_{1\rightarrow2}&space;=&space;G&space;\frac{m_1&space;m_2}{\left&space;\|&space;\vec{r}_{2}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{2}-\vec{r}_1)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\vec{F}_{1\rightarrow2}&space;=&space;-G&space;\frac{m_1&space;m_2}{\left&space;\|&space;\vec{r}_{2}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{2}-\vec{r}_1)" title="\vec{F}_{1\rightarrow2} = G \frac{m_1 m_2}{\left \| \vec{r}_{2} - \vec{r}_{1} \right \|^{3}}(\vec{r}_{2}-\vec{r}_1)" /></a>

<a><img src="https://latex.codecogs.com/svg.latex?G"/></a> is the **gravitational constant** and <a><img src="https://latex.codecogs.com/svg.latex?\vec{r}"/></a> is the **vector of position**. The gravitational force in the satellite is the the sum of the force from the Earth and Moon. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;\vec{F}_{g}&space;&=&space;\vec{F}_{1\rightarrow&space;3}&space;&plus;&space;\vec{F}_{2\rightarrow3}\\&space;&=&space;-G&space;\frac{m_1&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\vec{F}_{g}&space;&=&space;\vec{F}_{1\rightarrow&space;3}&space;&plus;&space;\vec{F}_{2\rightarrow3}\\&space;&=&space;-G&space;\frac{m_1&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" title="\begin{align*} \vec{F}_{g} &= \vec{F}_{1\rightarrow 3} + \vec{F}_{2\rightarrow3}\\ &= -G \frac{m_1 m_3}{\left \| \vec{r}_{3} - \vec{r}_{1} \right \|^{3}}(\vec{r}_{3}-\vec{r}_1) -G \frac{m_2 m_3}{\left \| \vec{r}_{3} - \vec{r}_{2} \right \|^{3}}(\vec{r}_{3}-\vec{r}_2) \end{align*}" /></a>

With the **Second Law of Newton**, this force needs to be equal to <a href="https://www.codecogs.com/eqnedit.php?latex=\vec{F}&space;=&space;m\vec{a}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\vec{F}&space;=&space;m\vec{a}" title="\vec{F} = m\vec{a}" /></a>.

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;m_3&space;\vec{a}&space;&=&space;-G&space;\frac{m_1&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)\\&space;\vec{a}&space;&=&space;-G&space;\frac{m_1}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;m_3&space;\vec{a}&space;&=&space;-G&space;\frac{m_1&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2&space;m_3}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)\\&space;\vec{a}&space;&=&space;-G&space;\frac{m_1}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" title="\begin{align*} m_3 \vec{a} &= -G \frac{m_1 m_3}{\left \| \vec{r}_{3} - \vec{r}_{1} \right \|^{3}}(\vec{r}_{3}-\vec{r}_1) -G \frac{m_2 m_3}{\left \| \vec{r}_{3} - \vec{r}_{2} \right \|^{3}}(\vec{r}_{3}-\vec{r}_2)\\ \vec{a} &= -G \frac{m_1}{\left \| \vec{r}_{3} - \vec{r}_{1} \right \|^{3}}(\vec{r}_{3}-\vec{r}_1) -G \frac{m_2}{\left \| \vec{r}_{3} - \vec{r}_{2} \right \|^{3}}(\vec{r}_{3}-\vec{r}_2) \end{align*}" /></a>

The acceleration needs to be written as a **variation of time**, that means:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;\frac{d^2\vec{r}}{dt^2}&space;&=&space;-G&space;\frac{m_1}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\frac{d^2\vec{r}_3}{dt^2}&space;&=&space;-G&space;\frac{m_1}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" title="\begin{align*} \frac{d^2\vec{r}}{dt^2} &= -G \frac{m_1}{\left \| \vec{r}_{3} - \vec{r}_{1} \right \|^{3}}(\vec{r}_{3}-\vec{r}_1) -G \frac{m_2}{\left \| \vec{r}_{3} - \vec{r}_{2} \right \|^{3}}(\vec{r}_{3}-\vec{r}_2) \end{align*}" /></a>

The position of the satellite can be calculated by resolving this **Differential Equation of Second Order**.  This equation resembles the equation of the Three Body Problem by [Musielak and Quarles [2015]](https://arxiv.org/abs/1508.02312v1). In order to solve this equation, it's important to change it to first order using a change of variables.

Let <a href="https://www.codecogs.com/eqnedit.php?latex=\vec{z}_1&space;=&space;\vec{r}_3" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\vec{z}_1&space;=&space;\vec{r}_3" title="\vec{z}_1 = \vec{r}_3" /></a>. Then,

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;\vec{z}_1&space;&=&space;\vec{r}_3&space;\\&space;\vec{z}_2&space;&=\frac{d\vec{z_1}}{dt}&space;=&space;\frac{d\vec{r}_3}{dt}&space;=&space;\vec{v}_3&space;\\&space;\frac{d\vec{z}_2}{dt}&space;&&space;=&space;\frac{d^2\vec{z}_1}{dt^2}&space;=&space;\frac{d^2\vec{r}_3}{dt^2}&space;=&space;-G&space;\frac{m_1}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\vec{z}_1&space;&=&space;\vec{r}_3&space;\\&space;\vec{z}_2&space;&=\frac{d\vec{z_1}}{dt}&space;=&space;\frac{d\vec{r}_3}{dt}&space;=&space;\vec{v}_3&space;\\&space;\frac{d\vec{z}_2}{dt}&space;&&space;=&space;\frac{d^2\vec{z}_1}{dt^2}&space;=&space;\frac{d^2\vec{r}_3}{dt^2}&space;=&space;-G&space;\frac{m_1}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{1}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_1)&space;-G&space;\frac{m_2}{\left&space;\|&space;\vec{r}_{3}&space;-&space;\vec{r}_{2}&space;\right&space;\|^{3}}(\vec{r}_{3}-\vec{r}_2)&space;\end{align*}" title="\begin{align*} \vec{z}_1 &= \vec{r}_3 \\ \vec{z}_2 &=\frac{d\vec{z_1}}{dt} = \frac{d\vec{r}_3}{dt} = \vec{v}_3 \\ \frac{d\vec{z}_2}{dt} & = \frac{d^2\vec{z}_1}{dt^2} = \frac{d^2\vec{r}_3}{dt^2} = -G \frac{m_1}{\left \| \vec{r}_{3} - \vec{r}_{1} \right \|^{3}}(\vec{r}_{3}-\vec{r}_1) -G \frac{m_2}{\left \| \vec{r}_{3} - \vec{r}_{2} \right \|^{3}}(\vec{r}_{3}-\vec{r}_2) \end{align*}" /></a>

Inserting this equation in code, is needed to separate the vectors in the components <a><img src="https://latex.codecogs.com/svg.latex? x "/></a> and <a><img src="https://latex.codecogs.com/svg.latex? y "/></a>. Before was discussed, that the satellite had an initial position and velocity. The final goal of this program is to test the motion of the satellite with the given initials conditions, and check which conditions are better.

### Results

![result](..\Three Body Problem\result.png)



