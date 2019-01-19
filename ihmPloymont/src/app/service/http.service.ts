import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  public API = 'http://laumio_0fbfbf/api/';
  public LAUMIOS_API = this.API + '/laumio';

  constructor(private http: HttpClient) {
   }

   getAll(): Observable<any> {
     return this.http.get(this.API);
   }

   getByName(name: string) {
     return this.http.get(this.LAUMIOS_API + '/' + name);
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
