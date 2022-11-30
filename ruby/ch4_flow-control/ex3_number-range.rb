def number_validator
  puts 'Input a number: '
  number = gets.chomp.to_i

  if number <= 0:
    puts 'Insert a number from 0 to 100'
  elsif number <= 50
    puts '0 <= number <= 50'
  elsif number <= 100
    puts '51 <= number <= 100'
  else
    puts 'number >= 100'
  end

  number
end

number_validator
