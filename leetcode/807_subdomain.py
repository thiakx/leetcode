import unittest
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_dict = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            domain_parts = domain.split('.')
            domain_key = ''
            for domain_part in reversed(domain_parts):
                if domain_key == '':
                    domain_key = domain_part + domain_key
                else:
                    domain_key = domain_part + '.' + domain_key

                if domain_key not in count_dict:
                    count_dict[domain_key] = int(count)
                else:
                    count_dict[domain_key] += int(count)
        return [str(v) + ' ' + k for k, v in count_dict.items()]


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.subdomainVisits(["9001 discuss.leetcode.com"])
        expected = ["9001 com", "9001 leetcode.com", "9001 discuss.leetcode.com"]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
