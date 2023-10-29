import { Component } from '@angular/core';
import { NavigationBarService } from './navigation-bar.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation-bar',
  templateUrl: './navigation-bar.component.html',
  styleUrls: ['./navigation-bar.component.scss'],
})
export class NavigationBarComponent {
  constructor(
    public navService: NavigationBarService,
    private router: Router
  ) {}

  navigate(route: string) {
    this.router.navigate([route]);
    this.navService.toggleSidenav();
  }
}
