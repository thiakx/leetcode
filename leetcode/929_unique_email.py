import unittest
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_list = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            if '+' in local:
                local = local[:local.index('+')]
            email_list.add(local + '@' + domain)
        return len(email_list)


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.numUniqueEmails(
            ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])
        expected = 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
