# 1. Use `each` method to iterate over an Array
original_array = (1..10).to_a

original_array.each { |number| p number }
puts ''

# 2. Same as 1. but only values greater than 5
mod_array = original_array
            .filter { |number| number > 5 }
            .each { |number| p number }
puts ''

# 3. All odd number from Array returned from 2.
mod_array.select { |num| num.odd? }

# 4. Append and Prepand to original array
original_array.push(11)
original_array.prepend(0)

# 5. get rid of 11 and append a 3
original_array.pop # return Integer 11
original_array.push(3)
p original_array
print ''

# alternative solution:
(0..11).to_a.slice(0..-2).push(3) # retrn a new Array

# 6. de-dupliate
de_dup_array = original_array.uniq
print de_dup_array

# 8.
original_hash_1 = Hash.new('defalt')
original_hash_1 = { text: 'hello, world' }

original_hash_2 = { text: 'moro, maailma' }

# 9.
h = { a: 1, b: 2, c: 3, d: 4 }
# 9.1. Get the value of key `:b`.
h[:b]
# 9.2. Add to this hash the key:value pair `{e:5}`
h[:e] = 5
# 9.3. Remove all key:value pairs whose value is less than 3.5
h.delete_if { |_key, value| value < 3.5 }

# 10.
# Hash values is arrays
hash_arr = {
  arr_1: [1, 2, 3],
  arr_2: %w[hello world]
}
# Array of hashes
arr_hashes = [
  {
    style: {
      font_size: '1rem',
      margin: '5% auto'
    }
  },
  {
    inner_text: {
      text_1: 'hello',
      text_2: 'world'
    }
  }
]

# 11
contact_data = [
  ['joe@email.com', '123 Main st.', '555-123-4567'],
  ['sally@email.com', '404 Not Found Dr.', '123-234-3454']
]

contacts = {
  'Joe Smith' => {},
  'Sally Johnson' => {}
}

# Expected output:
#  {
#    "Joe Smith"=>{:email=>"joe@email.com", :address=>"123 Main st.", :phone=>"555-123-4567"},
#    "Sally Johnson"=>{:email=>"sally@email.com", :address=>"404 Not Found Dr.",  :phone=>"123-234-3454"}
#  }

def map_data_to_contact(contact_data, contact_ds, contact_name)
  person = contact_ds[contact_name]

  person[:email] = contact_data[0]
  person[:address] = contact_data[1]
  person[:phone] = contact_data[2]
end

map_data_to_contact(contact_data[0],
                    contacts,
                    'Joe Smith')
map_data_to_contact(contact_data[1],
                    contacts,
                    'Sally Johnson')

# 16. define method to write data from `contact_data` Array to each person as key in the `contacts` Hash

# redefine `contacts`
contacts = {
  'Joe Smith' => {},
  'Sally Johnson' => {}
}

def map_data_to_contact_2(contact_data, contact_ds)
  info_semantic = %i[email address phone]

  contact_ds.each do |person, _value|
    info_ds = contact_data.shift

    info_ds.each_index do |index|
      info_value = info_ds[index]
      info_key = info_semantic[index]
      # puts "#{person}: #{info_key}, #{info_value}"
      contact_ds[person][info_key] = info_value
    end
  end
end

map_data_to_contact_2(contact_data, contacts)

p contacts

# 12. Joe's email and Sally's phone
contacts['Joe Smith'][:email]
contacts['Sally Johnson'][:phone]
