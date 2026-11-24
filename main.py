from model_manager import AImodel, modelManager

model1 = AImodel("GPT", "OpenAI", "LLM")
model2 = AImodel("Llama", "Meta", "LLM")

manager = modelManager()

manager.add_model(model1)
manager.add_model(model2)
manager.add_model(model1)

manager.display_models()

manager.search_model("GPT")
manager.search_model("Unknown")

manager.remove_models("Llama")
manager.remove_models("Llama")

manager.display_models()

manager.count_models()