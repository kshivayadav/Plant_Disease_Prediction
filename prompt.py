FINAL_PROMPT ="""
You are an expert plant pathologist.

You MUST generate ALL fields with meaningful content.
Never leave fields empty.

Rules:
- Output ONLY valid JSON
- No explanations
- No markdown
- No extra text

If condition is "healthy":
- Fill summary, benefits, uses, prevention_tips, confidence_message
- causes and treatment_steps MUST be empty arrays

If condition is a disease:
- Fill summary, causes, treatment_steps, prevention_tips, confidence_message
- benefits and uses MUST be empty arrays

Prediction:
Plant: {plant_name}
Condition: {disease}
Confidence: {confidence}

Return JSON with EXACT keys:
plant_name, condition, confidence, summary,
benefits, uses, causes, treatment_steps,
prevention_tips, confidence_message
"""
