<div algin="center">
    <img src="hello_logo.png" width="300">
</div>

# What's new in the Hello programming language?
Now you can create variables as in the C language and you can display them on the screen using the print_variable command from the standart input/output library standart.json.
Here is an example of creating and displaying variables on the screen:
```c
include "standart.json"

start_program
{
  int x = 5;
  int y = 6;
  print_variable(x);
  print_variable(y);
}
return 0;
```

# Hello-Programing-Language
This is the Hello Programming Language - a joke programming language with C-like syntax

Repository instructions:
README.md - repository description
hello_interpreter.exe - ready-made program
hello_interpreter.py - source code Hello Programming language
main.hello - file with source code in a Hello Programming language
standart.json - standard input/output library Hello Programming language

An example of a program written in Hello:
```c
include "standart.json"

start_program
{
  print_to_screen("Hello, World!");
}
return 0;
```

You can write Hello code in any text editor. I recommend it in notepad :)
Save the file with the extension .hello
To run the file and see the result, go to the important directory where the interpreter, the language library and your file itself are located, right-click and go to “Open in terminal”.
<div algin="center">
    <img src="interpreting.png" width="1000">
</div>
Next, enter the command .\hello interpreter and file name with extension .hello to run the interpretation process. At the end you will see the desired result.
