from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time: float = customers[0][0] if customers else 0.0
        waiting_times: List[float] = []
        for i in range(len(customers)):
            (arrival_time, prep_time) = customers[i]
            current_time = max(current_time, arrival_time)
            finish_time: int = current_time + prep_time
            waiting_time = finish_time - arrival_time
            waiting_times.append(float(waiting_time))
            current_time = finish_time
        assert len(customers) == len(waiting_times)
        return sum(waiting_times) / float(len(waiting_times))


if __name__ == "__main__":
    # print(Solution().averageWaitingTime([[1,2],[2,5],[4,3]]))
    print(Solution().averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
