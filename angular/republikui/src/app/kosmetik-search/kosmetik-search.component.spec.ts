import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KosmetikSearchComponent } from './kosmetik-search.component';

describe('KosmetikSearchComponent', () => {
  let component: KosmetikSearchComponent;
  let fixture: ComponentFixture<KosmetikSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KosmetikSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KosmetikSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
