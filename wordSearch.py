def exist(board, word):
    # li = list(word)
    # first = li.pop(0)
    # firstplace=[]
    # for r in range(0,len(board)):
    #     for col in range(0,len(board[r])):
    #         if (board[r][col] == first):
    #             firstplace.append([r,col])
    
    # def next(board, done, char):
    #     row = done[len(done)-1][0]
    #     col = done[len(done)-1][1]
    #     possible = []
    #     if [row-1,col] not in done:
    #         possible.append([row-1,col])
    #     if [row+1,col] not in done:
    #         possible.append([row+1,col])
    #     if [row,col-1] not in done:
    #         possible.append([row,col-1])
    #     if [row,col+1] not in done:
    #         possible.append([row,col+1])
    #     for p in possible:
    #         if not board[p[0]][p[1]]==char:
    #             possible.remove(p)
    #     return possible

    # def check(board, done, possible, index):
    #     for p in possible:
    #         done.append(p)
    #         nextpos=next(board,done,li[index])
    #         if len(nextpos)>0:
    #             check(board,done,nextpos,li[index+1])
    #         elif len(done) == len(li):
    #             return True
    #     return False
            

    # for pair in firstplace:
    #     done=[pair]
    #     check(board,done,)
        





board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCCED"
print (exist(board,word))