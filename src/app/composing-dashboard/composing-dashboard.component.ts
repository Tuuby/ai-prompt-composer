import { Component } from '@angular/core';
import { LLMsService, PostPromptRequest } from '../api/v1';
import { PromptService } from '../api/v1';
import { FormControl } from '@angular/forms';
import { Validators } from '@angular/forms';

import { jsonValidator, templateValidator } from './customValidators';

@Component({
  selector: 'app-composing-dashboard',
  templateUrl: './composing-dashboard.component.html',
  styleUrls: ['./composing-dashboard.component.scss']
})
export class ComposingDashboardComponent {
  userPrompt: FormControl = new FormControl('', Validators.required);
  systemPrompt: FormControl = new FormControl('', Validators.required);
  inputData: FormControl = new FormControl('', [Validators.required, jsonValidator()]);
  template: FormControl = new FormControl('', [Validators.required, templateValidator()]);
  output: FormControl = new FormControl('')

  llms$ = this.llmsService.llmsGet();
  prompt$ = this.promptService.promptPost();

  constructor(private llmsService: LLMsService, private promptService: PromptService) {
    this.userPrompt.valueChanges.subscribe(value => {console.log(value)});
    this.systemPrompt.valueChanges.subscribe(value => {console.log(value)});
    this.inputData.valueChanges.subscribe(value => {console.log(value)});
    this.template.valueChanges.subscribe(value => {console.log(value)});
  }

  submitPrompt() {
    let request: PostPromptRequest = {
      userPrompt: this.userPrompt.value,
      systemPrompt: this.systemPrompt.value,
      inputData: this.inputData.value,
      template: this.template.value
    }
    //send and handle request

    let response: string = "This is the response!";
    this.output.setValue(response);
  }

}
