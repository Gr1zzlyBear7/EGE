def mean_absolute_difference_solution(real, predicted):
    ans = []
    for x in range(len(real)):
        ans.append(abs(real[x] - predicted[x]))
    return sum(ans) / len(ans)


print(mean_absolute_difference_solution([12, 9, 16, 20, 18],
                                        [11, 6, 17, 18, 15]))