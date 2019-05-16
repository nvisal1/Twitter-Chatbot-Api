import { Component, OnInit, HostListener, Input } from '@angular/core';
import { SocketService } from '../socket-service.service';
import { trigger, transition, query, style, stagger, animate } from '@angular/animations';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss'],
  animations: [
    trigger('stagger', [
      transition('* => *', [
        query(':enter', [
          style({ opacity: 0, transform: 'translateY(10px)' }),
          stagger('100ms', [
            animate('100ms ease', style({ opacity: 1, transform: 'translateY(0px)' }))
          ])
        ])
      ])
    ])
  ]
})
export class ChatComponent implements OnInit {

  messages = []

  input: string;
  focused: boolean;

  @HostListener('window:keypress', ['$event']) handeKeypress(event: KeyboardEvent) {
    if (event.keyCode === 13 && this.input && this.focused) {
      this.sendMessage(this.input);
      this.input = '';
    }
  }

  constructor(private socket: SocketService) {
    this.socket.messages.subscribe(message => {
      message.owned = message.source === this.socket.id;
      this.messages.push(message);
    });
  }

  ngOnInit() {
  }

  sendMessage(text: string) {
    this.socket.emit(text);
  }

  trackby(index, item) {
    return item.id;
  }

}
