# 14.

a = [
  'white snow',
  'winter wonderland',
  'melting ice',
  'slippery sidewalk',
  'salted roads',
  'white trees'
]

output_a = a.map { |words| words.split(' ') }
            .flatten

p output_a
