# 2. merge() and merge!() methods

family = {  uncles: ["bob", "joe", "steve"],
            sisters: ["jane", "jill", "beth"],
            brothers: ["frank","rob","david"],
            aunts: ["mary","sally","susan"]
          }

def print_hash(input_hash)
  input_hash.each do |key, value|
    print "#{key}: #{value}\n"
  end
  print "\n"
end

family_extended = family.merge( { parents: ['mom', 'dad'] } )

print_hash family_extended

family_extended.merge!({ 
  sisters: ["panh", "linh", "uyen"],
  cousins: ["chi"]
}) { |key, val1, val2| val1 + val2 }
print_hash family_extended