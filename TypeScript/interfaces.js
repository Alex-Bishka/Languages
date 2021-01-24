// our original function
/*
function showTodo(todo: {title: string, text: string}) {
    console.log(`${todo.title}: ${todo.text}`);
}

let myTodo = {title: 'Trash', text: 'Take out trash'}

showTodo(myTodo);
*/
function showTodo(todo) {
    console.log(todo.title + ": " + todo.text);
}
var myTodo = { title: 'Trash', text: 'Take out trash' };
// let myTodo = {title: 1, text: 'Take out trash'}; // this will error
showTodo(myTodo);
