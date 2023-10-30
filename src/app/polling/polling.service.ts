import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { timer, BehaviorSubject } from 'rxjs';
import { switchMap, share, tap } from 'rxjs/operators';

// Component decorator
@Injectable({
  providedIn: 'root'
})
export class PollingService {

  // Variable declaration
  private infoSubject = new BehaviorSubject<any>(null);
  infoPoll$ = this.infoSubject.asObservable();

  // Constructor
  constructor(private http: HttpClient) {
    this.startPolling();
  }

  // Pollingmethod sends a request to the server to recive updates. This is repeated every x seconds.
  private startPolling(): void {
    timer(0, 5000).pipe(
      switchMap(() => this.http.get('http://127.0.0.1:8000/api/get/polling', { observe: 'response' })),
      tap(response => {
        if (response.status === 200) {
          this.infoSubject.next(response.body);
        }
      }),
      share()
    ).subscribe(
      () => {},  // Success handler is empty since we handle the response in tap
      error => console.error(error)
    );
  }
}
