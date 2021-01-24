/*
    A class can have properties and methods.
    A property is a key-value pair.
    A method is a function within the class.

    Regular JavaScript CANNOT do classes.
    ES6 can do classes, but you CANNOT do static typing.

    We can add in access modifiers like private.
*/
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var User = /** @class */ (function () {
    // access modifer options
    // age: number;
    // public age: number; // regular access
    // protected age: number; // can be accessed through inheritance
    // private age: number; // cannot be accessed outside of the class
    // constructor (runs when we instantiate an object with this class)
    // this will run when we create a user
    function User(name, email, age) {
        this.name = name; // this pertains to the class, so this.name pertains to the name property of the class
        this.email = email;
        this.age = age;
        console.log("User created: " + this.name);
    }
    // example of a method
    // these can also have access modifiers
    User.prototype.register = function () {
        console.log(this.name + " is now registered");
    };
    User.prototype.payInvoice = function () {
        console.log(this.name + " paid invoice");
    };
    return User;
}());
// creating a user object
var john = new User('John Doe', 'jdoe@gmail.com', 34);
// obtains John's age
console.log(john.age); // when private this cannot be accessed outside the class. Public would work. Protected works with inheritance.
john.register(); // if method is private, could only be called within the class
// inheritance time
var Member = /** @class */ (function (_super) {
    __extends(Member, _super);
    function Member(id, name, email, age) {
        var _this = 
        /*
            Super is used to refer to the parent class object.
            If a derived class contains a constructor function, it must call
            super(), which will execute the constructor of the abse class.
            This must be called before we ever access a property on this in a
            constructor body.
            Takes in properties of the class it is inheriting.
        */
        _super.call(this, name, email, age) || this;
        _this.id = id; // no need to do it for name, email, age, as super will execute the constructor above
        return _this;
    }
    Member.prototype.payInvoice = function () {
        _super.prototype.payInvoice.call(this);
    };
    return Member;
}(User));
var mike = new Member(1, 'Mike Smith', 'mike@gmail.com', 33);
mike.payInvoice();
