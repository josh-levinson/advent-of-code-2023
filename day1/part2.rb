
# input_file = './input.txt'
input_file = './example.txt'
raw_input = []

File.open(input_file, 'r') do |file|
  file.each_line do |line|
    raw_input.append(line)
  end
end

replacement_values = {
  'one' => 1,
  'two' => 2,
  'three' => 3,
  'four' => 4,
  'five' => 5,
  'six' => 6,
  'seven' => 7,
  'eight' => 8,
  'nine' => 9,
  'zero' => 0
}

calibrated_values = []
possible_text_values = text_values.keys

raw_input.each do |line|
  puts "before: #{line}"

  text_values.each do |text, val|
    if line.include?(text)
      line.gsub!(text, val.to_s)
    end
  end

  puts "after: #{line}"

  digits = line.scan(/\d/)
  puts "digits found: #{digits.to_s}"
  derived_value = "#{digits[0]}#{digits[-1]}".to_i
  calibrated_values.append(derived_value)
  puts "derived value: #{derived_value}"
end

puts calibrated_values.sum
