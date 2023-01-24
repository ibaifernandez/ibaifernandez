# JavaScript

## Exportación de módulos en JavaScript

> Más información en [Exportar módulos en **Lenguaje JS**](https://lenguajejs.com/javascript/modulos/export/)

Un módulo de exportación es un elemento que pone a disposición de otros ficheros Javascript, datos o código que tenemos en el fichero actual. Esto puede ser algo muy interesante de cara a organizar nuestro código en diferentes ficheros, reutilizarlos y facilitar la tarea de mantenerlo.

## Importación de módulos en JavaScript

> Más información en [Importar módulos en **Lenguaje JS**](https://lenguajejs.com/javascript/modulos/import/)

[...] vamos a ver como realizar la operación inversa a la exportación; esto es, utilizar la palabra clave `import` para cargar elementos de módulos de exportación de ficheros externos y utilizarlos en el fichero actual.

## Importación dinámica en JavaScript

> Más información en [_Import_ dinámico en Javascript en **Lenguaje JS**](https://lenguajejs.com/javascript/modulos/dynamic-import/)

[...] existe otro tipo de importación en Javascript, popularmente conocida como `import` dinámico (_dynamic import_), que tiene el siguiente aspecto, ligeramente diferente al anterior:

    import("./module.js")                   // Dynamic import
        .then(data => { /* ... */ });
