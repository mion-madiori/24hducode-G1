import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LaumioListComponent } from './laumio-list/laumio-list.component';
import { AnimationComponent } from './animation/animation.component';

const routes: Routes = [
  { path: 'basique', component: LaumioListComponent },
  { path: 'animation', component: AnimationComponent },
  { path: '', redirectTo: '/basique', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
