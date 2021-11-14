var_1 = 'walternate'
var_2 = "Double quotes also work, just like Python"
var_3 = [[ To create a multi-line string,
        start it with double square brackets
        instead of a single or double quote]]

var_1 = nil -- Removes the definition of "var_1"

num = 0

while num < 50 do -- Blocks of code are always denoted with a keyword, like "do"
  num = num + 1
end

if num > 40 then -- Keyword here is "then"
  print('over 40')
elseif s ~= 'walternate' then -- ~= is "not equals"
  -- To check equality, use "=="
  io.write("not over 40 \n")
else
  -- Variables made to be global variables by default
  thisIsGlobal = 5

  -- Make a local variable
  local line = io.read() -- reads the next input line

  -- String concatenation (formating string to include the value of a variable uses the ".." operator)
  print("Winter is coming, " .. line)
end
