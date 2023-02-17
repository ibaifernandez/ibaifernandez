1. En un momento determinado, yo solito conseguí sumar «Hellos» al array que es luego mapeado y mostrado en el «Dropdown» de arriba a la derecha de la pantalla, en el que se acumulan los diferentes favoritos que va seleccionando el usuario tal y como se pretendía.

Ahora bien, en cierto punto, mi duda era cómo sumar el nombre de los personajes seleccionados. Es obvio que, tal y como ahora mismo, el sistema funciona y hace precisamente eso, pero no tengo la más mínima idea de cómo o porqué. Es decir, en resumen:

> ¿Cómo identifico a cada personaje de los que quiero añadir a favoritos? Es decir, ¿como sustituyo esos «Hellos» que fui capaz de ir añadiendo por el nombre de cada personaje en concreto? ¿Cuál ha sido el método —y el proceso— usado a tal finalidad?

2. Una vez el array —y por tanto el «Dropdown» se está llenando con los nombres de los personajes… ¿Cómo puedo conseguir hacer de cada uno de esos nombres un enlace que muestre la página de detalle de ese personaje en concreto? Ejemplo: tengo en mi lista de favoritos a Luke Skywalker. Pues yo hago clic sobre el nombre de «Luke Skywalker» en mi lista de favoritos y voy a la vista en la que se me dan detalles al respecto de Luke Skywalker.

3. Tal y como están las cosas en este momento, si, una vez ha sido añadido, borro un elemento de mi lista de favoritos, el botón del corazón de dicho elemento no se actualiza. Es decir:
    1. Añado a Luke Skywalker a mi lista de favoritos.
    2. Luke Skywalker aparece en mi lista de favoritos y el botón del corazón queda «encendido».
    3. Voy a mi lista de favoritos y borro a Luke Skywalker haciendo clic en la cruz que aparece junto al nombre.
    4. Luke Skywalker queda eliminado, pero el corazón sigue estando activo, de modo tal que tengo que hacer clic dos veces en el corazón para volver a añadir a Luke Skywalker a mi lista de favoritos (uno para desactivar el botón y otro para volver a activarlo y, con ello, sumar a Luke a mi lista de favoritos).

La pregunta sería:

> ¿Cómo se podría actualizar el estado del botón del corazón de cada personaje una vez se elimina a dicho personaje de la lista de favoritos, de modo que vuelva a pasar a inactivo y, por tanto, me permita volver a añadir a ese personaje a la lista de favoritos con un solo clic?

4. Me gustaría repasar cómo he/se ha conseguido que el botón del corazón cambie su estado entre activo e inactivo de modo tal que se quede «encendido» —fondo rojo— en el primer caso y «apagado» —fondo neutro— en el segundo.

5. Sigo sin ser capaz de poner detalles del personaje en el módulo en el que aparecen todos ellos. Como te comenté, traté de hacer lo que me sugeriste, pero solo conseguí crear un bucle infinito que me baneó de hacer más peticiones al servidor durante un buen rato.

6. El ejercicio tiene un bonus que es «Implementar una barra de búsqueda con función de auto-completado que, además, al hacer clic en cualquiera de los resultados arrojados nos lleve a la página de dicho personaje, planeta o vehículo. De esto no tengo ni la menor idea.

---

7. El otro de los bonus de este ejercicio es «Evitar que el sitio web haga fetch de la API de Star Wars en caso de que la página sea refrescada». Esto, según llegué a entender, se consigue usando algo llamado `LocalStorage`, si mal no estoy. Pues bien, en términos generales, ¿cómo se utiliza el `LocalStorage`? Y en términos específicos, ¿cómo podría utilizarlo aquí de modo que cumpla con el objetivo de este bonus?

[¿Qué es y cómo utilizar localStorage y sessionStorage?](https://ed.team/blog/que-es-y-como-utilizar-localstorage-y-sessionstorage)

---

8. Esta se nos quedó pendiente desde la semana pasada: el código necesario para mostrar una animación cualquiera mientras la data está siendo cargada.

---

9. Si algo me confundió del dictado de código del viernes pasado fue el porqué detrás de tener que llamar a las funciones de la siguiente manera: `{()=>handleClick()}`. Es decir:

> ¿Cuál es la diferencia entre llamar, por ejemplo, al clic de un botón tal que
> `onClick={handleClick()}`
> y
> `onClick={()=>handleClick()}`
> ?

**Respuesta**

La diferencia, en principio, no es ninguna (**consultar con Alfredo**).

---

10. Temas de `async/await`, no solo no los entiendo del todo, sino que no he encontrado forma de ponerlos en práctica. ¿Qué es lo que he hecho mal al respecto —en lo que a mi aplicación de Star Wars se refiere— como para no haberlo necesitado?

[Cómo usar Async / Await para escribir un código mejor en JavaScript](https://www.freecodecamp.org/espanol/news/como-usar-async-await-para-escribir-un-codigo-mejor-en-javascript/)

---

11. `.stringify()` es un método, ¿cierto? ¿Para qué se usa, cómo se usa, qué resultado da…?

[JSON.stringify()](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

---

12. Finalmente y para tener la relativa certeza de que he consolidado bien el aprendizaje, me gustaría hacer un repaso sobre:

    -   React Outlet
    -   React Context
        -   El contexto es un tipo de atajo para compartir datos y funciones entre distintos componentes.
    -   React useParams()

---

13. Si bien entiendo que ReactJS y React Native son dos cosas diferentes utilizadas con dos finalidades diferentes... ¿se utilizan de la misma manera en términos de organización del código, su sintaxis, etc.? ¿O es más bien como si de dos cosas diferentes —a aprender de forma diferenciada— se tratare?

[https://www.ranktracker.com/es/blog/reactjs-vs-react-native-which-is-the-best-option-to-consider-for-mobile-apps/](https://www.ranktracker.com/es/blog/reactjs-vs-react-native-which-is-the-best-option-to-consider-for-mobile-apps/)
