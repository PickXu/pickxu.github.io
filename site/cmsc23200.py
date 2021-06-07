from course import Course, CourseDate

c = course = Course(term="win", term_start=CourseDate(1,4), term_end=CourseDate(3,11), class_days=[0, 2, 4])

# c.dates[19].tbd=True
# c.dates[19].note_change = True

c.dates.insert(4, CourseDate(1,11,note_change=True,special_time="6&ndash;8pm"))

hw = [c.addHomework(name="Homework 1", url="static/hw/cmsc-23200-w16-hw1.pdf"),
      c.addHomework(name="Homework 2"),#, url="static/hw/cmsc-23200-f15-hw2.pdf"),
      c.addHomework(name="Homework 3"),#, url="static/hw/cmsc-23200-f15-hw3.pdf"),
      c.addHomework(name="Homework 4"),#, url="static/hw/cmsc-23200-f15-hw4.pdf"),
      c.addHomework(name="Homework 5")]#, url="static/hw/cmsc-23200-f15-hw5.pdf")]
 
pr = [c.addProject(name="Project 1"),#, url="project1.html"),
      c.addProject(name="Project 2"),#, url="project2.html"),
      c.addProject(name="Project 3"),#, url="project3.html"),
      c.addProject(name="Project 4"),#, url="project4.html"),
      c.addProject(name="Project 5")]#, url="project5.html")]

resp = [c.addPaperResponse("Grad. paper response " + `x + 1`) for x in range(9)]

############################################################

# c.addAnnouncement(title="Late Chips", desc="""
# <p>We've decided not to use an automated late chip server. Instead, to use some of your late days, post a private message on Piazza
# to the 'late_chips' folder with your name, CNetID, the assignment, and the number of late chips you are requesting.
# <b>You must request late chips for an assignment before you hand it in.</b></p>
# 
# <p>Remember, with the exception of extraordinary circumstances, assignments submitted late without using late chips will receive no credit.</p>
# """)
# 
# c.addAnnouncement(title="Kevin Fu Talk", desc="""
# <p><a href="https://web.eecs.umich.edu/~kevinfu/">Kevin Fu</a>, Associate Professor at the University of Michigan, is giving a talk entitled "Medical Device Cyber Security: The First 164 Years" 
# on Tuesday, October 7 at 4:30pm in Ry 251. Refreshments will be at 3:30pm in Ry 255. The talk is hosted by <a href="https://people.cs.uchicago.edu/~shanlu/">Shan Lu</a></p>
# """)
# 
# c.addAnnouncement(title="Security Seminar", desc="""
# <p>For this quarter, the Security and Systems seminars have been combined. The next meeting will be tomorrow, Tuesday, October 7 12&ndash;1pm in Searle 240b.</p>
# 
# <p>Kevin Fu will be attending, and so we'll be reading a paper from his research group:
# Rushanan et al. <b><a href="https://spqr.eecs.umich.edu/papers/rushanan-sok-oakland14.pdf">SoK: Security and Privacy in Implantable Medical Devices and Body Area Networks.</a></b> 
# <em>IEEE Symposium on Security and Privacy</em>. 2014. There will be Pizza.</p>
# 
# <p>If you're interested, we encourage you to sign up for the <a href="https://mailman.cs.uchicago.edu/mailman/listinfo/security-seminar">mailing list</a>.</p>
# """)

# c.addAnnouncement(title="Security Seminar", desc="""
# <p>The first meeting of the security seminar (which is completely separate from this class) is this Thursday 12&ndash;1pm in Room 240b of the Searle Chemistry Laboratory.
# We'll be reading Brocker and Checkoway. <b><a href="https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-brocker.pdf">iSeeYou: Disabling the MacBook 
# Webcam Indicator LED</a></b>. <em>Proc. 23rd Usenix Security Symposium</em>. There will be Pizza.
# If you're interested, we encourage you to sign up for the <a href="https://mailman.cs.uchicago.edu/mailman/listinfo/security-seminar">mailing list</a>.</p>
# 
# <p><b>Note: After this Thursday's meeting, the seminar will be moving to Tuesdays 12&ndash;1pm in Searle 240b because we'll be taking over the Tuesday Systems Seminar for this quarter.</b></p>
# """)


############################################################

# Week 1
c.addLecture(name="The security mindset")

c.addLecture(name="Message integrity")
c.available(hw[0], c.today())

c.addLecture(name="Hash functions and pseudorandomness")
             
c.addReading("<a href=\"https://www.win.tue.nl/hashclash/rogue-ca/\">MD5 Considered Harmful Today</a>. Sotirov, Stevens, Appelbaum, Lenstra, Molnar, Osvik, and Weger. CCC 2008.")


# Week 2
c.addLecture(name="Confidentiality")
c.available(pr[0], c.today())

c.addDiscussion(name="Java minicourse<br>(in Ry 276)",star=True)
                    
c.addLecture(name="Block ciphers")
c.due(hw[0], c.today())
c.available(hw[1], c.today())
c.due(resp[0], c.today())

c.addLecture(name="Public key cryptography")

c.addReading("<a href=\"http://dl.acm.org/citation.cfm?id=1315304\">Cryptanalysis of the Windows Random Number Generator</a>. Dorrendorf, Gutterman, Pinkas. CCS 2007. [<a href=\"#closed-access\">*closed access</a>]")


# Week 3
c.addLecture(desc="MLK Day &ndash; No lecture",
             holiday=True)

c.addLecture(name="RSA")
c.due(resp[1], c.today())
              
c.addLecture(name="Digital signatures")
c.due(hw[1], c.today())

c.addReading("<a href=\"http://www-ee.stanford.edu/~hellman/publications/24.pdf\">New Directions in Cryptography</a>. Diffie, Hellman. IEEE Trans. on Information Theory. 1976.")


# Week 4
c.addLecture(name="Key exchange and key management")
c.due(pr[0], c.today())
c.available(pr[1], c.today())

c.addLecture(name="TLS and HTTPS")
c.due(resp[2], c.today())

c.addLecture(name="Web architecture")

c.addReading("<a href=\"http://seclab.stanford.edu/websec/csrf/csrf.pdf\">Robust Defenses for Cross-Site Request Forgery</a>. Barth, Jackson, Mitchell. CCS 2008.")


# Week 5
c.addLecture(name="Web attacks and defenses")
c.due(pr[1], c.today())
c.available(pr[2], c.today())

c.addLecture(name="Authenticating people")
c.due(resp[3], c.today())

c.addLecture(name="Authentication (cont.) and access control")
c.available(hw[2], c.today())

c.addReading("<a href=\"http://www.jbonneau.com/doc/DBCBW14-NDSS-tangled_web.pdf\">The Tangled Web of Password Reuse</a>. Das, Bonneau, Caesar, Borisov, Wang. NDSS 2014.")


# Week 6
c.addLecture(name="Networking basics")
c.due(pr[1], c.today())
c.available(pr[2], c.today())

c.addLecture(name="Network attacks")
c.due(resp[4], c.today())

c.addLecture(desc="College Break &ndash; No lecture",
             holiday=True)

c.addReading("<a href=\"https://www.cs.columbia.edu/~smb/papers/ipext.pdf\">A Look Back at \"Security Problems in the TCP/IP Protocol Suite\"</a>. Bellovin. ACSAC 2004.")


# Week 7
c.addLecture(name="Network attacks (cont.)")
c.due(hw[2], c.today())

c.addLecture(name="Network defenses")
c.due(resp[5], c.today())
c.available(hw[3], c.today())
 
c.addLecture(name="Memory safety")
c.due(pr[2], c.today())
c.available(pr[3], c.today())

c.addReading("<a href=\"http://portal.acm.org/ft_gateway.cfm?id=1315313&type=pdf&coll=GUIDE&dl=GUIDE&CFID=81508189&CFTOKEN=42789745\">The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)</a>. Shacham. CCS 2007. [<a href=\"#closed-access\">*closed access</a>]")


# Week 8
c.addLecture(name="Memory safety (cont.)")

c.addLecture(name="Isolation")
c.due(resp[6], c.today())

c.addLecture(name="Trusted computing and side channels")
c.due(hw[3], c.today())

c.addReading("<a href=\"https://svn.torproject.org/svn/projects/design-paper/tor-design.pdf\">Tor: The Second-Generation Onion Router</a>. Dingledine, Mathewson, Syverson. Usenix Security 2004.")
      
      
# Week 9              
c.addLecture(name="Anonymity")

c.addLecture(name="Web privacy")
c.due(resp[7], c.today())
c.due(pr[3], c.today())
c.available(pr[4], c.today())

c.addLecture(name="The underground economy")
c.available(hw[4], c.today())

c.addReading("<a href=\"http://www.icir.org/christian/publications/2008-ccs-spamalytics.pdf\">Spamalytics: An Empirical Analysis of Spam Marketing Conversion</a>. Kanich et al. CCS 2008.")


# Week 10
c.addLecture(name="Security ethics and economics")

# c.addLecture(name="Advanced threats")
                    
c.addLecture(name="Human factors")
c.due(resp[8], c.today())
                    
c.addLecture(name="Exam review")
c.due(hw[4], c.today())
c.due(pr[4], c.today())
