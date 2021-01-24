/*
 to compile in js type "tsc file_name"

 to compile in watch mode type "tsc file_name -w"
 this way every time you save the .ts file it will
 automatically recompile

 opening the index.html file and looking at the console 
 will display or console log statements
*/

// as always the start for all languages
console.log("Hello world");

// basic datatypes/declarations
let myString: string; // can concat strs, function returns
let myNum: number; // can be ints, positive, negative, expressions, decimals, hex
let myBool: boolean;
let myVar: any; // can be any data type

myString = 'Hello world 2.0';
myString = 'Hello' + ' ' + ' world 3.0';
myString = 'Hello'.slice(0, 3);
// myString = 1; // this will cause an error since we have declared myString as a string

// examples of numbers
myNum = 22;
myNum = 5.5;
myNum = -2;
myNum = 0xf00D;
// myNum = 'test'; // this will cause an error as well, as again myNum is being set to a type it was not declared as

myBool = true;
// myBool = 1; // once again type error, 1 is not assignable to a bool

myVar = 1;
//console.log(myVar);
myVar = true;
//console.log(myVar);
myVar = "str";
//console.log(myVar);

//console.log(myString);
//console.log(myNum);
//console.log(myBool);


// array time
let strArr: string[];
let numArr: number[];
let boolArr: boolean[];

strArr = ['Hello', 'World'];
//strArr = ['Hello', 'World', 1]; // this will error as our array can only have strings in it

numArr = [1, 2, 3];
// numArr = [1, 2, 3, "test"]; // again, error due to type

boolArr = [true, false, true];

console.log(strArr);
console.log(numArr);
console.log(boolArr);

// other way to define arrays:
let strArr2: Array<string>;
let numArr2: Array<number>;
let boolArr2: Array<boolean>;


// tupule time
// basically an array with a defined number of elements
let stringNumTuple: [string, number]; // has to be an array with a string and then a number

stringNumTuple = ['hello', 4];
// stringNumTuple = [3, 4]; // error due to type with 0th element
// stringNumTuple = ['hello', 't']; // error due to type with 1st element
// stringNumTuple = ['hello', 4, 3]; // not possible, too many arguments in this case

console.log(stringNumTuple);


// void, undefined, and null
let myVoid: void = null; // void can be null
let myNull: null = undefined; // can also be set to null
let myUndefined: undefined = null; // can also be set to undefined

myVoid = undefined; // this is okay
// myVoid = 1; // this errors due to type

console.log(myVoid);