#!/usr/bin/env ruby
value = ARGV[0].scan(/\[from:(\w+|\+?\d+)\] \[to:(\w+|\+?\d+)\] \[flags:(\-?\d:\-?\d:\-?\d:\-?\d:\-?\d)\]/)
puts "#{value[0][0]},#{value[0][1]},#{value[0][2]}"
