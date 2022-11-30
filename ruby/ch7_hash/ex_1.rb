# 1. Given a hash of family members, with keys as the title and an array of names as the values, 
# use Ruby's built-in select method to gather only immediate family members' names into a new array

family = {  uncles: ["bob", "joe", "steve"],
            sisters: ["jane", "jill", "beth"],
            brothers: ["frank","rob","david"],
            aunts: ["mary","sally","susan"]
          }

is_immediate_family = lambda do |relationship, name| 
  (relationship == :sisters) || (relationship == :brothers)
end

immediate_family = family
                      .select( &is_immediate_family )
                      .values
                      .flatten

print "1. select() method to gather immediate family members' names in a new array.\n"
print immediate_family
