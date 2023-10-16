export * from './lLMs.service';
import { LLMsService } from './lLMs.service';
export * from './prompt.service';
import { PromptService } from './prompt.service';
export const APIS = [LLMsService, PromptService];
