import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LaumioListComponent } from './laumio-list.component';

describe('LaumioListComponent', () => {
  let component: LaumioListComponent;
  let fixture: ComponentFixture<LaumioListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LaumioListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LaumioListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
