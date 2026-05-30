class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        result_dict = defaultdict(list)
        return_result = []

        for i in range(26):
            letter = ord('a')
            letter += i
            buckets[chr(letter)] = 0

        for i in strs:
            tmp_buckets = dict(buckets)
            for j in i:
                tmp_buckets[j] += 1
            result_dict[tuple(tmp_buckets.items())].append(i)

        for bucket in result_dict:
            
            return_result.append(result_dict[bucket])
        
        return return_result
