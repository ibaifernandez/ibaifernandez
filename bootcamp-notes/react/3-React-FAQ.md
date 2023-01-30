## **1. ¿Cuándo se necesita el _fragment_?**

El siguiente _snippet_ renderiza:

```
export const Home = () => {
    return (
        <header>
        ...
        </header>
    );
};
```

Pero esto no...

```
export const Home = () => {
    return (
        <header>
        ...
        </header>
        <main>
        ...
        </main>
        <footer>
        ...
        </footer>
    );
};
```

De modo que me tengo que ayudar del `fragment` tal que así:

```
export const Home = () => {
    return (
        <>
        <header>
        ...
        </header>
        <main>
        ...
        </main>
        <footer>
        ...
        </footer>
        </>
    );
};
```

**¿Por qué?**

## **2. Es importante recordar como se escribe estilos en línea (_inline styles_) en React:**

```
    <h1 style={{color: "red"}}>Hello Style!</h1>
```

## **3. ¿Por qué no puedo hacer funcionar este proyecto como en el proyecto «hello-react» que hicimos anteriormente?**

Es decir, en «hello-react», `index.js` funcionaba con el siguiente código:

```
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
      <Header />
      <Hero />
      ...
  </React.StrictMode>
);
```

Y, así, iba renderizando `<Header />`, `<Hero />`, etc.

Pero cuando trato de implementar el mismo modo de hacer las coas en el presente proyecto, esa misma estrcutura anterior no me funciona... **¿por qué?**

## **4. Comentarios HTML in React**

Obsérvese igualmente como los «comentarios HTML» en React no se hacen como si de HTML se tratare, mas como si fuere JavaScript. Eso sí, encapsulando el comentario entre llaves (`{*/ Aquí va un comentario */}`).

## **5. _Blank spaces_ en React**

Finalmente, cuando se quiere insertar un espacio en un archivo `.jsx`, en lugar del tradicional `&nbsp;`, se pone un espacio entre comillas y llaves (`{" "}`).
