import { TestBed } from '@angular/core/testing';

import { KosmetikService } from './kosmetik.service';

describe('KosmetikService', () => {
  let service: KosmetikService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KosmetikService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
