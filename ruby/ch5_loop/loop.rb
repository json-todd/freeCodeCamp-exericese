def loop1 
  i = 0
  loop do 
    i = i + 2
    if i == 4 
      next
    end
    puts i
    if i == 10 
      break
    end
  end
end

def loop2
  puts "Type a number:"
  x = gets.chomp.to_i

  while x >= 0 
    puts x
    x -= 1
  end

  puts "Done!"
end

def loop3 
  puts "Type a number:"
  x = gets.chomp.to_i

  until x < 0 
    puts x
    x -= 1
  end
    
  puts "Done!"
end

def loop4
  loop do 
    puts "Let's do it again?" 
    answer = gets.chomp
    if answer == "no" 
      break
    end
  end
end

def loop5
  x = [1, 2, 3, 4, 5]

  for i in x.reverse do 
    puts i
  end

  for i in 1..5 do 
    puts i - 1
  end

  puts "Done"
end

loop5()