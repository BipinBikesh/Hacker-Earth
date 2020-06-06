n=int(input())
for i in range(n):
    SH,SM,EH,EM=map(int,input().split())
    tot_min=60*(EH-SH)+(EM-SM)
    wr_hr=tot_min//60
    wr_min=tot_min%60
    print(wr_hr,wr_min)
