## Experiment 1: Temperature

- **Model and settings:** openai/gpt-oss-120b; temperature 0 and 1.2; three runs for each setting.
- **What I saw:** At temperature 0, the model suggested Al-Qahwa al-Qadima, Rihan Café, and Sahra Café. At temperature 1.2, it suggested Bustan Bean Café, Al-Quds Café, and Nablus Nook Café. The answers were different at both settings, even at temperature 0.
- **What I would change in the prompt:** I would ask for shorter descriptions and more variety in the café names.
## Experiment 2: System Prompt

- **Model and settings:** openai/gpt-oss-120b; same question with System Prompt A and System Prompt B.
- **What I saw:** Prompt A gave a direct, professional answer by stating the problem first and then the fix. Prompt B used simple language and everyday examples, such as apples and a ruler. Both answers correctly explained why we should split the data before scaling.
- **What I would change in the prompt:** I would ask the model to use shorter sentences and one clear example to make the explanation easier to understand.

## Experiment 3: Few-Shot Prompting

- **Model and settings:** openai/gpt-oss-120b; compared prompts with and without three examples at temperature 0. Also tested temperature 1.2.
- **What I saw:** Without examples, the model scored 9/10 at temperature 0 and 10/10 at temperature 1.2. With three examples, it scored 10/10 at both temperatures. The model repeatedly added reasoning text even though I requested labels only.
- **What I would change in the prompt:** I would specify a strict output format, such as exactly 10 labels on separate lines, with no reasoning or extra text.
