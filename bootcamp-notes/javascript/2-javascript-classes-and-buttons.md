# JavaScript Classes and Buttons

## Classes

    class Player {                                                                              //  Class' name must be written in Pascalcase
        name;                                                                                   //  Declare the variables.They do not need
        age;                                                                                    //  any sort of keyword (const, let, var)
        position;                                                                               //  as they are implicit.
        constructor(name, age, position) {                                                              //  Declare the 'constructor' function
                                                                                                        //  passing on, as parametes, the
                                                                                                        //  variables previously declared.
            this.name = name;                                                                           //  Set the
            this.age = age;                                                                             //  construction
            this.position = position;                                                                   //  declaration.
    }
    display() {                                                                                         //  Declare the methods as anonymous
        console.log(`${this.name}, your age is ${this.age}, and your position is ${this position}.`);   //  functions without having to use the
    }                                                                                                   //   'function' keyword.

    const MichaelJordan = new Player("Michael Jordan", 62, "small forward");

    console.log(MichaelJordan.display())                                                        //  returns "Michael Jordan, your age is 62,
                                                                                                //  and your position is small forward."

## Buttons

    <button onClick={handleClick}>Click Me</button>                                 //  Calls the function 'handleClick' passing the event
                                                                                    //  (click) as a parameter.
    // is equivalent to

    <button onClick={(e)=>{handleClick(e)}>Click Me</button>

    // is different to

    <button onClick={()=>{handleClick(param1,param2... paramN)}>Click Me</button>   //  Calls the function 'handleClick' with the params being
                                                                                    //  passed on.
