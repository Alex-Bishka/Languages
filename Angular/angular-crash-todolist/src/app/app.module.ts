import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

/* 
  The entry point to angular, the meeting place for all of your components.

  Angular is comprised of different modules. 

  Declarations are where your components will go (including the main app component). New
  components are added here. The cli allows for generation of components, which will automatically
  get added to declarations.

  Modules have to be added to imports. Browsing module has to deal with the DOM. The routing module
  deals with routing.

  Providers deals with services.

  Bootstrapping the main app component.

  All components will have a TS file.
*/

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
