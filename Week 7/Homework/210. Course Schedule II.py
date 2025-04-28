class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_deg = [0] * numCourses
        r = []

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_deg[course] += 1

        q = deque([i for i in range(numCourses) if in_deg[i] == 0])

        while q:
            course = q.popleft()
            r.append(course)

            for nebor in graph[course]:
                in_deg[nebor] -= 1
                if in_deg[nebor] == 0:
                    q.append(nebor)

        return r if len(r) == numCourses else []