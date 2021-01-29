import { Component, OnInit } from '@angular/core';
import { TodoService } from '../../services/todo.service';

import { Todo } from '../../models/Todo';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})
export class TodosComponent implements OnInit {
  // properties:
  todos:Todo[] = [];

  // import services, do not want to use this 
  // for too much
  constructor(private todoService: TodoService) { }

  // like component did mount in react
  // runs right away
  ngOnInit(): void {
    /*
     .subscribe is like .then
    */
    this.todoService.getTodos().subscribe(todos => {
      this.todos = todos;
    }); 
  }

  deleteTodo(todo: Todo) {
    // UI removal
    this.todos = this.todos.filter(t => t.id !== todo.id);

    // serivce removal
    this.todoService.deleteTodo(todo).subscribe();
  }

  addTodo(todo: Todo) {
    this.todoService.addTodo(todo).subscribe(todo => {
      this.todos.push(todo);
    })
  }

}
