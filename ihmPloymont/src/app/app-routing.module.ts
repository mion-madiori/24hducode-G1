import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LaumioListComponent } from './laumio-list/laumio-list.component';

const routes: Routes = [
  { path: 'basique', component: LaumioListComponent },
  { path: '', redirectTo: '/basique', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
