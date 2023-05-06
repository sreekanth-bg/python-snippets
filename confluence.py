from atlassian import Confluence

page_url = "https://confluence.global.tesco.org/display/CO/2.App+Layer+-+AKS"

confluence = Confluence(
        url='https://confluence.global.tesco.org/',
        username="",
        password="")

spaces = confluence.get_all_spaces(start=0, limit=500, expand=None)
slist = spaces['results']
for s in slist:
    print(s['key'], s['name'], s['type'])
