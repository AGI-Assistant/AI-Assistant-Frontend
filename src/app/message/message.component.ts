import { Component, Input } from '@angular/core';

// Message interface
interface Message {
  text: string;
  isUser: boolean;
  time: Date;
}

// Component declarator
@Component({
  selector: 'app-message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.scss']
})
export class MessageComponent {
  // Recives the message contents from the chat component on display
  @Input() message!: Message;
  constructor() { }
}
