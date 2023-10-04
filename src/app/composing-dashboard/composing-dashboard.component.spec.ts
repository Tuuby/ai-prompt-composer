import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComposingDashboardComponent } from './composing-dashboard.component';

describe('ComposingDashboardComponent', () => {
  let component: ComposingDashboardComponent;
  let fixture: ComponentFixture<ComposingDashboardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ComposingDashboardComponent]
    });
    fixture = TestBed.createComponent(ComposingDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
