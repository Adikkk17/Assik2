def count_students_whocan_to_eat(stud, samsa):
    stud_queue = stud.copy()
    samsa_stack = samsa[::-1]
    stud_idx = 0
    while stud_idx < len(stud_queue):
        if stud_queue[stud_idx] == samsa_stack[-1]:
            stud_queue.pop(stud_idx)
            samsa_stack.pop()
        else:
            stud_queue.append(stud_queue.pop(stud_idx))
        if not samsa_stack:
            return 0
    return len(stud_queue)

#Test case 1
students1 = [1, 1, 0, 0]
samsas1 = [0, 1, 0, 1]
print(count_students_whocan_to_eat(students1, samsas1))
students2 = [1, 1, 1, 0, 0, 1]
samsas2 = [1, 0, 0, 0, 1, 1]
print(count_students_whocan_to_eat(students2, samsas2))
