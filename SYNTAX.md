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
This command copies from the <a href="https://github.com/EVenom22/HRMLang/blob/main/TERMS.md">floor</a> by [floor_id] to the hands and ignores what is in the hands
