import { Component, OnInit, HostListener, Input } from '@angular/core';
import { MessageService } from '../message.service';
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

  constructor(private message: MessageService) {
   
  }

  ngOnInit() {
  }

  async sendMessage(text: string) {
    const messages = await this.message.send(text);
    console.log(messages);
  }

  trackby(index, item) {
    return item.id;
  }

}
