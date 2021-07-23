import numpy as np



def edit_score(s1,s2):
    print("Edit Score!")
    return levenstein(s1, s2, True)

def levenstein(s1, s2, norm=False):
    m_row, n_col = len(s1), len(s2)


    D = np.zeros([m_row+1, n_col+1], np.float64)
    for i in range(m_row):
        D[i,0]=i
    for i in range(n_col):
        D[0,i] = i

    for j in range(1, n_col+1):
        for i in range(1, m_row+1):
            if s2[j-1] == s1[i-1]:
                D[i,j] = D[i-1, j-1]
                
            else: # cost가 최소가 되도록 찾는 과정
                D[i,j] = min(D[ i-1 ,  j  ] + 1, # 전행 같은열(윗칸)- deletion cost
                             D[  i  , j-1 ] + 1, # 같은행 전열(왼쪽)
                             D[ i-1 , j-1 ] + 1) # 전행 전열(왼쪽 대각 위)
                
    print(D)
    
    if norm:
        score = (1 - D[-1, -1]/ max(m_row, n_col)) * 100
    else:
        score = D[-1,-1]
    return score





if __name__ == '__main__':
    
    print("Edit Score")
    s1 = '꿈을꾸는아이'
    s2 = '아이오아이'
    
    edit_score(s1, s2)
    
    
    