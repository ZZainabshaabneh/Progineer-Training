## Experiment 1: Temperature

- **Model and settings:** openai/gpt-oss-120b; temperature 0 and 1.2; three runs for each setting.
- **What I saw:** At temperature 0, the model suggested Al-Qahwa al-Qadima, Rihan Café, and Sahra Café. At temperature 1.2, it suggested Bustan Bean Café, Al-Quds Café, and Nablus Nook Café. The answers were different at both settings, even at temperature 0.
- **What I would change in the prompt:** I would ask for shorter descriptions and more variety in the café names.
## Experiment 2: System Prompt

- **Model and settings:** openai/gpt-oss-120b; same question with System Prompt A and System Prompt B.
- **What I saw:** Prompt A gave a direct, professional answer by stating the problem first and then the fix. Prompt B used simple language and everyday examples, such as apples and a ruler. Both answers correctly explained why we should split the data before scaling.
- **What I would change in the prompt:** I would ask the model to use shorter sentences and one clear example to make the explanation easier to understand.
