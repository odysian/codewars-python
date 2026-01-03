def domain_name(url):
    # Remove scheme and subdomain
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")

    # Remove Paths
    url = url.split("/")[0]
    # Remove top-level domain
    return url.split(".")[0]
