import os
import sys
import json
import re

class HelloInterpreter:
    def __init__(self):
        self.commands = self.load_commands()
        self.variables = {}

    def load_commands(self):
        with open("standart.json", "r") as file:
            commands_data = json.load(file)
        return commands_data["commands"]

    def print_to_screen_function(self, message):
        print(message)

    def print_variable_function(self, variable_name):
        if variable_name in self.variables:
            print(self.variables[variable_name])
        else:
            print(f"Error: Variable '{variable_name}' not found")

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
            elif line.startswith("print_variable"):
                variable_name = line.split("(")[1].split(")")[0].strip("\"'")
                self.print_variable_function(variable_name)
            elif line.startswith("get_input"):
                prompt = line[line.index("(") + 1:line.index(")")]
                result = self.get_input_function(prompt.strip("\"'"))
                print(result)
            elif line.startswith("int "):
                _, rest = line.split("int ")
                variable, value = rest.split("=")
                value = value.replace(';', '').strip()
                self.variables[variable.strip()] = int(value)
            elif line.startswith("double "):
                _, rest = line.split("double ")
                variable, value = rest.split("=")
                value = value.replace(';', '').strip()
                self.variables[variable.strip()] = float(value)
            elif line.startswith("float "):
                _, rest = line.split("float ")
                variable, value = rest.split("=")
                value = value.replace(';', '').strip()
                self.variables[variable.strip()] = float(value)
            elif line.startswith("char "):
                _, rest = line.split("char ")
                variable, value = rest.split("=")
                value = value.replace(';', '').strip()
                if len(value) != 1:
                    print("Error: Char variables can only hold one character.")
                    continue
                self.variables[variable.strip()] = value


if __name__ == "__main__":
    interpreter = HelloInterpreter()
    if len(sys.argv) != 2:
        print("Usage: python hello_interpreter.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    interpreter.interpret_file(filename)
