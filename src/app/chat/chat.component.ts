import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PollingService } from '../polling/polling.service';
import { Subscription } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { NavigationBarService } from '../navbar/navigation-bar.service';

// Message interface
interface ChatResponse {
  text: string,
  isUser: boolean,
  time: Date
}

// Component decorator
@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit, OnDestroy {
  constructor(private http: HttpClient, private pollingService: PollingService, private navService: NavigationBarService) { }
  
  toggleNavbar() {
    this.navService.toggleSidenav();
  }

  // Variable initialization
  backendUrl: string = 'http://127.0.0.1:8000/api/'
  newMessage: string = '';
  messages: ChatResponse[] = [];
  private pollingSubscription!: Subscription;

  // Subscribes to the polling service, to recive new messages
  ngOnInit(): void {
    this.pollingSubscription = this.pollingService.infoPoll$.subscribe(
      newInfo => {
        this.checkForNewMessages(newInfo);
      }
    );
  }

  // Unsubscribes from the polling service on destroy
  ngOnDestroy() {
    if (this.pollingSubscription) {
      this.pollingSubscription.unsubscribe();
    }
  }

  // Check if the polling service update contains new messages
  checkForNewMessages(newInfo: any): void {
    if (newInfo && newInfo.messageID) {
      const messageIDs = newInfo.messageID;
      // Now messageIDs is an array of the new message IDs
      // You can process these IDs as needed
      // For example, you could fetch the full message data for these IDs from the server
    }
  }

  // Sends a request to the server to get a message and add it to the message array
  getMessage() {
    const headers = new HttpHeaders().set('messageID', String(this.messages.length));
    this.http.get<ChatResponse[]>(this.backendUrl + 'get/messages', { headers }).subscribe({
      next: (response) => {
        const newMessages = response.map(message => ({
          ...message,
          time: new Date(message.time)
        }));
        this.messages.push(...newMessages);
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }

  // Sends a message to the server
  sendMessage() {
    const currentTime = new Date();
    const payload = { text: this.newMessage, isUser: true, time: currentTime };

    this.http.post<ChatResponse>(this.backendUrl + 'chat', payload).subscribe({
      next: (response) => {
        this.messages.push({ text: response.text, isUser: false, time: new Date(response.time) });
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
    this.messages.push(payload);
    this.newMessage = '';
  }

  // Sends a request to the server to get the chat history
  getChatHistory() {
    this.http.get<ChatResponse[]>(this.backendUrl + 'get/messages')
  }
}
