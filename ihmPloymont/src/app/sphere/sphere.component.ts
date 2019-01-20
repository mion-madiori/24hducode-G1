import { Component, OnInit, Input } from '@angular/core';
import { Sphere } from '../model/sphere';
import { HttpService } from '../service/http.service';

@Component({
  selector: 'app-sphere',
  templateUrl: './sphere.component.html',
  styleUrls: ['./sphere.component.scss']
})
export class SphereComponent implements OnInit {

  @Input() id: string;
  sphere: Sphere;
  currentColor = null;

  constructor(
    private httpService: HttpService
  ) { }

  ngOnInit() {
  }

  onColorChange(ev) {
    this.currentColor = this.hexToRgb(ev);
    this.sphere = {
      name: this.id,
      color: {
        r: this.currentColor.r,
        g: this.currentColor.g,
        b: this.currentColor.b
      }
    };
    console.log(this.sphere);
    this.httpService.powerOnLaumio(this.sphere);
  }

  private hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  }

}
