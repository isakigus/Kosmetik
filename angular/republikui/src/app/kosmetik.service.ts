import { Injectable } from '@angular/core';
import { Observable, throwError, of } from 'rxjs';
import { catchError, retry, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';


interface searchResult {
  name: String
}

@Injectable({
  providedIn: 'root'
})
export class KosmetikService {

  serachUrl: string = 'http://localhost:8000/api/search/'

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) {
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      console.log(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }

  doSearch(search_text: string, search_mode: string): Observable<searchResult[]> {
    return this.http.post<searchResult[]>(this.serachUrl, {
      search_text: search_text,
      search_mode: search_mode
    }, this.httpOptions).pipe(
      tap(_ => console.log('fetched heroes')),
      catchError(this.handleError<searchResult[]>('getHeroes', []))
    );

  }

  getProducts() {

  }
}
