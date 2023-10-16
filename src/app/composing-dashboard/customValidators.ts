import { AbstractControl, ValidationErrors, ValidatorFn } from "@angular/forms";

/* export function jsonValidator(control: AbstractControl): ValidationErrors | null {
    try {
        JSON.parse(control.value);
    } catch (e) {
        return { jsonInvalid: true };
    }
    
    return null;
}; */

/* export function templateValidator(control: AbstractControl): ValidationErrors | null {
    const template: string = control.value;
    if (template.includes("{systemPrompt}") && template.includes("{userPrompt}") && template.includes("{inputData}")) {
        return null;
    } else {
        return { templateInvalid: true };
    }
} */

export function jsonValidator(): ValidatorFn {
    return (control: AbstractControl): ValidationErrors |  null => {
        let invalid: boolean = false;
        try {
            JSON.parse(control.value);
        } catch (e) {
           invalid = true;
        }
        
        return invalid ? {jsonInvalid: {value: control.value}} : null;
    };
}

export function templateValidator(): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
        const template: string = control.value;
        if (template.includes("{systemPrompt}") && template.includes("{userPrompt}") && template.includes("{inputData}")) {
            return null;
        } else {
            return { templateInvalid: true };
        }
    }
}