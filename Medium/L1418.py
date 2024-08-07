class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        mp, order_items, table_st = defaultdict(lambda: defaultdict(int)), set(), set()

        for cust, table, order in orders:
            mp[table][order] += 1
            order_items.add(order)
            table_st.add(int(table))

        res, col_mp = [["0" for _ in range(len(order_items) + 1)] for _ in range(len(mp.keys()) + 1)], defaultdict(int)
        res[0][0], idx = "Table", 1
        for o in sorted(list(order_items)):
            res[0][idx] = o
            col_mp[o] = idx
            idx += 1
        idx = 1
        for k in sorted(table_st):
            res[idx][0] = str(k)
            for itm, val in mp[str(k)].items():
                row, col = idx, col_mp[itm]
                res[row][col] = str(val)
            idx += 1
        return res
