# Bootcamp Notes

## Code Editors

1. **Differences among a code editor and a IDE.**

2. **Emmet Abbreviations**

## HTML

3.  **Meta tags**

    -   `viewport`
    -   `http-equiv`
    -   `Open Graph`
    -   `keywords, author, description`...

4.  **HTML specification**

    -   How important is to use every single HTML according to their specific use? Example: is it necessary to put every single `img` tag into a `figure` tag?

5.  **HTML Accesibility for all audiences**

    -   **ARIA**, also known as **WAI-ARIA**, stands for **_Accessible Rich Internet Applications_**. ARIA defines a variety of markup extensions, usually HTML5 attributes, that can be added to elements to give screen readers more information about the element and help visually-impaired users better grasp what’s happening on the webpage.

## CSS

8. **Which are the differences among...**

    - \*.css
    - \*.scss
    - \*.min.css
    - \*.min.js

9. **Are a library and a framework the same thing?**

    - What is a library?

    - What is a framework?

10. ### Bootstrap

## Command Line

11. **[Official Documentation on Command Line](https://cmdchallenge.com/)**

12. **In the Command Line, what's the difference among `-R` and `-r`?**

## Git, GitHub, GitFlow

-   `git checkout “index.html”` => reestablecer al ultimo commit realizado.
-   `git commit -a -m "Reorganized project"` => add y commit en una sola line, solo funciona con archivo trackeados.
-   `git merge my_version` => combinar cambios en styles con main.
-   `git init`= Convertir un directorio local en un repositorio local de GIT.
-   `git remote add origin XXX` = Conecta a un remoto (y añade un repo local con el nombre **origin**) desde la dirección `XXX`.
-   `git pull origin master` = Tráete a mi repositorio local de nombre **origin** todo lo que encuentres en la **rama** `master` del repositorio remoto al que ya debería estar enganchado.

## JEST Unit Testing

| Description                             | Syntax                                                                 |
| --------------------------------------- | ---------------------------------------------------------------------- |
| Expect the opposite                     | `expect(false).not.toBe(true)`                                         |
| Expect string to contain another string | `expect("hello world").stringContaining("world")`                      |
| Expect variable to be defined           | `expect(variable_name).toBeDefined()`                                  |
| Expect array to contain another         | `expect(['a','b','c','e']).toEqual(expect.arrayContaining(['b','c']))` |

»»» **[More "expect" statements here!](https://jestjs.io/docs/expect)** «««

### Questions

**(1)**

```

// This is a function that sums two numbers

const sum = (a,b) => {
return a + b
}

// export the function to be used on other files (similar to the keyword `export` when using webpack)

module.exports = { sum };

```

Let's focus on that last bit. This is:

```

// export the function to be used on other files (similar to the keyword `export` when using webpack)

module.exports = { sum };

```

1. ¿Da «el temario» —al menos en este punto de él— por sobreentendido que hemos practicado export en algún otro lugar?

2. ¿Hemos practicado export en algún otro lugar?

3. ¿Dan esas tres últimas líneas por sobreentendido que entendemos qué es webpack?

---

**(2)**

Taking the next snippet in consideration:

```
const { sum } = require('./app.js');

test('adds 14 + 9 to equal 23', () => {
let total = sum(14, 9);

    expect(total).toBe(23);

});

test("One euro should be 1.206 dollars", function(){
const { fromEuroToDollar } = require('./app.js')

    const dollars = fromEuroToDollar(3.5)

    const expected = 3.5 * 1.2;

     expect(fromEuroToDollar(3.5)).toBe(4.2); //1 euro are 1.2 dolares, then 3.5 euros should be = (3.5 * 1.2)

});

```

For the 1st test, the import of the function `sum` from `app.js` is done **_outside_** of the `test` declaration, whereas the import of the
function `fromEuroToDollar` is donde **_inside_** the `test` declaration... In general terms, are both of them equally _good_, or is it one more _correct_ than the other?

## JavaScript

-   `import` (?)
-   `export`(?)

## Other topics that require inquiry

-   ### **Vim**

-   ### **[srcset](https://cssworkout.guide/2019/07/03/exercise-4-adjusting-image-screen-resolution-with-srcset/)**

-   ### **What are YAML/YML files and what are they used for?**

-   ### npm

-   ### webpack

-   ### learnpack
