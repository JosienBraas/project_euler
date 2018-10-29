# Project Euler
# 9 - Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def solution_space
  space = []
  (0..333).to_a.each do |a|
    (1..500).to_a.each do |b|
      c = 1000 - a - b
      possible_solution = [a, b, c]
      if (a < b) && (b < c)
        space << possible_solution
      end
    end
  end
  return space
end

solution_space.each do |a, b, c|
  if (a**2 + b**2 == c**2)
    puts "a: #{a}, b: #{b}, c: #{c}"
    puts "Sum is: #{a * b * c}"
  end
end
