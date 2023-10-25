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

  spinner = false;

  inputDataObj = 
  {
    "kunde" : "Hans Mustermann",
    "zählerstand" : 123456
  };

  inputDataPreset = JSON.stringify(this.inputDataObj);
  userPromptPreset = 'Hallo [Energieversorger-Team],\nleider habe ich heute meinen Zählerstand heute erst verspätet eingegeben - die aktuelle Rechnung wurde aber bereits auf den Schätzwert ausgestellt und ist damit zu hoch ausgefallen - ebenso der Abschlag.\nKann die aktuelle Rechnung noch anhand des neuen, heute am 15.10.21 eingegebenen Wertes korrigiert werden und der Abschlag angepasst werden?\nDanke vorab und freundliche Grüße\n[Name des Kunden]'
  systemPromptPreset = 'Du bist ein Kundenbetreuer bei einem deutschen Energieversorger.\nUnten steht eine Mail eines Kunden und die dazugehörigen Stammdaten.\nFormuliere eine freundliche Antwortmail und gib diese aus.'
  templatePreset = 'systemprompt: {systemPrompt}\nuserData: {inputData}\nuserPrompt: {userPrompt}'

  userPrompt: FormControl = new FormControl(this.userPromptPreset, Validators.required);
  systemPrompt: FormControl = new FormControl(this.systemPromptPreset, Validators.required);
  inputData: FormControl = new FormControl(this.inputDataPreset, [Validators.required, jsonValidator()]);
  template: FormControl = new FormControl(this.templatePreset, [Validators.required, templateValidator()]);
  output: FormControl = new FormControl('')

  llms$ = this.llmsService.llmsGet();
  prompt$ = this.promptService.promptPost();

  constructor(private llmsService: LLMsService, private promptService: PromptService) {
  }

  submitPrompt() {
    let request: PostPromptRequest = {
      userPrompt: this.userPrompt.value,
      systemPrompt: this.systemPrompt.value,
      inputData: JSON.parse(this.inputData.value),
      template: this.template.value,
      modelName: 'gpt-3.5-turbo',
    }
    //send and handle request
    this.output.setValue('');
    this.spinner = true;
    this.promptService.promptPost(undefined, request).subscribe(e => {    
      console.log(e.response)
      this.output.setValue(e.response);
      this.spinner = false;
    });
  }
}
