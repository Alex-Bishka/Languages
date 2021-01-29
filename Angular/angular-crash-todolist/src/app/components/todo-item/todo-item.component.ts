import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { TodoService } from '../../services/todo.service';

import { Todo } from 'src/app/models/Todo';

@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todo-item.component.css']
})
export class TodoItemComponent implements OnInit {
  // '!' is a postfix which is syntax that exists for the case
  // where you cannot guarante the value will be defined
  // immediately - default value is usually prefered
  @Input() todo!: Todo;
  @Output() deleteTodo: EventEmitter<Todo> = new EventEmitter;

  constructor(private todoService: TodoService) {}

  ngOnInit(): void {}

  // set Dynamic Classes
  setClasses() {
    let classes = {
      todo: true,
      'is-complete': this.todo.completed,
    }

    return classes;
  }

  onToggle(todo: Todo) {
    // Toggle in UI
    todo.completed = !todo.completed;

    // Toggle on server
    this.todoService.toggleCompleted(todo).subscribe(todo => {
      console.log(todo)
    });
  }

  onDelete(todo: Todo) {
    this.deleteTodo.emit(todo);
  }
}
