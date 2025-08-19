---
layout: default
title: Home
---
 
I am an Assistant Professor of [ECE](https://www.ece.ucr.edu/) and [CSE](https://www1.cs.ucr.edu/) at the [University of California, Riverside](https://cisl.ucr.edu/),
where I lead the [Collaborative Intelligence Systems Lab](https://cisl.ucr.edu/) (CISL) which innovates in cooperative robots and networked autonomous systems.
I am also a faculty member of Center for Robotics and Intelligent Systems ([CRIS](https://www.cris.ucr.edu/)), 
and a faculty member of Center for Environmental Research and Technology ([CE-CERT](https://www.cert.ucr.edu/)).

My lab's mission is to infuse collaborative intelligence into today's autonomous systems, 
breaking the barriers between robot intelligence, edge/cloud intelligence, and human intelligence,
empowering them to communicate and cooperate to achieve capabilities beyond individuals.
In this interdisciplinary effort, our research focuses on networked systems problems at the intersection of machine learning systems, robotics, cyber-physical systems, edge computing, and networking.

Before joining UCR as faculty, I was a software engineer at [Waymo](https://waymo.com), Google's (Alphabet's) self-driving car spin-off, 
a postdoctoral scholar in the [Platform Lab](https://platformlab.stanford.edu/student/han-qiu/) at [Stanford University](https://www.stanford.edu/), 
worked in [Microsoft Research](https://www.microsoft.com/en-us/research/group/networking-research/), [IBM Research](https://research.ibm.com/labs/watson/), and collaborated with [General Motors](https://www.gm.com/) for over five years.
I received my Ph.D. from the [Networked Systems Lab](https://nsl.usc.edu/) at [University of Southern California](https://www.usc.edu/), and my bachelor degree from the [IIoT](https://iiot.sjtu.edu.cn/) at [Shanghai Jiao Tong University](https://en.sjtu.edu.cn/).


**Prospective Students**: please check out our lab's [Join Us](https://cisl.ucr.edu/joinus/) page. I may not be able to reply every email, but I do read all of them ;-)

<hr>

#### Hiring for Fall 2026:

We are hiring from both **ECE** and **CSE** department, in the following areas.
* Vehicular/Robotic Networks, Edge Computing
* ML Systems, Systems for ML

<hr>

#### Recent News:
{% assign news = site.data.news | concat: site.data.lab_news | sort : "date" | reverse %}
<ul>
{% for item in news %}
    <li> {{ item.date | date: "%b %Y"}}: <em>{{ item.title | markdownify | remove: '<p>' | remove: '</p>'}}</em></li>
{% endfor %}
</ul>