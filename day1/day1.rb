
input_file = './input.txt'
raw_input = []

File.open(input_file, 'r') do |file|
  file.each_line do |line|
    raw_input.append(line)
  end
end

# puts raw_input

calibrated_values = []

raw_input.each do |line|
  digits = line.scan(/\d/)
  calibrated_values.append("#{digits[0]}#{digits[-1]}".to_i)
end

puts calibrated_values.sum
