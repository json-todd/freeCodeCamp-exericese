def all_cap(word)
  if word.length > 10
    word.upcase
  else
    word
  end
end

puts(all_cap('hello'))
puts(all_cap('hello world'))
