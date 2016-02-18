import urllib2

#old_url='http://union.click.jd.com/jdc?e=&p=AyIBZRprFDJWWA1FBCVbV0IUEEULWldTCQQAQB1AWQkFWxAFEwFRGkRMR05aZWc8ZRxEWgZiO0IYUmRXchBmURMFHHtXGTISDlUdUhMCEAdlHl8VBRYOVStrdHAiNw==&t=W1dCFBBFC1pXUwkEAEAdQFkJBVsQBRMBURpETEdOWg=='
#old_url='http://www.mmrosi.com/plus/download.php?open=2&id=2&uhash=a624a864db380566a4759b8a'
#old_url='http://www.w3cschool.cc'
old_url='http://www.rosimm.com'
req=urllib2.Request(old_url)
response=urllib2.urlopen(old_url)
print 'Old url:'+old_url
print 'Real url:'+response.geturl()
#print response.read()
