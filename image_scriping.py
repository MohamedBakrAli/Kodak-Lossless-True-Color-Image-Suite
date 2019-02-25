import urllib.request

print ("start scriping.")
cnt = 0
for im in range(1,25):
	im_path = '/home/bakr/Desktop/validation/'+str(im)+'.png'
	if im < 10:
		im_url = 'http://r0k.us/graphics/kodak/kodak/kodim0' + 	str(im) + '.png'
	else:
		im_url = 'http://r0k.us/graphics/kodak/kodak/kodim' + 	str(im) + '.png'
	try:
		urllib.request.urlretrieve(im_url, im_path)
		print (str(im) + " : is saved.") 
		cnt += 1	
	except:
		print (str(im) + " : isn't saved.")
		pass
print("saved image count : " + str(cnt))
print ("finish scriping.")
