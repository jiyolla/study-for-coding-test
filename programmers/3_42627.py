# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

# 평균 요청 시점에서부터 처리까지 시간을 줄이는 것은
# 총 대기 시간을 줄이는 것과 같은데
# 작업을 최소 소요 시간이 낮은 것부터 처리하면 그렇게 될 것 같다
# 물론 요청들오온 시간을 지키면서
# 그리고 문제에서 디스크 노는 것을(먼저 들어왔어도, 기다렸다가 더 짧은 것을 처리하는 최적화) 제외시켰기 때문에
# 단순하게 할 수 있을 것 같다.

import heapq


def solution(jobs):
    jobs.sort()

    job_count = len(jobs)
    time_count = 0
    cur_time = 0
    pending_jobs = []
    while jobs or pending_jobs:
        if not pending_jobs:
            start_time, process_time = jobs.pop(0)
            cur_time = start_time
        else:
            process_time, start_time = heapq.heappop(pending_jobs)
        cur_time += process_time
        time_count += cur_time - start_time
        while jobs:
            if jobs[0][0] <= cur_time:
                start_time, process_time = jobs.pop(0)
                heapq.heappush(pending_jobs, (process_time, start_time))
            else:
                break

    return int(time_count/job_count)

print(solution([[0, 3], [1, 9], [2, 6]]))
