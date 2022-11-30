# 6.
x = "hi there"

my_hash = {x: "some value"}
my_hash2 = {x => "some value"}

puts my_hash # {x: "some value"}
puts
puts my_hash2 # {"hi there": "some value"}

# my_hash is using a Symbol x as a key, 
#   :x => "some value"
# but written in a more concise way of
# moving the colon to the right of the symbol 
# and removing the hash rocket.
# my_hash2 is using a String assigned to variable x as a key 

# 7.
# `NoMethodError: undefined method `keys' for Array`
# The error's console output warns us that there's no method called `keys` for Array objets
puts [1,2,3].keys # NoMethodError