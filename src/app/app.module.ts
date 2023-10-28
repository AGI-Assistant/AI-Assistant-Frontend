import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// Navigation bar imports
import { NavigationBarComponent } from './navbar/navigation-bar/navigation-bar.component';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';

// Polling imports
import { HttpClientModule } from '@angular/common/http';

// Chat imports
import { ChatComponent } from './chat/chat.component';
import { MessageComponent } from './message/message.component';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule } from '@angular/forms';

// Landing page imports
import { LandingpageComponent } from './landingpage/landingpage.component';

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    ChatComponent,
    MessageComponent,
    LandingpageComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    MatListModule,
    MatIconModule,
    MatInputModule,
    MatButtonModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
