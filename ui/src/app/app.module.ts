import { NgModule, APP_INITIALIZER } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ComposingDashboardComponent } from './composing-dashboard/composing-dashboard.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatInputModule } from '@angular/material/input';
import { MatGridListModule } from '@angular/material/grid-list'
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ApiModule } from './api/v1';
import { HttpClientModule } from '@angular/common/http';
import { Configuration } from './api/v1/configuration';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatSelectModule } from '@angular/material/select'
import { APP_BASE_HREF } from '@angular/common';
//import { AppConfigService } from './AppConfig/AppConfigService';
//
//export function initConfig(appConfig: AppConfigService) {
//    return () => appConfig.loadConfig();
//}


@NgModule({
  declarations: [
    AppComponent,
    ComposingDashboardComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatGridListModule,
    MatFormFieldModule,
    MatButtonModule,
    FormsModule,
    ReactiveFormsModule,
    ApiModule.forRoot(() => {
      return new Configuration({
        basePath: 'WEB_BASE_URL/api'
      })}),
    HttpClientModule,
    MatProgressSpinnerModule,
    MatSelectModule
  ],
  providers: [
    { provide: APP_BASE_HREF, useValue: 'WEB_BASE_URL' }
   ],
//  providers: [{
//      provide: APP_INITIALIZER,
//      useFactory: initConfig,
//      deps: [AppConfigService],
//      multi: true,
//    },
//  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
