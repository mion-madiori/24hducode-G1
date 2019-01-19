import { Component, OnInit, Input } from '@angular/core';
import { Sphere } from '../model/sphere';

@Component({
  selector: 'app-sphere',
  templateUrl: './sphere.component.html',
  styleUrls: ['./sphere.component.scss']
})
export class SphereComponent implements OnInit {

  @Input() id: string;
  sphere: Sphere;
  currentColor = null;

  constructor() { }

  ngOnInit() {
  }

  onColorChange(ev) {
    this.currentColor = this.hexToRgb(ev);
    console.log(this.hexToRgb(ev));

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
