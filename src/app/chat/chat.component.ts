import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PollingService } from '../polling/polling.service';
import { Subscription } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { NavigationBarService } from '../navbar/navigation-bar.service';

// Message interface
interface MessageDict {
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
  constructor(private http: HttpClient, private pollingService: PollingService, private navService: NavigationBarService) { 
    this.getChatHistory('conversation0');
  }
  
  toggleNavbar() {
    this.navService.toggleSidenav();
  }

  // Variable initialization
  backendUrl: string = 'http://127.0.0.1:8080/api/'
  newMessage: string = '';
  messages: MessageDict[] = [];
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
    if (newInfo && newInfo.conversationIds) {
      //this.getMessages(newInfo.conversationIds);
    }
  }

  // Sends a request to the server to get a message and adds it to the message array
  getMessages(messageIds: string[]) {
    const headers = new HttpHeaders().set('messageIds', messageIds);
    this.http.get<MessageDict[]>(this.backendUrl + 'get/messages', { headers }).subscribe({
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
  postMessage() {
    const timestamp = new Date();
    this.http.post(this.backendUrl + 'post/message', { textContent: this.newMessage, isUser: true, timestamp: Math.floor(timestamp.getTime() / 1000) }, { observe: 'response' }).subscribe({
      next: (response) => {
        if (response.status === 201) {
          this.messages.push({ text: this.newMessage, isUser: true, time: timestamp });
          this.newMessage = '';
        } else {
          console.error('Unexpected status code:', response.status);
        }
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }

  // Sends a request to the server to get the chat history
  getChatHistory(conversationId: string) {
      const headers = new HttpHeaders().set('conversationId', conversationId);
      this.http.get<any>(this.backendUrl + 'get/history', { headers }).subscribe({
        next: (response) => {
          if (response.hasOwnProperty(conversationId)) {
            const newMessages = response[conversationId].map((message: MessageDict) => ({
              ...message,
              time: new Date(message.time)
            }));
            this.messages = newMessages;
          } else {
            console.warn(`No conversation found with ID: ${conversationId}`);
          }
        },
        error: (error) => {
          console.error('There was an error!', error);
        }
      });
    }
}
