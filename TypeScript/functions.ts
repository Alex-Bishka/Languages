/*
    time to learn about functions!
    if you have a return type, you must return!
*/

function getSum(num1: number, num2: number): number {
    return num1 + num2;
    // return "hello" // error due to function return type
}

// console.log(getSum(1, 4));
// console.log(getSum("h", 4)); // error due to type

let mySum = function(num1: any, num2: any): number {
    if (typeof num1 == 'string') {
        num1 = parseInt(num1);
    }
    if (typeof num2 == 'string') {
        num2 = parseInt(num2);
    }
    return num1 + num2;
}

// console.log(mySum(3, 5));
// console.log(mySum('3', '5'));

// the '?' after the lastName makes the paramenter optional
function getName(firstName: string, lastName?: string): string {
    if (lastName == undefined) {
        return firstName;
    }
    return `${firstName} ${lastName}`
}

console.log(getName("John", "Doe"));
console.log(getName("John"));

/* 
    For some reason myVoid errors only in VScode (not the compiler)
    I think it is a weird error from the auto-complete since we used
    myVoid in types.ts
*/ 
function myVoidFunc(): void {
    // return 0; // this would error
    return; // this is okay though
}