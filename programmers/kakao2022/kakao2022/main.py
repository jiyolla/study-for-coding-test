from .solver import alpha_solve, beta_solve, solve_limitmaxdiff_discountedlinear, solve_limitmaxdiff_preventabusediscountedlinear


# 460.19
# 445.07
# 435.06

def main():
    # # Problem #, Matching Policy, Grading Policy
    # runs = [
    #     [1, 'fcfs', 'simplelinear']
    # ]

    # for p, matching_policy, grading_policy in runs:
    #     print(f'Solving problem #{p!r} with alpha solver matching_policy={matching_policy!r} and grading_policy={grading_policy!r}...')
    #     result = alpha_solve(p, grading_policy, grading_policy)
    #     print(result)
    #     with open('results.log', 'w+') as f:
    #         f.write(f'alpha_solve({p!r}, {matching_policy!r}, {grading_policy!r}): ')
    #         f.write(f'{result}')
    # print(solve_limitmaxdiff_preventabusediscountedlinear(1))
    print(solve_limitmaxdiff_preventabusediscountedlinear(1))

        
if __name__ == '__main__':
    main()
