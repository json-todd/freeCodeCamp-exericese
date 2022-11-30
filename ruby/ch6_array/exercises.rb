# 1.  Define program that checks if a number appears in the array,
# the equivalent to include() method
arr = [1, 3, 5, 7, 9, 11]
number = 3

def array_include_number?(input_array, number_to_check)
  input_array
    .filter {|entry|  entry == number_to_check}
    .length > 0
end

puts array_include_number?(arr, number)

# 2.

# 2.2
arr = ['a','b']
arr = arr.product([Array(1..3)])
print arr.first.delete(arr.first.last) 
# expect: [1, 2, 3]
print "\n#{arr}"
# expect: [['a'], ['b',[1,2,3]]]