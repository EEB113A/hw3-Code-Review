from operator import index

def sort_by_occurrence(nums):
    output_nums = []
    for i in nums:
        if i not in output_nums:
            output_nums.append(i)
            for j in output_nums:
                if nums.count(i) < nums.count(j):
                    output_nums.remove(i)
                    output_nums.insert(output_nums.index(j), i)
                    break
    return output_nums

if __name__ == '__main__':
    input_list = [2, 0, 9, 8, 9, 2, 8, 2, 0, 9, 7, 9, 8, 2, 9]
    output_list = sort_by_occurrence(input_list)
    print(output_list)

#留言板