class Solution:
	# @Return a list of strings
	def phoneCombinations(self, digits):
		if len(digits) < 1: return []
		dic = {
			'2':['a','b','c'],
			'3':['d','e','f'],
			'4':['g','h','i'],
			'5':['j','k','l'],
			'6':['m','n','o'],
			'7':['p','q','r','s'],
			'8':['t','u','v'],
			'9':['w','x','y','z']
		}
		res = []
		self.getStrings(res,'',len(digits),0,digits,dic)
		return res	
		
	def getStrings(self,res,string,length,pos,digits,dic):
		if (pos == length):
			res.append(string)
			return
		for ch in dic[digits[pos]]:
			self.getStrings(res,string+ch,length,pos+1,digits,dic)
	
test = Solution()
print(test.phoneCombinations("23"))			

			
