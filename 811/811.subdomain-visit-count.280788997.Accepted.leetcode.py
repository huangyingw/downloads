from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        counts = defaultdict(int)
        for cpdomain in cpdomains:
            count, domains = cpdomain.split(" ")
            domains = domains.split(".")
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                counts[domain] += int(count)
        return [str(count) + " " + domain for domain, count in counts.items()]

