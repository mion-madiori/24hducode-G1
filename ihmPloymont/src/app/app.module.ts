import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import {ColorPickerModule} from 'ngx-color-picker';
import {RouterModule} from '@angular/router';

import {
  MatInputModule,
  MatTabsModule,
  MatButtonModule,
  MatMenuModule,
  MatIconModule
} from '@angular/material';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { HttpService} from './service/http.service'
import { LaumioListComponent } from './laumio-list/laumio-list.component';
import { SphereComponent } from './sphere/sphere.component';

@NgModule({
  declarations: [
    AppComponent,
    LaumioListComponent,
    SphereComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    ColorPickerModule,
    RouterModule,

    MatInputModule,
    MatTabsModule,
    MatButtonModule,
    MatMenuModule,
    MatIconModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
