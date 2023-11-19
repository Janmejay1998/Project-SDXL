from transformers import pipeline

magic_prompt_generator = pipeline("text-generation", model="Gustavosta/MagicPrompt-Stable-Diffusion", device=0)  # Use appropriate model name

def generate_prompt(user_input):
    prompt = magic_prompt_generator(user_input, max_length=50, num_return_sequences=3)
    return [p['generated_text'].strip() for p in prompt]

def get_user_input():
    user_input = input("Enter your text prompt: ")
    return user_input

def display_prompt_options(prompts):
    print("Choose a prompt:")
    for i, prompt in enumerate(prompts):
        print(f"{i + 1}. {prompt}")

def get_user_prompt_choice(prompts):
    display_prompt_options(prompts)
    choice = int(input("Enter the number of the prompt you want to choose: "))
    
    if 1 <= choice <= len(prompts):
        return prompts[choice - 1]
    else:
        print("Invalid choice. Please enter a valid prompt number.")
        return get_user_prompt_choice(prompts)

user_input = get_user_input()
generated_prompts = generate_prompt(user_input)
selected_prompt = get_user_prompt_choice(generated_prompts)

print(selected_prompt)