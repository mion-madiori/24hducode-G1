import { Component, OnInit } from '@angular/core';
import { Sphere, RGB } from '../model/sphere';
import { HttpService } from '../service/http.service';

@Component({
  selector: 'app-animation',
  templateUrl: './animation.component.html',
  styleUrls: ['./animation.component.scss']
})
export class AnimationComponent implements OnInit {

  listSphere: Array<Sphere> = [];
  sphere: Sphere = { name: '', color: { r: 0, g: 0, b: 0 } };
  startInterval;

  colorb1;
  colorb2;

  name = 'Laumio_0FPFPF';
  interval = 2;

  constructor(
    private http: HttpService
  ) { }

  ngOnInit() {
    this.http.getAllMock().subscribe(data => {
      this.listSphere = data.sphere;
    });
  }

  onColor1Change(ev) {
    this.colorb1 = this.hexToRgb(ev);
    this.sphere.color = this.colorb1;
  }

  onColor2Change(ev) {
    this.colorb2 = this.hexToRgb(ev);
  }

  valid() {
    if (this.interval > 1) {

      this.sphere.color = this.colorb2;
      this.http.powerOnLaumio(this.sphere).subscribe(data => {
        console.log(data);
        
      });
      this.startInterval = setInterval(() => {
        this.sphere.name = this.name;
        if (this.sphere.color === this.colorb1) {

          this.sphere.color = this.colorb2;
          this.http.powerOnLaumio(this.sphere).subscribe(data => {
            console.log(data);
            
          });

        } else {
          this.sphere.color = this.colorb1;
          this.http.powerOnLaumio(this.sphere).subscribe(data => {
            console.log(data);
            
          });

        }

      }, this.interval * 1000);
    }
  }

  clear() {
    clearInterval(this.startInterval);
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

interface Anim {
  name: string;
  color1: RGB;
  color2: RGB;
  interval: number;
}