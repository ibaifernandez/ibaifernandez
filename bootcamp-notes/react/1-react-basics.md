# React Basics

## Empezando

> Esta página es un resumen de la documentación de React y recursos relacionados.

**React** es una biblioteca Javascript para crear interfaces de usuario. Aprende todo de lo que trata React en nuestra página principal o en este tutorial.

-   Prueba React

-   Aprende React

-   Mantente Informado

-   Documentación por Versiones

-   ¿Algo hace falta?

Más información en [https://es.reactjs.org/docs/getting-started.html](https://es.reactjs.org/docs/getting-started.html)

## Create a New React App

> Use an integrated toolchain for the best user and developer experience.

This page describes a few popular React toolchains which help with tasks like:

-   Scaling to many files and components.
-   Using third-party libraries from npm.
-   Detecting common mistakes early.
-   Live-editing CSS and JS in development.
-   Optimizing the output for production.

The toolchains recommended on this page **don’t require configuration to get started**.

Más información en [https://reactjs.org/docs/create-a-new-react-app.html](https://reactjs.org/docs/create-a-new-react-app.html)

## Typechecking With PropTypes

As your app grows, you can catch a lot of bugs with typechecking. For some applications, you can use JavaScript extensions like Flow or TypeScript to typecheck your whole application. But even if you don’t use those, React has some built-in typechecking abilities. To run typechecking on the props for a component, you can assign the special `propTypes` property:

    import PropTypes from 'prop-types';

    class Greeting extends React.Component {
    render() {
        return (
        <h1>Hello, {this.props.name}</h1>
        );
    }
    }

    Greeting.propTypes = {
    name: PropTypes.string
    };

Más información en [https://reactjs.org/docs/typechecking-with-proptypes.html](https://reactjs.org/docs/typechecking-with-proptypes.html)

## ReactStrap

### **Bootstrap for React**

Más información en [https://reactstrap.github.io/](https://reactstrap.github.io/)
