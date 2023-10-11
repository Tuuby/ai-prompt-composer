import { Component } from '@angular/core';

@Component({
  selector: 'app-composing-dashboard',
  templateUrl: './composing-dashboard.component.html',
  styleUrls: ['./composing-dashboard.component.scss']
})
export class ComposingDashboardComponent {
  userPrompt: string = "";
  systemPrompt: string = "";
  inputData: string = "";
  template: string = "";

  onUserPromptChange(e: Event) {
    console.log("[User prompt]: " + this.userPrompt)
  }

  onSystemPromptChange(e: Event) {
    console.log("[System prompt]: " + this.systemPrompt)
  }

  onInputDataChange(e: Event) {
    try {
      JSON.parse(this.inputData);
    } catch (e) {
      console.log("[Input data]: not a valid JSON string")
      return;
    }
    console.log("[Input data]: " + this.inputData)
  }

  onTemplateChange(e: Event) {
    if (this.template.includes("{systemPrompt}") && this.template.includes("{userPrompt}") && this.template.includes("{inputData}")) {
      console.log("[Template]: " + this.template)
    } else {
      console.log("[Template]: missing placeholders")
    }
  }
}
