city = "markham"
prov = "ontario"
rc = "racecar"

def palindrome_tester(s)
	if s == s.reverse
    	puts "Palindrome"
	else
		puts "not a palindrome"
	end
end

a = "A man, a plan, a canal, Panama".split(",")
puts s = a.join()

s = s.split(" ").join()
puts s
palindrome_tester(s)
palindrome_tester(s.downcase)

puts arr =('a'..'z').to_a
arr[7]

# (0..16).each { |i| puts 2**i } 
def yeller(a)
	a.map { |c| c.upcase }
	a.join()
end

yeller(["o", "l", "d"])

def random_subdomain()
	('a'..'z').to_a.shuffle[0..7].join
end

puts random_subdomain()

def string_shuffle(s)
	s.split('').shuffle.join
end

puts string_shuffle("abcd")

numbers = { 'one' => 'uno', 'two' => 'dos', 'three' => 'tres' }
numbers.each do |key, value|
	puts "'#{key}' in spanish is '#{value}'"
end

p1 = { :first => "FN1", :last => "LN1" }
p2 = { :first => "FN2", :last => "LN2" }
p3 = { :first => "FN3", :last => "LN3" }

family = { :father => p1, :mother => p2, :child => p3 }
puts family[:father], family[:mother], family[:child]
