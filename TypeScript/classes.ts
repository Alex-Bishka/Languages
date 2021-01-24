/*
    A class can have properties and methods.
    A property is a key-value pair.
    A method is a function within the class.

    Regular JavaScript CANNOT do classes.
    ES6 can do classes, but you CANNOT do static typing.

    We can add in access modifiers like private.
*/

interface UserInterFace {
    name: string;
    email: string;
    age: number;
    register();
    payInvoice();
}

class User implements UserInterFace {
    // our properties - with static typing
    name: string;
    email: string;
    age: number;

    // access modifer options
    // age: number;
    // public age: number; // regular access
    // protected age: number; // can be accessed through inheritance
    // private age: number; // cannot be accessed outside of the class

    // constructor (runs when we instantiate an object with this class)
    // this will run when we create a user
    constructor(name: string, email: string, age: number) {
        this.name = name; // this pertains to the class, so this.name pertains to the name property of the class
        this.email = email;
        this.age = age;

        console.log(`User created: ${this.name}`);
    }

    // example of a method
    // these can also have access modifiers
    register() {
        console.log(`${this.name} is now registered`);
    }

    payInvoice() {
        console.log(`${this.name} paid invoice`);
    }
}

// creating a user object
let john = new User('John Doe', 'jdoe@gmail.com', 34);

// obtains John's age
console.log(john.age); // when private this cannot be accessed outside the class. Public would work. Protected works with inheritance.

john.register(); // if method is private, could only be called within the class


// inheritance time
class Member extends User {
    // properties
    id: number;

    constructor(id: number, name: string, email: string, age: number) {
        /* 
            Super is used to refer to the parent class object.
            If a derived class contains a constructor function, it must call
            super(), which will execute the constructor of the abse class.
            This must be called before we ever access a property on this in a 
            constructor body.
            Takes in properties of the class it is inheriting.
        */
        super(name, email, age);
        this.id = id; // no need to do it for name, email, age, as super will execute the constructor above
    }

    payInvoice() {
        super.payInvoice();
    }
}

let mike: User = new Member(1, 'Mike Smith', 'mike@gmail.com', 33);

mike.payInvoice();