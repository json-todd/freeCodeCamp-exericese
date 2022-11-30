# 1. Write a program that checks if "lab" exists in a string. If it does, print out the world

def include_lab?(input_string)
  input_string =~ /lab/
end

puts [
  'laboratory',
  'experiment',
  'Pans Labyrinth',
  'elaborate',
  'polar bear'
].filter { |string| include_lab?(string) }
# laboratory, elaborate

# 2. Programming console output and return
def execute(&block)
  block
end

execute { puts 'Hello from inside the execution! ' }
easdf