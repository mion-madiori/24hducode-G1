import { Component, OnInit } from '@angular/core';
import { HttpService } from '../service/http.service';

@Component({
  selector: 'app-meteo',
  templateUrl: './meteo.component.html',
  styleUrls: ['./meteo.component.scss']
})
export class MeteoComponent implements OnInit {

  constructor(
    private http: HttpService
  ) { }

  villes = ['Paris', 'Nantes', 'Lille', 'Marseille', 'Strasbourg', 'Montpellier'];
  ville: string = '';
  ngOnInit() {
  }

  valid() {
    console.log(this.ville);
    this.http.getMeteo(this.ville).subscribe(data => {
      console.log(data);

    })
  }

}
