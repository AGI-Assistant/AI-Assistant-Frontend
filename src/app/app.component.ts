import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Assistant';

  constructor(private statusService: StatusBarService) { }

  toggleNavbar() {
    this.statusService.toggleSidenav();
  }
}
