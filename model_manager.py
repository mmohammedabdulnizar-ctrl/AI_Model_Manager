class AImodel:
    def __init__(self,model_name,provider,model_type):
        self.model_name = model_name
        self.provider = provider
        self.model_type = model_type
        pass
    
    def display_details(self):
        print("Model name :",self.model_name)
        print("Provider :",self.provider)
        print("model type :",self.model_type)
        

model1 = AImodel("GPT","OpenAI","LLM")
model2 = AImodel("llma","meta","LLM")


class  modelManager:
    def __init__(self):
        self.models=[]
    
    def add_model(self,model_obj):
        for existing_models in self.models:
            if existing_models.model_name == model_obj.model_name:
                print("Model is already added")
                return
                
        self.models.append(model_obj)    
        print("model added successfully")
    
    def display_models(self):
        if not self.models:
            print("Model not addded")
            return
        
        for model in self.models:
            model.display_details()
            print("---------------")
    def search_model(self,model_name):
        for model in self.models:
            if model.model_name == model_name:
                print("model found")
                model.display_details()
                return
        
        print("model not found")


    def remove_models(self,model_name):
        for model in self.models:
            if model.model_name == model_name:
                self.models.remove(model)
                print("model removed succesfully")
                return
                
        print("model not found")
        