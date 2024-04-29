A simple python tool to make api calls
#usage
python request.py <request method> url

#Usage in Linux
create a file called request with the following content "python3 /path/request.py/"

#now move request to /usr/bin and make it executable

sudo mv request /usr/bin && chmod +x request

#using it as an executable

request <method> url

#Methods: GET, POST, OPTIONS, PUT, DELETE, PATCH
