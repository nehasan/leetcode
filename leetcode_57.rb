# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
=begin
def insert(intervals, new_interval)
    result = []
    i = 0
    n = intervals.length

    # Add all intervals ending before new_interval starts
    while i < n && intervals[i][1] < new_interval[0]
        result << intervals[i]
        i += 1
    end

    # Merge overlapping intervals
    while i < n && intervals[i][0] <= new_interval[1]
        new_interval[0] = [new_interval[0], intervals[i][0]].min
        new_interval[1] = [new_interval[1], intervals[i][1]].max
        i += 1
    end
    result << new_interval

    # Add remaining intervals
    while i < n
        result << intervals[i]
        i += 1
    end

    result
end
=end

# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
def insert(intervals, new_interval)
    inserted = []
    i = 0
    n = intervals.length

    # Add all intervals ending before new_interval starts
    while i < n && intervals[i][0] <= new_interval[0]
        inserted << intervals[i]
        i += 1
    end

    # Insert new_interval and other intervals
    inserted << new_interval
    while i < n
        inserted << intervals[i]
        i += 1
    end
    puts "After inserting new interval: #{inserted.inspect}"

    # Merge overlapping intervals
    merged = []
    n = inserted.length
    merged << inserted[0]
    for j in 1...n
        if merged[-1][1] >= inserted[j][0]
            merged[-1][1] = [merged[-1][1], inserted[j][1]].max
        else
            merged << inserted[j]
        end
    end

    puts "After merging intervals: #{merged.inspect}"

    merged

end

# intervals = [[1,3],[6,9]]
# new_interval = [2,5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# new_interval = [4,8]
# intervals = [[1,5]]
# new_interval = [2,3]
# intervals = []
# new_interval = [5,7]
intervals = [[3,5],[8,10]]
new_interval = [1,2]
insert(intervals, new_interval)