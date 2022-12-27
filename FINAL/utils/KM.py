from scipy.optimize import linear_sum_assignment
import numpy as np


def match(student, mentor):
    # calculate similarity
    similarity_matrix = []
    for i in range(len(student)):
        all_data = []
        for j in range(len(mentor)):
            data = (np.array(student[i])[2:] == np.array(mentor[j])[2:5])
            all_data.append(np.sum(data))
        similarity_matrix.append(all_data)
    # matching students and mentors
    similarity_matrix = np.array(similarity_matrix)
    print(similarity_matrix)
    row, col = linear_sum_assignment(similarity_matrix, True)
    id = []
    name = []
    for i in range(len(row)):
        id.append([student[row[i]][0], mentor[col[i]][0]])
        name.append([student[row[i]][1], mentor[col[i]][1]])
    sum = np.sum(similarity_matrix[row, col])
    remaining_student = []
    for i in range(len(student)):
        if i not in row:
            remaining_student.append(student[i])

    return remaining_student, id, name, sum
