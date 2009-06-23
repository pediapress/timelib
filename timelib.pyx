import datetime
import time

        
cdef extern from "timelib.h":
    struct timelib_rel_time:
        int y, m, d          # /* Years, Months and Days */
        int h, i, s          # /* Hours, mInutes and Seconds */
        
        int weekday          # /* Stores the day in 'next monday' */
        int weekday_behavior # /* 0: the current day should *not* be counted when advancing forwards; 1: the current day *should* be counted */
        
    struct timelib_time:
        int y, m, d, h, i, s
        timelib_rel_time relative
        long sse
        
    struct timelib_tzdb:
        pass
    
    struct timelib_error_container:
        pass

    struct timelib_tzinfo:
        pass
    
    long timelib_date_to_int(timelib_time *d, int *error)

    void timelib_time_dtor(timelib_time* t)
    
    timelib_time *timelib_strtotime(char *s, int len, timelib_error_container **errors, timelib_tzdb *tzdb)

    timelib_tzdb *timelib_builtin_db()
    
    void timelib_update_ts(timelib_time* time, timelib_tzinfo* tzi)
    void timelib_fill_holes(timelib_time *parsed, timelib_time *now, int options)
    void timelib_update_from_sse(timelib_time *tm)
    timelib_time * timelib_time_ctor()
    
    void timelib_dump_date(timelib_time *, int)
    void timelib_unixtime2gmt(timelib_time *tm, long ts)
    void timelib_unixtime2local(timelib_time *tm, long ts)
    

def strtotime(char *s, now=None):
    cdef timelib_time *t = NULL
    cdef timelib_time *tm_now = NULL
    
    t = timelib_strtotime(s, len(s), NULL, timelib_builtin_db())

    if now is None:
        now = int(time.time())
    else:
        now = int(now)
        
    tm_now = timelib_time_ctor()
    
    # tm_now.sse = now
    # timelib_update_from_sse(tm_now)

    timelib_unixtime2gmt(tm_now, now)
    # timelib_unixtime2local(tm_now, now)
    

    
    timelib_fill_holes(t, tm_now, 0)
    
    cdef int error=0
    timelib_update_ts(t, NULL)
    retval = timelib_date_to_int(t, &error)
    if error:
        raise RuntimeError("error occured")
    
    
    timelib_time_dtor(t)
    timelib_time_dtor(tm_now)
    
    return retval
