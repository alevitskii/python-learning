from collections import defaultdict
from typing import List

from m_accounts_merge_helper import UnionFind


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # initialize a constructor that will create the parents array with unique IDs
        uf = UnionFind(len(accounts))

        # create a map for mapping emails to their parent IDs
        email_mapping = {}
        for idx, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                # if the email already exists in the map, take union
                if email in email_mapping:
                    # before we take the union, make sure both the accounts have the same name
                    if account[0] != accounts[email_mapping[email]][0]:
                        return []
                    uf.union(email_mapping[email], idx)

                # add email with its ID to the map
                email_mapping[email] = idx

        # create a map to store the merged accounts
        merged_accounts = defaultdict(list)
        for email, idx in email_mapping.items():
            merged_accounts[uf.find(idx)].append(email)

        # sort the merged accounts
        final_merged = []
        for parent, emails in merged_accounts.items():
            final_merged.append([accounts[parent][0]] + sorted(emails))
        return final_merged


def main() -> None:
    inputs = [
        [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
        [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ],
    ]
    s = Solution()
    for accounts in inputs:
        print(s.accountsMerge(accounts))


if __name__ == "__main__":
    main()
