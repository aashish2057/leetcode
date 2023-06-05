class Array:
    def __init__(self) -> None:
        self.nums = [1,2,3,4]

    def productExceptSelf(self):
        answer = [] 
        pre, post = 1, 1
        for i in range(len(self.nums)):
            answer.append(pre)
            pre *= self.nums[i]
        for i in range(len(self.nums)-1, -1, -1):
            answer[i] *= post
            post *= self.nums[i]
        print(answer)
            
a = Array()
print(a.productExceptSelf())

