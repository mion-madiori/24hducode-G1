import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Sphere } from '../model/sphere';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  public API = '//localhost:5000';
  public LAUMIOS_API = this.API + '/api';

  public IPMALO = 'http://192.168.0.161:5000/';

  constructor(private http: HttpClient) {
  }

  getAll(): Observable<any> {
    return this.http.get(this.LAUMIOS_API + '/laumio/names');
  }

  getAllMock(): Observable<any> {
    return this.http.get('assets/test.json');
  }

  powerOnLaumio(sphere: Sphere): Observable<any> {
    return this.http.post(this.IPMALO + 'fill', sphere);
  }

  powerOffLaumio(name: string): Observable<any> {
    return this.http.get(this.LAUMIOS_API + '/' + name + 'powerOffLaumio');
  }

  changeColor(name: string) {
    return this.http.get(this.LAUMIOS_API + '/' + name + '/fill');
  }

  getCapteur(): Observable<any> {
    return this.http.get(this.API);
  }

  getMeteo(ville: string): Observable<any> {
    return this.http.post<any>(this.IPMALO + 'weather', {'city': ville});
  }

}
