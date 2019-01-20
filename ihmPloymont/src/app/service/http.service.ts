import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  public API = '//localhost:5000';
  public LAUMIOS_API = this.API + '/api/laumio';

  constructor(private http: HttpClient) {
   }

   getAll(): Observable<any> {
     return this.http.get(this.LAUMIOS_API + '/all/rainbow');
   }

   powerLaumio(laumio: any): Observable<any> {
    let result: Observable<Object>;
    if (laumio['href']) {
      result = this.http.put(laumio.href, laumio);
    } else {
      result = this.http.post(this.LAUMIOS_API, laumio);
    }
    return result;
    }  

   changeColor(name : string) {
    return this.http.get(this.LAUMIOS_API + '/' + name + '/fill');
   }

   getCapteur(): Observable<any> {
    return this.http.get(this.API );
   }



}
