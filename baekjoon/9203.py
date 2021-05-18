from sys import stdin
import datetime

T = int(stdin.readline())

while T > 0:
    B, C = map(int, stdin.readline().split())
    standard = datetime.datetime(2013, 1, 1, 0, 0)

    start_list = list()
    end_list = list()

    for i in range(B):
        inputs_ = list(stdin.readline().split())

        start = inputs_[1] + ' ' + inputs_[2]
        end = inputs_[3] + ' ' + inputs_[4]

        s_year = int(''.join(map(str, list(inputs_[1])[0:4])))
        s_month = int(''.join(map(str, list(inputs_[1])[5:7])))
        s_day = int(''.join(map(str, list(inputs_[1])[8:10])))

        s_hour=int(''.join(map(str,list(inputs_[2])[0:2])))
        s_minutes=int(''.join(map(str,list(inputs_[2])[3:5])))



        e_year = int(''.join(map(str, list(inputs_[3])[0:4])))
        e_month = int(''.join(map(str, list(inputs_[3])[5:7])))
        e_day = int(''.join(map(str, list(inputs_[3])[8:10])))

        e_hour=int(''.join(map(str,list(inputs_[4])[0:2])))
        e_minutes=int(''.join(map(str,list(inputs_[4])[3:5])))

        times=[0,44640,84960,129600,172800,217440,260640,305280,349920,393120,437760,480960]
        if s_year==2016 and s_month>2:

            
            
            s_year=(s_year-2013)*525600
            s_month=times[s_month-1]
            
            s_day=(s_day-1)*1440
            s_hour=s_hour*60

            start_list.append(s_year+s_month+s_day+s_hour+s_minutes+1440)

        else:
            s_year=(s_year-2013)*525600
            s_month=times[s_month-1]
            s_day=(s_day-1)*1440
            s_hour=s_hour*60

            start_list.append(s_year+s_month+s_day+s_hour+s_minutes)
        
        if e_year==2016 and e_month>2: 
            e_year=(e_year-2013)*525600
            e_month=times[e_month-1]
            
            e_day=(e_day-1)*1440
            e_hour=e_hour*60

            end_list.append(e_year+e_month+e_day+e_hour+e_minutes+1440)

        else:
            e_year=(e_year-2013)*525600
            e_month=times[e_month-1]
            e_day=(e_day-1)*1440
            e_hour=e_hour*60

            end_list.append(e_year+e_month+e_day+e_hour+e_minutes)

            

    start_list.sort()
    end_list.sort()

    counter = 0
    room = 0
    for i in range(B):
        # 지금 입장시간이 가장 빨리 끝나는 방의 
        # 종료시간+청소시간보다 빠른건
        # 가장 빨리 끝나는 방에 못들어가기 때문에
        # 새로운 방이 필요함
        if start_list[i] < end_list[counter] + C:
            room += 1
        # 가장 빨리 끝나는 방에 들어갈수 있기 때문에
        # 가장 빨리 끝나는 방을 갱신해줘야함
        else:
            counter += 1

    print(room)
    T -= 1
