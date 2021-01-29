import { Component } from '@angular/core';

/* 
  @Component is a decorator. 

  The selector is what will be used in the directive or html element. <app-root></app-root> in
  the index.html file comes from here. The cli will add a selector for us.

  The templateUrl is just point to the html template.

  The stlyeUrls points to the style sheet.

  The class only has one property, the title (by default).
*/
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  // properties:
  name: string = 'brad'
}
