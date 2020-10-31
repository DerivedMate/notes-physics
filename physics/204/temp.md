Witam serdecznie,  
Piszę w sprawie udostępnionych rozwiązań pierwszej części zadań olimpiady, dokładniej pytania pierwszego zadań numerycznych. Osobiście rozwiązałem je poprzez rozwiązanie równania różniczkowego wynikającego z drugiego prawa Newtona i podanego wzoru na opór powietrza, i znalezienie miejsce przecięcia z $h=h_{\text{końcowe}}$, gdyż nie znalazłem sposobu na rozwiązanie $h(t)$ dla $t$ względem $h$ (bez wykorzystywania funkcji W Lamberta): 
$$
\begin{aligned}
  \beta = 6\pi r\eta & ; & m = \frac{4}{3}\pi r^3 * 997
\end{aligned} \\ 
ma = mg - \beta v  \\
\lrArr \frac{dv}{dt} = g - \frac{\beta}{m}v \\
\int \frac{1}{g - \frac{\beta}{m}v} dv = \int dt \\
v(t) = \frac{m}{\beta} [g - Ce^{\frac{-\beta}{m}t}] \\
v(0) = 0 \rArr C = g \\
\frac{dh}{dt} = \frac{mg}{\beta} [1 - e^{\frac{-\beta}{m}t}] \\
h(t) = \frac{mg}{\beta} [t + \frac{m}{\beta}e^{\frac{-\beta}{m}t}] + C \\
h(0) = 0 \rArr C = -\frac{m^2}{\beta^2}g \\
h(t) = \frac{mg}{\beta}t + g\frac{m^2}{\beta^2}e^{\frac{-\beta}{m}t} - \frac{m^2}{\beta^2}g
$$  

Znalazłem również wzór który okazał się dobrym przybliżeniem dla małych wartości $r$, jednak jego wyprowadzenie nie wydaje mi się poprawne (szczególnie, że z pierwszego wzoru można wykazać, że $v_t$ osiągnięte zostanie dopiero w nieskończoności):  
$$
m\frac{dv}{dt} = mg - \beta \frac{dh}{dt} \\
\int_0^{v_t} dv = \int_0^t g dt - \int_0^h \frac{\beta}{m} dh \\
v_t = gt - \frac{\beta h}{m} \\
$$
Z faktu, że $v_t$ osiągnięte jest w momencie kiedy siły ciężaru i oporu działające na ciało się równoważą, czyli $a = 0$:  
$$
v_t = \frac{mg}{\beta} \\
\rArr gt - \frac{\beta h}{m} = \frac{mg}{\beta} \\
t =  \frac{m}{\beta} + \frac{\beta h}{mg}
$$  
Zastanawia mnie jednak, czy nie istniałaby prostsza metoda rozwiązania tego problemu. Załączam również link do wyżej wspomnianego  wykresu: https://www.desmos.com/calculator/frofatothg?lang=es .  
Z góry dziękuję za wszelką odpowiedź i serdecznie pozdrawiam,  
Tomasz Surowiec