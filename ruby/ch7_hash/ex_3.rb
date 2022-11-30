# 3. Write a method to print a hash's
#     - keys 🔑
#     - values
#     - both

def print_hash_keys(input_hash)
  input_hash.keys.each { |key| print "#{key}\n"}
end

def print_hash_values(input_hash)
  input_hash.values.each{ |value| print "#{value}\n"}
end

def print_hash(input_hash)
  input_hash.each {|key, value| print "#{key}: #{value}\n"}
end

