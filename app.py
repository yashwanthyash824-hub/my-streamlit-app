class StreamlitEngine:
    def __init__(self):
        self.elements = []

    def title(self, text: str):
        self.elements.append({"type": "title", "content": text})

    def write(self, text: str):
        self.elements.append({"type": "text", "content": text})

    def button(self, label: str):
        self.elements.append({"type": "button", "label": label})

    def get_elements(self):
        return self.elements

st = StreamlitEngine()