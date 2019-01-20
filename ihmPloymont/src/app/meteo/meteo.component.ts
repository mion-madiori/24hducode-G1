import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-meteo',
  templateUrl: './meteo.component.html',
  styleUrls: ['./meteo.component.scss']
})
export class MeteoComponent implements OnInit {

  constructor() { }

  villes = ['Paris', 'Nantes', 'Lille', 'Marseille', 'Strasbourg', 'Montpellier'];
  ville: string = '';
  ngOnInit() {
  }

  valid() {
    console.log(this.ville);

  }

}
