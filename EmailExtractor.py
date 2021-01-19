import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545 +91-9826232632
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin +91-9009111512
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# extracting email
email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-z.]+", mystr)

# extracting indian phone numbers
# email = re.findall(r"[+][0-9]+[-][0-9]+", mystr)

with open("Email.txt", "a") as file:
    i = 1
    for match in email:
        file.write(f"Email{i} - {match}\n")
        i+=1