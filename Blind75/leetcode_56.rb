# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
  intervals.sort!
  len = intervals.length
  merged = [intervals[0]]

  for i in 1...len
    # If they overlap, when prev interval's end > current interval's start
    if merged[-1][1] >= intervals[i][0]
      merged[-1][0] = [merged[-1][0], intervals[i][0]].min
      merged[-1][1] = [merged[-1][1], intervals[i][1]].max
    else
      merged << intervals[i]
    end
  end

  merged
end

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [4, 5]]
# intervals = [[4, 7], [1, 4]]
intervals = [[1, 4], [0, 0]]
puts("#{merge(intervals)}")
