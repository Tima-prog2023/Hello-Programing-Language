import os
import sys
import json

class HelloInterpreter:
    def __init__(self):
        self.commands = self.load_commands()

    def load_commands(self):
        with open("standart.json", "r") as file:
            commands_data = json.load(file)
        return commands_data["commands"]

    def print_to_screen_function(self, message):
        print(message)

    def get_input_function(self, prompt):
        return input(prompt)

    def interpret_file(self, filename):
        _, file_extension = os.path.splitext(filename)
        if file_extension != '.hello':
            print("Error: Invalid file format. Expected .hello")
            return
        with open(filename, "r") as file:
            code = file.read()
        self.interpret(code)

    def interpret(self, code):
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith("print_to_screen"):
                message = line[line.index("(") + 1:line.index(")")]
                self.print_to_screen_function(message.strip("\"'"))
            elif line.startswith("get_input"):
                prompt = line[line.index("(") + 1:line.index(")")]
                result = self.get_input_function(prompt.strip("\"'"))
                print(result)

if __name__ == "__main__":
    interpreter = HelloInterpreter()
    if len(sys.argv) != 2:
        print("Usage: python hello_interpreter.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    interpreter.interpret_file(filename)

