import datetime

# Structures used to define course schedule and assignments

class CourseDate(object):
    def __init__(self, month=None, day=None, year=datetime.date.today().year, tbd=False, note_change=False, special_time=None):
        if month and day:
            self.date = datetime.datetime(year, month, day)
        else:
            self.date = None
            
        self.tbd = tbd
        self.note_change = note_change
        self.special_time = special_time
        
    def __to_str(self, date_str):
        if self.tbd:
            return "TBD"
        else:
            return date_str
            
    def short(self):
        return self.__to_str(self.date.strftime("%b") + ". " + str(self.date.day))
        
    def long(self):
        return self.__to_str(self.date.strftime("%A,") + " " + self.date.strftime("%B") + " " + str(self.date.day))
    
    def time(self):
        time_str = self.date.strftime("%I%p").lower()
        if time_str[0] == "0":
            time_str = time_str[1:]
        return time_str
            
    def isPast(self):
        return self.date < datetime.datetime.now()
    
    def weekday(self):
        return self.date.weekday()
    
    def offset(self, n):
        d = CourseDate()
        d.date = self.date + datetime.timedelta(n)
        return d
    
    def __eq__(self, other):
        if isinstance(other, CourseDate):
            return self.date == other.date
        return NotImplemented
    
    def isSameDate(self, other):
        if isinstance(other, CourseDate):
            return self.date.month == other.date.month and self.date.day == other.date.day
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, CourseDate):
            return self.date < other.date
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, CourseDate):
            return self.date <= other.date
        return NotImplemented
    
    def __str__(self):
        return self.short()
    
 

class Course(object):
    def __init__(self, term, term_start, term_end, class_days):

        def __courseDates():
            curr_date = term_start
            class_days.sort()
            i = 0
            
            while i < len(class_days):
                if curr_date.weekday() <= class_days[i]:
                    break
                i += 1
            i %= len(class_days)
                
            while True:
                offset = (class_days[i] + 7 - curr_date.weekday()) % 7
                curr_date = curr_date.offset(offset)
                if curr_date > term_end:
                    break
                
                yield curr_date
                i = (i + 1) % len(class_days)
                
        self.dates = list(__courseDates())
        
        self.term = term
        self.year = term_start.date
        self.currentDate = None
        self.weeks = []
        self.week = None
        self.work = []
        self.discuss = []
        self.announcements = []
        
    def __addWeek(self):
        self.week = {"classes":[], "readings":[]}
        self.weeks += [self.week]
        return self.week

    def __addClass(self, date=None, **kwargs):
        if date is None:
            date = self.dates.pop(0)
        if self.currentDate is None or date.weekday() < self.currentDate.weekday():
            self.__addWeek()
        self.currentDate = date
        
        kwargs["date"] = date
        self.week["classes"] += [kwargs]
        return kwargs

    def addLecture(self, name=None, url=None, desc=None, date=None, holiday=False, star=False):
        return self.__addClass(style="lecture", name=name, url=url, desc=desc, 
                               star=star, holiday=holiday, date=date)
        
    def addDiscussion(self, name=None, url=None, desc=None, date=None, holiday=False, star=False):
        return self.__addClass(style="discussion", name=name, url=url, desc=desc, 
                               star=star, holiday=holiday, date=date)
        
    def addReading(self, desc=None):
        self.week["readings"] += [desc]

    def __addWork(self, **kwargs):
        self.work += [kwargs]
        return kwargs

    def addHomework(self, name=None, url=None, available=None, due=None):
        return self.__addWork(style="homework", name=name, url=url, available=available, due=due)

    def addProject(self, name=None, url=None, available=None, due=None):
        return self.__addWork(style="project", name=name, url=url, available=available, due=due)
    
    def addPaperResponse(self, name=None, url=None, available=None, due=None):
        return self.__addWork(style="paper-response", name=name, url=url, available=available, due=due)
    
    def addAnnouncement(self, title=None, desc=None):
        self.announcements += [{"title": title, "desc": desc}]

    def today(self, offset=None):
        if offset is not None:
            return self.currentDate.offset(offset)
        return self.currentDate

    def available(self, what, when):
        what['available'] = when
#         self.discuss += ["Introduce " + what['name']]

    def due(self, what, when, hour=18):
        d = CourseDate()
        d.date = when.date.replace(hour=hour)
        what['due'] = d
#         self.discuss += ["Review " + what['name']]

    def termStrShort(self):
        s = ""
        if self.term == "aut":
            s += "Fall"
        elif self.term == "win":
            s += "Winter"
        elif self.term == "spr":
            s += "Spring"
            
        return s

    def termStr(self):
        return self.termStrShort() + " " + self.longYear()
    
    def longYear(self):
        return self.year.strftime("%Y")
    
    def shortYear(self):
        return self.year.strftime("%y")
    
    def piazzaUrl(self):
        return "https://piazza.com/uchicago/%s/cmsc2320033250/home" % \
            (self.termStrShort() + self.longYear()).lower()