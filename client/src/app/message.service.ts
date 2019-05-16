import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MessageService {

  id: string;

  constructor(private http: HttpClient) {
  }

  send(text: string): Promise<any> {
    return this.http
      .get(
        `http://localhost:5000/actors?text=${text}`,
      )
      .toPromise();
  }
}
