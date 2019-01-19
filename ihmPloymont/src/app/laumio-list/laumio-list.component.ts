import { Component, OnInit } from '@angular/core';
import { HttpService } from '../service/http.service';

@Component({
  selector: 'app-laumio-list',
  templateUrl: './laumio-list.component.html',
  styleUrls: ['./laumio-list.component.scss']
})
export class LaumioListComponent implements OnInit {

  laumios: Array<any>;

  constructor(private httpService: HttpService) { }

  ngOnInit() {
    this.httpService.getAll().subscribe(data => {
      this.laumios = data;
      console.log(data);      
    })
  }

}
