import json
import http.client


#Annouce the tool
print("Welcome to my learning world")
print("This is a tool for searching in google with custom filters")

#inputGrabber is the input we receive from the user
def inputGrabber(str1):

    filteredData = json.dumps(whatToSearch)
    print("por enquanto: \n", filteredData, "\noque nao incluir: ", notInclude)

whatToSearch = input("digite oque voce quer pesquisar\n")

notInclude = input("digite 1 palavra do site que vc nao quer(ex catho)")
if notInclude is None:
    notInclude = ""

inputGrabber(whatToSearch)
print(chamarGoogle())

def chamarGoogle(str1, str2):
    conn = http.client.HTTPSConnection("localhost", 8081)
    conn.set_tunnel("https://google.com")
    conn.request("HEAD","/index.html")


# def inputGrabber(str1,str2):
#     filteredData = 



