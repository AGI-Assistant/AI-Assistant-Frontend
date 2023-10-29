import { Component } from '@angular/core';
import { NavigationBarService } from '../navbar/navigation-bar.service';


@Component({
  selector: 'app-landingpage',
  templateUrl: './landingpage.component.html',
  styleUrls: ['./landingpage.component.scss']
})
export class LandingpageComponent {
    constructor(private navService: NavigationBarService) { }
  
    toggleNavbar() {
      this.navService.toggleSidenav();
    }
}
