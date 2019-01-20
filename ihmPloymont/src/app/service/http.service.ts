import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  public API = '//localhost:5000';
  public LAUMIOS_API = this.API + '/api/';

  constructor(private http: HttpClient) {
   }

   getAll(): Observable<any> {
     return this.http.get(this.LAUMIOS_API + '/all/');
   }

   powerOnLaumio(name: string): Observable<any> {
      return this.http.get(this.LAUMIOS_API + '/' + name + 'powerOnLaumio' );
    }  

    powerOffLaumio(name: string): Observable<any> {
      return this.http.get(this.LAUMIOS_API + '/' + name + 'powerOffLaumio' );
    } 

   changeColor(name : string) {
    return this.http.get(this.LAUMIOS_API + '/' + name + '/fill');
   }

   getCapteur(): Observable<any> {
    return this.http.get(this.API );
   }



}
