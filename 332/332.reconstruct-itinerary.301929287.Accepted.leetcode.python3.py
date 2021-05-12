from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        tickets.sort(reverse=True)
        flights = defaultdict(list)
        for start, end in tickets:
            flights[start].append(end)
        journey = []

        def visit(airport):
            while flights[airport]:
                visit(flights[airport].pop())
            journey.append(airport)
        visit("JFK")
        return journey[::-1]

