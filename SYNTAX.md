# SYNTAX
in version a0.1 has 5 commands (not counting comments)

# ENTRY [input] [floor]
all programs on this language must start with command ENTRY

Without this command or you don't whrite 2 arguments you get SyntaxError

<li>[input] - With this argument, the program creates input. </li>
<li>[floor] - takes only an int and uses it to create a floor. </li>

# INBOX
This command takes the first character in the input and moves it to the hands.

# OUTBOX
This command transfers from hands at the beginning of output

# COPYTO [floor_id]
This command transfers from hands to the floor by [floor_id]

# COPYFROM [floor_id]
This command copies from the floor by [floor_id] to the hands and ignores what is in the hands
