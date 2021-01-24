// our original function
/*
function showTodo(todo: {title: string, text: string}) {
    console.log(`${todo.title}: ${todo.text}`);
}

let myTodo = {title: 'Trash', text: 'Take out trash'}

showTodo(myTodo);
*/

// creating an interface
// basically creating our own type
interface Todo {
    title: string;
    text: string;
}

function showTodo(todo: Todo): void {
    console.log(`${todo.title}: ${todo.text}`);
}

let myTodo = {title: 'Trash', text: 'Take out trash'};
// let myTodo = {title: 1, text: 'Take out trash'}; // this will error

showTodo(myTodo);