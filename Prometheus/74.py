def create_calendar_page(month=None,year=None):
    import datetime
    head="--------------------\nMO TU WE TH FR SA SU\n--------------------\n"
    count=1
    n=1
    cn=0
    if month==None:
        month=(datetime.date.today()).month
    if year==None:
        year=(datetime.date.today()).year
    dt= datetime.date(year,month,1)
    str_days='  '*(dt.weekday())+' '*(dt.weekday()-1)
    dt2=datetime.timedelta(days=1)
    while dt.month==month:
        s=str(n)
        if len(s)<2:
            s="0"+s
        if (len(str_days)-cn)%20==0:
            str_days=str_days+s
        else:
            str_days=str_days+' '+s
        n=n+1
        dt=dt+dt2
        if len(str_days)==20 or len(str_days)==41 or len(str_days)==62 or len(str_days)==83 or len(str_days)==104:
            str_days=str_days+"\n"
            cn=cn+1
    res=head+str_days
    return res
print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)
