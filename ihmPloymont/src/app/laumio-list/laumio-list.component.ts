import { Component, OnInit } from '@angular/core';
import { HttpService } from '../service/http.service';
import { Subscription } from 'rxjs';
import { Laumio } from '../model/laumio';
import { Sphere } from '../model/sphere';

@Component({
  selector: 'app-laumio-list',
  templateUrl: './laumio-list.component.html',
  styleUrls: ['./laumio-list.component.scss']
})
export class LaumioListComponent implements OnInit {

  laumios: Array<Sphere>;
  laumio: Laumio;
  checkPower: boolean;

  sub: Subscription;

  constructor(private httpService: HttpService) { }

  ngOnInit() {
    this.httpService.getAllMock().subscribe(data => {
      console.log(data);
      this.laumios = data.sphere;
    });
  }

  powerOnLaumio(name: Sphere) {
    this.httpService.powerOnLaumio(name).subscribe(error => {
      console.error(error);
    });
  }

  powerOffLaumio(name: string) {
    this.httpService.powerOffLaumio(name).subscribe(error => {
      console.error(error);
    });
  }

  changeColor(name: string) {
    this.httpService.changeColor(name)
  }
}
