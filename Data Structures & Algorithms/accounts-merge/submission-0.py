class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # build adj_lst 
        email_to_name = {}
        adj_lst = defaultdict(list)
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                adj_lst[first_email].append(email)
                adj_lst[email].append(first_email)
                email_to_name[email] = name 
        # print(adj_lst)
        visit = set()
        def dfs(email, components):
            visit.add(email)
            components.append(email)

            for nei in adj_lst[email]:
                if nei not in visit:
                    dfs(nei, components)



        res = []
        for email in adj_lst:
            if email not in visit:
                components = []
                dfs(email,components)
                res.append([email_to_name[email]] + sorted(components))
        return res
