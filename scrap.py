# Go to home page
#
b.open("http://www.tucarro.com.ve")
#
# Navigate through the paginated list of cameras
#
next_page = 0
while next_page == 0:
     #
     # Display and save details of every listed item
     #
     url = b.response.url
     next_element = 0
     while next_element >= 0:
      try:
       b.follow_link(url_regex=re.compile(r"cameraDetail"), nr=next_element)
       next_element = next_element + 1
       print save_response(b,"dvspot_camera_"+str(next_element))
       # go back to home page
       b.open(url)
       # if you crawled too many items, stop crawling
       if next_element*next_page > MAX_NR_OF_ITEMS_PER_SESSION:
          next_element = -1
          next_page = -1
      except LinkNotFoundError:
       # You certainly reached the last item in this page
       next_element = -1
    #
     try:
      b.open(url)
      b.follow_link(text_regex=re.compile(r"Next Page"), nr=0)
      print "processing Next Page"
     except LinkNotFoundError:
      # You reached the last page of the listing of items
      next_page = -1
