import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SocketService {

  id: string;

  constructor(private socket: Socket) {
    this.socket.fromOneTimeEvent('init').then((val: any) => {
      this.id = val.id;
      console.log(this.id);
    });
  }

  emit(text: string) {
    this.socket.emit('message', { text, source: this.id });
  }

  get messages(): Observable<any> {
    return this.socket.fromEvent('message');
  }
}
