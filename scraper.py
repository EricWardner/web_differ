from lxml import html
import requests
import difflib

page = requests.get('http://www.humanesociety.org/about/employment/?credit=web_id93480558')
tree = html.fromstring(page.content)

jobs = ""
campaigns = "campaigns\n"
marketing= "marketing\n"
policy = "policy\n"
hr = "hr\n"
care = "care\n"
affiliates = "affiliates\n"

c1 = tree.xpath('//*[@id="main"]/div/ul[2]/*/*/text()')
c2 = tree.xpath('//*[@id="main"]/div/ul[2]/*/text()')
for(a,b) in zip(c1,c2):
    campaigns += a+b+"\n"

m1 = tree.xpath('//*[@id="main"]/div/ul[3]/*/*/text()')
m2 = tree.xpath('//*[@id="main"]/div/ul[3]/*/text()')
for(a,b) in zip(m1,m2):
    marketing += a+b+"\n"

p1 = tree.xpath('//*[@id="main"]/div/ul[4]/*/*/text()')
p2 = tree.xpath('//*[@id="main"]/div/ul[4]/*/text()')
for(a,b) in zip(p1,p2):
    policy += a+b+"\n"

h1 = tree.xpath('//*[@id="main"]/div/ul[5]/*/*/text()')
h2 = tree.xpath('//*[@id="main"]/div/ul[5]/*/text()')
for(a,b) in zip(h1,h2):
    hr += a+b+"\n"

ca1 = tree.xpath('//*[@id="main"]/div/ul[6]/*/*/text()')
ca2 = tree.xpath('//*[@id="main"]/div/ul[6]/*/text()')
for(a,b) in zip(ca1,ca2):
    care += a+b+"\n"

a1 = tree.xpath('//*[@id="main"]/div/ul[7]/*/*/text()')
a2 = tree.xpath('//*[@id="main"]/div/ul[7]/*/text()')
for(a,b) in zip(a1,a2):
    affiliates += a+b+"\n"

jobs = campaigns+marketing+policy+hr+care+affiliates

f = open('job_openings.txt', 'r')
oldjobs = f.read()
f.close()

jobsbyline = jobs.splitlines(1)
oldjobsbyline = oldjobs.splitlines(1)

d = difflib.Differ()
diffList = list(d.compare(jobsbyline,oldjobsbyline))

numdiffs = 0
diffs = ''
for line in diffList:
    if line[0] == '+':
        diffs += line
        numdiffs = numdiffs+1

if(numdiffs > 0):
    print("New job posted!")
    print(diffs)
    f = open('job_openings.txt', 'w')
    f.write(jobs)

f.close()
