def rob( nums) -> int:
        def recurrob(s, subarr):
            if not subarr: return s
            return max([recurrob(n + s, subarr[:i-1] + subarr[i+1:]) for i, n in enumerate(subarr)])
        return recurrob(0, nums)

def main()