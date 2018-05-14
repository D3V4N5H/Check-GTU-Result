import bs4,requests,webbrowser

url='http://www.gtu.ac.in/StudentCorner.aspx'
page=requests.get(url)
page.raise_for_status()

soup=bs4.BeautifulSoup(page.text, 'html.parser')

elements=soup.select('#ContentPlaceHolder1_lvCircular_lblContentHeading_0 > p > a')

for i in range(len(elements)):
    if 'BE' in elements[i].text:
        print('Result may be out!')
    else:
        print('Negative. Want to see it for yourself?')
        reply=input('(y/n)\n')
        if reply.lower()=='y':
            webbrowser.open(url)