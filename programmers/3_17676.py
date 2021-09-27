# https://programmers.co.kr/learn/courses/30/lessons/17676
# [1차] 추석 트래픽

from collections import namedtuple


def time_to_count(time):
    h, m, s = time.split(':')
    return int(h)*60*60*1000 + int(m)*60*1000 + int(float(s)*1000)


def solution(lines):
    # 직관적인 O(N^2) 풀이
    # Job = namedtuple('Job', ['start', 'end'])
    # jobs = []
    # for _, end, duration in map(str.split, lines):
    #     end = time_to_count(end)
    #     start = end - int(float(duration[:-1])*1000) + 1
    #     jobs.append(Job(start, end))
    
    # max_traffic = 0
    # for idx, first_job in enumerate(jobs):
    #     traffic = 0
    #     for job in jobs[idx:]:
    #         if job.start < first_job.end + 1000:
    #             traffic += 1
    #     if max_traffic < traffic:
    #         max_traffic = traffic

    # O(N log N) 풀이
    # https://www.geeksforgeeks.org/maximum-number-of-overlapping-intervals/
    Event = namedtuple('Event', ['time', 'type'])
    events = []
    for _, end, duration in map(str.split, lines):
        end = time_to_count(end)
        start = end - int(float(duration[:-1])*1000) + 1
        events.append(Event(start, 'start'))
        # 뒤에 보면 알겠지만
        # 1000을 더하지 않을 때는, start와 end가 겹쳐야 유량에 추가가 되지만
        # 1000을 더하면 최대 1000의 간격 동안 벌어지는 것을 허용해주는 것이다.
        events.append(Event(end + 1000, 'end'))
    
    events.sort()

    max_traffic, cur_traffic = 0, 0
    for event in events:
        if event.type == 'start':
            cur_traffic += 1
            if max_traffic < cur_traffic:
                max_traffic = cur_traffic
        elif event.type == 'end':
            cur_traffic -= 1
            
    return max_traffic

print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
