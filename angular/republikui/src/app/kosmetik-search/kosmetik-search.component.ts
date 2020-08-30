import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { KosmetikService } from '../kosmetik.service';
import { debounceTime } from 'rxjs/operators';

@Component({
  selector: 'app-kosmetik-search',
  templateUrl: './kosmetik-search.component.html',
  styleUrls: ['./kosmetik-search.component.scss']
})
export class KosmetikSearchComponent implements OnInit {

  search = new FormControl('');
  service: KosmetikService

  mode: string = 'ING'
  results: any[]
  search_text: string = ''

  constructor(private kosmectikService: KosmetikService) { }

  ngOnInit(): void {
    this.onChanges();
  }

  onChanges(): void {
    this.search.valueChanges.pipe(debounceTime(1000)).subscribe(val => {
      this.search_action(val)
    });
  }

  search_action(search_text: string) {
    this.search_text = search_text
    if (this.search_text ==='')
         return
    this.kosmectikService.doSearch(
      search_text,
      this.mode
    ).subscribe((results) => {
      this.results = results
    })

  }

  setSearchMode(mode: string): void {
    this.mode = mode
    this.search_action(this.search_text)
  }

}
