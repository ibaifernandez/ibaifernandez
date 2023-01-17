# **JEST Unit Testing**

| **Description**                         | **Syntax**                                                             |
| --------------------------------------- | ---------------------------------------------------------------------- |
| Expect the opposite                     | `expect(false).not.toBe(true)`                                         |
| Expect string to contain another string | `expect("hello world").stringContaining("world")`                      |
| Expect variable to be defined           | `expect(variable_name).toBeDefined()`                                  |
| Expect array to contain another         | `expect(['a','b','c','e']).toEqual(expect.arrayContaining(['b','c']))` |

### Resources

-   [Expect](https://jestjs.io/docs/expect)

## Questions

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

## Instructions

1. Check for node.js' latest version.

`node -v`

2. Initialize the project with the `npm init` command:

`npm init -y`

> **Note**: adding the `-y` option answers 'yes' to many questions that we _don't need_ to answer.

> > Why don't we need those questions answered?

> Check for the `package.json` file in your project folder.

3. When using the **NPM package manager**, install any 3rd party package or library by running the next command having <your_package_name> replaced with the name of your package.

`npm install <your_package_name> --save`

In this case:

`npm install jest --save`

> If installed successfully, the folder `./node_modules` must have been created in the root of your project.

4. Choose the file that represents the **entry point** of our application.

It will generally be `app.js`// the main JS file of our project // the first JS file to be loaded thru the HTML script.

> **Which one is it!?**

5. The **entry point file** of our project will most probably have some functions. We need to export those functions. Example:

```

const sum = (a,b) => {
    return a + b
}

module.exports = { sum };

```

6. Create a `test.js` file on the root of our project

7. Write the code of your `test.js` file. Example:

```

// import the function sum from the app.js file
const { sum } = require('./app.js');

// start your first test
test('adds 14 + 9 to equal 23', () => {
//inside the test we call our sum function with 2 numbers
let total = sum(14, 9);

// we expect the sum of those 2 numbers to be 23
expect(total).toBe(23);

});
```

8. Update the `package.json` file to specify the test command with the word `jest` like this:

{
"scripts": {
"test": "jest"
}
}

9. What about...

```
Test suite failed to run

The error below may be caused by using the wrong test environment, see https://jestjs.io/docs/configuration#testenvironment-string.
Consider using the "jsdom" test environment.

```
