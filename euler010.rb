# Project Euler
# 10 - Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def is_a_prime?(number)
  if number < 2
    return false
  elsif number == 2
    return true
  elsif is_even?(number)
    return false
  end

  root = Math.sqrt(number)
  (3..root + 1).to_a.each do |test_number|
    next if is_even?(test_number)
    return false if number.modulo(test_number) == 0
  end

  return true
end

def is_even?(number)
  number.modulo(2) == 0
end

def puts_primes(limit)
  return unless limit > 0
  (0..limit).to_a.each do |potential_prime|
    puts potential_prime if is_a_prime?(potential_prime)
  end
end

def sum_primes(limit)
  return unless limit > 0
  sum = 0
  (0..limit).to_a.each do |potential_prime|
    sum = sum + potential_prime if is_a_prime?(potential_prime)
  end
  return sum
end

puts_primes(10)
puts "Sum for limit 10 is: #{sum_primes(10)}"

puts "Sum for limit 2.000.000 is: #{sum_primes(2000000)}"
