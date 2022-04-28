"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
def domain_name(url):
    domain = ""

    if "www" in url:
        domain = url.split(".")
        return domain[1]
    
    elif "http" in url:
        domain = url.split("//")
        domain = domain[1].split(".")
        return domain[0]
    
    else:
        domain = url.split(".")
        return domain[0]

"""
Best solution:

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
"""