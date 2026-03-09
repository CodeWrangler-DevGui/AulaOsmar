def get_cowboy_greeting(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("O nome precisa ser um texto.")
    
    name = name.strip()
    if not name:
        raise ValueError("O forasteiro precisa ter um nome.")
        
    return f"Howdy, {name}! Ready to code in the Wild West?"