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

  inputDataObj = {
    "kunde" : "Hans Mustermann",
    "zählerstand" : 123456
  }

  inputDataPreset = JSON.stringify(this.inputDataObj);
  userPromptPreset = 'Sehr geehrtes Energieversorgungsunternehmen,\n\nhiermit teile ich Ihnen meinen aktuellen Zählerstand mit: [Zählerstand].\n\nVielen Dank und freundliche Grüße,\n[Kunde]'
  systemPromptPreset = 'Du bist ein Kundenbetreuer bei einem deutschen Energieversorger. Unten steht eine Mail eines Kunden. Formuliere eine freundliche Antwortmail und gib diese aus.'
  templatePreset = 'systemprompt: {systemPrompt} userData: {inputData} userPrompt: {userPrompt}'

  userPrompt: FormControl = new FormControl(this.userPromptPreset, Validators.required);
  systemPrompt: FormControl = new FormControl(this.systemPromptPreset, Validators.required);
  inputData: FormControl = new FormControl(this.inputDataPreset, [Validators.required, jsonValidator()]);
  template: FormControl = new FormControl(this.templatePreset, [Validators.required, templateValidator()]);
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
      inputData: JSON.parse(this.inputData.value),
      template: this.template.value
    }
    //send and handle request
    this.output.setValue('');
    this.promptService.promptPost(undefined, request).subscribe(e => {    
      console.log(e.response)
      this.output.setValue(e.response);
    });
  }
}
