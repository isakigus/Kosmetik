import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { KosmetikSearchComponent } from './kosmetik-search/kosmetik-search.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'search',
    pathMatch: 'full'
  },
  { path: 'search', component: KosmetikSearchComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
