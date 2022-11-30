5# 5. Write a method to represent Hash has_value? built-in method
def _has_value?(input_hash, value_validate)
  input_hash
    .values
    .include?(value_validate)
end
puts _has_value?( person, 'web developer'  )