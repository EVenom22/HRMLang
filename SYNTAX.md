# SYNTAX
in version a0.1 has 5 commands (not counting comments)

# ENTRY [input] [floor]
all programs on this language must start with command ENTRY

Without this command or you don't write 2 arguments you get SyntaxError

<ul>
  <li>[input] - With this argument, the program creates <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">input.</a></li>
  <li>[floor] - takes only an int and uses it to create a <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">floor.</a> </li>
</ul>

# INBOX
This command takes the first character in the <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">input</a> and moves it to the hands.

# OUTBOX
This command transfers from hands at the beginning of <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">output.</a>

# COPYTO [floor_id]
This command transfers from hands to the <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">floor</a> by [floor_id]

# COPYFROM [floor_id]
This command copies from a specific <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">floor</a> cell using [floor_id], upon copying, whatever is held in hand is replaced by the item on the floor.

# JUMP [key_name]
This command resumes program execution from the <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">key</a> specified by `[key_name] + :`. Do not include the colon when writing the [key_name].

# JUMPZ [key_name]
This command is the same as <a href="https://github.com/EVenom22/HRMLang/edit/main/SYNTAX.md#jump-key_name">JUMP</a>, but it only executes if the value is 0. Do not include a colon when writing the key.

# JUMPN [key_name]
This command is the same as <a href="https://github.com/EVenom22/HRMLang/edit/main/SYNTAX.md#jump-key_name">JUMP</a>, but it only works if the value on hand is less than 0. Do not include a colon when writing the key.
